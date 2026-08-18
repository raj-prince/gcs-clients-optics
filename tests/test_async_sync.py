"""
Unit tests for Use Case 5: Async vs Sync Filesystem Method Usage.
"""

import json
import sqlite3
from pathlib import Path
from gcs_clients_optics.cli import main
from gcs_clients_optics.storage.sqlite_store import (
    init_db,
    ingest_async_sync_reports,
)
from gcs_clients_optics.usecases.async_sync import (
    AsyncSyncASTVisitor,
    AsyncSyncUseCase,
)


def test_async_vs_sync_ast_visitor():
    code = """
import fsspec
from fsspec.asyn import sync, AsyncFileSystem

# 1. Sync blocking call in sync function
def sync_worker():
    fs = fsspec.filesystem('gcs')
    with fs.open('gs://bucket/file.txt', 'rb') as f:
        data = f.readinto(buf)
    fs.ls('gs://bucket/')

# 2. Async coroutines and context managers
async def async_worker():
    fs = fsspec.filesystem('gcs', asynchronous=True)
    async with fsspec.open_async('gs://bucket/file.txt', 'rb') as f:
        data = await f.read()
    files = await fs._cat_file('gs://bucket/file.txt')
    # 3. Anti-pattern: Sync blocking call inside async def
    blocking_data = fs.open('gs://bucket/blocking.txt')

# 4. Async bridge
def bridge_worker(loop):
    result = sync(loop, fs._cat_file, 'gs://bucket/file.txt')
"""
    uc = AsyncSyncUseCase()
    usages = uc.scan_code("sample_async.py", code)

    assert len(usages) >= 6

    # Verify sync calls
    sync_calls = [u for u in usages if u.execution_mode == "sync"]
    assert len(sync_calls) >= 3
    assert any(u.base_method == "open" for u in sync_calls)
    assert any(u.base_method == "readinto" for u in sync_calls)

    # Verify async calls
    async_calls = [u for u in usages if u.execution_mode == "async"]
    assert len(async_calls) >= 3
    assert any(u.base_method == "_cat_file" for u in async_calls)
    assert any(u.async_mechanism in ("async_with", "await_expression") for u in async_calls)
    assert any(u.async_mechanism == "async_fs_init" for u in async_calls)

    # Verify potential event loop blocking detection
    blocking_calls = [u for u in usages if u.potential_event_loop_block]
    assert len(blocking_calls) >= 1
    assert any(u.base_method == "open" and u.is_async_context for u in blocking_calls)


def test_async_sync_aggregation_and_report():
    uc = AsyncSyncUseCase()
    code = """
async def fetch_data():
    await fs._cat_file('gs://bucket/a.txt')
    fs.ls('gs://bucket/')
"""
    usages = uc.scan_code("worker.py", code)
    report = uc.aggregate_report("Local:worker.py", 1, 1, usages)

    assert report.total_usages_found == 2
    assert report.async_count == 1
    assert report.sync_count == 1
    assert report.async_pct == 50.0
    assert report.potential_blocks_count == 1


def test_async_sync_exports(tmp_path):
    uc = AsyncSyncUseCase()
    code = "async def run(): await fs._cat_file('p')\n"
    usages = uc.scan_code("run.py", code)
    report = uc.aggregate_report("Local:run.py", 1, 1, usages)

    csv_path = str(tmp_path / "report.csv")
    json_path = str(tmp_path / "report.json")
    md_path = str(tmp_path / "report.md")
    db_path = str(tmp_path / "optics.db")

    generated = uc.export_reports(
        [report],
        output_csv=csv_path,
        output_json=json_path,
        output_md=md_path,
        output_sqlite=db_path,
    )

    assert Path(csv_path).exists()
    assert Path(json_path).exists()
    assert Path(md_path).exists()
    assert Path(db_path).exists()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT target_name, execution_mode, async_mechanism FROM async_sync_usages;")
    rows = cursor.fetchall()
    conn.close()

    assert len(rows) == 1
    assert rows[0][0] == "fs._cat_file"
    assert rows[0][1] == "async"


def test_cli_async_sync_command(tmp_path):
    sample_file = tmp_path / "sample.py"
    sample_file.write_text(
        "async def fetch():\n    await fs._cat_file('gs://b/f')\n", encoding="utf-8"
    )
    json_out = tmp_path / "async_sync.json"

    ret = main(
        [
            "async-sync",
            "--local-file",
            str(sample_file),
            "--format",
            "json",
            "-o",
            str(json_out),
        ]
    )
    assert ret == 0
    assert json_out.exists()
