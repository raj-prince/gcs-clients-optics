"""
GCS Clients Optics - Extensible AST code crawling, issue tracking, and filesystem analytics.
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
from gcs_clients_optics.engine.optics_engine import OpticsEngine
from gcs_clients_optics.issues.analyzer import IssuePerformanceAnalyzer
from gcs_clients_optics.issues.crawler import GitHubIssuesCrawler
from gcs_clients_optics.issues.models import GitHubIssue, IssueCrawlReport
from gcs_clients_optics.simulation.simulator import run_fsspec_simulation
from gcs_clients_optics.storage.sqlite_store import (
    init_db,
    ingest_cache_reports,
    ingest_fsspec_reports,
    ingest_issue_reports,
    ingest_json_report,
    ingest_protocol_reports,
)
from gcs_clients_optics.usecases import (
    BaseUseCase,
    CacheTypeUseCase,
    FsspecMethodsUseCase,
    IssuesPerformanceUseCase,
    ProtocolsUseCase,
    get_use_case,
    list_use_cases,
    register_use_case,
)

__all__ = [
    "__version__",
    "OpticsEngine",
    "BaseUseCase",
    "FsspecMethodsUseCase",
    "CacheTypeUseCase",
    "IssuesPerformanceUseCase",
    "ProtocolsUseCase",
    "register_use_case",
    "get_use_case",
    "list_use_cases",
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
    "init_db",
    "ingest_fsspec_reports",
    "ingest_cache_reports",
    "ingest_protocol_reports",
    "ingest_issue_reports",
    "ingest_json_report",
]
