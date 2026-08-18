"""
Use Case 6: ReadView & Zero-Copy Optimization Analysis.

Identifies read(), cat_file(), and streaming byte access operations, and analyzes
whether the returned buffer ownership is immediately descoped (safe for zero-copy
memoryview / readview) vs retained/escaping in memory.
"""

import ast
import csv
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

from gcs_clients_optics.usecases.base import BaseUseCase

READ_METHOD_NAMES: Set[str] = {
    "read",
    "cat",
    "cat_file",
    "cat_ranges",
    "read_block",
    "read_bytes",
    "readinto",
    "readinto1",
    "readline",
    "readlines",
}

# Known immediate zero-copy friendly consumers
KNOWN_CONSUMERS: Dict[str, str] = {
    "frombuffer": "NUMPY_OR_TORCH_FROMBUFFER",
    "np.frombuffer": "NUMPY_FROMBUFFER",
    "numpy.frombuffer": "NUMPY_FROMBUFFER",
    "torch.frombuffer": "TORCH_FROMBUFFER",
    "torch.load": "TORCH_LOAD",
    "pa.py_buffer": "PYARROW_BUFFER",
    "pa.BufferReader": "PYARROW_BUFFER_READER",
    "pyarrow.BufferReader": "PYARROW_BUFFER_READER",
    "pyarrow.py_buffer": "PYARROW_BUFFER",
    "io.BytesIO": "BYTESIO_STREAM",
    "BytesIO": "BYTESIO_STREAM",
    "json.loads": "JSON_LOADS",
    "pickle.loads": "PICKLE_LOADS",
    "yaml.safe_load": "YAML_LOADS",
    "hashlib.sha256": "HASHLIB_HASH",
    "hashlib.md5": "HASHLIB_HASH",
    "hashlib.sha1": "HASHLIB_HASH",
    "struct.unpack": "STRUCT_UNPACK",
    "struct.unpack_from": "STRUCT_UNPACK",
    "Image.open": "PIL_IMAGE_OPEN",
    "PIL.Image.open": "PIL_IMAGE_OPEN",
    "cv2.imdecode": "OPENCV_IMDECODE",
    "zlib.decompress": "DECOMPRESS_ZLIB",
    "gzip.decompress": "DECOMPRESS_GZIP",
    "ParseFromString": "PROTOBUF_PARSE",
    "memoryview": "MEMORYVIEW_WRAP",
    "decode": "STRING_DECODE",
}


@dataclass
class ReadViewCandidate:
    """Represents a detected read call and its buffer ownership / descoping profile."""

    file_path: str
    line_number: int
    target_name: str
    call_text: str
    is_descoped: bool
    is_zero_copy_ready: bool
    consumer_category: str
    consumer_name: str
    descoped_reason: str
    enclosing_class: Optional[str] = None
    enclosing_function: Optional[str] = None
    file_url: Optional[str] = None
    code_snippet: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class ReadViewReport:
    """Target-level aggregate report for ReadView and zero-copy candidate analysis."""

    target_source: str
    total_files_scanned: int
    files_with_usages: int
    total_read_calls: int
    zero_copy_ready_calls: int
    descoped_percentage: float
    candidates: List[ReadViewCandidate] = field(default_factory=list)
    consumer_summary: Dict[str, int] = field(default_factory=dict)
    repo_url: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["candidates"] = [c.to_dict() for c in self.candidates]
        return d


