"""
Use Case 5: Async vs Sync Filesystem Method Usage Analysis.

Analyzes asynchronous vs synchronous execution patterns in cloud storage / fsspec interactions:
- Async execution: `await fs._cat_file()`, `async with fsspec.open_async()`, `_ls`, `_info`, `asynchronous=True`
- Sync execution: `fs.open()`, `fs.cat_file()`, `fs.ls()`, `fs.exists()`, `f.readinto()`
- Async bridge wrappers: `fsspec.asyn.sync()`, `sync_wrapper()`, `_run_coros()`
- Event loop stall warnings: synchronous blocking calls invoked inside `async def` coroutines.
"""

import ast
import csv
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from gcs_clients_optics.analysis.categorization import categorize_method
from gcs_clients_optics.usecases.base import BaseUseCase

# Explicit internal coroutine methods on fsspec.asyn.AsyncFileSystem
ASYNC_COROUTINE_METHODS = {
    "_cat_file",
    "_cat",
    "_cat_ranges",
    "_ls",
    "_info",
    "_rm_file",
    "_rm",
    "_rmdir",
    "_pipe_file",
    "_pipe",
    "_get_file",
    "_get",
    "_put_file",
    "_put",
    "_cp_file",
    "_copy",
    "_mkdir",
    "_makedirs",
    "_expand_path",
    "_isdir",
    "_isfile",
    "_size",
    "_exists",
    "_open",
    "open_async",
    "_walk",
    "_glob",
    "_find",
    "_touch",
    "_checksum",
    "_ukey",
}

# Standard synchronous methods
SYNC_FS_METHODS = {
    "open",
    "open_files",
    "cat",
    "cat_file",
    "cat_ranges",
    "pipe",
    "pipe_file",
    "head",
    "tail",
    "read_block",
    "read_bytes",
    "read_text",
    "write_bytes",
    "write_text",
    "ls",
    "listdir",
    "glob",
    "find",
    "walk",
    "tree",
    "expand_path",
    "exists",
    "lexists",
    "info",
    "stat",
    "isdir",
    "isfile",
    "size",
    "sizes",
    "du",
    "checksum",
    "ukey",
    "mkdir",
    "makedirs",
    "touch",
    "rm",
    "rm_file",
    "rmdir",
    "delete",
    "copy",
    "cp",
    "move",
    "mv",
    "rename",
    "get",
    "get_file",
    "download",
    "put",
    "put_file",
    "upload",
    "read",
    "readinto",
    "readinto1",
    "readline",
    "readlines",
    "write",
    "flush",
    "close",
    "seek",
    "tell",
}

ASYNC_BRIDGE_FUNCS = {
    "sync",
    "sync_wrapper",
    "_run_coros",
    "run_coro",
    "call_coro",
}


@dataclass
class AsyncSyncUsageItem:
    """Represents a detected filesystem call with async vs sync classification."""

    file_path: str
    line_number: int
    target_name: str
    base_method: str
    category: str
    execution_mode: str  # "async" or "sync"
    async_mechanism: str  # "await_expression", "async_with", "async_coroutine_method", "async_fs_init", "async_bridge", "sync_blocking", "sync_in_async_context"
    is_async_context: bool  # True if inside `async def`
    is_coroutine_call: bool  # True if invoked with await or async with
    potential_event_loop_block: bool  # True if sync blocking call inside `async def`
    enclosing_class: Optional[str] = None
    enclosing_function: Optional[str] = None
    repo_url: Optional[str] = None
    file_url: Optional[str] = None
    code_snippet: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class AsyncSyncReport:
    """Aggregated Async vs Sync usage report for a repository or target."""

    target_source: str
    total_files_scanned: int
    files_with_usages: int
    total_usages_found: int
    async_count: int = 0
    sync_count: int = 0
    async_pct: float = 0.0
    mechanism_counts: Dict[str, int] = field(default_factory=dict)
    potential_blocks_count: int = 0
    repo_url: Optional[str] = None
    items: List[AsyncSyncUsageItem] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["items"] = [i.to_dict() for i in self.items]
        return data


