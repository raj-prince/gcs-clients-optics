"""
Tests for repository dependents loader and discovery.
"""

import json
from pathlib import Path
import pytest

from gcs_clients_optics.crawler.dependents import load_repos_from_file


def test_load_github_dependents_info_json(tmp_path: Path):
    """Test parsing github-dependents-info standard JSON format."""
    data = {
        "public_dependents_number": 1200,
        "public_dependents_stars": 50000,
        "packages": [
            {
                "name": "fsspec",
                "public_dependents_number": 1200,
                "public_dependents_stars": 50000,
                "public_dependents": [
                    {"name": "dask/dask", "stars": 12000},
                    {"name": "huggingface/datasets", "stars": 18000},
                    {"name": "tiny-project/tiny", "stars": 5},
                ],
            }
        ],
    }
    dep_file = tmp_path / "dependents.json"
    dep_file.write_text(json.dumps(data), encoding="utf-8")

    # All repos
    repos = load_repos_from_file(dep_file)
    assert len(repos) == 3
    # Sorted by stars: datasets (18k), dask (12k), tiny (5)
    assert repos[0] == ("datasets", "huggingface/datasets")
    assert repos[1] == ("dask", "dask/dask")
    assert repos[2] == ("tiny", "tiny-project/tiny")

    # Filter by min_stars
    starred = load_repos_from_file(dep_file, min_stars=100)
    assert len(starred) == 2
    assert ("tiny", "tiny-project/tiny") not in starred

    # Limit
    limited = load_repos_from_file(dep_file, limit=1)
    assert len(limited) == 1
    assert limited[0] == ("datasets", "huggingface/datasets")


def test_load_json_list_of_objects(tmp_path: Path):
    """Test parsing flat JSON list of repository objects."""
    data = [
        {"name": "ray-project/ray", "stars": 30000},
        {"repo": "zarr-developers/zarr-python", "stars": 1500},
        {"full_name": "iterative/dvc", "stars": 13000},
    ]
    dep_file = tmp_path / "repos.json"
    dep_file.write_text(json.dumps(data), encoding="utf-8")

    repos = load_repos_from_file(dep_file, min_stars=2000)
    assert len(repos) == 2
    assert repos[0] == ("ray", "ray-project/ray")
    assert repos[1] == ("dvc", "iterative/dvc")


def test_load_json_list_of_strings(tmp_path: Path):
    """Test parsing simple JSON string array."""
    data = ["dask/dask", "pydata/xarray", "apache/arrow"]
    dep_file = tmp_path / "simple_list.json"
    dep_file.write_text(json.dumps(data), encoding="utf-8")

    repos = load_repos_from_file(dep_file)
    assert len(repos) == 3
    assert ("arrow", "apache/arrow") in repos


def test_load_plain_text_file(tmp_path: Path):
    """Test parsing text file with comments and repo paths."""
    text_content = """
    # Major dependents
    dask/dask
    huggingface/datasets
    # Another one
    Lightning-AI/pytorch-lightning
    """
    dep_file = tmp_path / "repos.txt"
    dep_file.write_text(text_content, encoding="utf-8")

    repos = load_repos_from_file(dep_file)
    assert len(repos) == 3
    assert ("dask", "dask/dask") in repos
    assert ("datasets", "huggingface/datasets") in repos
    assert ("pytorch-lightning", "Lightning-AI/pytorch-lightning") in repos


def test_get_default_target_repos():
    """Test loading default curated target repos from data/default_dependents.json."""
    from gcs_clients_optics.crawler.repos import get_default_target_repos

    repos = get_default_target_repos(min_stars=5000)
    assert len(repos) >= 5
    repo_slugs = [r for _, r in repos]
    assert "pytorch/pytorch" in repo_slugs
    assert "dask/dask" in repo_slugs


def test_cli_repo_accepts_file_path(tmp_path: Path, monkeypatch):
    """Test that CLI --repo accepts a file path to dependents JSON or text."""
    from gcs_clients_optics.cli import _resolve_target_repos
    import argparse

    dep_file = tmp_path / "custom_dependents.json"
    dep_file.write_text(
        json.dumps([{"name": "custom/repo1", "stars": 500}, {"name": "custom/repo2", "stars": 100}]),
        encoding="utf-8",
    )

    args = argparse.Namespace(
        repo=[str(dep_file)],
        all=False,
        dependents_file=None,
        repos_file=None,
        dependents_of=None,
        min_stars=200,
        limit=None,
    )

    resolved = _resolve_target_repos(args, [])
    assert resolved == ["custom/repo1"]