class ReadViewASTVisitor(ast.NodeVisitor):
    """
    AST Visitor that analyzes read operations and tracks whether returned buffer
    ownership is descoped immediately or retained across lifecycles.
    """

    def __init__(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ):
        self.file_path = file_path
        self.source_code = source_code
        self.repo_url = repo_url
        self.branch = branch
        self.source_lines = source_code.splitlines()
        self.candidates: List[ReadViewCandidate] = []
        self._class_stack: List[str] = []
        self._func_stack: List[ast.AST] = []

    def _get_call_name(self, node: ast.AST) -> str:
        """Extract call string from AST node (e.g. 'f.read', 'fs.cat_file')."""
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            val = self._get_call_name(node.value)
            return f"{val}.{node.attr}" if val else node.attr
        elif isinstance(node, ast.Call):
            return self._get_call_name(node.func)
        return ""

    def _get_snippet(self, lineno: int, context: int = 2) -> str:
        """Extract surrounding source snippet."""
        start = max(0, lineno - context - 1)
        end = min(len(self.source_lines), lineno + context)
        return "\n".join(self.source_lines[start:end])

    def _get_file_url(self, lineno: int) -> Optional[str]:
        if not self.repo_url:
            return None
        clean_url = self.repo_url.rstrip("/")
        return f"{clean_url}/blob/{self.branch}/{self.file_path}#L{lineno}"

    def visit_ClassDef(self, node: ast.ClassDef):
        self._class_stack.append(node.name)
        self.generic_visit(node)
        self._class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._func_stack.append(node)
        self.generic_visit(node)
        self._func_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self._func_stack.append(node)
        self.generic_visit(node)
        self._func_stack.pop()

    def _is_read_call(self, node: ast.Call) -> Tuple[bool, str]:
        """Check if call is a filesystem/file read operation."""
        call_name = self._get_call_name(node.func)
        base_name = call_name.split(".")[-1]
        if base_name in READ_METHOD_NAMES:
            return True, call_name
        return False, ""

    def _analyze_ownership_and_descoping(
        self, call_node: ast.Call
    ) -> Tuple[bool, str, str, str]:
        """
        Analyze whether the read buffer is descoped or escaping.
        Returns: (is_descoped, consumer_category, consumer_name, descoped_reason)
        """
        parent = getattr(call_node, "parent", None)
        if parent is None:
            return True, "LOCAL_TRANSIENT", "unknown", "Assumed local transient read"

        # 1. Direct Chained Transformation: e.g. f.read().decode("utf-8")
        if isinstance(parent, ast.Attribute) and parent.attr in ("decode", "splitlines", "strip", "split"):
            return (
                True,
                "CHAINED_TRANSFORMATION",
                parent.attr,
                f"Immediately transformed in-place via .{parent.attr}()",
            )

        # 2. Direct Consumer Argument: e.g. json.loads(f.read()), np.frombuffer(f.read())
        if isinstance(parent, ast.Call) and parent.func != call_node.func:
            outer_name = self._get_call_name(parent.func)
            # Match longest key first (e.g. torch.frombuffer before frombuffer)
            for k in sorted(KNOWN_CONSUMERS.keys(), key=len, reverse=True):
                cat = KNOWN_CONSUMERS[k]
                if outer_name == k or outer_name.endswith(f".{k}"):
                    return (
                        True,
                        cat,
                        outer_name,
                        f"Direct in-place consumer '{outer_name}' (safe zero-copy candidate)",
                    )
            return (
                True,
                "DIRECT_CALL_ARGUMENT",
                outer_name or "call()",
                f"Passed directly to consumer function '{outer_name}'",
            )

        # 3. Direct Return: e.g. return f.read()
        if isinstance(parent, ast.Return):
            return (
                False,
                "ESCAPING_RETURN",
                "return",
                "Directly returned from function (caller assumes ownership)",
            )

        # 4. Attribute Assignment: e.g. self.data = f.read() or obj.buf = f.read()
        if isinstance(parent, ast.Assign):
            for t in parent.targets:
                if isinstance(t, ast.Attribute):
                    attr_name = self._get_call_name(t)
                    return (
                        False,
                        "ESCAPING_ATTRIBUTE",
                        attr_name,
                        f"Assigned to persistent attribute '{attr_name}' (persists across calls)",
                    )
                elif isinstance(t, ast.Name):
                    var_name = t.id
                    # Inspect enclosing function to see if var_name escapes
                    if self._func_stack:
                        func_node = self._func_stack[-1]
                        escapes, reason = self._check_variable_escape(func_node, var_name)
                        if escapes:
                            return (
                                False,
                                "ESCAPING_LOCAL_VAR",
                                var_name,
                                reason,
                            )
                    return (
                        True,
                        "DESCUPED_LOCAL_VARIABLE",
                        var_name,
                        f"Local transient variable '{var_name}' (ownership discarded at function exit)",
                    )

        # 5. Standalone expression statement: f.read() (draining or side-effect)
        if isinstance(parent, ast.Expr):
            return (
                True,
                "STANDALONE_DRAIN",
                "expr",
                "Result discarded immediately after execution",
            )

        return (
            True,
            "LOCAL_TRANSIENT",
            "local",
            "Local scope execution without explicit escape detected",
        )

    def _check_variable_escape(
        self, func_node: ast.AST, var_name: str
    ) -> Tuple[bool, str]:
        """Check if a local variable name escapes via return or attribute assignment."""
        for n in ast.walk(func_node):
            # Check returns: return data, return (x, data), etc.
            if isinstance(n, ast.Return) and n.value:
                for ret_name in ast.walk(n.value):
                    if isinstance(ret_name, ast.Name) and ret_name.id == var_name:
                        return True, f"Variable '{var_name}' returned from function"

            # Check assignment to self: self.foo = data
            if isinstance(n, ast.Assign):
                for t in n.targets:
                    if isinstance(t, ast.Attribute) and isinstance(n.value, ast.Name) and n.value.id == var_name:
                        return True, f"Variable '{var_name}' stored into attribute '{self._get_call_name(t)}'"

        return False, ""

    def visit_Call(self, node: ast.Call):
        is_read, call_name = self._is_read_call(node)
        if is_read:
            lineno = getattr(node, "lineno", 1)
            is_descoped, cat, consumer, reason = self._analyze_ownership_and_descoping(node)

            call_text = ""
            if 0 < lineno <= len(self.source_lines):
                call_text = self.source_lines[lineno - 1].strip()

            enclosing_cls = self._class_stack[-1] if self._class_stack else None
            enclosing_fn = (
                getattr(self._func_stack[-1], "name", None)
                if self._func_stack
                else None
            )

            cand = ReadViewCandidate(
                file_path=self.file_path,
                line_number=lineno,
                target_name=call_name,
                call_text=call_text,
                is_descoped=is_descoped,
                is_zero_copy_ready=is_descoped,
                consumer_category=cat,
                consumer_name=consumer,
                descoped_reason=reason,
                enclosing_class=enclosing_cls,
                enclosing_function=enclosing_fn,
                file_url=self._get_file_url(lineno),
                code_snippet=self._get_snippet(lineno),
            )
            self.candidates.append(cand)

        self.generic_visit(node)


