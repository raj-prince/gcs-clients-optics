"""
GitHub and local code AST crawler package for filesystem & fsspec optics.
"""

from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.engine import (
    FsspecCrawlerEngine,
    OpticsEngine,
    is_relevant_python_file,
    is_relevant_source_or_manifest_file,
)
from gcs_clients_optics.crawler.models import (
    CrawlReport,
    FsspecUsage,
    SPECIFIED_CACHE_KEYWORDS,
)
from gcs_clients_optics.crawler.dependents import (
    DEFAULT_TARGET_REPOS,
    fetch_github_dependents_html,
    get_default_target_repos,
    load_repos_from_file,
)
from gcs_clients_optics.crawler.regex_scanner import RegexFallbackScanner

__all__ = [
    "FsspecASTVisitor",
    "FsspecCrawlerEngine",
    "OpticsEngine",
    "is_relevant_python_file",
    "is_relevant_source_or_manifest_file",
    "FsspecUsage",
    "CrawlReport",
    "SPECIFIED_CACHE_KEYWORDS",
    "RegexFallbackScanner",
    "DEFAULT_TARGET_REPOS",
    "get_default_target_repos",
    "load_repos_from_file",
    "fetch_github_dependents_html",
]
