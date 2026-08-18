"""
Unit tests for reports export, method distribution matrix, and summary table generators.
"""

import json
import pytest
from pathlib import Path
from gcs_clients_optics.analysis.matrix import generate_method_matrix
from gcs_clients_optics.analysis.summary_table import generate_summary_table
from gcs_clients_optics.crawler.models import CrawlReport, FsspecUsage
from gcs_clients_optics.issues.models import GitHubIssue, IssueCrawlReport
from gcs_clients_optics.reporters.code_reports import (
    export_csv_report,
    export_json_report,
    export_markdown_report,
)
from gcs_clients_optics.reporters.issue_reports import (
    export_issues_csv,
    export_issues_json,
    export_issues_markdown,
)


def test_code_reports_export(tmp_path):
    usage = FsspecUsage(
        file_path="dask/io.py",
        line_number=10,
        end_line_number=12,
        target_name="fsspec.open",
        cache_type="mmap",
        is_specified_cache_keyword=True,
        repo_url="https://github.com/dask/dask",
        file_url="https://github.com/dask/dask/blob/main/dask/io.py#L10",
        code_snippet="with fsspec.open(url, 'rb', cache_type='mmap'): pass",
    )
    report = CrawlReport(
        target_source="GitHub:dask/dask (main)",
        total_files_scanned=10,
        files_with_usages=1,
        total_usages_found=1,
        repo_url="https://github.com/dask/dask",
        cache_type_summary={"mmap": 1},
        usages=[usage],
    )

    csv_file = tmp_path / "code.csv"
    export_csv_report(report, str(csv_file))
    assert csv_file.exists()
    assert "dask/dask" in csv_file.read_text(encoding="utf-8")

    json_file = tmp_path / "code.json"
    export_json_report(report, str(json_file), elapsed_seconds=1.23)
    assert json_file.exists()
    json_data = json.loads(json_file.read_text(encoding="utf-8"))
    assert json_data["summary"]["total_repositories"] == 1

    md_file = tmp_path / "code.md"
    export_markdown_report(report, str(md_file))
    assert md_file.exists()
    assert "Master FSSPEC Usage Report" in md_file.read_text(encoding="utf-8")


def test_issues_reports_export(tmp_path):
    issue = GitHubIssue(
        repo_name="fsspec/gcsfs",
        issue_number=505,
        title="gcsfs read_block latency issue",
        html_url="https://github.com/fsspec/gcsfs/issues/505",
        state="open",
        created_at="2026-02-01T00:00:00Z",
        updated_at="2026-02-02T00:00:00Z",
        author="benchuser",
        labels=["perf", "gcs"],
        matched_fs_keywords=["gcsfs"],
        matched_perf_keywords=["latency", "slow"],
        relevance_score=18,
        body_snippet="read_block takes too long on GCS",
    )

    report = IssueCrawlReport(
        target_repo="fsspec/gcsfs",
        total_issues_scanned=10,
        matched_issues_count=1,
        repo_url="https://github.com/fsspec/gcsfs",
        issues=[issue],
    )

    csv_path = tmp_path / "issues.csv"
    export_issues_csv([report], str(csv_path))
    assert csv_path.exists()
    assert "gcsfs read_block latency issue" in csv_path.read_text(encoding="utf-8")

    json_path = tmp_path / "issues.json"
    export_issues_json([report], str(json_path))
    assert json_path.exists()

    md_path = tmp_path / "issues.md"
    export_issues_markdown([report], str(md_path))
    assert md_path.exists()
    assert "GitHub Issues Performance & FSSPEC Crawl Report" in md_path.read_text(
        encoding="utf-8"
    )


def test_matrix_and_summary_generation(tmp_path):
    sample_json_data = {
        "summary": {"total_repositories": 2},
        "per_repository": [
            {
                "target_source": "GitHub:dask/dask (main)",
                "usages": [
                    {
                        "target_name": "fsspec.open",
                        "code_snippet": "with fsspec.open(u): pass",
                    },
                    {
                        "target_name": "fs.exists",
                        "code_snippet": "if fs.exists(p): pass",
                    },
                ],
            },
            {
                "target_source": "GitHub:intake/intake (main)",
                "usages": [
                    {
                        "target_name": "fsspec.open",
                        "code_snippet": "with fsspec.open(u): pass",
                    }
                ],
            },
        ],
    }

    matrix_file = tmp_path / "matrix.md"
    matrix_md = generate_method_matrix(
        sample_json_data, output_path=str(matrix_file)
    )
    assert matrix_file.exists()
    assert "Complete Cross-Repository Method Distribution Matrix" in matrix_md
    assert "fsspec.open" in matrix_md
    assert "fs.exists" in matrix_md

    summary_file = tmp_path / "summary.md"
    summary_md = generate_summary_table(
        sample_json_data, output_path=str(summary_file)
    )
    assert summary_file.exists()
    assert "Complete 4-Column Summary Table" in summary_md
    assert "fsspec.open" in summary_md