class AsyncSyncASTVisitor(ast.NodeVisitor):
    """AST Visitor that classifies every filesystem call into async vs sync mode."""

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
        self.usages: List[AsyncSyncUsageItem] = []

        self.class_stack: List[str] = []
        self.func_stack: List[str] = []
        self.async_func_stack: List[bool] = []
        self.await_stack: List[bool] = []
        self.async_with_stack: List[bool] = []

    def _get_code_snippet(self, node: ast.AST) -> str:
        lineno = getattr(node, "lineno", 1)
        if 1 <= lineno <= len(self.source_lines):
            return self.source_lines[lineno - 1].strip()
        return ""

    def _build_file_url(self, lineno: int) -> Optional[str]:
        if not self.repo_url:
            return None
        clean_url = self.repo_url.rstrip("/")
        return f"{clean_url}/blob/{self.branch}/{self.file_path}#L{lineno}"

    def visit_ClassDef(self, node: ast.ClassDef):
        self.class_stack.append(node.name)
        self.generic_visit(node)
        self.class_stack.pop()

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.func_stack.append(node.name)
        self.async_func_stack.append(False)
        self.generic_visit(node)
        self.async_func_stack.pop()
        self.func_stack.pop()

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.func_stack.append(node.name)
        self.async_func_stack.append(True)
        self.generic_visit(node)
        self.async_func_stack.pop()
        self.func_stack.pop()

    def visit_Await(self, node: ast.Await):
        self.await_stack.append(True)
        self.generic_visit(node)
        self.await_stack.pop()

    def visit_AsyncWith(self, node: ast.AsyncWith):
        self.async_with_stack.append(True)
        for item in node.items:
            if isinstance(item.context_expr, ast.Call):
                self._inspect_call(item.context_expr, is_async_with=True)
        self.generic_visit(node)
        self.async_with_stack.pop()

    def visit_Call(self, node: ast.Call):
        is_await = bool(self.await_stack and self.await_stack[-1])
        is_async_with = bool(self.async_with_stack and self.async_with_stack[-1])
        self._inspect_call(node, is_await=is_await, is_async_with=is_async_with)
        self.generic_visit(node)

    def _inspect_call(
        self,
        node: ast.Call,
        is_await: bool = False,
        is_async_with: bool = False,
    ):
        target_name = self._resolve_target_name(node.func)
        if not target_name:
            return

        base_method = target_name.split(".")[-1].strip()
        is_in_async_def = bool(
            self.async_func_stack and self.async_func_stack[-1]
        )

        execution_mode = "sync"
        async_mechanism = "sync_blocking"
        is_coroutine_call = is_await or is_async_with
        potential_event_loop_block = False

        # 1. Explicit Async Coroutine Methods (_cat_file, _ls, open_async, etc.)
        if base_method in ASYNC_COROUTINE_METHODS or target_name.endswith(
            "_async"
        ):
            execution_mode = "async"
            if is_await:
                async_mechanism = "await_expression"
            elif is_async_with:
                async_mechanism = "async_with"
            else:
                async_mechanism = "async_coroutine_method"

        # 2. Async bridge functions (fsspec.asyn.sync, sync_wrapper, etc.)
        elif (
            base_method in ASYNC_BRIDGE_FUNCS
            or "fsspec.asyn" in target_name
            or "asyn.sync" in target_name
        ):
            execution_mode = "async"
            async_mechanism = "async_bridge"

        # 3. Filesystem Instantiation with asynchronous=True
        elif base_method in {
            "filesystem",
            "GCSFileSystem",
            "S3FileSystem",
            "AsyncFileSystem",
        }:
            has_async_kwarg = False
            for kw in node.keywords:
                if kw.arg == "asynchronous":
                    if isinstance(kw.value, ast.Constant) and kw.value.value is True:
                        has_async_kwarg = True
            if has_async_kwarg or base_method == "AsyncFileSystem":
                execution_mode = "async"
                async_mechanism = "async_fs_init"
            elif base_method in SYNC_FS_METHODS or "open" in base_method:
                execution_mode = "sync"
                async_mechanism = "sync_blocking"
            else:
                return

        # 4. Standard FS method called with await or async with
        elif (
            base_method in SYNC_FS_METHODS
            or target_name.startswith("fs.")
            or target_name.startswith("fsspec.")
            or target_name.startswith("self.fs.")
        ):
            if is_await:
                execution_mode = "async"
                async_mechanism = "await_expression"
            elif is_async_with:
                execution_mode = "async_with"
            elif is_in_async_def:
                execution_mode = "sync"
                async_mechanism = "sync_in_async_context"
                # Flag potential event loop blocking call in async context
                if base_method in {
                    "open",
                    "cat",
                    "cat_file",
                    "get",
                    "put",
                    "ls",
                    "glob",
                    "read",
                    "write",
                    "readinto",
                }:
                    potential_event_loop_block = True
            else:
                execution_mode = "sync"
                async_mechanism = "sync_blocking"
        else:
            return

        category = categorize_method(target_name)
        lineno = getattr(node, "lineno", 1)

        item = AsyncSyncUsageItem(
            file_path=self.file_path,
            line_number=lineno,
            target_name=target_name,
            base_method=base_method,
            category=category,
            execution_mode=execution_mode,
            async_mechanism=async_mechanism,
            is_async_context=is_in_async_def,
            is_coroutine_call=is_coroutine_call,
            potential_event_loop_block=potential_event_loop_block,
            enclosing_class=(
                self.class_stack[-1] if self.class_stack else None
            ),
            enclosing_function=(
                self.func_stack[-1] if self.func_stack else None
            ),
            repo_url=self.repo_url,
            file_url=self._build_file_url(lineno),
            code_snippet=self._get_code_snippet(node),
        )
        self.usages.append(item)

    def _resolve_target_name(self, node: ast.AST) -> Optional[str]:
        if isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Attribute):
            val = self._resolve_target_name(node.value)
            return f"{val}.{node.attr}" if val else node.attr
        return None


