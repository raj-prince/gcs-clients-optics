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
    assert "scan" in captured.out
    assert "dependents" in captured.out


def test_cli_scan_local_file(tmp_path):
    sample_file = tmp_path / "read_sample.py"
    sample_file.write_text(
        "import fsspec\nwith fsspec.open('gs://b/f.parquet', 'rb', cache_type='mmap') as f:\n    f.read()\n",
        encoding="utf-8",
    )
    out_md = tmp_path / "methods_out.md"
    ret = main(["scan", "--local-file", str(sample_file), "--output-md", str(out_md)])
    assert ret == 0
    assert out_md.exists()
    assert "fsspec.open" in out_md.read_text(encoding="utf-8")


def test_cli_direct_invocation_shorthand(tmp_path):
    sample_file = tmp_path / "alias_sample.py"
    sample_file.write_text(
        "import fsspec\nfs = fsspec.filesystem('gcs')\nfs.ls('gs://bucket')\n",
        encoding="utf-8",
    )
    out_json = tmp_path / "alias_out.json"
    # Calling without typing 'scan' explicitly
    ret = main(["--local-file", str(sample_file), "--output-json", str(out_json)])
    assert ret == 0
    assert out_json.exists()


def test_cli_format_json_and_csv(tmp_path):
    sample_file = tmp_path / "sample.py"
    sample_file.write_text(
        "import fsspec\nwith fsspec.open('gs://b/f.csv', 'rb', cache_type='readahead') as f:\n    f.read()\n",
        encoding="utf-8",
    )
    # Test --format json with -o dir
    ret_json = main(
        [
            "scan",
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
            "scan",
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
