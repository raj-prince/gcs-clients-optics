"""
Fallback regular expression scanner for unparseable Python files or text snippets.
"""

import re
from pathlib import Path
from typing import List, Optional

from gcs_clients_optics.crawler.models import FsspecUsage, SPECIFIED_CACHE_KEYWORDS


class RegexFallbackScanner:
    """Fallback scanner using regular expressions for unparseable Python files or strings."""

    REGEX_PATTERNS = [
        re.compile(r"(?:fsspec|gcsfs)\.open(?:_files|_local)?\s*\("),
        re.compile(r"(?:fs|filesystem|gcs_fs)\.open\s*\("),
        re.compile(r"from\s+fsspec\s+import\s+.*open"),
    ]

    CACHE_TYPE_PATTERN = re.compile(r"cache_type\s*=\s*[\"']?([a-zA-Z0-9_-]+)[\"']?")

    @classmethod
    def scan_content(
        cls,
        file_path: str,
        content: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[FsspecUsage]:
        """Scan file text line by line using regex patterns."""
        usages: List[FsspecUsage] = []
        lines = content.splitlines()
        for idx, line in enumerate(lines, start=1):
            for pattern in cls.REGEX_PATTERNS:
                if pattern.search(line):
                    match_ct = cls.CACHE_TYPE_PATTERN.search(line)
                    ct_val = match_ct.group(1) if match_ct else "NOT_EXPLICIT"
                    file_url = (
                        f"{repo_url}/blob/{branch}/{file_path}#L{idx}"
                        if repo_url
                        else f"file://{Path(file_path).resolve()}#L{idx}"
                    )
                    usages.append(
                        FsspecUsage(
                            file_path=file_path,
                            line_number=idx,
                            end_line_number=idx,
                            target_name="regex_match",
                            cache_type=ct_val,
                            is_specified_cache_keyword=ct_val.lower()
                            in SPECIFIED_CACHE_KEYWORDS,
                            repo_url=repo_url,
                            file_url=file_url,
                            code_snippet=line.strip(),
                            detection_method="regex",
                        )
                    )
                    break
        return usages
