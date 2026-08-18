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
