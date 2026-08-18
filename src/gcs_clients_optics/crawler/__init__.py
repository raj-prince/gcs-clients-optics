"""
GitHub and local code AST crawler package for filesystem & fsspec optics.
"""

from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.engine import FsspecCrawlerEngine
from gcs_clients_optics.crawler.models import (
    CrawlReport,
    FsspecUsage,
    SPECIFIED_CACHE_KEYWORDS,
)
from gcs_clients_optics.crawler.regex_scanner import RegexFallbackScanner
from gcs_clients_optics.crawler.repos import DEFAULT_TARGET_REPOS

__all__ = [
    "FsspecASTVisitor",
    "FsspecCrawlerEngine",
    "FsspecUsage",
    "CrawlReport",
    "SPECIFIED_CACHE_KEYWORDS",
    "RegexFallbackScanner",
    "DEFAULT_TARGET_REPOS",
]
