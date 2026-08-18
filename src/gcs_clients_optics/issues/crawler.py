"""
GitHub Issues REST API Crawler and batch scanner.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Dict, List, Optional, Set

from gcs_clients_optics.issues.analyzer import IssuePerformanceAnalyzer
from gcs_clients_optics.issues.models import GitHubIssue, IssueCrawlReport


class GitHubIssuesCrawler:
    """Engine that fetches issues from GitHub REST API and filters them."""

    def __init__(
        self,
        github_token: Optional[str] = None,
        max_issues_per_repo: int = 200,
        fs_keywords: Optional[Set[str]] = None,
        perf_keywords: Optional[Set[str]] = None,
        perf_labels: Optional[Set[str]] = None,
    ):
        self.github_token = github_token or os.getenv("GITHUB_TOKEN")
        self.max_issues_per_repo = max_issues_per_repo
        self.analyzer = IssuePerformanceAnalyzer(
            fs_keywords, perf_keywords, perf_labels
        )

    def _make_request(self, url: str) -> Optional[Any]:
        """Execute HTTP GET request to GitHub API with headers."""
        headers = {
            "User-Agent": "GCS-Clients-Optics-Issues-Crawler",
            "Accept": "application/vnd.github.v3+json",
        }
        if self.github_token:
            headers["Authorization"] = f"token {self.github_token}"

        req = urllib.request.Request(url, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 403:
                print(
                    f"GitHub API Rate Limit Exceeded or Forbidden for {url}",
                    file=sys.stderr,
                )
            elif e.code != 404:
                print(
                    f"HTTP Error {e.code} for {url}: {e.reason}",
                    file=sys.stderr,
                )
            return None
        except Exception as e:
            print(f"Failed to fetch {url}: {e}", file=sys.stderr)
            return None

    def crawl_repository_issues(
        self, repo_name: str, state: str = "open"
    ) -> IssueCrawlReport:
        """
        Fetch and filter issues for a GitHub repository.
        e.g. repo_name = 'dask/dask' or 'fsspec/gcsfs'
        """
        repo_url = f"https://github.com/{repo_name}"
        scanned_issues = 0
        matched_issues: List[GitHubIssue] = []

        page = 1
        per_page = 100

        while scanned_issues < self.max_issues_per_repo:
            api_url = (
                f"https://api.github.com/repos/{repo_name}/issues"
                f"?state={state}&per_page={per_page}&page={page}"
            )
            raw_data = self._make_request(api_url)

            if not raw_data or not isinstance(raw_data, list) or len(raw_data) == 0:
                break

            for issue_raw in raw_data:
                scanned_issues += 1
                parsed_issue = self.analyzer.analyze_issue(repo_name, issue_raw)
                if parsed_issue:
                    matched_issues.append(parsed_issue)

            if len(raw_data) < per_page:
                break

            page += 1

        # Sort matched issues by relevance score descending
        matched_issues.sort(key=lambda x: x.relevance_score, reverse=True)

        return IssueCrawlReport(
            target_repo=repo_name,
            total_issues_scanned=scanned_issues,
            matched_issues_count=len(matched_issues),
            repo_url=repo_url,
            issues=matched_issues,
        )

    def crawl_multiple_repositories(
        self,
        target_repos: List[str],
        state: str = "open",
        max_workers: int = 5,
        progress_callback: Optional[Callable[[str, IssueCrawlReport], None]] = None,
    ) -> List[IssueCrawlReport]:
        """Crawl issues concurrently across multiple repositories."""

        def _crawl_one(repo: str) -> IssueCrawlReport:
            report = self.crawl_repository_issues(repo, state=state)
            if progress_callback:
                progress_callback(repo, report)
            return report

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            return list(executor.map(_crawl_one, target_repos))