class AsyncSyncUseCase(BaseUseCase):
    """
    Use Case 5: Async vs Sync Filesystem Method Usage Analysis.
    """

    name = "async-sync"
    description = (
        "Analyze asynchronous vs synchronous filesystem calls, coroutines, and event-loop bridges."
    )
    aliases = ["async", "async-optics", "concurrency-modes", "sync-async"]

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[AsyncSyncUsageItem]:
        """Scan a single Python source file for async vs sync usage."""
        try:
            tree = ast.parse(source_code, filename=file_path)
            visitor = AsyncSyncASTVisitor(
                file_path, source_code, repo_url=repo_url, branch=branch
            )
            visitor.visit(tree)
            return visitor.usages
        except SyntaxError:
            return []

    def aggregate_report(
        self,
        target_source: str,
        total_files_scanned: int,
        files_with_usages: int,
        usages: List[AsyncSyncUsageItem],
        repo_url: Optional[str] = None,
    ) -> AsyncSyncReport:
        """Aggregate file-level usages into repository-level Async vs Sync report."""
        async_count = sum(1 for u in usages if u.execution_mode == "async")
        sync_count = sum(1 for u in usages if u.execution_mode == "sync")
        total = len(usages)
        async_pct = round((async_count / total * 100.0), 1) if total > 0 else 0.0

        mech_counts: Dict[str, int] = {}
        blocks_count = 0
        for u in usages:
            mech_counts[u.async_mechanism] = (
                mech_counts.get(u.async_mechanism, 0) + 1
            )
            if u.potential_event_loop_block:
                blocks_count += 1

        return AsyncSyncReport(
            target_source=target_source,
            total_files_scanned=total_files_scanned,
            files_with_usages=files_with_usages,
            total_usages_found=total,
            async_count=async_count,
            sync_count=sync_count,
            async_pct=async_pct,
            mechanism_counts=mech_counts,
            potential_blocks_count=blocks_count,
            repo_url=repo_url,
            items=usages,
        )

    def export_reports(
        self,
        reports: List[AsyncSyncReport],
        output_csv: Optional[str] = None,
        output_json: Optional[str] = None,
        output_md: Optional[str] = None,
        output_sqlite: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, str]:
        """Export CSV, JSON, Markdown, and SQLite reports."""
        generated: Dict[str, str] = {}

        if output_sqlite:
            from gcs_clients_optics.storage.sqlite_store import (
                ingest_async_sync_reports,
            )

            ingest_async_sync_reports(
                reports,
                output_sqlite,
                elapsed_seconds=kwargs.get("elapsed_seconds", 0.0),
            )
            generated["sqlite"] = output_sqlite

        if output_csv:
            export_async_sync_csv(reports, output_csv)
            generated["csv"] = output_csv

        if output_json:
            export_async_sync_json(
                reports,
                output_json,
                elapsed_seconds=kwargs.get("elapsed_seconds", 0.0),
            )
            generated["json"] = output_json

        if output_md:
            export_async_sync_markdown(reports, output_md)
            generated["markdown"] = output_md

        return generated

    def print_summary(self, reports: List[AsyncSyncReport]) -> None:
        """Print rich console summary of Async vs Sync method distribution."""
        total_targets = len(reports)
        total_files = sum(r.total_files_scanned for r in reports)
        files_with = sum(r.files_with_usages for r in reports)
        total_calls = sum(r.total_usages_found for r in reports)
        total_async = sum(r.async_count for r in reports)
        total_sync = sum(r.sync_count for r in reports)
        total_blocks = sum(r.potential_blocks_count for r in reports)

        overall_async_pct = (
            round((total_async / total_calls * 100.0), 1)
            if total_calls > 0
            else 0.0
        )

        print("\n" + "=" * 70)
        print("  ⚡ ASYNC VS SYNC METHOD USAGE SUMMARY")
        print("=" * 70)
        print(f"  • Total Targets Scanned: {total_targets}")
        print(f"  • Total Files Scanned:   {total_files}")
        print(f"  • Files with Usages:     {files_with}")
        print(f"  • Total Method Calls:    {total_calls}")
        print(f"  • Asynchronous Calls:    {total_async} ({overall_async_pct}%)")
        print(
            f"  • Synchronous Calls:     {total_sync} ({100.0 - overall_async_pct:.1f}%)"
        )
        if total_blocks > 0:
            print(
                f"  ⚠️  Potential Event Loop Blocks (Sync in Async Def): {total_blocks}"
            )
        print("-" * 70)

        # Breakdown per target
        print(
            f"\n{'Target / Repository':<35} | {'Async Calls':<12} | {'Sync Calls':<12} | {'Async %'}"
        )
        print("-" * 70)
        for r in reports:
            print(
                f"{r.target_source:<35} | {r.async_count:<12} | {r.sync_count:<12} | {r.async_pct}%"
            )
        print("=" * 70 + "\n")


