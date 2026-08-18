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

    ret_matrix = main(["matrix", "--input-json", str(report_file), "--output-md", str(matrix_out)])
    assert ret_matrix == 0
    assert matrix_out.exists()

    ret_summary = main(["summary", "--input-json", str(report_file), "--output-md", str(summary_out)])
    assert ret_summary == 0
    assert summary_out.exists()
