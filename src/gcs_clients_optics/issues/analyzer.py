"""
Issue analyzer and relevance scoring engine for GitHub issues.
"""

import re
from typing import Any, Dict, Optional, Set

from gcs_clients_optics.issues.keywords import (
    FILESYSTEM_KEYWORDS,
    PERFORMANCE_KEYWORDS,
    PERFORMANCE_LABELS,
)
from gcs_clients_optics.issues.models import GitHubIssue


class IssuePerformanceAnalyzer:
    """Analyzes issue title, body, and labels to score performance and fsspec relevance."""

    def __init__(
        self,
        fs_keywords: Optional[Set[str]] = None,
        perf_keywords: Optional[Set[str]] = None,
        perf_labels: Optional[Set[str]] = None,
    ):
        self.fs_keywords = fs_keywords or FILESYSTEM_KEYWORDS
        self.perf_keywords = perf_keywords or PERFORMANCE_KEYWORDS
        self.perf_labels = perf_labels or PERFORMANCE_LABELS

    def analyze_issue(
        self, repo_name: str, issue_raw: Dict[str, Any]
    ) -> Optional[GitHubIssue]:
        """
        Inspect raw GitHub REST API issue payload.
        Returns GitHubIssue object if relevant, or None if irrelevant.
        """
        # Skip pull requests (GitHub API returns PRs in /issues endpoint)
        if "pull_request" in issue_raw:
            return None

        title = issue_raw.get("title", "")
        body = issue_raw.get("body", "") or ""
        labels_raw = issue_raw.get("labels", [])
        labels = [
            lbl.get("name", "") if isinstance(lbl, dict) else str(lbl)
            for lbl in labels_raw
        ]

        combined_text = f"{title}\n{body}".lower()
        labels_text = " ".join(labels).lower()

        # Match keywords
        matched_fs = [kw for kw in self.fs_keywords if kw in combined_text]
        matched_perf = [kw for kw in self.perf_keywords if kw in combined_text]

        # Label matching
        has_perf_label = any(pl in labels_text for pl in self.perf_labels)

        # Repos dedicated to filesystem (e.g. fsspec/gcsfs, fsspec/filesystem_spec) implicitly match FS
        is_filesystem_repo = (
            "fsspec" in repo_name.lower()
            or "gcsfs" in repo_name.lower()
            or "s3fs" in repo_name.lower()
        )
        if is_filesystem_repo and not matched_fs:
            matched_fs.append("repo:fsspec")

        # Determine relevance criteria:
        # 1. Must have at least 1 performance keyword or performance label.
        # 2. Must have at least 1 filesystem keyword (or belong to fsspec/gcsfs repo).
        if not (matched_perf or has_perf_label):
            return None
        if not matched_fs:
            return None

        # Calculate relevance score
        score = (
            (len(matched_fs) * 2)
            + (len(matched_perf) * 3)
            + (10 if has_perf_label else 0)
        )

        # Create body snippet (first 300 characters cleaned)
        clean_body = re.sub(r"\s+", " ", body).strip()
        snippet = clean_body[:300] + ("..." if len(clean_body) > 300 else "")

        user_info = issue_raw.get("user", {})
        author = (
            user_info.get("login", "unknown")
            if isinstance(user_info, dict)
            else "unknown"
        )

        return GitHubIssue(
            repo_name=repo_name,
            issue_number=issue_raw.get("number", 0),
            title=title,
            html_url=issue_raw.get("html_url", ""),
            state=issue_raw.get("state", "open"),
            created_at=issue_raw.get("created_at", ""),
            updated_at=issue_raw.get("updated_at", ""),
            author=author,
            labels=labels,
            matched_fs_keywords=sorted(list(set(matched_fs))),
            matched_perf_keywords=sorted(list(set(matched_perf))),
            relevance_score=score,
            body_snippet=snippet,
        )
