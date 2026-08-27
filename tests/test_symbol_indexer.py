import pytest
from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.symbol_indexer import (
    RepoSymbolIndexer,
    RepoSymbolTable,
    build_repo_symbol_table,
    path_to_module_parts,
)


def test_path_to_module_parts():
    parts = path_to_module_parts("src/lightning/fabric/utilities/cloud_io.py")
    assert "lightning.fabric.utilities.cloud_io" in parts
    assert "cloud_io" in parts
    assert "fabric.utilities.cloud_io" in parts


def test_cross_file_symbol_indexing_and_resolution():
    # File A: Defines helper with non-standard name returning filesystem
    file_a = """
import fsspec
from fsspec.core import url_to_fs
from fsspec.implementations.local import AbstractFileSystem

def setup_checkpoint_backend(path: str) -> AbstractFileSystem:
    fs, _ = url_to_fs(path)
    return fs

def make_stream(path: str):
    return fsspec.open(path, "rb")
"""

    # File B: Imports helper from File A and invokes chained methods
    file_b = """
from my_pkg.storage.backend import setup_checkpoint_backend, make_stream

def run_backup(uri: str):
    # Cross-file resolved call without assignment
    setup_checkpoint_backend(uri).mv("source", "target")
    setup_checkpoint_backend(uri).exists("target")

    # Cross-file resolved stream
    with make_stream(uri) as handle:
        handle.read()
"""

    files_map = {
        "src/my_pkg/storage/backend.py": file_a,
        "src/my_pkg/pipelines/runner.py": file_b,
    }

    # Step 1: Build symbol table across in-memory files
    symbol_table = build_repo_symbol_table(files_map)
    assert symbol_table.is_fs_factory("setup_checkpoint_backend")
    assert symbol_table.is_fs_factory("my_pkg.storage.backend.setup_checkpoint_backend")
    assert symbol_table.is_open_factory("make_stream")

    # Step 2: Visit File B with symbol table
    visitor = FsspecASTVisitor(
        "src/my_pkg/pipelines/runner.py",
        file_b,
        repo_symbols=symbol_table,
    )
    import ast
    tree = ast.parse(file_b, filename="src/my_pkg/pipelines/runner.py")
    visitor.visit(tree)

    target_names = [u.target_name for u in visitor.usages]
    assert "fs.mv" in target_names
    assert "fs.exists" in target_names
    assert "f.read" in target_names


def test_custom_filesystem_subclass_cross_file():
    file_class = """
from fsspec.spec import AbstractFileSystem

class CustomDistributedFS(AbstractFileSystem):
    def __init__(self, cluster_id):
        pass
"""

    file_consumer = """
from my_pkg.fs.custom import CustomDistributedFS

def process():
    fs = CustomDistributedFS("cluster-1")
    fs.ls("gs://my-bucket")
"""

    files_map = {
        "my_pkg/fs/custom.py": file_class,
        "my_pkg/worker.py": file_consumer,
    }

    symbol_table = build_repo_symbol_table(files_map)
    assert symbol_table.is_fs_class("CustomDistributedFS")
    assert symbol_table.is_fs_class("my_pkg.fs.custom.CustomDistributedFS")

    import ast
    visitor = FsspecASTVisitor(
        "my_pkg/worker.py",
        file_consumer,
        repo_symbols=symbol_table,
    )
    tree = ast.parse(file_consumer, filename="my_pkg/worker.py")
    visitor.visit(tree)

    target_names = [u.target_name for u in visitor.usages]
    assert "fs.ls" in target_names
