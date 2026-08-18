"""
Parser and loader for GitHub repository dependents (from github-dependents-info, JSON, or text files).
"""

import json
import random
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Union


def load_repos_from_file(
    file_path: Union[str, Path],
    min_stars: int = 0,
    limit: Optional[int] = None,
) -> List[Tuple[str, str]]:
    """
    Load and parse target repositories from a file.

    Supports:
    1. `github-dependents-info` JSON format (nested `packages` -> `public_dependents`)
    2. JSON list of repository objects (`[{"name": "owner/repo", "stars": 120}, ...]`)
    3. JSON list of repository name strings (`["owner/repo1", "owner/repo2", ...]`)
    4. Plain text / CSV files with one repository per line (`owner/repo`, ignoring comments)

    Returns a list of tuples: `[(repo_display_name, "owner/repo"), ...]`,
    filtered by `min_stars` and sorted by stars descending (if star counts are present).
    """
    p = Path(file_path)
    if not p.exists():
        print(f"Error: Dependents file not found at '{file_path}'", file=sys.stderr)
        return []

    content = p.read_text(encoding="utf-8", errors="ignore").strip()
    if not content:
        return []

    repos_with_stars: List[Tuple[str, str, int]] = []
    seen: Set[str] = set()

    # Try JSON parsing first
    if p.suffix.lower() == ".json" or content.startswith("{") or content.startswith("["):
        try:
            data = json.loads(content)
            repos_with_stars = _parse_json_dependents(data, min_stars=min_stars)
        except json.JSONDecodeError:
            pass

    # Fallback to plain text line-by-line parsing
    if not repos_with_stars:
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # Match owner/repo pattern
            match = re.search(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", line)
            if match:
                repo = match.group(1)
                if repo not in seen:
                    seen.add(repo)
                    name = repo.split("/")[-1]
                    repos_with_stars.append((name, repo, 0))

    # Sort by stars descending if available
    repos_with_stars.sort(key=lambda x: x[2], reverse=True)

    if limit and limit > 0:
        repos_with_stars = repos_with_stars[:limit]

    return [(name, repo) for name, repo, _ in repos_with_stars]


def _parse_json_dependents(
    data: Any, min_stars: int = 0
) -> List[Tuple[str, str, int]]:
    """Extract repositories and star counts from various JSON schemas."""
    results: List[Tuple[str, str, int]] = []
    seen: Set[str] = set()

    def _add_repo(repo_full_name: str, stars: int):
        clean_repo = repo_full_name.strip().strip("/")
        if "/" in clean_repo and clean_repo not in seen:
            if stars >= min_stars:
                seen.add(clean_repo)
                display_name = clean_repo.split("/")[-1]
                results.append((display_name, clean_repo, stars))

    # 1. github-dependents-info schema: {"packages": [{"public_dependents": [...]}]}
    if isinstance(data, dict):
        packages = data.get("packages", [])
        if packages:
            for pkg in packages:
                if isinstance(pkg, dict):
                    for dep in pkg.get("public_dependents", []):
                        if isinstance(dep, dict):
                            repo = dep.get("name") or dep.get("repo") or dep.get("full_name") or ""
                            stars = dep.get("stars", 0) or 0
                            if repo:
                                _add_repo(repo, stars)
                        elif isinstance(dep, str):
                            _add_repo(dep, 0)
        # Direct list under "dependents" or "repositories" or "items"
        for key in ("dependents", "repositories", "items", "public_dependents"):
            if key in data and isinstance(data[key], list):
                for item in data[key]:
                    if isinstance(item, dict):
                        repo = item.get("name") or item.get("full_name") or item.get("repo") or ""
                        stars = item.get("stars", 0) or item.get("stargazers_count", 0) or 0
                        if repo:
                            _add_repo(repo, stars)
                    elif isinstance(item, str):
                        _add_repo(item, 0)

    # 2. JSON list: [{"name": "owner/repo", "stars": 100}, ...] or ["owner/repo", ...]
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                repo = item.get("name") or item.get("full_name") or item.get("repo") or ""
                stars = item.get("stars", 0) or item.get("stargazers_count", 0) or 0
                if repo:
                    _add_repo(repo, stars)
            elif isinstance(item, str):
                _add_repo(item, 0)

    return results


def fetch_github_dependents_html(
    repo_name: str,
    min_stars: int = 10,
    limit: int = 50,
    github_token: Optional[str] = None,
    max_retries: int = 3,
) -> List[Tuple[str, str]]:
    """
    Directly scrape GitHub's Network Dependents page for a repository.
    Example repo_name: 'fsspec/filesystem_spec' or 'fsspec/gcsfs'
    """
    url = f"https://github.com/{repo_name}/network/dependents"
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml",
    }
    if github_token:
        headers["Authorization"] = f"token {github_token}"

    req = urllib.request.Request(url, headers=headers)
    html = ""
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                html = resp.read().decode("utf-8", errors="ignore")
                break
        except urllib.error.HTTPError as e:
            if e.code in (403, 429, 500, 502, 503, 504) and attempt < max_retries - 1:
                time.sleep(min(2 ** attempt + random.uniform(0.5, 1.5), 10.0))
                continue
            print(
                f"HTTP Error {e.code} fetching dependents for {repo_name}: {e.reason}",
                file=sys.stderr,
            )
            return []
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(min(2 ** attempt + random.uniform(0.5, 1.5), 10.0))
                continue
            print(f"Failed to fetch GitHub dependents for {repo_name}: {e}", file=sys.stderr)
            return []

    if not html:
        return []

    # Regex search for dependent repo links: href="/owner/repo" in dependents list
    matches = re.findall(
        r'data-repository-hovercards-enabled.*?href="/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)"',
        html,
        re.DOTALL,
    )
    if not matches:
        matches = re.findall(r'href="/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)"\s+class="text-bold"', html)

    results: List[Tuple[str, str]] = []
    seen: Set[str] = set()
    for repo in matches:
        if "/" in repo and repo not in seen and repo != repo_name:
            seen.add(repo)
            display_name = repo.split("/")[-1]
            results.append((display_name, repo))
            if len(results) >= limit:
                break

    return results
