"""
Use Case 1: FSSPEC & Abstract Filesystem Method Usage Analysis across codebases.
"""

import ast
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from gcs_clients_optics.analysis.matrix import generate_method_matrix
from gcs_clients_optics.analysis.summary_table import generate_summary_table
from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.models import CrawlReport, FsspecUsage
from gcs_clients_optics.crawler.regex_scanner import RegexFallbackScanner
from gcs_clients_optics.reporters.code_reports import (
    export_csv_report,
    export_json_report,
    export_markdown_report,
)
from gcs_clients_optics.usecases.base import BaseUseCase


class FsspecMethodsUseCase(BaseUseCase):
    """
    Analyzes all abstract filesystem API usages (open, exists, info, ls, glob,
    find, walk, makedirs, get, put, etc.) across target codebases.
    """

    name = "fsspec-methods"
    description = (
        "Analyze all fsspec and abstract filesystem API method calls across repositories."
    )
    aliases = ["methods", "fsspec", "crawl-code", "code"]

    def __init__(self, use_regex_fallback: bool = True):
        self.use_regex_fallback = use_regex_fallback

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[FsspecUsage]:
        """Scan Python code for abstract filesystem method usages."""
        try:
            tree = ast.parse(source_code, filename=file_path)
            visitor = FsspecASTVisitor(
                file_path, source_code, repo_url=repo_url, branch=branch
            )
            visitor.visit(tree)
            return visitor.usages
        except SyntaxError:
            if self.use_regex_fallback:
                return RegexFallbackScanner.scan_content(
                    file_path, source_code, repo_url=repo_url, branch=branch
                )
            return []
        except Exception:
            return []

    def aggregate_report(
        self,
        target_source: str,
        total_files_scanned: int,
        files_with_usages: int,
        usages: List[FsspecUsage],
        repo_url: Optional[str] = None,
    ) -> CrawlReport:
        """Aggregate usages into a CrawlReport."""
        summary: Dict[str, int] = {}
        for u in usages:
            summary[u.cache_type] = summary.get(u.cache_type, 0) + 1

        return CrawlReport(
            target_source=target_source,
            total_files_scanned=total_files_scanned,
            files_with_usages=files_with_usages,
            total_usages_found=len(usages),
            repo_url=repo_url,
            cache_type_summary=summary,
            usages=usages,
        )

    def export_reports(
        self,
        reports: List[CrawlReport],
        output_csv: Optional[str] = None,
        output_json: Optional[str] = None,
        output_md: Optional[str] = None,
        matrix_md: Optional[str] = None,
        summary_md: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, str]:
        """Export CSV, JSON, Markdown, Matrix, and Summary reports."""
        generated: Dict[str, str] = {}

        if output_csv:
            export_csv_report(reports, output_csv)
            generated["csv"] = output_csv

        if output_json:
            export_json_report(
                reports, output_json, elapsed_seconds=kwargs.get("elapsed_seconds", 0.0)
            )
            generated["json"] = output_json

        if output_md:
            export_markdown_report(
                reports,
                output_md,
                include_tests=kwargs.get("include_tests", False),
            )
            generated["markdown"] = output_md

        # Generate matrix and summary table if requested or if output_json is present
        if matrix_md and output_json and Path(output_json).exists():
            generate_method_matrix(output_json, output_path=matrix_md)
            generated["matrix"] = matrix_md

        if summary_md and output_json and Path(output_json).exists():
            generate_summary_table(output_json, output_path=summary_md)
            generated["summary"] = summary_md

        return generated

    def print_summary(self, reports: List[CrawlReport]) -> None:
        """Print method usage overview."""
        total_files = sum(r.total_files_scanned for r in reports)
        total_matched_files = sum(r.files_with_usages for r in reports)
        total_usages = sum(r.total_usages_found for r in reports)

        print("\n" + "=" * 70)
        print("  📊 FSSPEC METHODS USAGE SUMMARY")
        print("=" * 70)
        print(f"  • Total Targets Scanned: {len(reports)}")
        print(f"  • Total Files Scanned:   {total_files}")
        print(f"  • Files with Usages:     {total_matched_files}")
        print(f"  • Total Method Calls:    {total_usages}")
        print("=" * 70)
