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
from typing import Any, Callable, Dict, List, Optional, Tuple

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
        max_workers: int = 16,
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

    def scan_local_directory_multi(
        self, dir_path: str, use_cases: List[BaseUseCase]
    ) -> Dict[str, Any]:
        """
        Scan a local directory once and evaluate multiple use cases simultaneously
        on each file.
        """
        root = Path(dir_path).resolve()
        py_files = []
        for p in root.rglob("*.py"):
            if not self.include_tests and (
                p.name.startswith("test_") or p.name.endswith("_test.py")
            ):
                continue
            py_files.append(p)

        # Collect usages per use case: {uc_name: {"files_with": int, "usages": list}}
        uc_data: Dict[str, Dict[str, Any]] = {
            uc.name: {"files_with": 0, "usages": []} for uc in use_cases
        }

        for p in py_files:
            rel_path = str(p.relative_to(root))
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
                for uc in use_cases:
                    usages = uc.scan_code(rel_path, content)
                    if usages:
                        uc_data[uc.name]["files_with"] += 1
                        uc_data[uc.name]["usages"].extend(usages)
            except Exception:
                continue

        reports: Dict[str, Any] = {}
        for uc in use_cases:
            reports[uc.name] = uc.aggregate_report(
                target_source=f"Local:{root.name}",
                total_files_scanned=len(py_files),
                files_with_usages=uc_data[uc.name]["files_with"],
                usages=uc_data[uc.name]["usages"],
                repo_url=None,
            )
        return reports

    def scan_github_repo_multi(
        self,
        repo_name: str,
        use_cases: List[BaseUseCase],
        branch: str = "main",
    ) -> Dict[str, Any]:
        """
        Crawl a remote GitHub repository tree once, download each Python file once,
        and evaluate all use cases simultaneously in a single pass.
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
                return self.scan_github_repo_multi(
                    repo_name, use_cases, branch="master"
                )
            print(
                f"HTTP Error {e.code} fetching GitHub tree for {repo_name}: {e.reason}",
                file=sys.stderr,
            )
            return {
                uc.name: uc.aggregate_report(
                    target_source=repo_name,
                    total_files_scanned=0,
                    files_with_usages=0,
                    usages=[],
                    repo_url=repo_url,
                )
                for uc in use_cases
            }
        except Exception as e:
            print(
                f"Failed to fetch GitHub repository tree for {repo_name}: {e}",
                file=sys.stderr,
            )
            return {
                uc.name: uc.aggregate_report(
                    target_source=repo_name,
                    total_files_scanned=0,
                    files_with_usages=0,
                    usages=[],
                    repo_url=repo_url,
                )
                for uc in use_cases
            }

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

        scanned_count = len(py_files)

        def _fetch_and_scan_multi(rel_path: str) -> Dict[str, List[Any]]:
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

                file_results = {}
                for uc in use_cases:
                    file_results[uc.name] = uc.scan_code(
                        rel_path, content, repo_url=repo_url, branch=branch
                    )
                return file_results
            except Exception:
                return {uc.name: [] for uc in use_cases}

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            all_file_results = list(
                executor.map(_fetch_and_scan_multi, py_files)
            )

        # Aggregate across all files for each use case
        reports: Dict[str, Any] = {}
        for uc in use_cases:
            uc_usages = []
            files_with_matches = 0
            for file_res in all_file_results:
                usages = file_res.get(uc.name, [])
                if usages:
                    files_with_matches += 1
                    uc_usages.extend(usages)

            reports[uc.name] = uc.aggregate_report(
                target_source=f"GitHub:{repo_name} ({branch})",
                total_files_scanned=scanned_count,
                files_with_usages=files_with_matches,
                usages=uc_usages,
                repo_url=repo_url,
            )

        return reports

    def scan_multiple_repositories(
        self,
        target_repos: List[str],
        branch: str = "main",
        max_repo_workers: int = 16,
        progress_callback: Optional[Callable[[str, Any], None]] = None,
    ) -> List[Any]:
        """
        Scan a list of GitHub repositories with optional repo-level concurrency
        and progress reporting.
        """
        if max_repo_workers > 1:
            def _scan_one(repo: str):
                rep = self.scan_github_repo(repo, branch=branch)
                if progress_callback:
                    progress_callback(repo, rep)
                return rep

            with ThreadPoolExecutor(max_workers=max_repo_workers) as executor:
                return list(executor.map(_scan_one, target_repos))
        else:
            reports = []
            for repo in target_repos:
                report = self.scan_github_repo(repo, branch=branch)
                if progress_callback:
                    progress_callback(repo, report)
                reports.append(report)
            return reports

    def scan_multiple_repositories_multi(
        self,
        target_repos: List[str],
        use_cases: List[BaseUseCase],
        branch: str = "main",
        max_repo_workers: int = 16,
        progress_callback: Optional[
            Callable[[str, Dict[str, Any]], None]
        ] = None,
    ) -> Dict[str, List[Any]]:
        """
        Scan multiple GitHub repositories in parallel, running all use cases
        in a single pass per repository. Returns {use_case_name: [reports...]}.
        """
        aggregated: Dict[str, List[Any]] = {
            uc.name: [] for uc in use_cases
        }

        def _scan_one_repo(repo: str) -> Tuple[str, Dict[str, Any]]:
            repo_reports = self.scan_github_repo_multi(
                repo, use_cases, branch=branch
            )
            if progress_callback:
                progress_callback(repo, repo_reports)
            return repo, repo_reports

        if max_repo_workers > 1:
            with ThreadPoolExecutor(max_workers=max_repo_workers) as executor:
                results = list(executor.map(_scan_one_repo, target_repos))
        else:
            results = [_scan_one_repo(repo) for repo in target_repos]

        for _, repo_reports in results:
            for uc_name, rep in repo_reports.items():
                aggregated[uc_name].append(rep)

        return aggregated
