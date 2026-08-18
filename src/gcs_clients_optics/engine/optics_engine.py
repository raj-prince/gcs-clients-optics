import http.client
import io
import json
import os
import random
import sys
import tarfile
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Tuple

from gcs_clients_optics.usecases.base import BaseUseCase

_thread_local = threading.local()

# Directories that do not contain core library code (test suites, documentation, examples, build assets)
EXCLUDED_DIR_NAMES = {
    "test",
    "tests",
    "testing",
    "unit",
    "integration",
    "e2e",
    "doc",
    "docs",
    "documentation",
    "tutorial",
    "tutorials",
    "example",
    "examples",
    "sample",
    "samples",
    "benchmark",
    "benchmarks",
    "thirdparty",
    "third_party",
    "vendor",
    "site-packages",
    "build",
    "dist",
    ".github",
    "node_modules",
    "ci",
    "release",
    "scripts",
    "docker",
}


def is_relevant_python_file(
    path_str: str,
    include_tests: bool = False,
    subpath: Optional[str] = None,
) -> bool:
    """Check if a file path is a relevant Python source file for scanning."""
    if not path_str.endswith(".py"):
        return False

    if subpath:
        norm_sub = subpath.strip("/")
        if not path_str.startswith(norm_sub):
            return False

    if include_tests:
        return True

    p = Path(path_str)
    fn = p.name.lower()
    if (
        fn.startswith("test_")
        or fn.endswith("_test.py")
        or fn in ("conftest.py", "setup.py")
    ):
        return False

    for part in p.parts[:-1]:
        part_lower = part.lower()
        if part_lower in EXCLUDED_DIR_NAMES or part_lower.startswith("test"):
            return False

    return True


def fetch_raw_github_content(
    repo_name: str,
    branch: str,
    rel_path: str,
    github_token: Optional[str] = None,
    timeout: int = 15,
    max_retries: int = 3,
) -> str:
    """
    Fetch raw file content from GitHub using thread-local HTTPS persistent connection pooling (Keep-Alive)
    with exponential backoff retries for transient throttling and connection drops.
    """
    headers = {"User-Agent": "GCS-Clients-Optics-Engine"}
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    path = f"/{repo_name}/{branch}/{rel_path}"

    for attempt in range(max_retries):
        conn = getattr(_thread_local, "conn", None)
        if conn is None:
            conn = http.client.HTTPSConnection(
                "raw.githubusercontent.com", timeout=timeout
            )
            _thread_local.conn = conn

        try:
            conn.request("GET", path, headers=headers)
            resp = conn.getresponse()
            if resp.status == 200:
                return resp.read().decode("utf-8", errors="ignore")
            elif resp.status in (403, 429, 500, 502, 503, 504) and attempt < max_retries - 1:
                resp.read()
                time.sleep(0.4 * (2 ** attempt) + random.uniform(0.1, 0.3))
                continue
            resp.read()
            return ""
        except Exception:
            try:
                conn.close()
            except Exception:
                pass
            _thread_local.conn = http.client.HTTPSConnection(
                "raw.githubusercontent.com", timeout=timeout
            )
            if attempt < max_retries - 1:
                time.sleep(0.4 * (2 ** attempt) + random.uniform(0.1, 0.3))
                continue
            return ""
    return ""


