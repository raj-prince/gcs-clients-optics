"""
AST Visitor for identifying and extracting fsspec and filesystem API usages from Python source code.
"""

import ast
import re
from enum import Enum, auto
from pathlib import Path
from typing import Dict, List, Optional, Set

from gcs_clients_optics.crawler.models import FsspecUsage, SPECIFIED_CACHE_KEYWORDS
from gcs_clients_optics.crawler.symbol_indexer import RepoSymbolTable


class InferredType(Enum):
    """Semantic type classifications for AST expressions during static analysis."""
    UNKNOWN = auto()
    FILESYSTEM = auto()         # Filesystem instance (e.g. AbstractFileSystem, fs, self.fs, get_filesystem())
    FILE_STREAM = auto()        # File stream / open file handle (e.g. f, fo, stream, OpenFile, fs.open())
    FS_FACTORY = auto()         # Function producing a filesystem instance (e.g. fsspec.filesystem, get_filesystem)
    FS_TUPLE_FACTORY = auto()   # Function returning (fs, path, ...) tuple (e.g. url_to_fs, get_fs_token_paths)
    OPEN_FACTORY = auto()       # Function returning file stream(s) (e.g. fsspec.open, open_files, open_local)
    FS_MODULE = auto()          # Backend / fsspec module (e.g. fsspec, gcsfs, s3fs, adlfs, abfs)