def export_async_sync_csv(
    reports: List[AsyncSyncReport], output_path: Union[str, Path]
) -> None:
    """Export all async vs sync usage records to a flat CSV file."""
    p = Path(output_path)
    p.parent.mkdir(parents=True, exist_ok=True)

    with open(p, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Target Source",
            "File Path",
            "Line Number",
            "Target Name",
            "Base Method",
            "Category",
            "Execution Mode",
            "Async Mechanism",
            "Is Async Context",
            "Is Coroutine Call",
            "Potential Event Loop Block",
            "Enclosing Class",
            "Enclosing Function",
            "File URL",
            "Code Snippet",
        ])
        for report in reports:
            for item in report.items:
                writer.writerow([
                    report.target_source,
                    item.file_path,
                    item.line_number,
                    item.target_name,
                    item.base_method,
                    item.category,
                    item.execution_mode,
                    item.async_mechanism,
                    item.is_async_context,
                    item.is_coroutine_call,
                    item.potential_event_loop_block,
                    item.enclosing_class or "",
                    item.enclosing_function or "",
                    item.file_url or "",
                    item.code_snippet,
                ])


def export_async_sync_json(
    reports: List[AsyncSyncReport],
    output_path: Union[str, Path],
    elapsed_seconds: float = 0.0,
) -> None:
    """Export aggregated async vs sync reports to a structured JSON file."""
    p = Path(output_path)
    p.parent.mkdir(parents=True, exist_ok=True)

    total_calls = sum(r.total_usages_found for r in reports)
    total_async = sum(r.async_count for r in reports)
    total_sync = sum(r.sync_count for r in reports)

    data = {
        "summary": {
            "total_repositories": len(reports),
            "total_files_scanned": sum(r.total_files_scanned for r in reports),
            "files_with_usages": sum(r.files_with_usages for r in reports),
            "total_method_calls": total_calls,
            "total_async_calls": total_async,
            "total_sync_calls": total_sync,
            "overall_async_pct": (
                round(total_async / total_calls * 100.0, 1)
                if total_calls > 0
                else 0.0
            ),
            "elapsed_seconds": round(elapsed_seconds, 2),
        },
        "per_repository": [r.to_dict() for r in reports],
    }

    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def export_async_sync_markdown(
    reports: List[AsyncSyncReport], output_path: Union[str, Path]
) -> None:
    """Export comprehensive Markdown report for Async vs Sync usage."""
    p = Path(output_path)
    p.parent.mkdir(parents=True, exist_ok=True)

    total_calls = sum(r.total_usages_found for r in reports)
    total_async = sum(r.async_count for r in reports)
    total_sync = sum(r.sync_count for r in reports)
    total_blocks = sum(r.potential_blocks_count for r in reports)

    lines = [
        "# ⚡ Async vs Sync Filesystem Method Usage Report",
        "",
        "> Comparative analysis of asynchronous coroutines (`await fs._cat_file()`, `open_async`, `asynchronous=True`) versus synchronous blocking calls (`fs.open()`, `fs.ls()`, `fs.exists()`) across cloud storage codebases.",
        "",
        "## 📊 Executive Summary",
        "",
        f"- **Total Target Repositories**: {len(reports)}",
        f"- **Total Files Scanned**: {sum(r.total_files_scanned for r in reports):,}",
        f"- **Total Method Calls**: {total_calls:,}",
        f"- **Asynchronous Calls**: {total_async:,} ({round(total_async / total_calls * 100.0, 1) if total_calls > 0 else 0.0}%)",
        f"- **Synchronous Calls**: {total_sync:,} ({round(total_sync / total_calls * 100.0, 1) if total_calls > 0 else 0.0}%)",
        f"- **Potential Event Loop Blocking Calls**: {total_blocks:,}",
        "",
        "---",
        "",
        "## 🏢 Repository Breakdown",
        "",
        "| Repository / Target | Files Scanned | Total Calls | Async Calls | Sync Calls | Async % | Event Loop Warnings |",
        "| :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
    ]

    for r in reports:
        lines.append(
            f"| `{r.target_source}` | {r.total_files_scanned:,} | {r.total_usages_found:,} | {r.async_count:,} | {r.sync_count:,} | **{r.async_pct}%** | {r.potential_blocks_count} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 🛠️ Async Mechanisms & Patterns",
        "",
        "| Mechanism | Description | Count |",
        "| :--- | :--- | :--- |",
    ])

    global_mech: Dict[str, int] = {}
    for r in reports:
        for k, v in r.mechanism_counts.items():
            global_mech[k] = global_mech.get(k, 0) + v

    mech_descriptions = {
        "await_expression": "Direct `await` invocation (`await fs._cat_file()`, `await f.read()`)",
        "async_with": "Asynchronous context manager (`async with fsspec.open_async()`)",
        "async_coroutine_method": "Direct coroutine method reference (`_cat_file`, `_ls`, `_info`)",
        "async_fs_init": "Async filesystem initialization (`asynchronous=True` / `AsyncFileSystem`)",
        "async_bridge": "Event loop runner bridge (`fsspec.asyn.sync()`, `sync_wrapper()`)",
        "sync_in_async_context": "Synchronous call inside `async def` function",
        "sync_blocking": "Standard synchronous blocking call in sync function",
    }

    for mech, count in sorted(
        global_mech.items(), key=lambda x: x[1], reverse=True
    ):
        desc = mech_descriptions.get(mech, mech)
        lines.append(f"| `{mech}` | {desc} | {count:,} |")

    lines.extend(["", "---", ""])

    with open(p, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
