"""
Generic crawling and analysis engine for executing Optics use cases against local code and remote GitHub repositories.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, List, Optional

from gcs_clients_optics.usecases.base import BaseUseCase


class OpticsEngine:
    """
    Generic execution engine that runs any BaseUseCase against local files,
    directories, or remote GitHub repositories.
    """

    def __init__(
        self,
        use_case: BaseUseCase,
        include_tests: bool = False,
        github_token: Optional[str] = None,
        max_workers: int = 20,
    ):
        self.use_case = use_case
        self.include_tests = include_tests
        self.github_token = github_token or os.getenv("GITHUB_TOKEN")
        self.max_workers = max_workers

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[Any]:
        """Delegate single Python source code string scanning to the active use case."""
        return self.use_case.scan_code(
            file_path, source_code, repo_url=repo_url, branch=branch
        )

    def scan_local_file(self, file_path: str) -> Any:
        """Scan a single local Python file using the active use case."""
        p = Path(file_path)
        if not p.exists() or not p.is_file():
            return self.use_case.aggregate_report(
                target_source=f"Local:{p.name}",
                total_files_scanned=0,
                files_with_usages=0,
                usages=[],
                repo_url=None,
            )
        try:
            content = p.read_text(encoding="utf-8", errors="ignore")
            usages = self.scan_code(str(p), content)
            return self.use_case.aggregate_report(
                target_source=f"Local:{p.name}",
                total_files_scanned=1,
                files_with_usages=1 if usages else 0,
                usages=usages,
                repo_url=None,
            )
        except Exception as e:
            print(f"Error reading local file {file_path}: {e}", file=sys.stderr)
            return self.use_case.aggregate_report(
                target_source=f"Local:{p.name}",
                total_files_scanned=1,
                files_with_usages=0,
                usages=[],
                repo_url=None,
            )

    def scan_local_directory(self, dir_path: str) -> Any:
        """Scan all Python files within a local directory tree using the active use case."""
        root = Path(dir_path).resolve()
        py_files = []
        for p in root.rglob("*.py"):
            if not self.include_tests and (
                p.name.startswith("test_") or p.name.endswith("_test.py")
            ):
                continue
            py_files.append(p)

        all_usages: List[Any] = []
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

        return self.use_case.aggregate_report(
            target_source=f"Local:{root.name}",
            total_files_scanned=len(py_files),
            files_with_usages=files_with_usages,
            usages=all_usages,
            repo_url=None,
        )

    def scan_github_repo(
        self, repo_name: str, branch: str = "main"
    ) -> Any:
        """
        Crawl a remote GitHub repository via GitHub Trees API and scan all Python files
        using the active use case.
        """
        repo_url = f"https://github.com/{repo_name}"
        tree_url = (
            f"https://api.github.com/repos/{repo_name}/git/trees/{branch}?recursive=1"
        )
        headers = {
            "User-Agent": "GCS-Clients-Optics-Engine",
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
                # Fallback to master branch
                return self.scan_github_repo(repo_name, branch="master")
            print(
                f"HTTP Error {e.code} fetching GitHub tree for {repo_name}: {e.reason}",
                file=sys.stderr,
            )
            return self.use_case.aggregate_report(
                target_source=repo_name,
                total_files_scanned=0,
                files_with_usages=0,
                usages=[],
                repo_url=repo_url,
            )
        except Exception as e:
            print(
                f"Failed to fetch GitHub repository tree for {repo_name}: {e}",
                file=sys.stderr,
            )
            return self.use_case.aggregate_report(
                target_source=repo_name,
                total_files_scanned=0,
                files_with_usages=0,
                usages=[],
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

        all_usages: List[Any] = []
        scanned_count = len(py_files)
        files_with_matches = 0

        def _fetch_and_scan(rel_path: str):
            raw_url = (
                f"https://raw.githubusercontent.com/{repo_name}/{branch}/{rel_path}"
            )
            try:
                raw_req = urllib.request.Request(
                    raw_url,
                    headers={"User-Agent": "GCS-Clients-Optics-Engine"},
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

        return self.use_case.aggregate_report(
            target_source=f"GitHub:{repo_name} ({branch})",
            total_files_scanned=scanned_count,
            files_with_usages=files_with_matches,
            usages=all_usages,
            repo_url=repo_url,
        )

    def scan_multiple_repositories(
        self,
        target_repos: List[str],
        branch: str = "main",
        progress_callback: Optional[Callable[[str, Any], None]] = None,
    ) -> List[Any]:
        """Scan a list of GitHub repositories sequentially with progress reporting."""
        reports = []
        for repo in target_repos:
            report = self.scan_github_repo(repo, branch=branch)
            if progress_callback:
                progress_callback(repo, report)
            reports.append(report)
        return reports