class FsspecASTVisitor(ast.NodeVisitor):
    """AST NodeVisitor that inspects Python source trees for fsspec usages using semantic type inference."""

    TARGET_FUNCTION_NAMES: Set[str] = {
        "open_files",
        "open_local",
        "open_file",
        "url_to_fs",
        "filesystem",
        "get_fs_token_paths",
        "get_filesystem_class",
        "read_block",
        "read_bytes",
        "read_text",
        "write_bytes",
        "write_text",
        "open_parquet_file",
        "stringify_path",
        "expand_paths_if_needed",
        "infer_compression",
    }

    TARGET_OBJECT_METHODS: Set[str] = {
        "open",
        "cat",
        "cat_file",
        "cat_ranges",
        "readinto",
        "readinto1",
        "read",
        "readline",
        "readlines",
        "readuntil",
        "read_block",
        "read_bytes",
        "read_text",
        "write",
        "write_bytes",
        "write_text",
        "writelines",
        "pipe",
        "pipe_file",
        "seek",
        "tell",
        "flush",
        "close",
        "readable",
        "writable",
        "seekable",
        "get",
        "get_file",
        "put",
        "put_file",
        "info",
        "stat",
        "size",
        "sizes",
        "du",
        "checksum",
        "ukey",
        "ls",
        "listdir",
        "glob",
        "find",
        "walk",
        "tree",
        "expand_path",
        "exists",
        "lexists",
        "isdir",
        "isfile",
        "mkdir",
        "makedirs",
        "rm",
        "rm_file",
        "rmdir",
        "copy",
        "cp",
        "mv",
        "move",
        "rename",
        "touch",
        "relparts",
        "relpath",
        "join",
        "split",
        "parts",
        "getcwd",
        "chdir",
        "isin",
        "normpath",
        "abspath",
        "commonpath",
        "as_posix",
    }

    FILE_STREAM_METHODS: Set[str] = {
        "read",
        "readinto",
        "readinto1",
        "readline",
        "readlines",
        "readuntil",
        "seek",
        "tell",
        "flush",
        "close",
        "write",
        "writelines",
        "readable",
        "writable",
        "seekable",
    }

    # Semantic pattern matchers
    _RE_FS_IDENTIFIER = re.compile(
        r"^(_)?(?:.*_)?(fs|filesystem)(_.*)?$", re.IGNORECASE
    )
    _RE_FILE_IDENTIFIER = re.compile(
        r"^(_)?(fo|fileobj|file_obj|stream|stream_handle|raw_file)(_.*)?$",
        re.IGNORECASE,
    )
    _RE_FS_FACTORY_FUNC = re.compile(
        r"^(?:get|create|init|resolve|build|load|make|fetch|new)_.*(?:fs|filesystem)$|^(?:fs|filesystem)$",
        re.IGNORECASE,
    )
    _RE_FS_CLASS = re.compile(r"^(?:.*_)?(?:FileSystem|FS|FSWrapper)$")
    _KNOWN_FS_MODULES = ("fsspec", "gcsfs", "s3fs", "adlfs", "abfs")

    def __init__(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
        repo_symbols: Optional[RepoSymbolTable] = None,
    ):
        self.file_path = file_path
        self.source_lines = source_code.splitlines()
        self.repo_url = repo_url
        self.branch = branch
        self.repo_symbols = repo_symbols
        self.usages: List[FsspecUsage] = []

        self.current_class: Optional[str] = None
        self.current_function: Optional[str] = None
        self.local_cache_type: Optional[str] = None
        self.dict_cache_types: Dict[str, str] = {}
        self.imports: Dict[str, str] = {}

        # Symbol type registries
        self.filesystem_vars: Set[str] = {
            "fs",
            "_fs",
            "self.fs",
            "self._fs",
            "cls.fs",
            "cls._fs",
            "gcs_fs",
            "s3_fs",
            "filesystem",
            "dirfs",
            "hffs",
            "backend",
        }
        self.file_vars: Set[str] = set()
        self.filesystem_classes: Set[str] = {
            "AbstractFileSystem",
            "AsyncFileSystem",
            "GCSFileSystem",
            "LocalFileSystem",
            "MemoryFileSystem",
            "DirFileSystem",
            "ArrowFSWrapper",
            "fsspec.AbstractFileSystem",
            "fsspec.asyn.AsyncFileSystem",
            "fsspec.implementations.local.LocalFileSystem",
            "fsspec.implementations.memory.MemoryFileSystem",
            "fsspec.implementations.dirfs.DirFileSystem",
            "fsspec.implementations.arrow.ArrowFSWrapper",
            "gcsfs.GCSFileSystem",
            "gcsfs.core.GCSFileSystem",
        }
        self.fs_factories: Set[str] = set()

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

    # --------------------------------------------------------------------------
    # Semantic Type Inference
    # --------------------------------------------------------------------------

    def _is_fs_module(self, name: str) -> bool:
        """Check if an identifier or import path refers to a filesystem backend module."""
        imported = self.imports.get(name, name)
        return imported.startswith(self._KNOWN_FS_MODULES) or name in self._KNOWN_FS_MODULES

    def _is_fs_class_name(self, name: str) -> bool:
        """Check if a name represents a filesystem class."""
        imported = self.imports.get(name, name)
        if self.repo_symbols and (self.repo_symbols.is_fs_class(name) or self.repo_symbols.is_fs_class(imported)):
            return True
        return (
            name in self.filesystem_classes
            or imported in self.filesystem_classes
            or bool(self._RE_FS_CLASS.match(name))
            or bool(self._RE_FS_CLASS.match(imported.split(".")[-1]))
        )

    def _is_fs_factory_name(self, name: str) -> bool:
        """Check if a function or method name represents a filesystem factory / constructor."""
        imported = self.imports.get(name, name)
        last_seg = name.split(".")[-1]
        imported_last_seg = imported.split(".")[-1]
        if self.repo_symbols and (
            self.repo_symbols.is_fs_factory(name)
            or self.repo_symbols.is_fs_factory(imported)
            or self.repo_symbols.is_fs_factory(last_seg)
            or self.repo_symbols.is_fs_factory(imported_last_seg)
        ):
            return True
        return (
            name in self.fs_factories
            or imported in self.fs_factories
            or self._is_fs_class_name(name)
            or self._is_fs_class_name(imported)
            or bool(self._RE_FS_FACTORY_FUNC.match(last_seg))
            or bool(self._RE_FS_FACTORY_FUNC.match(imported_last_seg))
            or (
                (self._is_fs_module(name.split(".")[0]) or self._is_fs_module(imported.split(".")[0]))
                and (last_seg == "filesystem" or imported_last_seg == "filesystem")
            )
        )

    def _is_tuple_factory_name(self, name: str) -> bool:
        """Check if a function returns an (fs, path, ...) tuple."""
        imported = self.imports.get(name, name)
        last_seg = name.split(".")[-1]
        imported_last_seg = imported.split(".")[-1]
        if self.repo_symbols and (
            self.repo_symbols.is_tuple_factory(name)
            or self.repo_symbols.is_tuple_factory(imported)
        ):
            return True
        return (
            last_seg in ("url_to_fs", "get_fs_token_paths")
            or imported_last_seg in ("url_to_fs", "get_fs_token_paths")
        )

    def _is_open_factory_name(self, name: str) -> bool:
        """Check if a function opens file streams."""
        imported = self.imports.get(name, name)
        last_seg = name.split(".")[-1]
        imported_last_seg = imported.split(".")[-1]
        if self.repo_symbols and (
            self.repo_symbols.is_open_factory(name)
            or self.repo_symbols.is_open_factory(imported)
        ):
            return True
        if last_seg in ("open_files", "open_local", "open_file", "OpenFile", "open_parquet_file"):
            return True
        if imported_last_seg in ("open_files", "open_local", "open_file", "OpenFile", "open_parquet_file"):
            return True
        if (
            (self._is_fs_module(name.split(".")[0]) or self._is_fs_module(imported.split(".")[0]))
            and (last_seg in ("open", "open_async") or imported_last_seg in ("open", "open_async"))
        ):
            return True
        return False

    def infer_node_type(self, node: Optional[ast.AST]) -> InferredType:
        """Recursively infer the semantic type (FILESYSTEM, FILE_STREAM, FS_FACTORY, etc.) of an AST node."""
        if node is None:
            return InferredType.UNKNOWN

        # 1. Identifiers (ast.Name)
        if isinstance(node, ast.Name):
            name = node.id
            if name in self.filesystem_vars or bool(self._RE_FS_IDENTIFIER.match(name)):
                return InferredType.FILESYSTEM
            if name in self.file_vars or bool(self._RE_FILE_IDENTIFIER.match(name)):
                return InferredType.FILE_STREAM
            if self._is_tuple_factory_name(name):
                return InferredType.FS_TUPLE_FACTORY
            if self._is_open_factory_name(name):
                return InferredType.OPEN_FACTORY
            if self._is_fs_factory_name(name):
                return InferredType.FS_FACTORY
            if self._is_fs_module(name):
                return InferredType.FS_MODULE
            return InferredType.UNKNOWN

        # 2. Attribute access (ast.Attribute: e.g. self.fs, fsspec.open, fs.open, get_fs().ls)
        if isinstance(node, ast.Attribute):
            attr = node.attr
            val_type = self.infer_node_type(node.value)
            val_str = self._get_node_source(node.value)
            full_attr_str = self._get_node_source(node)

            # Attribute on a filesystem module: fsspec.filesystem, fsspec.open, fsspec.core.url_to_fs
            if val_type == InferredType.FS_MODULE or self._is_fs_module(val_str):
                if attr in ("filesystem",) or self._is_fs_class_name(attr) or self._is_fs_factory_name(attr):
                    return InferredType.FS_FACTORY
                if attr in ("url_to_fs", "get_fs_token_paths"):
                    return InferredType.FS_TUPLE_FACTORY
                if attr in ("open", "open_async", "open_files", "open_local", "open_file", "open_parquet_file"):
                    return InferredType.OPEN_FACTORY
                return InferredType.UNKNOWN

            # Explicit filesystem attribute naming on instances (self.fs, self._fs, obj.filesystem)
            if full_attr_str in self.filesystem_vars or bool(self._RE_FS_IDENTIFIER.match(attr)):
                return InferredType.FILESYSTEM

            # Explicit file stream attribute naming (self.stream, obj.fileobj)
            if full_attr_str in self.file_vars or bool(self._RE_FILE_IDENTIFIER.match(attr)):
                return InferredType.FILE_STREAM

            # Method access on a filesystem object: fs.open
            if val_type == InferredType.FILESYSTEM and attr in ("open", "open_async"):
                return InferredType.OPEN_FACTORY

            # Factory method on object (e.g. backend.get_filesystem(), client.resolve_fs())
            if self._is_fs_factory_name(attr):
                return InferredType.FS_FACTORY

            return InferredType.UNKNOWN

        # 3. Call expressions (ast.Call: e.g. get_filesystem(...), fsspec.filesystem(...), fs.open(...))
        if isinstance(node, ast.Call):
            func_type = self.infer_node_type(node.func)
            func_str = self._get_node_source(node.func)

            # Calling a filesystem factory produces a filesystem instance
            if func_type == InferredType.FS_FACTORY or self._is_fs_factory_name(func_str):
                return InferredType.FILESYSTEM

            # Calling an open factory produces a file stream
            if func_type == InferredType.OPEN_FACTORY or self._is_open_factory_name(func_str):
                return InferredType.FILE_STREAM

            # Calling .open() on a filesystem instance produces a file stream
            if isinstance(node.func, ast.Attribute) and node.func.attr in ("open", "open_async"):
                if self.infer_node_type(node.func.value) == InferredType.FILESYSTEM:
                    return InferredType.FILE_STREAM

            # Calling a tuple factory produces an FS tuple
            if func_type == InferredType.FS_TUPLE_FACTORY or self._is_tuple_factory_name(func_str):
                return InferredType.FS_TUPLE_FACTORY

            return InferredType.UNKNOWN

        # 4. Subscript indexing (ast.Subscript: e.g. url_to_fs(...)[0])
        if isinstance(node, ast.Subscript):
            val_type = self.infer_node_type(node.value)
            if val_type == InferredType.FS_TUPLE_FACTORY:
                # First element of url_to_fs or get_fs_token_paths is the filesystem instance
                if isinstance(node.slice, ast.Constant) and node.slice.value == 0:
                    return InferredType.FILESYSTEM
            return InferredType.UNKNOWN

        return InferredType.UNKNOWN

    # --------------------------------------------------------------------------
    # AST Node Visitors
    # --------------------------------------------------------------------------

    def visit_ClassDef(self, node: ast.ClassDef):
        """Track class context and filesystem subclass inheritance."""
        old_class = self.current_class
        self.current_class = node.name

        # If class inherits from a known filesystem class, self/cls are filesystems
        is_fs_subclass = False
        for base in node.bases:
            base_str = self._get_node_source(base)
            if self._is_fs_class_name(base_str):
                is_fs_subclass = True
                break

        if is_fs_subclass:
            self.filesystem_classes.add(node.name)
            self.filesystem_vars.add("self")
            self.filesystem_vars.add("cls")

        self.generic_visit(node)
        self.current_class = old_class

    def visit_FunctionDef(self, node: ast.FunctionDef):
        """Track function context, return type annotations, filesystem parameters, and local cache_type defaults."""
        old_func = self.current_function
        old_ct = getattr(self, "local_cache_type", None)
        self.current_function = node.name
        self.local_cache_type = None

        # Return type annotation: if function returns a FileSystem, register as an fs factory
        if node.returns:
            ret_str = self._get_node_source(node.returns)
            if self._is_fs_class_name(ret_str):
                self.fs_factories.add(node.name)

        # Inspect parameters for explicit filesystem and file stream variables
        for arg in node.args.args + node.args.kwonlyargs:
            if bool(self._RE_FS_IDENTIFIER.match(arg.arg)):
                self.filesystem_vars.add(arg.arg)
            elif bool(self._RE_FILE_IDENTIFIER.match(arg.arg)):
                self.file_vars.add(arg.arg)
            elif arg.annotation:
                ann_str = self._get_node_source(arg.annotation)
                if self._is_fs_class_name(ann_str):
                    self.filesystem_vars.add(arg.arg)
                elif "AbstractBufferedFile" in ann_str or "BinaryIO" in ann_str:
                    self.file_vars.add(arg.arg)

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
        """Track async function context and arguments."""
        self.visit_FunctionDef(node)

    def visit_Import(self, node: ast.Import):
        """Track module imports like `import fsspec` or `import gcsfs as gcs`."""
        for alias in node.names:
            local_name = alias.asname or alias.name
            self.imports[local_name] = alias.name
            if alias.name in self._KNOWN_FS_MODULES:
                self.filesystem_classes.add(local_name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        """Track from imports like `from fsspec.core import url_to_fs` or `from cloud_io import get_filesystem`."""
        module = node.module or ""
        for alias in node.names:
            local_name = alias.asname or alias.name
            full_name = f"{module}.{alias.name}" if module else alias.name
            self.imports[local_name] = full_name

            if self._is_fs_class_name(alias.name) or self._is_fs_class_name(full_name):
                self.filesystem_classes.add(local_name)
            elif self._is_fs_factory_name(alias.name) or self._is_fs_factory_name(full_name):
                self.fs_factories.add(local_name)
        self.generic_visit(node)

    def _track_assignment(self, targets: List[ast.AST], value: ast.AST):
        """Helper to track variable assignments from filesystem and file stream expressions."""
        val_type = self.infer_node_type(value)

        if val_type == InferredType.FILESYSTEM:
            for target in targets:
                var_name = self._get_node_source(target)
                if var_name:
                    self.filesystem_vars.add(var_name)

        elif val_type == InferredType.FILE_STREAM:
            for target in targets:
                var_name = self._get_node_source(target)
                if var_name:
                    self.file_vars.add(var_name)

        elif val_type == InferredType.FS_TUPLE_FACTORY:
            for target in targets:
                if isinstance(target, (ast.Tuple, ast.List)) and target.elts:
                    fs_var = self._get_node_source(target.elts[0])
                    if fs_var:
                        self.filesystem_vars.add(fs_var)
                else:
                    var_name = self._get_node_source(target)
                    if var_name:
                        self.filesystem_vars.add(var_name)

    def visit_Assign(self, node: ast.Assign):
        """Track filesystem assignments and dictionary cache_type assignments."""
        self._track_assignment(node.targets, node.value)

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

    def visit_AnnAssign(self, node: ast.AnnAssign):
        """Track annotated assignments: fs: GCSFileSystem = ..."""
        if node.value:
            self._track_assignment([node.target], node.value)
        if node.annotation:
            ann_str = self._get_node_source(node.annotation)
            if self._is_fs_class_name(ann_str):
                var_name = self._get_node_source(node.target)
                if var_name:
                    self.filesystem_vars.add(var_name)
        self.generic_visit(node)

    def visit_With(self, node: ast.With):
        """Track file handle variables in with statements (e.g. with fs.open(...) as f)."""
        for item in node.items:
            ctx_type = self.infer_node_type(item.context_expr)
            if ctx_type == InferredType.FILE_STREAM and item.optional_vars:
                var_name = self._get_node_source(item.optional_vars)
                if var_name:
                    self.file_vars.add(var_name)
        self.generic_visit(node)

    def visit_AsyncWith(self, node: ast.AsyncWith):
        """Track file handle variables in async with statements."""
        for item in node.items:
            ctx_type = self.infer_node_type(item.context_expr)
            if ctx_type == InferredType.FILE_STREAM and item.optional_vars:
                var_name = self._get_node_source(item.optional_vars)
                if var_name:
                    self.file_vars.add(var_name)
        self.generic_visit(node)

    def visit_For(self, node: ast.For):
        """Track file variables in for loops (e.g. for f in open_files(...) or for f in files)."""
        iter_type = self.infer_node_type(node.iter)
        iter_str = self._get_node_source(node.iter)
        if (
            iter_type == InferredType.FILE_STREAM
            or iter_str in self.file_vars
            or "open_files" in iter_str
        ):
            target_str = self._get_node_source(node.target)
            if target_str:
                self.file_vars.add(target_str)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call):
        """Analyze call sites for fsspec and filesystem usages using semantic type inference."""
        is_match = False
        target_name = ""

        # Case 1: Direct function calls (e.g. `open_files(...)`, `url_to_fs(...)`, `open(...)` from fsspec)
        if isinstance(node.func, ast.Name):
            func_id = node.func.id
            # Exclude class constructors (PascalCase names like ArrowFSWrapper, LocalFileSystem, OpenFile)
            if func_id and not func_id[0].isupper():
                imported_orig = self.imports.get(func_id, "")
                orig_name = imported_orig.split(".")[-1] if imported_orig else func_id
                if (
                    imported_orig.startswith(self._KNOWN_FS_MODULES)
                    and (orig_name in self.TARGET_FUNCTION_NAMES or orig_name in self.TARGET_OBJECT_METHODS or orig_name == "open")
                ):
                    is_match = True
                    if orig_name == "open" or orig_name in self.TARGET_OBJECT_METHODS:
                        target_name = f"fs.{orig_name}"
                    else:
                        target_name = orig_name
                elif func_id in {"url_to_fs", "get_fs_token_paths", "open_files", "open_local"}:
                    is_match = True
                    if func_id in ("open_files", "open_local"):
                        target_name = f"fs.{func_id}"
                    else:
                        target_name = func_id

        # Case 2: Attribute calls (e.g. `fsspec.open(...)`, `fs.open(...)`, `get_filesystem().mv(...)`, `f.read(...)`)
        elif isinstance(node.func, ast.Attribute):
            attr = node.func.attr
            # Exclude class constructors (PascalCase attribute names)
            if attr and not attr[0].isupper():
                receiver_type = self.infer_node_type(node.func.value)
                val_id = self._get_node_source(node.func.value)
                imported_orig = self.imports.get(val_id, val_id)

                # Subcase 2a: Module-level fsspec calls (fsspec.open, fsspec.core.url_to_fs)
                if receiver_type == InferredType.FS_MODULE or imported_orig in ("fsspec", "fsspec.core", "fsspec.parquet"):
                    if (
                        attr in self.TARGET_OBJECT_METHODS
                        or attr in self.TARGET_FUNCTION_NAMES
                        or attr in ("sync", "sync_wrapper")
                    ):
                        is_match = True
                        if attr == "open" or attr in self.TARGET_OBJECT_METHODS:
                            target_name = f"fs.{attr}"
                        elif attr in ("open_files", "open_local"):
                            target_name = f"fs.{attr}"
                        elif attr in ("url_to_fs", "get_fs_token_paths"):
                            target_name = attr
                        else:
                            target_name = f"fsspec.{attr}"

                # Subcase 2b: Filesystem instance calls (fs.open, self.fs.makedirs, get_filesystem().mv)
                elif receiver_type == InferredType.FILESYSTEM and attr in self.TARGET_OBJECT_METHODS:
                    is_match = True
                    target_name = f"fs.{attr}"

                # Subcase 2c: File stream handle calls (f.read, stream.seek, fileobj.close)
                elif receiver_type == InferredType.FILE_STREAM and attr in self.FILE_STREAM_METHODS:
                    is_match = True
                    target_name = f"f.{attr}"

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
