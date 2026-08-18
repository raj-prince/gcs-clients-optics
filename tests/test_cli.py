"""
Unit tests for CLI parser and subcommands.
"""

import pytest
from unittest.mock import patch
from gcs_clients_optics.cli import build_parser, main


def test_cli_help(capsys):
    parser = build_parser()
    with pytest.raises(SystemExit) as exc:
        parser.parse_args(["--help"])
    assert exc.value.code == 0
    captured = capsys.readouterr()
    assert "gcs-optics" in captured.out


def test_cli_list_usecases(capsys):
    ret = main(["list-usecases"])
    assert ret == 0
    captured = capsys.readouterr()
    assert "fsspec-methods" in captured.out
    assert "cache-type" in captured.out
    assert "issues" in captured.out
    assert "protocols" in captured.out


def test_cli_simulate_subcommand():
    ret = main(["simulate", "--quiet"])
    assert ret == 0


def test_cli_matrix_and_summary_subcommands(tmp_path):
    report_file = tmp_path / "report.json"
    report_file.write_text(
        '{"summary": {}, "per_repository": [{"target_source": "GitHub:test/repo", "usages": [{"target_name": "fs.open"}]}]}',
        encoding="utf-8",
    )
    matrix_out = tmp_path / "matrix.md"
    summary_out = tmp_path / "summary.md"

    ret_matrix = main(
        [
            "matrix",
            "--input-json",
            str(report_file),
            "--output-md",
            str(matrix_out),
        ]
    )
    assert ret_matrix == 0
    assert matrix_out.exists()

    ret_summary = main(
        [
            "summary",
            "--input-json",
            str(report_file),
            "--output-md",
            str(summary_out),
        ]
    )
    assert ret_summary == 0
    assert summary_out.exists()


def test_cli_cache_type_local_file(tmp_path):
    sample_file = tmp_path / "read_sample.py"
    sample_file.write_text(
        "import fsspec\nwith fsspec.open('gs://b/f.parquet', 'rb', cache_type='mmap'): pass\n",
        encoding="utf-8",
    )
    out_md = tmp_path / "cache_out.md"
    ret = main(["cache-type", "--local-file", str(sample_file), "--output-md", str(out_md)])
    assert ret == 0
    assert out_md.exists()


def test_cli_protocols_local_file(tmp_path):
    sample_file = tmp_path / "proto_sample.py"
    sample_file.write_text(
        "url = 'gs://bucket/data.parquet'\nurl2 = 's3://aws/file.csv'\n",
        encoding="utf-8",
    )
    out_md = tmp_path / "proto_out.md"
    ret = main(["protocols", "--local-file", str(sample_file), "--output-md", str(out_md)])
    assert ret == 0
    assert out_md.exists()


def test_cli_format_json_and_csv(tmp_path):
    sample_file = tmp_path / "sample.py"
    sample_file.write_text(
        "import fsspec\nwith fsspec.open('gs://b/f.csv', 'rb', cache_type='readahead'): pass\n",
        encoding="utf-8",
    )
    # Test --format json with -o dir
    ret_json = main(
        [
            "fsspec-methods",
            "--local-file",
            str(sample_file),
            "--format",
            "json",
            "-o",
            str(tmp_path),
        ]
    )
    assert ret_json == 0
    assert (tmp_path / "fsspec_methods.json").exists()

    # Test --format csv with -o file.csv
    csv_file = tmp_path / "custom.csv"
    ret_csv = main(
        [
            "cache-type",
            "--local-file",
            str(sample_file),
            "--format",
            "csv",
            "-o",
            str(csv_file),
        ]
    )
    assert ret_csv == 0
    assert csv_file.exists()


def test_cli_issues_format_json(tmp_path):
    mock_issues = [
        {
            "number": 1,
            "title": "Slow gcsfs read",
            "body": "latency is slow",
            "html_url": "https://github.com/dask/dask/issues/1",
            "state": "open",
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-02T00:00:00Z",
            "labels": [{"name": "perf"}],
            "user": {"login": "user1"},
        }
    ]
    with patch("gcs_clients_optics.issues.crawler.GitHubIssuesCrawler._make_request", return_value=mock_issues):
        json_out = tmp_path / "issues.json"
        ret = main(["issues", "--repo", "dask/dask", "--format", "json", "-o", str(json_out)])
        assert ret == 0
        assert json_out.exists()
