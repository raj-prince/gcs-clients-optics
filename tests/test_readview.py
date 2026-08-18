"""
Unit tests for ReadView & Zero-Copy buffer ownership use case.
"""

import sqlite3
import tempfile
from pathlib import Path

import pytest

from gcs_clients_optics.cli import main
from gcs_clients_optics.storage.sqlite_store import init_db
from gcs_clients_optics.usecases.readview import ReadViewASTVisitor, ReadViewUseCase


SAMPLE_SAFE_CONSUMER_CODE = """
import fsspec
import json
import numpy as np
import torch

def parse_config(path):
    with fsspec.open(path, "rb") as f:
        # 1. Immediate in-place consumer: json.loads
        config = json.loads(f.read())
    return config

def load_weights(path):
    fs = fsspec.filesystem("gs")
    # 2. Immediate in-place consumer: torch.frombuffer
    tensor = torch.frombuffer(fs.cat_file(path), dtype=torch.float32)
    return tensor

def decode_text(path):
    with fsspec.open(path, "rb") as f:
        # 3. Chained transformation
        text = f.read().decode("utf-8")
    return text

def local_transient(path):
    with fsspec.open(path, "rb") as f:
        # 4. Local transient variable
        raw = f.read()
        processed = len(raw)
    return processed
"""

SAMPLE_ESCAPING_CODE = """
import fsspec

def get_raw_stream(path):
    with fsspec.open(path, "rb") as f:
        # 1. Direct return (escapes scope)
        return f.read()

class DataLoader:
    def __init__(self):
        self.cached_bytes = None

    def cache_dataset(self, path):
        fs = fsspec.filesystem("gs")
        # 2. Direct attribute assignment (escapes scope)
        self.cached_bytes = fs.cat_file(path)

    def load_transient_but_escape(self, path):
        with fsspec.open(path, "rb") as f:
            data = f.read()
            # 3. Variable returned (escapes scope)
            return data
"""


def test_readview_ast_visitor_safe_consumers():
    uc = ReadViewUseCase()
    candidates = uc.scan_code("test_safe.py", SAMPLE_SAFE_CONSUMER_CODE)

    assert len(candidates) == 4
    # All 4 in SAMPLE_SAFE_CONSUMER_CODE should be safe / descoped
    for c in candidates:
        assert c.is_descoped is True
        assert c.is_zero_copy_ready is True

    # Check specific consumer categories
    categories = [c.consumer_category for c in candidates]
    assert "JSON_LOADS" in categories
    assert "TORCH_FROMBUFFER" in categories
    assert "CHAINED_TRANSFORMATION" in categories
    assert "DESCUPED_LOCAL_VARIABLE" in categories


def test_readview_ast_visitor_escaping_buffers():
    uc = ReadViewUseCase()
    candidates = uc.scan_code("test_escape.py", SAMPLE_ESCAPING_CODE)

    assert len(candidates) == 3
    # All 3 in SAMPLE_ESCAPING_CODE escape scope
    for c in candidates:
        assert c.is_descoped is False
        assert c.is_zero_copy_ready is False

    categories = [c.consumer_category for c in candidates]
    assert "ESCAPING_RETURN" in categories
    assert "ESCAPING_ATTRIBUTE" in categories
    assert "ESCAPING_LOCAL_VAR" in categories


def test_readview_aggregate_and_export(tmp_path: Path):
    uc = ReadViewUseCase()
    cands_safe = uc.scan_code("test_safe.py", SAMPLE_SAFE_CONSUMER_CODE)
    cands_escape = uc.scan_code("test_escape.py", SAMPLE_ESCAPING_CODE)

    report_safe = uc.aggregate_report("TargetSafe", 1, 1, cands_safe)
    report_escape = uc.aggregate_report("TargetEscape", 1, 1, cands_escape)

    assert report_safe.total_read_calls == 4
    assert report_safe.zero_copy_ready_calls == 4
    assert report_safe.descoped_percentage == 100.0

    assert report_escape.total_read_calls == 3
    assert report_escape.zero_copy_ready_calls == 0
    assert report_escape.descoped_percentage == 0.0

    out_csv = tmp_path / "readview.csv"
    out_json = tmp_path / "readview.json"
    out_md = tmp_path / "readview.md"
    out_db = tmp_path / "optics.db"

    exported = uc.export_reports(
        [report_safe, report_escape],
        output_csv=str(out_csv),
        output_json=str(out_json),
        output_md=str(out_md),
        output_sqlite=str(out_db),
    )

    assert out_csv.exists()
    assert out_json.exists()
    assert out_md.exists()
    assert out_db.exists()

    # Verify SQLite data
    conn = sqlite3.connect(str(out_db))
    rows = conn.execute(
        "SELECT repository, target_name, is_zero_copy_ready, consumer_category FROM readview_candidates;"
    ).fetchall()
    conn.close()

    assert len(rows) == 7
    ready_count = sum(1 for r in rows if r[2] == 1)
    assert ready_count == 4


def test_cli_readview_local_file(tmp_path: Path):
    sample_file = tmp_path / "sample_reader.py"
    sample_file.write_text(SAMPLE_SAFE_CONSUMER_CODE, encoding="utf-8")
    out_db = tmp_path / "cli_readview.db"

    ret = main([
        "readview",
        "-f", str(sample_file),
        "-t", "sqlite",
        "-o", str(out_db),
    ])
    assert ret == 0
    assert out_db.exists()

    conn = sqlite3.connect(str(out_db))
    count = conn.execute("SELECT COUNT(*) FROM readview_candidates;").fetchone()[0]
    conn.close()
    assert count == 4
