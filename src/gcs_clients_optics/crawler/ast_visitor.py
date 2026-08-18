"""
AST Visitor for identifying and extracting fsspec and filesystem API usages from Python source code.
"""

import ast
from pathlib import Path
from typing import Dict, List, Optional, Set

from gcs_clients_optics.crawler.models import FsspecUsage, SPECIFIED_CACHE_KEYWORDS


class FsspecASTVisitor(ast.NodeVisitor):
    """AST NodeVisitor that inspects Python source trees for fsspec usages."""

    TARGET_FUNCTION_NAMES: Set[str] = {
        "open",
        "open_files",
        "open_local",
        "url_to_fs",
        "filesystem",
        "get_fs_token_paths",
        "open_parquet_file",
    }

    TARGET_OBJECT_METHODS: Set[str] = {
        "open",
        "cat",
        "get",
        "put",
        "read_block",
        "info",
        "ls",
        "exists",
        "isdir",
        "isfile",
        "ukey",
        "relparts",
        "join",
        "parts",
        "getcwd",
        "chdir",
        "isin",
        "normpath",
    }

    def __init__(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ):
        self.file_path = file_path
        self.source_lines = source_code.splitlines()
        self.repo_url = repo_url
        self.branch = branch
        self.usages: List[FsspecUsage] = []

        self.current_class: Optional[str] = None
        self.current_function: Optional[str] = None
        self.local_cache_type: Optional[str] = None
        self.dict_cache_types: Dict[str, str] = {}
        self.imports: Dict[str, str] = {}
        self.filesystem_vars: Set[str] = {"fs", "self.fs", "gcs_fs", "s3_fs"}

    def _get_node_source(self, node: ast.AST) -> str:
        """Extract literal source snippet for an AST node."""
        try:
            return ast.unparse(node)
        except Exception:
            return ""

    def _get_snippet(self, start_line: int, end_line: int) -> str:
        """Extract code snippet across specified line range (1-indexed)."""
        s_idx = max(0, start_line - 1)
        e_idx = min(len(self.source_lines), end_line)
        return "\n".join(self.source_lines[s_idx:e_idx])

    def _clean_str_literal(self, val_str: str) -> str:
        """Strip surrounding quotes from a string representation."""
        val_str = val_str.strip()
        if (val_str.startswith('"') and val_str.endswith('"')) or (
            val_str.startswith("'") and val_str.endswith("'")
        ):
            return val_str[1:-1]
        return val_str

    def _build_file_url(self, start_line: int) -> Optional[str]:
        """Construct full line-level web link for GitHub or local file."""
        if self.repo_url:
            clean_repo = self.repo_url.rstrip("/")
            return f"{clean_repo}/blob/{self.branch}/{self.file_path}#L{start_line}"
        abs_p = Path(self.file_path).resolve()
        return f"file://{abs_p}#L{start_line}"

    def visit_ClassDef(self, node: ast.ClassDef):
        """Track class context."""
        old_class = self.current_class
        self.current_class = node.name
        self.generic_visit(node)
        self.current_class = old_class

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Track function context and local kwargs.pop/get('cache_type', default) assignments."""
        old_func = self.current_function
        old_ct = getattr(self, "local_cache_type", None)
        self.current_function = node.name
        self.local_cache_type = None

        # Inspect function body to detect cache_type = kwargs.pop/get("cache_type", default)
        for child in ast.walk(node):
            if isinstance(child, ast.Assign) and isinstance(child.value, ast.Call):
                func_val = child.value.func
                if (
                    isinstance(func_val, ast.Attribute)
                    and func_val.attr in ("pop", "get")
                    and child.value.args
                ):
                    arg0 = child.value.args[0]
                    if isinstance(arg0, ast.Constant) and arg0.value == "cache_type":
                        if len(child.value.args) >= 2 and isinstance(
                            child.value.args[1], ast.Constant
                        ):
                            self.local_cache_type = str(child.value.args[1].value)

        self.generic_visit(node)
        self.current_function = old_func
        self.local_cache_type = old_ct

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        """Track async function context."""
        self.visit_FunctionDef(node)

    def visit_Import(self, node: ast.Import):
        """Track module imports like `import fsspec` or `import fsspec.parquet as fsspec_parquet`."""
        for alias in node.names:
            local_name = alias.asname or alias.name
            self.imports[local_name] = alias.name
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        """Track from imports like `from fsspec import open`."""
        module = node.module or ""
        for alias in node.names:
            local_name = alias.asname or alias.name
            full_name = f"{module}.{alias.name}" if module else alias.name
            self.imports[local_name] = full_name
        self.generic_visit(node)

    def visit_Assign(self, node: ast.Assign):
        """Track filesystem assignments and dictionary cache_type assignments."""
        if isinstance(node.value, ast.Call):
            func = node.value.func
            if isinstance(func, ast.Attribute) and func.attr == "filesystem":
                for target in node.targets:
                    var_name = self._get_node_source(target)
                    if var_name:
                        self.filesystem_vars.add(var_name)

        # Track dict_name['cache_type'] = 'mmap' or dict_name['cache_type'] = val
        for target in node.targets:
            if isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name):
                dict_name = target.value.id
                slice_node = target.slice
                if isinstance(slice_node, ast.Constant) and slice_node.value in (
                    "cache_type",
                    "simple_cache",
                ):
                    if isinstance(node.value, ast.Constant):
                        self.dict_cache_types[dict_name] = str(node.value.value)
                    else:
                        self.dict_cache_types[dict_name] = self._get_node_source(
                            node.value
                        )

        # Track dict_name = {'cache_type': 'mmap'}
        if isinstance(node.value, ast.Dict):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    dict_name = target.id
                    for k, v in zip(node.value.keys, node.value.values):
                        if isinstance(k, ast.Constant) and k.value in (
                            "cache_type",
                            "simple_cache",
                        ):
                            if isinstance(v, ast.Constant):
                                self.dict_cache_types[dict_name] = str(v.value)
                            else:
                                self.dict_cache_types[dict_name] = (
                                    self._get_node_source(v)
                                )

        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Analyze call sites for fsspec and filesystem usages."""
        is_match = False
        target_name = ""

        # Case 1: Direct function calls (e.g. `fsspec.open(...)`, `open_files(...)`)
        if isinstance(node.func, ast.Name):
            func_id = node.func.id
            imported_orig = self.imports.get(func_id, "")
            if (
                imported_orig.startswith("fsspec")
                or func_id in self.TARGET_FUNCTION_NAMES
            ):
                is_match = True
                target_name = func_id

        # Case 2: Attribute calls (e.g. `fsspec.open(...)`, `fs.open(...)`, `self.fs.open(...)`)
        elif isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            val_id = self._get_node_source(node.func.value)
            imported_orig = self.imports.get(val_id, val_id)

            if (
                imported_orig == "fsspec"
                or imported_orig.startswith("fsspec.")
                or imported_orig == "gcsfs"
            ):
                is_match = True
                target_name = f"{val_id}.{attr}"
            elif (
                val_id in self.filesystem_vars
                or val_id.endswith(".fs")
                or "fs" in val_id
            ) and attr in self.TARGET_OBJECT_METHODS:
                is_match = True
                target_name = f"{val_id}.{attr}"

        if is_match:
            start_line = node.lineno
            end_line = getattr(node, "end_lineno", start_line)
            args_repr = [self._get_node_source(arg) for arg in node.args]
            kwargs_repr = {
                kw.arg: self._get_node_source(kw.value)
                for kw in node.keywords
                if kw.arg is not None
            }

            # Check for unpacked kwargs dictionary, e.g. **open_kwargs
            unpacked_ct = None
            for kw in node.keywords:
                if kw.arg is None and isinstance(kw.value, ast.Name):
                    dict_name = kw.value.id
                    if dict_name in self.dict_cache_types:
                        unpacked_ct = self.dict_cache_types[dict_name]

            # Extract cache_type and cache_options explicitly
            raw_cache_type = (
                kwargs_repr.get("cache_type")
                or kwargs_repr.get("simple_cache")
                or unpacked_ct
            )
            if raw_cache_type:
                cache_type = self._clean_str_literal(raw_cache_type)
            elif getattr(self, "local_cache_type", None):
                cache_type = getattr(self, "local_cache_type")
            else:
                cache_type = "NOT_EXPLICIT"
            cache_options = kwargs_repr.get("cache_options")

            file_url = self._build_file_url(start_line)
            snippet = self._get_snippet(start_line, end_line)

            self.usages.append(
                FsspecUsage(
                    file_path=self.file_path,
                    line_number=start_line,
                    end_line_number=end_line,
                    target_name=target_name,
                    enclosing_function=self.current_function,
                    enclosing_class=self.current_class,
                    cache_type=cache_type,
                    is_specified_cache_keyword=cache_type.lower()
                    in SPECIFIED_CACHE_KEYWORDS,
                    cache_options=cache_options,
                    repo_url=self.repo_url,
                    file_url=file_url,
                    args=args_repr,
                    kwargs=kwargs_repr,
                    code_snippet=snippet,
                    detection_method="ast",
                )
            )

        self.generic_visit(node)