def _fetch_github_tree_with_backoff(
    repo_name: str,
    branch: str,
    github_token: Optional[str] = None,
    max_retries: int = 3,
    timeout: int = 20,
) -> Tuple[Optional[List[Dict[str, Any]]], Optional[int]]:
    """
    Fetch GitHub Git Tree API with exponential backoff for rate limits and server errors.
    Returns (tree_list, status_code).
    """
    tree_url = (
        f"https://api.github.com/repos/{repo_name}/git/trees/{branch}?recursive=1"
    )
    headers = {
        "User-Agent": "GCS-Clients-Optics-Engine",
        "Accept": "application/vnd.github.v3+json",
    }
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    req = urllib.request.Request(tree_url, headers=headers)

    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data.get("tree", []), 200
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None, 404
            elif e.code in (403, 429):
                retry_after = e.headers.get("Retry-After")
                remaining = e.headers.get("x-ratelimit-remaining")
                if remaining == "0" and not github_token:
                    # Unauthenticated rate limit exhausted; return immediately to use archive fallback
                    return None, 403
                sleep_time = (
                    float(retry_after) + random.uniform(0.1, 0.5)
                    if retry_after
                    else min(2 ** attempt + random.uniform(0.5, 1.5), 10.0)
                )
                if attempt < max_retries - 1:
                    time.sleep(sleep_time)
                    continue
                return None, e.code
            elif e.code in (500, 502, 503, 504) and attempt < max_retries - 1:
                time.sleep(min(2 ** attempt + random.uniform(0.5, 1.5), 10.0))
                continue
            return None, e.code
        except Exception:
            if attempt < max_retries - 1:
                time.sleep(min(2 ** attempt + random.uniform(0.5, 1.5), 10.0))
                continue
            return None, 500
    return None, 500


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
        max_workers: int = 32,
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

    def scan_local_directory(
        self, dir_path: str, subpath: Optional[str] = None
    ) -> Any:
        """Scan all relevant Python files within a local directory tree using the active use case."""
        root = Path(dir_path).resolve()
        py_files = []
        for p in root.rglob("*.py"):
            rel_str = str(p.relative_to(root))
            if is_relevant_python_file(
                rel_str, include_tests=self.include_tests, subpath=subpath
            ):
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

    def _scan_github_repo_via_archive(
        self,
        repo_name: str,
        use_cases: List[BaseUseCase],
        branch: str = "main",
        subpath: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        """
        Fallback repository scanner that downloads a single compressed tarball from
        codeload.github.com without consuming GitHub REST API rate limits.
        """
        repo_url = f"https://github.com/{repo_name}"
        branches_to_try = [branch]
        if "main" not in branches_to_try:
            branches_to_try.append("main")
        if "master" not in branches_to_try:
            branches_to_try.append("master")

        headers = {"User-Agent": "GCS-Clients-Optics-Engine"}
        if self.github_token:
            headers["Authorization"] = f"token {self.github_token}"

        tar_bytes = None
        successful_branch = branch

        for b in branches_to_try:
            archive_url = (
                f"https://codeload.github.com/{repo_name}/tar.gz/refs/heads/{b}"
            )
            req = urllib.request.Request(archive_url, headers=headers)
            try:
                with urllib.request.urlopen(req, timeout=30) as resp:
                    if resp.status == 200:
                        tar_bytes = resp.read()
                        successful_branch = b
                        break
            except Exception:
                continue

        if not tar_bytes:
            return None

        uc_data: Dict[str, Dict[str, Any]] = {
            uc.name: {"files_with": 0, "usages": []} for uc in use_cases
        }
        scanned_count = 0

        try:
            with tarfile.open(fileobj=io.BytesIO(tar_bytes), mode="r:gz") as tar:
                for member in tar.getmembers():
                    if not member.isfile() or not member.name.endswith(".py"):
                        continue
                    # Strip archive root directory (e.g. 'repo-main/path/to/file.py' -> 'path/to/file.py')
                    parts = member.name.split("/", 1)
                    rel_path = parts[1] if len(parts) > 1 else parts[0]

                    if not is_relevant_python_file(
                        rel_path,
                        include_tests=self.include_tests,
                        subpath=subpath,
                    ):
                        continue

                    f = tar.extractfile(member)
                    if f is None:
                        continue

                    scanned_count += 1
                    try:
                        content = f.read().decode("utf-8", errors="ignore")
                        for uc in use_cases:
                            usages = uc.scan_code(
                                rel_path,
                                content,
                                repo_url=repo_url,
                                branch=successful_branch,
                            )
                            if usages:
                                uc_data[uc.name]["files_with"] += 1
                                uc_data[uc.name]["usages"].extend(usages)
                    except Exception:
                        continue
        except Exception as e:
            print(
                f"Error extracting archive for {repo_name}: {e}",
                file=sys.stderr,
            )
            return None

        reports: Dict[str, Any] = {}
        for uc in use_cases:
            reports[uc.name] = uc.aggregate_report(
                target_source=f"GitHub:{repo_name} ({successful_branch})",
                total_files_scanned=scanned_count,
                files_with_usages=uc_data[uc.name]["files_with"],
                usages=uc_data[uc.name]["usages"],
                repo_url=repo_url,
            )
        return reports

    def scan_github_repo(
        self,
        repo_name: str,
        branch: str = "main",
        subpath: Optional[str] = None,
    ) -> Any:
        """
        Crawl a remote GitHub repository via GitHub Trees API and scan all Python files
        using the active use case, with automatic backoff and zero-quota archive stream fallback.
        """
        multi_rep = self.scan_github_repo_multi(
            repo_name, [self.use_case], branch=branch, subpath=subpath
        )
        return multi_rep.get(
            self.use_case.name,
            self.use_case.aggregate_report(
                target_source=repo_name,
                total_files_scanned=0,
                files_with_usages=0,
                usages=[],
                repo_url=f"https://github.com/{repo_name}",
            ),
        )

    def scan_local_directory_multi(
        self,
        dir_path: str,
        use_cases: List[BaseUseCase],
        subpath: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Scan a local directory once and evaluate multiple use cases simultaneously
        on each file.
        """
        root = Path(dir_path).resolve()
        py_files = []
        for p in root.rglob("*.py"):
            rel_str = str(p.relative_to(root))
            if is_relevant_python_file(
                rel_str, include_tests=self.include_tests, subpath=subpath
            ):
                py_files.append(p)

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
        subpath: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Crawl a remote GitHub repository tree once, download each Python file once
        using Keep-Alive connection pooling, and evaluate all use cases simultaneously in a single pass.
        Falls back to codeload archive streaming if the GitHub REST API is rate limited.
        """
        repo_url = f"https://github.com/{repo_name}"
        tree_list, status_code = _fetch_github_tree_with_backoff(
            repo_name, branch, github_token=self.github_token
        )

        if tree_list is None and branch == "main" and status_code == 404:
            tree_list, status_code = _fetch_github_tree_with_backoff(
                repo_name, "master", github_token=self.github_token
            )
            if tree_list is not None:
                branch = "master"

        # If API rate limited (403/429) or unavailable, use the zero-quota archive fallback
        if tree_list is None:
            archive_reports = self._scan_github_repo_via_archive(
                repo_name, use_cases, branch=branch, subpath=subpath
            )
            if archive_reports:
                return archive_reports

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

        py_files = [
            f["path"]
            for f in tree_list
            if is_relevant_python_file(
                f.get("path", ""),
                include_tests=self.include_tests,
                subpath=subpath,
            )
        ]

        scanned_count = len(py_files)

        def _fetch_and_scan_multi(rel_path: str) -> Dict[str, List[Any]]:
            content = fetch_raw_github_content(
                repo_name,
                branch,
                rel_path,
                github_token=self.github_token,
            )
            if not content:
                return {uc.name: [] for uc in use_cases}

            file_results = {}
            for uc in use_cases:
                file_results[uc.name] = uc.scan_code(
                    rel_path, content, repo_url=repo_url, branch=branch
                )
            return file_results

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            all_file_results = list(
                executor.map(_fetch_and_scan_multi, py_files)
            )

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
        subpath: Optional[str] = None,
    ) -> List[Any]:
        """
        Scan a list of GitHub repositories with optional repo-level concurrency
        and progress reporting.
        """
        if max_repo_workers > 1:
            def _scan_one(repo: str):
                rep = self.scan_github_repo(repo, branch=branch, subpath=subpath)
                if progress_callback:
                    progress_callback(repo, rep)
                return rep

            with ThreadPoolExecutor(max_workers=max_repo_workers) as executor:
                return list(executor.map(_scan_one, target_repos))
        else:
            reports = []
            for repo in target_repos:
                report = self.scan_github_repo(repo, branch=branch, subpath=subpath)
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
        subpath: Optional[str] = None,
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
                repo, use_cases, branch=branch, subpath=subpath
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
