"""
Crawling and analysis engine for local files, directories, and remote GitHub repositories.
"""

import ast
import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Dict, List, Optional

from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.models import CrawlReport, FsspecUsage
from gcs_clients_optics.crawler.regex_scanner import RegexFallbackScanner


class FsspecCrawlerEngine:
    """Engine that manages AST scanning of local code and remote GitHub repositories."""

    def __init__(
        self,
        use_regex_fallback: bool = True,
        include_tests: bool = False,
        github_token: Optional[str] = None,
        max_workers: int = 16,
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
            if not self.include_tests and (
                p.name.startswith("test_") or p.name.endswith("_test.py")
            ):
                continue
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
        Example repo_name: 'dask/dask' or 'pytorch/pytorch'
        """
        repo_url = f"https://github.com/{repo_name}"
        tree_url = (
            f"https://api.github.com/repos/{repo_name}/git/trees/{branch}?recursive=1"
        )
        headers = {
            "User-Agent": "GCS-Clients-Optics-Crawler",
            "Accept": "application/vnd.github.v3+json",
        }
        if self.github_token:
            headers["Authorization"] = f"token {self.github_token}"

        req = urllib.request.Request(tree_url, headers=headers)

        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            if e.code == 404 and branch == "main":
                # Try fallback to 'master' branch
                return self.scan_github_repo(repo_name, branch="master")
            print(
                f"HTTP Error {e.code} fetching GitHub tree for {repo_name}: {e.reason}",
                file=sys.stderr,
            )
            return CrawlReport(
                target_source=repo_name,
                total_files_scanned=0,
                files_with_usages=0,
                total_usages_found=0,
                repo_url=repo_url,
            )
        except Exception as e:
            print(
                f"Failed to fetch GitHub repository tree for {repo_name}: {e}",
                file=sys.stderr,
            )
            return CrawlReport(
                target_source=repo_name,
                total_files_scanned=0,
                files_with_usages=0,
                total_usages_found=0,
                repo_url=repo_url,
            )

        tree = data.get("tree", [])
        py_files = [
            f["path"]
            for f in tree
            if f.get("path", "").endswith(".py")
            and (
                self.include_tests
                or not Path(f.get("path", "")).name.startswith("test_")
            )
        ]

        all_usages: List[FsspecUsage] = []
        scanned_count = len(py_files)
        files_with_matches = 0

        def _fetch_and_scan(rel_path: str):
            raw_url = (
                f"https://raw.githubusercontent.com/{repo_name}/{branch}/{rel_path}"
            )
            try:
                raw_req = urllib.request.Request(
                    raw_url,
                    headers={"User-Agent": "GCS-Clients-Optics-Crawler"},
                )
                with urllib.request.urlopen(raw_req, timeout=10) as raw_resp:
                    content = raw_resp.read().decode("utf-8", errors="ignore")
                return self.scan_code(
                    rel_path, content, repo_url=repo_url, branch=branch
                )
            except Exception:
                return []

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            file_usages = executor.map(_fetch_and_scan, py_files)

        for usages in file_usages:
            if usages:
                files_with_matches += 1
                all_usages.extend(usages)

        summary = self._build_cache_type_summary(all_usages)

        return CrawlReport(
            target_source=f"GitHub:{repo_name} ({branch})",
            total_files_scanned=scanned_count,
            files_with_usages=files_with_matches,
            total_usages_found=len(all_usages),
            repo_url=repo_url,
            cache_type_summary=summary,
            usages=all_usages,
        )
