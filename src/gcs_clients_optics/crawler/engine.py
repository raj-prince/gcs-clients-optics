"""
Crawling and analysis engine for local files, directories, and remote GitHub repositories.
"""

import ast
import os
from pathlib import Path
from typing import Dict, List, Optional

from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.models import CrawlReport, FsspecUsage
from gcs_clients_optics.crawler.regex_scanner import RegexFallbackScanner
from gcs_clients_optics.engine.optics_engine import is_relevant_python_file


class FsspecCrawlerEngine:
    """Engine that manages AST scanning of local code and remote GitHub repositories."""

    def __init__(
        self,
        use_regex_fallback: bool = True,
        include_tests: bool = False,
        github_token: Optional[str] = None,
        max_workers: int = 32,
    ):
        self.use_regex_fallback = use_regex_fallback
        self.include_tests = include_tests
        self.github_token = github_token or os.getenv("GITHUB_TOKEN")
        self.max_workers = max_workers

    def _build_cache_type_summary(self, usages: List[FsspecUsage]) -> Dict[str, int]:
        """Summarize count of each cache_type found in usages."""
        summary: Dict[str, int] = {}
        for u in usages:
            summary[u.cache_type] = summary.get(u.cache_type, 0) + 1
        return summary

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[FsspecUsage]:
        """Scan a single Python source code string."""
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

    def scan_local_file(self, file_path: str) -> List[FsspecUsage]:
        """Scan a single local Python file."""
        p = Path(file_path)
        if not p.exists() or not p.is_file():
            return []
        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
            return self.scan_code(str(p), content)
        except Exception:
            return []

    def scan_local_directory(self, dir_path: str) -> CrawlReport:
        """Scan all Python files within a local directory tree."""
        root = Path(dir_path).resolve()
        py_files = []
        for p in root.rglob("*.py"):
            rel_str = str(p.relative_to(root))
            if is_relevant_python_file(rel_str, include_tests=self.include_tests):
                py_files.append(p)

        all_usages: List[FsspecUsage] = []
        files_with_usages = 0

        for p in py_files:
            rel_path = str(p.relative_to(root))
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
                usages = self.scan_code(rel_path, content)
                if usages:
                    files_with_usages += 1
                    all_usages.extend(usages)
            except Exception:
                continue

        summary = self._build_cache_type_summary(all_usages)
        return CrawlReport(
            target_source=f"Local:{root.name}",
            total_files_scanned=len(py_files),
            files_with_usages=files_with_usages,
            total_usages_found=len(all_usages),
            repo_url=None,
            cache_type_summary=summary,
            usages=all_usages,
        )

    def scan_github_repo(self, repo_name: str, branch: str = "main") -> CrawlReport:
        """
        Crawl a remote GitHub repository via GitHub Trees API and scan all Python files.
        Automatically uses exponential backoff and zero-quota archive fallback on rate limits.
        """
        from gcs_clients_optics.engine.optics_engine import OpticsEngine
        from gcs_clients_optics.usecases.fsspec_methods import FsspecMethodsUseCase

        engine = OpticsEngine(
            use_case=FsspecMethodsUseCase(),
            include_tests=self.include_tests,
            github_token=self.github_token,
            max_workers=self.max_workers,
        )
        return engine.scan_github_repo(repo_name, branch=branch)

