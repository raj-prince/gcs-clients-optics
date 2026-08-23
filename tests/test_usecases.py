"""
Unit tests for modular Use Cases and the generic OpticsEngine.
"""

import pytest
from gcs_clients_optics.crawler.engine import OpticsEngine
from gcs_clients_optics.usecases import (
    BaseUseCase,
    FsspecMethodsUseCase,
    get_use_case,
    list_use_cases,
    register_use_case,
)


def test_list_and_get_use_cases():
    cases = list_use_cases()
    names = [c.name for c in cases]
    assert "fsspec-methods" in names

    # Test alias resolution
    assert get_use_case("methods") is not None
    assert get_use_case("methods").name == "fsspec-methods"
    assert get_use_case("crawl-code") is not None
    assert get_use_case("code") is not None


def test_fsspec_methods_use_case_scan():
    code = """
import fsspec

def read_data(path):
    with fsspec.open(path, "rb", cache_type="mmap") as f:
        return f.read()

def write_data(path):
    with fsspec.open(path, "wb") as f:
        f.write(b"data")
"""
    uc = FsspecMethodsUseCase()
    engine = OpticsEngine(use_case=uc)
    items = engine.scan_code("test_fsspec.py", code)

    assert len(items) >= 2
    target_names = [i.target_name for i in items]
    assert "fs.open" in target_names
    assert "f.read" in target_names
    assert "f.write" in target_names


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


def test_fsspec_methods_reports_export(tmp_path):
    uc = FsspecMethodsUseCase()
    code = "import fsspec\nwith fsspec.open('gs://b/f', 'rb', cache_type='parts') as f:\n    f.read()"
    items = uc.scan_code("test.py", code)
    report = uc.aggregate_report(
        target_source="GitHub:dask/dask (main)",
        total_files_scanned=1,
        files_with_usages=1,
        usages=items,
        repo_url="https://github.com/dask/dask",
    )

    csv_path = tmp_path / "methods.csv"
    json_path = tmp_path / "methods.json"
    md_path = tmp_path / "methods.md"

    uc.export_reports(
        [report],
        output_csv=str(csv_path),
        output_json=str(json_path),
        output_md=str(md_path),
    )

    assert csv_path.exists()
    assert json_path.exists()
    assert md_path.exists()
    assert "fsspec.open" in md_path.read_text(encoding="utf-8")
