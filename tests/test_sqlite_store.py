"""
Unit tests for SQLite storage and ingestion engine.
"""

import json
import sqlite3
import pytest
from gcs_clients_optics.cli import main
from gcs_clients_optics.storage.sqlite_store import (
    init_db,
    ingest_cache_reports,
    ingest_fsspec_reports,
    ingest_issue_reports,
    ingest_json_report,
    ingest_protocol_reports,
)
from gcs_clients_optics.usecases import (
    CacheTypeUseCase,
    FsspecMethodsUseCase,
    IssuesPerformanceUseCase,
    ProtocolsUseCase,
)


def test_init_db_creates_tables_and_indexes(tmp_path):
    db_path = tmp_path / "test.db"
    conn = init_db(db_path)

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = {row[0] for row in cursor.fetchall()}

    assert "scan_runs" in tables
    assert "method_usages" in tables
    assert "cache_usages" in tables
    assert "protocol_usages" in tables
    assert "issues" in tables

    conn.close()


def test_ingest_fsspec_reports(tmp_path):
    db_path = tmp_path / "fsspec.db"
    uc = FsspecMethodsUseCase()
    code = "import fsspec\nwith fsspec.open('gs://b/f', 'rb', cache_type='readahead') as f:\n    f.readinto(buf)"
    usages = uc.scan_code("sample.py", code)
    report = uc.aggregate_report("Local:sample.py", 1, 1, usages)

    inserted = ingest_fsspec_reports([report], db_path)
    assert inserted >= 1

    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute("SELECT target_name, base_method, category, cache_type FROM method_usages;")
    rows = cursor.fetchall()
    conn.close()

    assert len(rows) >= 1
    assert any(r[1] in ("open", "readinto") for r in rows)


def test_ingest_json_report(tmp_path):
    json_path = tmp_path / "report.json"
    db_path = tmp_path / "ingested.db"

    json_data = {
        "summary": {},
        "per_repository": [
            {
                "target_source": "GitHub:dask/dask",
                "repo_url": "https://github.com/dask/dask",
                "total_files_scanned": 10,
                "usages": [
                    {
                        "file_path": "dask/array/core.py",
                        "line_number": 100,
                        "target_name": "fs.open",
                        "cache_type": "mmap",
                        "code_snippet": "with fs.open(p) as f:",
                    }
                ],
            }
        ],
    }
    json_path.write_text(json.dumps(json_data), encoding="utf-8")

    count = ingest_json_report(json_path, db_path)
    assert count == 1

    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    cursor.execute("SELECT repository, target_name, cache_type, category FROM method_usages;")
    rows = cursor.fetchall()
    conn.close()

    assert len(rows) == 1
    assert rows[0][0] == "dask/dask"
    assert rows[0][1] == "fs.open"
    assert rows[0][2] == "mmap"
    assert rows[0][3] == "Stream Reading & Writing"


def test_cli_ingest_subcommand(tmp_path):
    json_path = tmp_path / "sample_report.json"
    db_path = tmp_path / "cli_test.db"

    json_data = {
        "per_repository": [
            {
                "target_source": "GitHub:huggingface/datasets",
                "usages": [
                    {
                        "file_path": "src/load.py",
                        "line_number": 50,
                        "target_name": "open_files",
                        "code_snippet": "open_files(paths)",
                    }
                ],
            }
        ]
    }
    json_path.write_text(json.dumps(json_data), encoding="utf-8")

    ret = main(["ingest", "--input", str(json_path), "--db", str(db_path)])
    assert ret == 0
    assert db_path.exists()


def test_cli_scan_with_sqlite_output(tmp_path):
    sample_file = tmp_path / "code.py"
    sample_file.write_text("import fsspec\nfs = fsspec.filesystem('gcs')\n", encoding="utf-8")
    db_path = tmp_path / "output.db"

    ret = main(
        [
            "fsspec-methods",
            "--local-file",
            str(sample_file),
            "--format",
            "sqlite",
            "-o",
            str(db_path),
        ]
    )
    assert ret == 0
    assert db_path.exists()
