"""
GCS Clients Optics - Extensible AST code crawling, issue tracking, and filesystem analytics.
"""

__version__ = "0.1.0"

from gcs_clients_optics.reporters.categorization import (
    USAGE_PATTERNS,
    categorize_method,
)
from gcs_clients_optics.reporters.matrix import generate_method_matrix
from gcs_clients_optics.reporters.summary_table import generate_summary_table
from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.models import CrawlReport, FsspecUsage
from gcs_clients_optics.crawler.engine import (
    FsspecCrawlerEngine,
    OpticsEngine,
)
from gcs_clients_optics.usecases import (
    BaseUseCase,
    FsspecMethodsUseCase,
    get_use_case,
    list_use_cases,
    register_use_case,
)

__all__ = [
    "__version__",
    "OpticsEngine",
    "BaseUseCase",
    "FsspecMethodsUseCase",
    "register_use_case",
    "get_use_case",
    "list_use_cases",
    "FsspecASTVisitor",
    "FsspecCrawlerEngine",
    "FsspecUsage",
    "CrawlReport",
    "generate_method_matrix",
    "generate_summary_table",
    "USAGE_PATTERNS",
    "categorize_method",
]
