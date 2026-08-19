"""
Unit tests for AST visitor and fsspec / filesystem usage extraction.
"""

try:
    import pytest
except ImportError:
    pytest = None
from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.engine import FsspecCrawlerEngine


def test_fsspec_direct_open():
    code = """
import fsspec

def read_gcs(url):
    with fsspec.open(url, "rb") as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("test.py", code)
    assert len(usages) == 1
    u = usages[0]
    assert u.target_name == "fsspec.open"
    assert u.enclosing_function == "read_gcs"
    assert u.args == ["url", "'rb'"]
    assert u.cache_type == "NOT_EXPLICIT"
    assert u.line_number == 5


def test_dask_kwargs_pop_parts_cache_type():
    code = """
import fsspec.parquet as fsspec_parquet

def _open_parquet_files(paths, fs=None, context_stack=None, **kwargs):
    cache_type = kwargs.pop("cache_type", "parts")
    if cache_type != "parts":
        raise ValueError()
    return [
        fsspec_parquet.open_parquet_file(
            path,
            fs=fs,
            **kwargs
        )
        for path in paths
    ]
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("dask/dataframe/io/utils.py", code)
    assert len(usages) == 1
    u = usages[0]
    assert u.target_name == "fsspec_parquet.open_parquet_file"
    assert u.cache_type == "parts"
    assert u.is_specified_cache_keyword is True


def test_repo_url_and_file_url():
    code = """
import fsspec

def read_parquet_mmap(url):
    with fsspec.open(url, "rb", cache_type="mmap") as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code(
        "google/cloud/bigquery/client.py",
        code,
        repo_url="https://github.com/googleapis/python-bigquery",
        branch="main",
    )
    assert len(usages) == 1
    u = usages[0]
    assert u.repo_url == "https://github.com/googleapis/python-bigquery"
    assert (
        u.file_url
        == "https://github.com/googleapis/python-bigquery/blob/main/google/cloud/bigquery/client.py#L5"
    )
    assert u.is_specified_cache_keyword is True


def test_cache_type_extraction():
    code = """
import fsspec

def read_parquet_mmap(url):
    with fsspec.open(url, "rb", cache_type="mmap") as f:
        return f.read()

def read_csv_block(url):
    with fsspec.open(url, "r", cache_type="block", cache_options={"block_size": 1048576}) as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("cache_test.py", code)
    assert len(usages) == 2

    assert usages[0].cache_type == "mmap"
    assert usages[0].cache_options is None

    assert usages[1].cache_type == "block"
    assert usages[1].cache_options == "{'block_size': 1048576}"


def test_fsspec_aliased_import():
    code = """
from fsspec import open as my_open

class Loader:
    def load(self, path):
        f = my_open(path, mode="w", compression="gzip", cache_type="none")
        return f
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("loader.py", code)
    assert len(usages) == 1
    u = usages[0]
    assert u.target_name == "my_open"
    assert u.enclosing_class == "Loader"
    assert u.enclosing_function == "load"
    assert u.cache_type == "none"
    assert u.kwargs == {
        "mode": "'w'",
        "compression": "'gzip'",
        "cache_type": "'none'",
    }


def test_filesystem_object_open():
    code = """
import fsspec

class BQHandler:
    def __init__(self):
        self.fs = fsspec.filesystem("gcs")
    
    def read_data(self, path):
        with self.fs.open(path, "r") as stream:
            return stream.readlines()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("bq_handler.py", code)
    assert len(usages) == 2
    assert usages[0].target_name == "fsspec.filesystem"
    u = usages[1]
    assert u.target_name == "self.fs.open"
    assert u.enclosing_class == "BQHandler"
    assert u.enclosing_function == "read_data"


def test_fsspec_url_to_fs():
    code = """
from fsspec.core import url_to_fs

def process_file(uri):
    fs, path = url_to_fs(uri)
    return fs
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("url_fs.py", code)
    assert len(usages) == 1
    u = usages[0]
    assert u.target_name == "url_to_fs"
    assert u.enclosing_function == "process_file"


def test_dict_subscript_cache_type_mmap():
    code = """
import fsspec

def main(args):
    open_kwargs = {}
    if args.cache_type is not None:
        open_kwargs["cache_type"] = args.cache_type
    else:
        open_kwargs["cache_type"] = "mmap"

    with fsspec.open(args.url, "rb", **open_kwargs) as f:
        pass
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("bench.py", code)
    assert len(usages) == 1
    assert usages[0].cache_type in ("mmap", "args.cache_type")
    assert (
        usages[0].is_specified_cache_keyword is True
        or usages[0].cache_type == "mmap"
    )


def test_builtin_open_ignored():
    code = """
import os

def load_config():
    with open(os.path.join("etc", "config.json"), "r") as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("config.py", code)
    assert len(usages) == 0


def test_imported_fsspec_open():
    code = """
from fsspec import open

def load_remote_dataset(url):
    with open(url, "rb") as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("dataset.py", code)
    assert len(usages) == 1
    assert usages[0].target_name == "open"
    assert usages[0].enclosing_function == "load_remote_dataset"

