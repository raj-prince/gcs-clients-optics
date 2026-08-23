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
    assert len(usages) == 2
    u = usages[0]
    assert u.target_name == "fs.open"
    assert u.enclosing_function == "read_gcs"
    assert u.args == ["url", "'rb'"]
    assert u.cache_type == "NOT_EXPLICIT"
    assert u.line_number == 5
    assert usages[1].target_name == "f.read"


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
    assert u.target_name == "fsspec.open_parquet_file"
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
    assert len(usages) == 2
    u = usages[0]
    assert u.repo_url == "https://github.com/googleapis/python-bigquery"
    assert (
        u.file_url
        == "https://github.com/googleapis/python-bigquery/blob/main/google/cloud/bigquery/client.py#L5"
    )
    assert u.is_specified_cache_keyword is True
    assert usages[1].target_name == "f.read"


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
    assert len(usages) == 4

    assert usages[0].target_name == "fs.open"
    assert usages[0].cache_type == "mmap"
    assert usages[0].cache_options is None
    assert usages[1].target_name == "f.read"

    assert usages[2].target_name == "fs.open"
    assert usages[2].cache_type == "block"
    assert usages[2].cache_options == "{'block_size': 1048576}"
    assert usages[3].target_name == "f.read"


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
    assert u.target_name == "fs.open"
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
    assert len(usages) == 3
    assert usages[0].target_name == "fsspec.filesystem"
    assert usages[1].target_name == "fs.open"
    assert usages[2].target_name == "f.readlines"


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
    assert len(usages) == 2
    assert usages[0].target_name == "fs.open"
    assert usages[0].enclosing_function == "load_remote_dataset"
    assert usages[1].target_name == "f.read"


def test_tuple_unpacking_url_to_fs():
    code = """
from fsspec.core import url_to_fs

def read_custom(path):
    fs, clean_path = url_to_fs(path)
    return fs.cat_file(clean_path)
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("reader.py", code)
    # url_to_fs + fs.cat_file
    target_names = [u.target_name for u in usages]
    assert "url_to_fs" in target_names
    assert "fs.cat_file" in target_names


def test_alias_and_constructor_tracking():
    code = """
from gcsfs import GCSFileSystem
from fsspec.implementations.local import LocalFileSystem

def sync_data():
    gcs = GCSFileSystem(project="my-p")
    local = LocalFileSystem()
    
    # Aliasing
    target_fs = gcs
    
    data = target_fs.cat("gs://bucket/file.txt")
    local.mkdir("/tmp/dest")
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("sync.py", code)
    target_names = [u.target_name for u in usages]
    assert "fs.cat" in target_names
    assert "fs.mkdir" in target_names


def test_false_positive_rejection():
    code = """
def process_data(diffs, offsets, actor_refs, tensor):
    # None of these are filesystems, but 'diffs', 'offsets', 'actor_refs' contain substring 'fs'
    v1 = diffs.get("key")
    v2 = offsets.size()
    v3 = actor_refs.get(0)
    v4 = tensor.split(2)
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("ml.py", code)
    assert len(usages) == 0


def test_class_inheritance_filesystem_tracking():
    code = """
from fsspec import AbstractFileSystem

class CustomGCSAdapter(AbstractFileSystem):
    def read_custom(self, path):
        return self.cat_file(path)
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("adapter.py", code)
    target_names = [u.target_name for u in usages]
    assert "fs.cat_file" in target_names


def test_class_constructors_not_reported_as_methods():
    code = """
from dask.dataframe.io.utils import ArrowFSWrapper
from fsspec.implementations.local import LocalFileSystem
from fsspec.core import OpenFile
from gcsfs import GCSFileSystem

def build_storage():
    gcs = GCSFileSystem(project="p")
    local = LocalFileSystem()
    wrapped = ArrowFSWrapper(gcs)
    of = OpenFile(local, "file.txt")
    
    # Genuine method usages
    with local.open("data.csv", "rb") as f:
        return f.read()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("build.py", code)
    target_names = [u.target_name for u in usages]
    assert "fs.open" in target_names
    assert "f.read" in target_names
    assert "ArrowFSWrapper" not in target_names
    assert "LocalFileSystem" not in target_names
    assert "GCSFileSystem" not in target_names
    assert "OpenFile" not in target_names
    assert len(usages) == 2


def test_file_stream_handle_method_tracking():
    code = """
import fsspec

def read_chunks(fo):
    # fo as file stream parameter
    hdr = fo.read(16)
    fo.seek(0)
    fo.readinto(bytearray(1024))
    return hdr

def open_and_process(path):
    with fsspec.open(path, "rb") as f:
        f.seek(100)
        data = f.read(500)
        f.close()
        return data
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("stream.py", code)
    target_names = [u.target_name for u in usages]
    assert "f.read" in target_names
    assert "f.seek" in target_names
    assert "f.readinto" in target_names
    assert "fs.open" in target_names
    assert "f.close" in target_names


def test_import_aliasing_and_core_functions():
    code = """
from fsspec.core import url_to_fs as my_url_to_fs
from fsspec import open as my_open
from fsspec.core import get_fs_token_paths as resolve_paths

def pipeline(url, paths):
    fs, path = my_url_to_fs(url)
    with my_open(path, "rb") as f:
        data = f.read()
    
    fs2, tok, p_list = resolve_paths(paths)
    return fs2.info(p_list[0])
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("pipeline.py", code)
    target_names = [u.target_name for u in usages]
    assert "url_to_fs" in target_names
    assert "fs.open" in target_names
    assert "f.read" in target_names
    assert "get_fs_token_paths" in target_names
    assert "fs.info" in target_names


def test_module_aliases_and_negative_non_fsspec():
    code = """
import fsspec as fs_lib
import gcsfs as gcs
import pyarrow.fs as pa_fs

def init_drivers():
    fs1 = fs_lib.filesystem("gcs")
    fs2 = gcs.GCSFileSystem(project="test-proj")
    pa_driver = pa_fs.FileSystem()
    
    # Genuine fsspec calls
    fs1.ls("gs://bucket")
    fs2.cat_file("gs://bucket/data.txt")
    
    # PyArrow call should NOT be tracked as fsspec
    pa_driver.open_input_file("test.parquet")
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("drivers.py", code)
    target_names = [u.target_name for u in usages]
    assert "fsspec.filesystem" in target_names
    assert "fs.ls" in target_names
    assert "fs.cat_file" in target_names
    assert "pa_driver.open_input_file" not in target_names
    assert "open_input_file" not in target_names


def test_variable_chaining_and_stream_aliasing():
    code = """
import fsspec

def multi_alias_flow(path):
    primary_fs = fsspec.filesystem("gcs")
    secondary_fs = primary_fs
    tertiary_fs = secondary_fs
    
    with tertiary_fs.open(path, "rb") as stream_handle:
        reader = stream_handle
        header = reader.read(128)
        reader.seek(0)
        pos = reader.tell()
        
    out_file = tertiary_fs.open("gs://bucket/out.bin", "wb")
    out_file.write(b"data")
    out_file.close()
"""
    engine = FsspecCrawlerEngine()
    usages = engine.scan_code("chaining.py", code)
    target_names = [u.target_name for u in usages]
    assert "fsspec.filesystem" in target_names
    assert "fs.open" in target_names
    assert "f.read" in target_names
    assert "f.seek" in target_names
    assert "f.tell" in target_names
    assert "f.write" in target_names
    assert "f.close" in target_names




