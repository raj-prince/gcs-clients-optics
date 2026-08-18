"""
Export formatters (CSV, JSON, Markdown) for code AST crawl reports.
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Union

from gcs_clients_optics.crawler.models import CrawlReport, SPECIFIED_CACHE_KEYWORDS

CACHE_DESCRIPTIONS: Dict[str, str] = {
    "readahead": "Default prefetching chunks for sequential reads",
    "mmap": "Memory-mapped temporary file for random access (Parquet/ORC)",
    "block": "Fixed-size block memory cache",
    "parts": "Parquet section/column block caching (required for fsspec.parquet precaching)",
    "none": "No cache, direct HTTP Range GET requests",
    "bytes": "Dictionary of exact byte ranges in RAM",
    "background": "Async background block prefetching",
    "file": "Downloads complete file to local disk first",
    "NOT_EXPLICIT": "cache_type keyword omitted (uses fsspec default)",
}


def export_csv_report(
    reports: Union[CrawlReport, List[CrawlReport]], output_path: str
) -> str:
    """Export crawl report(s) to CSV format."""
    if not isinstance(reports, list):
        reports = [reports]

    rows = []
    for r in reports:
        repo_name = r.target_source.replace("GitHub:", "").replace("Local:", "").split()[0]
        for u in r.usages:
            is_spec = u.cache_type.lower() in SPECIFIED_CACHE_KEYWORDS
            rows.append([
                repo_name,
                u.file_path,
                u.line_number,
                u.target_name,
                u.cache_type,
                is_spec,
                u.cache_options or "None",
                u.enclosing_class or "None",
                u.enclosing_function or "global",
                u.file_url or "",
                u.code_snippet.replace("\n", " "),
            ])

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "repository",
            "file_path",
            "line_number",
            "target_name",
            "cache_type",
            "is_specified_cache_keyword",
            "cache_options",
            "enclosing_class",
            "enclosing_function",
            "file_url",
            "code_snippet",
        ])
        writer.writerows(rows)

    return str(out_file)


def export_json_report(
    reports: Union[CrawlReport, List[CrawlReport]],
    output_path: str,
    elapsed_seconds: float = 0.0,
) -> str:
    """Export crawl report(s) to JSON format."""
    if not isinstance(reports, list):
        reports = [reports]

    global_cache_summary: Dict[str, int] = {}
    for r in reports:
        for ct, cnt in r.cache_type_summary.items():
            global_cache_summary[ct] = global_cache_summary.get(ct, 0) + cnt

    json_data: Dict[str, Any] = {
        "summary": {
            "total_repositories": len(reports),
            "total_files_scanned": sum(r.total_files_scanned for r in reports),
            "files_with_usages": sum(r.files_with_usages for r in reports),
            "total_usages_found": sum(r.total_usages_found for r in reports),
            "cache_type_summary": global_cache_summary,
            "elapsed_seconds": round(elapsed_seconds, 2),
        },
        "per_repository": [r.to_dict() for r in reports],
    }

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(json_data, indent=2), encoding="utf-8")
    return str(out_file)


def export_markdown_report(
    reports: Union[CrawlReport, List[CrawlReport]],
    output_path: str,
    include_tests: bool = False,
) -> str:
    """Generate a clean Markdown summary report across one or multiple crawl reports."""
    if not isinstance(reports, list):
        reports = [reports]

    total_files = sum(r.total_files_scanned for r in reports)
    total_matches = sum(r.files_with_usages for r in reports)
    total_usages = sum(r.total_usages_found for r in reports)

    global_cache_summary: Dict[str, int] = {}
    for r in reports:
        for ct, cnt in r.cache_type_summary.items():
            global_cache_summary[ct] = global_cache_summary.get(ct, 0) + cnt

    md_lines = [
        "# Master FSSPEC Usage Report Across GitHub Repositories",
        "",
        f"- **Repositories Crawled:** `{len(reports)}`",
        f"- **Total Files Scanned:** `{total_files}`",
        f"- **Files with FSSPEC Usages:** `{total_matches}`",
        f"- **Total FSSPEC Usages Detected:** `{total_usages}`",
        f"- **Skipping Test Files (test_*.py):** `{not include_tests}`",
        "",
        "---",
        "",
        "## 📊 Repository Summary Table",
        "",
        "| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Cache_Types |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for r in reports:
        repo_name = (
            r.target_source.replace("GitHub:", "").replace("Local:", "").split()[0]
        )
        ct_str = (
            ", ".join([f"{k}:{v}" for k, v in r.cache_type_summary.items()])
            if r.cache_type_summary
            else "None"
        )
        repo_link = (
            f"[{repo_name}]({r.repo_url})"
            if r.repo_url
            else f"`{repo_name}`"
        )
        md_lines.append(
            f"| {repo_link} | `{r.total_files_scanned}` | `{r.files_with_usages}` | `{r.total_usages_found}` | `{ct_str}` |"
        )

    md_lines.extend([
        "",
        "---",
        "",
        "## 📈 Global Cache_Type Breakdown",
        "",
        "| Cache_Type Option | Total Occurrences | Is Specified Keyword | Description |",
        "| :--- | :--- | :--- | :--- |",
    ])

    for ct, cnt in global_cache_summary.items():
        desc = CACHE_DESCRIPTIONS.get(ct, "Custom cache strategy")
        is_spec = ct.lower() in SPECIFIED_CACHE_KEYWORDS
        md_lines.append(f"| `{ct}` | `{cnt}` | `{is_spec}` | {desc} |")

    md_lines.extend([
        "",
        "---",
        "",
        "## 🔍 Detailed Usage Breakdown by Repository",
        "",
    ])

    for r in reports:
        repo_name = (
            r.target_source.replace("GitHub:", "").replace("Local:", "").split()[0]
        )
        repo_header = (
            f"### [{repo_name}]({r.repo_url})"
            if r.repo_url
            else f"### `{repo_name}`"
        )
        md_lines.extend([
            repo_header,
            f"- **Usages Found:** `{r.total_usages_found}` in `{r.files_with_usages}` files.",
            "",
        ])
        if not r.usages:
            md_lines.append("No direct filesystem / fsspec usages detected in this target.\n")
        else:
            for idx, usage in enumerate(r.usages, start=1):
                func_info = (
                    f"`{usage.enclosing_class}.{usage.enclosing_function}`"
                    if usage.enclosing_class
                    else f"`{usage.enclosing_function or 'global'}`"
                )
                file_link_str = (
                    f"[{usage.file_path}]({usage.file_url})"
                    if usage.file_url
                    else f"`{usage.file_path}`"
                )
                md_lines.extend([
                    f"#### {idx}. {file_link_str} (Line {usage.line_number})",
                    f"- **Line Link:** {usage.file_url or 'N/A'}",
                    f"- **Target Call:** `{usage.target_name}` | **Cache_Type:** `{usage.cache_type}` | **Is Specified Keyword:** `{usage.is_specified_cache_keyword}`",
                    f"- **Context:** {func_info}",
                    f"- **Arguments:** `{', '.join(usage.args)}`",
                    f"- **Keywords:** `{usage.kwargs}`",
                    "",
                    "```python",
                    f"{usage.code_snippet}",
                    "```",
                    "",
                ])

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("\n".join(md_lines), encoding="utf-8")
    return str(out_file)
