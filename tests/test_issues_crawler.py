"""
Unit tests for GitHub issues crawler.
"""

import pytest
from unittest.mock import patch, MagicMock
from gcs_clients_optics.issues.crawler import GitHubIssuesCrawler


def test_issues_crawler_with_mocked_response():
    mock_issues = [
        {
            "number": 1,
            "title": "Slow gcsfs fsspec read throughput",
            "body": "Download is slow with high latency.",
            "html_url": "https://github.com/dask/dask/issues/1",
            "state": "open",
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-02T00:00:00Z",
            "labels": [{"name": "perf"}],
            "user": {"login": "user1"},
        },
        {
            "number": 2,
            "title": "Update README docs",
            "body": "Fix typo",
            "html_url": "https://github.com/dask/dask/issues/2",
            "state": "open",
            "labels": [],
            "user": {"login": "user2"},
        },
    ]

    crawler = GitHubIssuesCrawler()

    with patch.object(crawler, "_make_request", return_value=mock_issues):
        report = crawler.crawl_repository_issues("dask/dask")
        assert report.target_repo == "dask/dask"
        assert report.total_issues_scanned == 2
        assert report.matched_issues_count == 1
        assert report.issues[0].issue_number == 1
