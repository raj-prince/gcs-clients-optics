"""
Data models for GitHub issues crawling and performance analysis.
"""

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List


@dataclass
class GitHubIssue:
    """Represents a single parsed GitHub issue matched by the crawler."""

    repo_name: str
    issue_number: int
    title: str
    html_url: str
    state: str
    created_at: str
    updated_at: str
    author: str
    labels: List[str] = field(default_factory=list)
    matched_fs_keywords: List[str] = field(default_factory=list)
    matched_perf_keywords: List[str] = field(default_factory=list)
    relevance_score: int = 0
    body_snippet: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


@dataclass
class IssueCrawlReport:
    """Summary report of an issue crawling session for a single repository."""

    target_repo: str
    total_issues_scanned: int
    matched_issues_count: int
    repo_url: str
    issues: List[GitHubIssue] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        data["issues"] = [i.to_dict() for i in self.issues]
        return data
