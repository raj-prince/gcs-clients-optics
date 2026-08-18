"""
Unit tests for Dependency Versions use case.
"""

import sqlite3
from pathlib import Path

import pytest

from gcs_clients_optics.cli import main
from gcs_clients_optics.usecases.dependencies import (
    DependencyVersionsUseCase,
    parse_dependency_line,
)


SAMPLE_REQUIREMENTS_TXT = """
# Core storage dependencies
fsspec>=2023.1.0
gcsfs~=2024.2.0
s3fs==2023.9.2
adlfs
pyarrow>=14.0.0, <17.0.0
numpy>=1.24.0
"""

SAMPLE_PYPROJECT_TOML = """
[project]
name = "my-ml-app"
dependencies = [
    "fsspec[gcs] >= 2024.1.0",
    "google-cloud-storage == 2.14.0",
    "torch >= 2.0.0",
]
"""


def test_parse_dependency_lines():
    item1 = parse_dependency_line("fsspec>=2023.1.0", "requirements.txt", 1)
    assert item1 is not None
    assert item1.package_name == "fsspec"
    assert item1.specifier == ">=2023.1.0"
    assert item1.constraint_type == "minimum"

    item2 = parse_dependency_line("gcsfs~=2024.2.0", "requirements.txt", 2)
    assert item2 is not None
    assert item2.package_name == "gcsfs"
    assert item2.specifier == "~=2024.2.0"
    assert item2.constraint_type == "compatible"

    item3 = parse_dependency_line("s3fs==2023.9.2", "requirements.txt", 3)
    assert item3 is not None
    assert item3.package_name == "s3fs"
    assert item3.specifier == "==2023.9.2"
    assert item3.constraint_type == "pinned"

    item4 = parse_dependency_line("adlfs", "requirements.txt", 4)
    assert item4 is not None
    assert item4.package_name == "adlfs"
    assert item4.specifier == "*"
    assert item4.constraint_type == "unconstrained"

    item5 = parse_dependency_line("numpy>=1.24.0", "requirements.txt", 5)
    # numpy is not in TARGET_PACKAGES
    assert item5 is None


def test_dependency_scan_and_export(tmp_path: Path):
    uc = DependencyVersionsUseCase()
    items_req = uc.scan_code("requirements.txt", SAMPLE_REQUIREMENTS_TXT)
    items_toml = uc.scan_code("pyproject.toml", SAMPLE_PYPROJECT_TOML)

    assert len(items_req) == 5  # fsspec, gcsfs, s3fs, adlfs, pyarrow
    assert len(items_toml) == 2  # fsspec, google-cloud-storage

    report_req = uc.aggregate_report("TargetReq", 1, 1, items_req)
    report_toml = uc.aggregate_report("TargetToml", 1, 1, items_toml)

    out_csv = tmp_path / "deps.csv"
    out_json = tmp_path / "deps.json"
    out_md = tmp_path / "deps.md"
    out_db = tmp_path / "optics.db"

    exported = uc.export_reports(
        [report_req, report_toml],
        output_csv=str(out_csv),
        output_json=str(out_json),
        output_md=str(out_md),
        output_sqlite=str(out_db),
    )

    assert out_csv.exists()
    assert out_json.exists()
    assert out_md.exists()
    assert out_db.exists()

    conn = sqlite3.connect(str(out_db))
    rows = conn.execute(
        "SELECT repository, package_name, specifier, constraint_type FROM dependency_versions;"
    ).fetchall()
    conn.close()

    assert len(rows) == 7
    pkgs = [r[1] for r in rows]
    assert "fsspec" in pkgs
    assert "gcsfs" in pkgs
    assert "google-cloud-storage" in pkgs


def test_cli_dependencies_local_file(tmp_path: Path):
    req_file = tmp_path / "requirements.txt"
    req_file.write_text(SAMPLE_REQUIREMENTS_TXT, encoding="utf-8")
    out_db = tmp_path / "cli_deps.db"

    ret = main([
        "dependencies",
        "-f", str(req_file),
        "-t", "sqlite",
        "-o", str(out_db),
    ])
    assert ret == 0
    assert out_db.exists()

    conn = sqlite3.connect(str(out_db))
    count = conn.execute("SELECT COUNT(*) FROM dependency_versions;").fetchone()[0]
    conn.close()
    assert count == 5
