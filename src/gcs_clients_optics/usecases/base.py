"""
Base abstraction for GCS Clients Optics use cases.
"""

import abc
import argparse
from typing import Any, Dict, List, Optional


class BaseUseCase(abc.ABC):
    """
    Abstract base class for all Optics analysis use cases.
    Each use case encapsulates its AST visitor/scanner, models, aggregation,
    and domain-specific reporting formats.
    """

    name: str = ""
    description: str = ""
    aliases: List[str] = []

    @abc.abstractmethod
    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[Any]:
        """Scan a single Python source string and return detected usage items."""
        pass

    @abc.abstractmethod
    def aggregate_report(
        self,
        target_source: str,
        total_files_scanned: int,
        files_with_usages: int,
        usages: List[Any],
        repo_url: Optional[str] = None,
    ) -> Any:
        """Aggregate file-level usages into a target-level summary report."""
        pass

    @abc.abstractmethod
    def export_reports(
        self,
        reports: List[Any],
        output_csv: Optional[str] = None,
        output_json: Optional[str] = None,
        output_md: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, str]:
        """Export domain-specific reports in CSV, JSON, and Markdown formats."""
        pass

    def print_summary(self, reports: List[Any]) -> None:
        """Print console summary after crawling/analysis."""
        pass

    def add_cli_arguments(self, parser: argparse.ArgumentParser) -> None:
        """Add use-case specific CLI arguments (optional override)."""
        pass
