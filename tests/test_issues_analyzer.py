"""
Unit tests for GitHub issue performance analyzer and relevance scoring.
"""

import pytest
from gcs_clients_optics.issues.analyzer import IssuePerformanceAnalyzer


def test_issue_analyzer_performance_and_fs_match():
    analyzer = IssuePerformanceAnalyzer()
    raw_issue = {
        "number": 101,
        "title": "fsspec read is very slow with gcsfs readahead",
        "body": "When reading large parquet files using fsspec.open, the latency is high due to chunk_size buffering.",
        "html_url": "https://github.com/dask/dask/issues/101",
        "state": "open",
        "created_at": "2026-01-01T00:00:00Z",
        "updated_at": "2026-01-02T00:00:00Z",
        "labels": [{"name": "performance"}, {"name": "io"}],
        "user": {"login": "testuser"},
    }

    issue = analyzer.analyze_issue("dask/dask", raw_issue)
    assert issue is not None
    assert issue.issue_number == 101
    assert "fsspec" in issue.matched_fs_keywords
    assert "gcsfs" in issue.matched_fs_keywords
    assert "slow" in issue.matched_perf_keywords
    assert "latency" in issue.matched_perf_keywords
    assert issue.relevance_score > 10


def test_issue_analyzer_irrelevant_issue():
    analyzer = IssuePerformanceAnalyzer()
    raw_issue = {
        "number": 202,
        "title": "Fix typo in documentation README",
        "body": "There is a spelling mistake in the main title.",
        "html_url": "https://github.com/dask/dask/issues/202",
        "state": "open",
        "labels": [],
        "user": {"login": "docuser"},
    }

    issue = analyzer.analyze_issue("dask/dask", raw_issue)
    assert issue is None


def test_issue_analyzer_skip_pull_request():
    analyzer = IssuePerformanceAnalyzer()
    raw_issue = {
        "number": 303,
        "title": "fsspec performance optimization PR",
        "body": "Improves fsspec latency by 2x",
        "html_url": "https://github.com/dask/dask/pull/303",
        "state": "open",
        "pull_request": {
            "url": "https://api.github.com/repos/dask/dask/pulls/303"
        },
        "user": {"login": "contributor"},
    }

    issue = analyzer.analyze_issue("dask/dask", raw_issue)
    assert issue is None


def test_issue_analyzer_fsspec_repo_implicit_fs():
    analyzer = IssuePerformanceAnalyzer()
    raw_issue = {
        "number": 404,
        "title": "High memory leak during multi-threaded chunk download",
        "body": "Download stalls and causes throughput drop after 100MB.",
        "html_url": "https://github.com/fsspec/gcsfs/issues/404",
        "state": "open",
        "labels": [{"name": "perf"}],
        "user": {"login": "gcsuser"},
    }

    issue = analyzer.analyze_issue("fsspec/gcsfs", raw_issue)
    assert issue is not None
    assert "repo:fsspec" in issue.matched_fs_keywords
    assert (
        "memory leak" in issue.matched_perf_keywords
        or "throughput" in issue.matched_perf_keywords
    )
