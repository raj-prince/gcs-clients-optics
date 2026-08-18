"""
Use Case 3: GitHub Issues Performance & Filesystem Bottleneck Tracking.
"""

from typing import Any, Dict, List, Optional

from gcs_clients_optics.issues.analyzer import IssuePerformanceAnalyzer
from gcs_clients_optics.issues.crawler import GitHubIssuesCrawler
from gcs_clients_optics.issues.models import GitHubIssue, IssueCrawlReport
from gcs_clients_optics.reporters.issue_reports import (
    export_issues_csv,
    export_issues_json,
    export_issues_markdown,
)
from gcs_clients_optics.usecases.base import BaseUseCase


class IssuesPerformanceUseCase(BaseUseCase):
    """
    Tracks and analyzes GitHub issues related to filesystem performance,
    latency, throughput, OOM, prefetching, and cloud storage bottlenecks.
    """

    name = "issues"
    description = (
        "Crawl and analyze GitHub issues for filesystem performance bottlenecks."
    )
    aliases = ["crawl-issues", "issues-performance", "perf-issues"]

    def __init__(self, analyzer: Optional[IssuePerformanceAnalyzer] = None):
        self.analyzer = analyzer or IssuePerformanceAnalyzer()

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[Any]:
        """Issue crawler works with issue JSON payloads rather than code ASTs."""
        return []

    def aggregate_report(
        self,
        target_source: str,
        total_files_scanned: int,
        files_with_usages: int,
        usages: List[GitHubIssue],
        repo_url: Optional[str] = None,
    ) -> IssueCrawlReport:
        """Aggregate GitHubIssue items into an IssueCrawlReport."""
        return IssueCrawlReport(
            target_repo=target_source,
            total_issues_scanned=total_files_scanned,
            matched_issues_count=len(usages),
            repo_url=repo_url or f"https://github.com/{target_source}",
            issues=usages,
        )

    def export_reports(
        self,
        reports: List[IssueCrawlReport],
        output_csv: Optional[str] = None,
        output_json: Optional[str] = None,
        output_md: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, str]:
        """Export matched issues in CSV, JSON, and Markdown formats."""
        generated: Dict[str, str] = {}

        if output_csv:
            export_issues_csv(reports, output_csv)
            generated["csv"] = output_csv

        if output_json:
            export_issues_json(
                reports,
                output_json,
                elapsed_seconds=kwargs.get("elapsed_seconds", 0.0),
            )
            generated["json"] = output_json

        if output_md:
            export_issues_markdown(reports, output_md)
            generated["markdown"] = output_md

        return generated

    def print_summary(self, reports: List[IssueCrawlReport]) -> None:
        """Print console overview of issues."""
        total_scanned = sum(r.total_issues_scanned for r in reports)
        total_matched = sum(r.matched_issues_count for r in reports)

        print("\n" + "=" * 70)
        print("  🐛 GITHUB ISSUES PERFORMANCE & STORAGE SUMMARY")
        print("=" * 70)
        print(f"  • Repositories Crawled: {len(reports)}")
        print(f"  • Total Issues Scanned: {total_scanned}")
        print(f"  • Matched Perf Issues:  {total_matched}")
        print("=" * 70)
