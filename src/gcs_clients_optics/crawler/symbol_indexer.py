"""
Whole-Repository Symbol Indexer for cross-file fsspec and filesystem symbol resolution.
"""

import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set


@dataclass
class RepoSymbolTable:
    """Stores cross-file symbols discovered during repository pre-indexing."""
    fs_factories: Set[str] = field(default_factory=set)      # Functions returning FileSystem instances
    fs_classes: Set[str] = field(default_factory=set)        # Custom classes inheriting from AbstractFileSystem
    open_factories: Set[str] = field(default_factory=set)    # Functions opening/returning file streams
    tuple_factories: Set[str] = field(default_factory=set)   # Functions returning (fs, path) tuples

    def is_fs_factory(self, name: str) -> bool:
        return name in self.fs_factories or name.split(".")[-1] in self.fs_factories

    def is_fs_class(self, name: str) -> bool:
        return name in self.fs_classes or name.split(".")[-1] in self.fs_classes

    def is_open_factory(self, name: str) -> bool:
        return name in self.open_factories or name.split(".")[-1] in self.open_factories

    def is_tuple_factory(self, name: str) -> bool:
        return name in self.tuple_factories or name.split(".")[-1] in self.tuple_factories


def path_to_module_parts(rel_path: str) -> List[str]:
    """
    Convert relative file path to possible Python import module paths.
    E.g. 'src/lightning/fabric/utilities/cloud_io.py' ->
    ['lightning.fabric.utilities.cloud_io', 'src.lightning.fabric.utilities.cloud_io', 'fabric.utilities.cloud_io', 'cloud_io']
    """
    p = Path(rel_path)
    raw_parts = list(p.with_suffix("").parts)
    if not raw_parts:
        return []

    module_paths: List[str] = []
    # Direct dot-joined path
    module_paths.append(".".join(raw_parts))

    # Strip top-level source root prefixes (src, lib, python, pkg)
    if raw_parts[0] in ("src", "lib", "python", "pkg") and len(raw_parts) > 1:
        clean_parts = raw_parts[1:]
        module_paths.append(".".join(clean_parts))
    else:
        clean_parts = raw_parts

    # Add tail suffixes (e.g. 'cloud_io', 'utilities.cloud_io')
    for i in range(1, len(clean_parts)):
        module_paths.append(".".join(clean_parts[i:]))

    # Single stem name
    stem = p.stem
    if stem not in module_paths:
        module_paths.append(stem)

    return module_paths


class RepoSymbolIndexer(ast.NodeVisitor):
    """
    AST Visitor that scans a Python module AST and registers filesystem factories,
    subclasses, and open helpers into a shared RepoSymbolTable.
    """

    def __init__(self, rel_path: str, symbol_table: RepoSymbolTable):
        self.rel_path = rel_path
        self.symbol_table = symbol_table
        self.module_paths = path_to_module_parts(rel_path)
        self.imports: Dict[str, str] = {}

    def _unparse(self, node: ast.AST) -> str:
        try:
            return ast.unparse(node)
        except Exception:
            return ""

    def _register_fs_factory(self, func_name: str):
        self.symbol_table.fs_factories.add(func_name)
        for mod in self.module_paths:
            self.symbol_table.fs_factories.add(f"{mod}.{func_name}")

    def _register_fs_class(self, class_name: str):
        self.symbol_table.fs_classes.add(class_name)
        for mod in self.module_paths:
            self.symbol_table.fs_classes.add(f"{mod}.{class_name}")

    def _register_open_factory(self, func_name: str):
        self.symbol_table.open_factories.add(func_name)
        for mod in self.module_paths:
            self.symbol_table.open_factories.add(f"{mod}.{func_name}")

    def _register_tuple_factory(self, func_name: str):
        self.symbol_table.tuple_factories.add(func_name)
        for mod in self.module_paths:
            self.symbol_table.tuple_factories.add(f"{mod}.{func_name}")

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            local = alias.asname or alias.name
            self.imports[local] = alias.name
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        mod = node.module or ""
        for alias in node.names:
            local = alias.asname or alias.name
            self.imports[local] = f"{mod}.{alias.name}" if mod else alias.name
        self.generic_visit(node)

    def visit_ClassDef(self, node: ast.ClassDef):
        # Check if class inherits from known filesystem classes
        for base in node.bases:
            base_str = self._unparse(base)
            imported_base = self.imports.get(base_str, base_str)
            if (
                base_str.endswith(("FileSystem", "FS", "FSWrapper"))
                or imported_base.endswith(("FileSystem", "FS", "FSWrapper"))
                or "AbstractFileSystem" in base_str
                or "AbstractFileSystem" in imported_base
            ):
                self._register_fs_class(node.name)
                break
        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        self._analyze_function(node)
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self._analyze_function(node)
        self.generic_visit(node)

    def _analyze_function(self, node: ast.AST):
        func_name = getattr(node, "name", "")
        if not func_name:
            return

        # 1. Return annotation check (e.g. -> AbstractFileSystem or -> FileSystem)
        if getattr(node, "returns", None):
            ret_str = self._unparse(node.returns)
            imported_ret = self.imports.get(ret_str, ret_str)
            if (
                ret_str.endswith(("FileSystem", "FS", "FSWrapper", "AbstractFileSystem"))
                or imported_ret.endswith(("FileSystem", "FS", "FSWrapper", "AbstractFileSystem"))
            ):
                self._register_fs_factory(func_name)
                return

        # 2. Return statements inside the function body
        for child in ast.walk(node):
            if isinstance(child, ast.Return) and child.value:
                ret_val = child.value

                # Case A: Return expression is a call (e.g. return fsspec.filesystem(...), return url_to_fs(...))
                if isinstance(ret_val, ast.Call):
                    fn_name = self._unparse(ret_val.func)
                    imported = self.imports.get(fn_name, fn_name)

                    if (
                        fn_name.endswith((".filesystem", "url_to_fs"))
                        or imported.endswith((".filesystem", "url_to_fs"))
                        or fn_name in ("filesystem", "url_to_fs")
                    ):
                        self._register_fs_factory(func_name)
                        return

                    if fn_name.endswith((".open", "open_files", "open_local", "open_file")):
                        self._register_open_factory(func_name)
                        return

                # Case B: Return is a variable name assigned from url_to_fs / fsspec.filesystem in body
                if isinstance(ret_val, ast.Name):
                    ret_id = ret_val.id
                    for b_node in ast.walk(node):
                        if isinstance(b_node, ast.Assign) and isinstance(b_node.value, ast.Call):
                            call_fn = self._unparse(b_node.value.func)
                            imp_fn = self.imports.get(call_fn, call_fn)
                            if (
                                "url_to_fs" in call_fn
                                or "url_to_fs" in imp_fn
                                or "filesystem" in call_fn
                                or "filesystem" in imp_fn
                            ):
                                for tgt in b_node.targets:
                                    tgt_str = self._unparse(tgt)
                                    if ret_id in tgt_str:
                                        self._register_fs_factory(func_name)
                                        return


def build_repo_symbol_table(files_map: Dict[str, str]) -> RepoSymbolTable:
    """
    Fast in-memory pass over all Python source files in a repository to build
    a cross-file RepoSymbolTable.
    """
    symbol_table = RepoSymbolTable()
    for rel_path, code in files_map.items():
        if not rel_path.endswith(".py"):
            continue
        try:
            tree = ast.parse(code, filename=rel_path)
            indexer = RepoSymbolIndexer(rel_path, symbol_table)
            indexer.visit(tree)
        except Exception:
            continue
    return symbol_table