class ReadViewUseCase(BaseUseCase):
    """
    Use Case 6: ReadView & Zero-Copy Optimization Analysis.
    Audits read paths and verifies if buffer ownership is descoped for zero-copy readview.
    """

    name = "readview"
    description = "Audit read operations for zero-copy readview & buffer ownership descoping"
    aliases = ["zero-copy", "memoryview", "buffer-ownership", "read-view"]

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[ReadViewCandidate]:
        try:
            tree = ast.parse(source_code, filename=file_path)
            # Attach parent references
            for node in ast.walk(tree):
                for child in ast.iter_child_nodes(node):
                    child.parent = node

            visitor = ReadViewASTVisitor(
                file_path, source_code, repo_url=repo_url, branch=branch
            )
            visitor.visit(tree)
            return visitor.candidates
        except Exception:
            return []

    def aggregate_report(
        self,
        target_source: str,
        total_files_scanned: int,
        files_with_usages: int,
        usages: List[ReadViewCandidate],
        repo_url: Optional[str] = None,
    ) -> ReadViewReport:
        total_reads = len(usages)
        zero_copy = sum(1 for u in usages if u.is_zero_copy_ready)
        pct = (zero_copy / total_reads * 100.0) if total_reads > 0 else 0.0

        consumer_summary: Dict[str, int] = {}
        for u in usages:
            consumer_summary[u.consumer_category] = (
                consumer_summary.get(u.consumer_category, 0) + 1
            )

        return ReadViewReport(
            target_source=target_source,
            total_files_scanned=total_files_scanned,
            files_with_usages=files_with_usages,
            total_read_calls=total_reads,
            zero_copy_ready_calls=zero_copy,
            descoped_percentage=round(pct, 2),
            candidates=usages,
            consumer_summary=consumer_summary,
            repo_url=repo_url,
        )

    def export_reports(
        self,
        reports: List[ReadViewReport],
        output_csv: Optional[str] = None,
        output_json: Optional[str] = None,
        output_md: Optional[str] = None,
        output_sqlite: Optional[str] = None,
        elapsed_seconds: float = 0.0,
        **kwargs,
    ) -> Dict[str, str]:
        results = {}

        if output_csv:
            p = Path(output_csv)
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow([
                    "Target",
                    "File Path",
                    "Line",
                    "Target Name",
                    "Is Descoped (Zero-Copy Ready)",
                    "Consumer Category",
                    "Consumer Name",
                    "Descoping Rationale",
                    "Enclosing Class",
                    "Enclosing Function",
                    "File URL",
                ])
                for r in reports:
                    for c in r.candidates:
                        writer.writerow([
                            r.target_source,
                            c.file_path,
                            c.line_number,
                            c.target_name,
                            c.is_zero_copy_ready,
                            c.consumer_category,
                            c.consumer_name,
                            c.descoped_reason,
                            c.enclosing_class or "",
                            c.enclosing_function or "",
                            c.file_url or "",
                        ])
            results["csv"] = str(p)

        if output_json:
            p = Path(output_json)
            p.parent.mkdir(parents=True, exist_ok=True)
            data = {
                "total_targets": len(reports),
                "total_read_calls": sum(r.total_read_calls for r in reports),
                "total_zero_copy_ready": sum(r.zero_copy_ready_calls for r in reports),
                "elapsed_seconds": elapsed_seconds,
                "targets": [r.to_dict() for r in reports],
            }
            with open(p, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            results["json"] = str(p)

        if output_md:
            p = Path(output_md)
            p.parent.mkdir(parents=True, exist_ok=True)
            total_reads = sum(r.total_read_calls for r in reports)
            total_zc = sum(r.zero_copy_ready_calls for r in reports)
            overall_pct = (total_zc / total_reads * 100.0) if total_reads > 0 else 0.0

            lines = [
                "# 🚀 ReadView & Zero-Copy Optimization Analysis Report",
                "",
                f"Evaluated **{len(reports)}** repository targets in **{elapsed_seconds:.2f}s**.",
                "",
                "## 📊 Executive Summary",
                "",
                f"- **Total Read Operations Evaluated**: `{total_reads}`",
                f"- **Zero-Copy `readview` Ready (Descoped Ownership)**: `{total_zc}` (**{overall_pct:.1f}%**)",
                f"- **Retained / Escaping Ownership (Requires Copy)**: `{total_reads - total_zc}`",
                "",
                "## 📋 Repository ReadView Feasibility Breakdown",
                "",
                "| Repository | Files Scanned | Total Reads | Zero-Copy Ready | % Descoped | Top Consumer Pattern |",
                "| :--- | :---: | :---: | :---: | :---: | :--- |",
            ]
            for r in reports:
                top_consumer = "None"
                if r.consumer_summary:
                    top_consumer = max(r.consumer_summary.items(), key=lambda x: x[1])[0]
                lines.append(
                    f"| **`{r.target_source}`** | {r.total_files_scanned} | {r.total_read_calls} | {r.zero_copy_ready_calls} | **{r.descoped_percentage:.1f}%** | `{top_consumer}` |"
                )

            lines.extend([
                "",
                "## 🔍 Actionable Zero-Copy Candidate Snippets",
                "",
            ])
            for r in reports:
                zc_cands = [c for c in r.candidates if c.is_zero_copy_ready][:3]
                if zc_cands:
                    lines.append(f"### `{r.target_source}`")
                    for c in zc_cands:
                        lines.append(f"- **{c.file_path}:{c.line_number}** (`{c.target_name}` ➔ `{c.consumer_category}`)")
                        lines.append(f"  *Reason*: {c.descoped_reason}")
                        if c.file_url:
                            lines.append(f"  *Link*: [{c.file_path}#L{c.line_number}]({c.file_url})")
                        lines.append("  ```python")
                        for sline in c.code_snippet.splitlines()[:5]:
                            lines.append(f"  {sline}")
                        lines.append("  ```")
                    lines.append("")

            with open(p, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            results["md"] = str(p)

        if output_sqlite:
            from gcs_clients_optics.storage.sqlite_store import ingest_readview_reports
            ingest_readview_reports(reports, output_sqlite, elapsed_seconds=elapsed_seconds)
            results["sqlite"] = output_sqlite

        return results

    def print_summary(self, reports: List[ReadViewReport]) -> None:
        total_reads = sum(r.total_read_calls for r in reports)
        total_zc = sum(r.zero_copy_ready_calls for r in reports)
        overall_pct = (total_zc / total_reads * 100.0) if total_reads > 0 else 0.0

        print("\n" + "=" * 70)
        print("  🚀 READVIEW ZERO-COPY BUFFER OWNERSHIP SUMMARY")
        print("=" * 70)
        print(f"  • Total Targets Scanned:       {len(reports)}")
        print(f"  • Total Read Calls Evaluated:  {total_reads}")
        print(f"  • Zero-Copy Ready (Descoped):  {total_zc} ({overall_pct:.1f}%)")
        print(f"  • Retained / Escaping Reads:   {total_reads - total_zc}")
        print("=" * 70)
