"""
Unit tests for crawler engine (local scans, regex fallback, etc.).
"""

import pytest
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
    assert usages[0].target_name == "fs.open"
    assert usages[0].cache_type == "mmap"


def test_crawler_engine_alias_and_variable_tracking():
    from gcs_clients_optics.usecases.fsspec_methods import FsspecMethodsUseCase

    code = """
import fsspec as fs_alias
from fsspec.core import url_to_fs as my_url_resolver

def process_stream(blob_url):
    fs, path = my_url_resolver(blob_url)
    assigned_fs = fs
    with assigned_fs.open(path, "rb") as stream_reader:
        handle = stream_reader
        data = handle.read(1024)
        handle.seek(0)
        pos = handle.tell()
        return data
"""
    use_case = FsspecMethodsUseCase()
    usages = use_case.scan_code("sample_proc.py", code)
    target_names = [u.target_name for u in usages]

    assert "url_to_fs" in target_names
    assert "fs.open" in target_names
    assert "f.read" in target_names
    assert "f.seek" in target_names
    assert "f.tell" in target_names
    assert len(usages) == 5


def test_scan_github_repo_archive_tarball(monkeypatch):
    """Test that archive fallback downloads tarball and scans Python files."""
    import io
    import tarfile
    from gcs_clients_optics.crawler.engine import OpticsEngine
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
    from gcs_clients_optics.crawler.engine import OpticsEngine
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


def test_crawler_engine_archive_scan_with_aliases_and_variables(monkeypatch):
    """Test archive scanning with import aliases, variable chains, and stream methods."""
    import io
    import tarfile
    import urllib.request
    from gcs_clients_optics.crawler.engine import OpticsEngine
    from gcs_clients_optics.usecases import FsspecMethodsUseCase

    code = (
        "import fsspec.parquet as f_parquet\n"
        "from fsspec.core import url_to_fs as my_url_to_fs\n"
        "def run_pipeline():\n"
        "    fs, path = my_url_to_fs('gs://bucket/data.parquet')\n"
        "    backend = fs\n"
        "    with backend.open(path, 'rb', cache_type='mmap') as stream:\n"
        "        chunk = stream.read(512)\n"
        "    fs.cat_file('gs://backup/meta.json')\n"
    ).encode("utf-8")

    tar_stream = io.BytesIO()
    with tarfile.open(fileobj=tar_stream, mode="w:gz") as tar:
        ti = tarfile.TarInfo(name="repo-main/io/pipeline.py")
        ti.size = len(code)
        tar.addfile(ti, io.BytesIO(code))

    tar_bytes = tar_stream.getvalue()

    def mock_urlopen(req, timeout=None):
        url = req.full_url if hasattr(req, "full_url") else str(req)
        if "api.github.com" in url:
            raise urllib.error.HTTPError(
                url, 403, "Rate Limit",
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

    monkeypatch.setattr(urllib.request, "urlopen", mock_urlopen)

    use_case = FsspecMethodsUseCase()
    engine = OpticsEngine(use_case=use_case)
    reports = engine.scan_github_repo_multi("test-org/repo", [use_case], branch="main")

    fsspec_rep = reports["fsspec-methods"]
    assert fsspec_rep.total_usages_found >= 3
    method_names = [u.target_name for u in fsspec_rep.usages]
    assert "url_to_fs" in method_names
    assert "fs.open" in method_names
    assert "f.read" in method_names
    assert "fs.cat_file" in method_names



