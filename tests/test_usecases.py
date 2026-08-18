"""
Unit tests for modular Use Cases and the generic OpticsEngine.
"""

import pytest
from gcs_clients_optics.engine.optics_engine import OpticsEngine
from gcs_clients_optics.usecases import (
    BaseUseCase,
    CacheTypeUseCase,
    FsspecMethodsUseCase,
    IssuesPerformanceUseCase,
    ProtocolsUseCase,
    get_use_case,
    list_use_cases,
    register_use_case,
)


def test_list_and_get_use_cases():
    cases = list_use_cases()
    names = [c.name for c in cases]
    assert "fsspec-methods" in names
    assert "cache-type" in names
    assert "issues" in names
    assert "protocols" in names

    # Test alias resolution
    assert get_use_case("caching") is not None
    assert get_use_case("caching").name == "cache-type"
    assert get_use_case("methods") is not None
    assert get_use_case("methods").name == "fsspec-methods"
    assert get_use_case("storage") is not None
    assert get_use_case("storage").name == "protocols"


def test_cache_type_use_case_scan():
    code = """
import fsspec

def read_data(path):
    with fsspec.open(path, "rb", cache_type="mmap") as f:
        return f.read()

def read_stream(path):
    with fsspec.open(path, "r", cache_type="readahead", cache_options={"block_size": 8388608}) as f:
        return f.read()

def write_data(path):
    with fsspec.open(path, "wb") as f:
        f.write(b"data")
"""
    uc = CacheTypeUseCase()
    engine = OpticsEngine(use_case=uc)
    items = engine.scan_code("test_cache.py", code)

    assert len(items) >= 2
    # First item should be mmap
    assert any(i.cache_type == "mmap" and i.is_explicit for i in items)
    # Second item should be readahead with cache_options
    assert any(
        i.cache_type == "readahead" and i.cache_options is not None for i in items
    )


def test_protocols_use_case_scan():
    code = """
import fsspec
import gcsfs

def load_gcs_data():
    fs = gcsfs.GCSFileSystem(project="my-project")
    url1 = "gs://my-bucket/dataset/data.parquet"
    url2 = "s3://aws-bucket/data.csv"
    url3 = "abfs://azure-container/data.orc"
    return fs
"""
    uc = ProtocolsUseCase()
    engine = OpticsEngine(use_case=uc)
    items = engine.scan_code("test_proto.py", code)

    protocols = [i.protocol for i in items]
    assert "gs" in protocols
    assert "s3" in protocols
    assert "abfs" in protocols
    assert "gcs" in protocols or "gcsfs" in [i.context for i in items]


def test_custom_use_case_registration():
    class CustomCompressionUseCase(BaseUseCase):
        name = "compression-optics"
        description = "Analyzes compression codecs"
        aliases = ["compression"]

        def scan_code(self, file_path, source_code, repo_url=None, branch="main"):
            return [{"codec": "gzip", "file": file_path}]

        def aggregate_report(self, target_source, total_files_scanned, files_with_usages, usages, repo_url=None):
            return {"target": target_source, "codecs": usages}

        def export_reports(self, reports, **kwargs):
            return {}

    custom_uc = CustomCompressionUseCase()
    register_use_case(custom_uc)

    assert get_use_case("compression-optics") is custom_uc
    assert get_use_case("compression") is custom_uc

    engine = OpticsEngine(use_case=custom_uc)
    res = engine.scan_code("sample.py", "dummy")
    assert len(res) == 1
    assert res[0]["codec"] == "gzip"


def test_cache_type_reports_export(tmp_path):
    uc = CacheTypeUseCase()
    code = "import fsspec\nwith fsspec.open('gs://b/f', 'rb', cache_type='parts'): pass"
    items = uc.scan_code("test.py", code)
    report = uc.aggregate_report(
        target_source="GitHub:dask/dask (main)",
        total_files_scanned=1,
        files_with_usages=1,
        usages=items,
        repo_url="https://github.com/dask/dask",
    )

    csv_path = tmp_path / "cache.csv"
    json_path = tmp_path / "cache.json"
    md_path = tmp_path / "cache.md"

    uc.export_reports(
        [report],
        output_csv=str(csv_path),
        output_json=str(json_path),
        output_md=str(md_path),
    )

    assert csv_path.exists()
    assert json_path.exists()
    assert md_path.exists()
    assert "parts" in md_path.read_text(encoding="utf-8")
