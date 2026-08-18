"""
GCS Clients Optics - AST code crawling, GitHub issues tracking, and filesystem analytics.
"""

__version__ = "0.1.0"

from gcs_clients_optics.analysis.categorization import (
    USAGE_PATTERNS,
    categorize_method,
)
from gcs_clients_optics.analysis.matrix import generate_method_matrix
from gcs_clients_optics.analysis.summary_table import generate_summary_table
from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.engine import FsspecCrawlerEngine
from gcs_clients_optics.crawler.models import CrawlReport, FsspecUsage
from gcs_clients_optics.issues.analyzer import IssuePerformanceAnalyzer
from gcs_clients_optics.issues.crawler import GitHubIssuesCrawler
from gcs_clients_optics.issues.models import GitHubIssue, IssueCrawlReport
from gcs_clients_optics.simulation.simulator import run_fsspec_simulation

__all__ = [
    "__version__",
    "FsspecASTVisitor",
    "FsspecCrawlerEngine",
    "FsspecUsage",
    "CrawlReport",
    "GitHubIssuesCrawler",
    "IssuePerformanceAnalyzer",
    "GitHubIssue",
    "IssueCrawlReport",
    "generate_method_matrix",
    "generate_summary_table",
    "run_fsspec_simulation",
    "USAGE_PATTERNS",
    "categorize_method",
]
