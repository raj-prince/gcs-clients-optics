"""
Data models and dataclasses for fsspec AST code crawling and usages.
"""

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional, Set

SPECIFIED_CACHE_KEYWORDS: Set[str] = {
    "mmap",
    "readahead",
    "first",
    "blockcache",
    "block",
    "bytes",
    "all",
    "parts",
    "background",
}


@dataclass
class FsspecUsage:
    """Represents a single detected usage of fsspec.open or related file handle call."""

    file_path: str
    line_number: int
    end_line_number: int
    target_name: str
    enclosing_function: Optional[str] = None
    enclosing_class: Optional[str] = None
    cache_type: str = "NOT_EXPLICIT"  # Extracted cache_type value or default
    is_specified_cache_keyword: bool = False  # True if cache_type in SPECIFIED_CACHE_KEYWORDS
    cache_options: Optional[str] = None  # Extracted cache_options dict string
    repo_url: Optional[str] = None  # Full repository web link
    file_url: Optional[str] = None  # Full line URL
    args: List[str] = field(default_factory=list)
    kwargs: Dict[str, str] = field(default_factory=dict)
    code_snippet: str = ""
    detection_method: str = "ast"  # "ast" or "regex"

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


@dataclass
class CrawlReport:
    """Summary report of a code crawling session for a single repository or target."""

    target_source: str
    total_files_scanned: int
    files_with_usages: int
    total_usages_found: int
    repo_url: Optional[str] = None
    cache_type_summary: Dict[str, int] = field(default_factory=dict)
    usages: List[FsspecUsage] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        data = asdict(self)
        data["usages"] = [u.to_dict() for u in self.usages]
        return data
