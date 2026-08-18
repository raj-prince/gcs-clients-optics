"""
Unit tests for crawler engine (local scans, regex fallback, etc.).
"""

import pytest
from pathlib import Path
from gcs_clients_optics.crawler.engine import FsspecCrawlerEngine
from gcs_clients_optics.crawler.models import CrawlReport


def test_syntax_error_fallback():
    invalid_code = """
import fsspec
def broken_func(
    with fsspec.open("gs://bucket/file.csv", cache_type="readahead") as f:
        pass
"""
    engine = FsspecCrawlerEngine(use_regex_fallback=True)
    usages = engine.scan_code("broken.py", invalid_code)
    assert len(usages) >= 1
    assert usages[0].detection_method == "regex"
    assert usages[0].cache_type == "readahead"


def test_scan_local_file(tmp_path):
    sample_file = tmp_path / "test_read.py"
    sample_file.write_text(
        "import fsspec\nwith fsspec.open('gs://data/file.parquet', 'rb', cache_type='mmap') as f:\n    pass\n",
        encoding="utf-8",
    )

    engine = FsspecCrawlerEngine()
    usages = engine.scan_local_file(str(sample_file))
    assert len(usages) == 1
    assert usages[0].target_name == "fsspec.open"
    assert usages[0].cache_type == "mmap"


def test_scan_local_directory(tmp_path):
    dir1 = tmp_path / "module_a"
    dir1.mkdir()
    (dir1 / "reader.py").write_text(
        "import fsspec\nwith fsspec.open('gs://b/1.csv'): pass\n",
        encoding="utf-8",
    )
    (dir1 / "helper.py").write_text(
        "from fsspec.core import url_to_fs\nfs, p = url_to_fs('s3://b/2.csv')\n",
        encoding="utf-8",
    )
    (dir1 / "test_reader.py").write_text(
        "import fsspec\nwith fsspec.open('file://dummy'): pass\n",
        encoding="utf-8",
    )

    engine = FsspecCrawlerEngine(include_tests=False)
    report = engine.scan_local_directory(str(tmp_path))

    assert report.total_files_scanned == 2
    assert report.files_with_usages == 2
    assert report.total_usages_found == 2


def test_scan_local_directory_multi(tmp_path):
    from gcs_clients_optics.engine.optics_engine import OpticsEngine
    from gcs_clients_optics.usecases import (
        AsyncSyncUseCase,
        CacheTypeUseCase,
        FsspecMethodsUseCase,
        ProtocolsUseCase,
    )

    src_dir = tmp_path / "src"
    src_dir.mkdir()
    (src_dir / "worker.py").write_text(
        "import fsspec\n"
        "async def fetch():\n"
        "    with fsspec.open('gs://my-bucket/data.csv', 'rb', cache_type='readahead') as f:\n"
        "        pass\n"
        "    await fs._cat_file('s3://backup/data.csv')\n",
        encoding="utf-8",
    )

    use_cases = [
        FsspecMethodsUseCase(),
        CacheTypeUseCase(),
        ProtocolsUseCase(),
        AsyncSyncUseCase(),
    ]
    engine = OpticsEngine(use_case=use_cases[0])
    reports = engine.scan_local_directory_multi(str(src_dir), use_cases)

    assert "fsspec-methods" in reports
    assert "cache-type" in reports
    assert "protocols" in reports
    assert "async-sync" in reports

    # Check that fsspec methods were found
    assert reports["fsspec-methods"].total_usages_found >= 1

    # Check that cache_type was found
    assert reports["cache-type"].total_read_calls >= 1

    # Check that protocols were found (gs:// and s3://)
    assert reports["protocols"].total_protocol_usages >= 2

    # Check that async vs sync calls were found
    assert reports["async-sync"].total_usages_found >= 2


def test_scan_github_repo_archive_tarball(monkeypatch):
    """Test that archive fallback downloads tarball and scans Python files."""
    import io
    import tarfile
    from gcs_clients_optics.engine.optics_engine import OpticsEngine
    from gcs_clients_optics.usecases.fsspec_methods import FsspecMethodsUseCase

    # Create a mock tarball in memory
    tar_stream = io.BytesIO()
    with tarfile.open(fileobj=tar_stream, mode="w:gz") as tar:
        code = b"import fsspec\nwith fsspec.open('gs://test/data.csv'): pass\n"
        ti = tarfile.TarInfo(name="myrepo-main/lib/reader.py")
        ti.size = len(code)
        tar.addfile(ti, io.BytesIO(code))

        # Non-python or test file
        test_code = b"def test_foo(): pass\n"
        ti2 = tarfile.TarInfo(name="myrepo-main/tests/test_reader.py")
        ti2.size = len(test_code)
        tar.addfile(ti2, io.BytesIO(test_code))

    tar_bytes = tar_stream.getvalue()

    class MockResponse:
        status = 200
        def read(self):
            return tar_bytes
        def __enter__(self):
            return self
        def __exit__(self, *args):
            pass

    import urllib.request
    monkeypatch.setattr(urllib.request, "urlopen", lambda *args, **kwargs: MockResponse())

    uc = FsspecMethodsUseCase()
    engine = OpticsEngine(use_case=uc, include_tests=False)
    reports = engine._scan_github_repo_via_archive("custom/myrepo", [uc], branch="main")

    assert reports is not None
    assert "fsspec-methods" in reports
    rep = reports["fsspec-methods"]
    assert rep.total_files_scanned == 1
    assert rep.files_with_usages == 1
    assert rep.total_usages_found == 1


def test_scan_github_repo_multi_falls_back_on_403(monkeypatch):
    """Test that scan_github_repo_multi falls back to archive if tree API returns 403."""
    import io
    import tarfile
    import urllib.error
    from gcs_clients_optics.engine.optics_engine import OpticsEngine
    from gcs_clients_optics.usecases.fsspec_methods import FsspecMethodsUseCase

    tar_stream = io.BytesIO()
    with tarfile.open(fileobj=tar_stream, mode="w:gz") as tar:
        code = b"import fsspec\nfs = fsspec.filesystem('gcs')\n"
        ti = tarfile.TarInfo(name="rate-limited-main/core.py")
        ti.size = len(code)
        tar.addfile(ti, io.BytesIO(code))

    tar_bytes = tar_stream.getvalue()

    def mock_urlopen(req, timeout=None):
        url = req.full_url if hasattr(req, "full_url") else str(req)
        if "api.github.com" in url:
            raise urllib.error.HTTPError(
                url, 403, "Rate Limit Exceeded",
                hdrs={"x-ratelimit-remaining": "0"}, fp=None
            )
        class MockResp:
            status = 200
            def read(self):
                return tar_bytes
            def __enter__(self):
                return self
            def __exit__(self, *args):
                pass
        return MockResp()

    import urllib.request
    monkeypatch.setattr(urllib.request, "urlopen", mock_urlopen)

    uc = FsspecMethodsUseCase()
    engine = OpticsEngine(use_case=uc)
    reports = engine.scan_github_repo_multi("test-org/rate-limited", [uc], branch="main")

    assert "fsspec-methods" in reports
    assert reports["fsspec-methods"].total_files_scanned == 1
    assert reports["fsspec-methods"].total_usages_found == 1

