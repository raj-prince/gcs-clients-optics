"""
Export formatters (CSV, JSON, Markdown) for code AST crawl reports.
"""

import csv
import json
from collections import Counter, defaultdict
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
    """Generate a comprehensive, single Markdown report containing summaries, ontology, matrix, and call sites."""
    if not isinstance(reports, list):
        reports = [reports]

    from gcs_clients_optics.reporters.categorization import (
        categorize_method,
        get_method_description,
    )

    total_files = sum(r.total_files_scanned for r in reports)
    total_matches = sum(r.files_with_usages for r in reports)
    total_usages = sum(r.total_usages_found for r in reports)

    # Collect methods, per-repo counts, and snippets
    global_methods: Counter = Counter()
    method_repos: Dict[str, Counter] = defaultdict(Counter)
    detected_repos: List[str] = []

    for r in reports:
        repo_name = r.target_source.replace("GitHub:", "").replace("Local:", "").split()[0]
        if repo_name and repo_name not in detected_repos:
            detected_repos.append(repo_name)
        for u in r.usages:
            global_methods[u.target_name] += 1
            method_repos[u.target_name][repo_name] += 1

    md_lines = [
        "# Master FSSPEC & Filesystem Method Usage Report",
        "",
        f"- **Repositories Crawled:** `{len(reports)}`",
        f"- **Total Files Scanned:** `{total_files}`",
        f"- **Files with Method Usages:** `{total_matches}`",
        f"- **Total Method Usages Detected:** `{total_usages}`",
        f"- **Distinct Methods Detected:** `{len(global_methods)}`",
        f"- **Skipping Test Files (test_*.py):** `{not include_tests}`",
        "",
        "---",
        "",
        "## 📊 Repository Summary Table",
        "",
        "| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Top Methods |",
        "| :--- | :--- | :--- | :--- | :--- |",
    ]

    for r in reports:
        repo_name = (
            r.target_source.replace("GitHub:", "").replace("Local:", "").split()[0]
        )
        repo_methods = Counter(u.target_name for u in r.usages).most_common(3)
        top_methods_str = ", ".join(f"`{m}` ({c})" for m, c in repo_methods) if repo_methods else "None"
        repo_link = (
            f"[{repo_name}]({r.repo_url})"
            if r.repo_url
            else f"`{repo_name}`"
        )
        md_lines.append(
            f"| {repo_link} | `{r.total_files_scanned}` | `{r.files_with_usages}` | `{r.total_usages_found}` | {top_methods_str} |"
        )

    def _slugify(text: str) -> str:
        return text.replace("/", "-").replace(".", "-").replace("_", "-").replace(" ", "-").lower()

    # Sorted methods by overall frequency
    sorted_methods = [method for method, _ in global_methods.most_common()]

    # 1. Repository x Target Call Metrics Matrix
    md_lines.extend([
        "",
        "---",
        "",
        f"## 📊 Repository × Target Call Usage Matrix ({len(sorted_methods)} Methods)",
        "",
    ])

    header_cols = ["Repository", "Total Calls"] + [f"`{m}`" for m in sorted_methods]
    align_cols = [":---", ":---:"] + [":---:" for _ in sorted_methods]
    md_lines.append("| " + " | ".join(header_cols) + " |")
    md_lines.append("| " + " | ".join(align_cols) + " |")

    for r in reports:
        repo_name = (
            r.target_source.replace("GitHub:", "").replace("Local:", "").split()[0]
        )
        repo_slug = _slugify(repo_name)
        repo_link = f"[{repo_name}]({r.repo_url})" if r.repo_url else f"`{repo_name}`"

        repo_method_counts = Counter(u.target_name for u in r.usages)
        row = [repo_link, f"**{r.total_usages_found}**"]

        for m in sorted_methods:
            cnt = repo_method_counts.get(m, 0)
            if cnt > 0:
                method_slug = _slugify(m)
                anchor = f"{repo_slug}-{method_slug}"
                row.append(f"[**{cnt}**](#{anchor})")
            else:
                row.append("-")
        md_lines.append("| " + " | ".join(row) + " |")

    # 2. Detailed Usage Breakdown by Repository (Grouped by Target Method)
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
        repo_slug = _slugify(repo_name)
        repo_header = (
            f"### [{repo_name}]({r.repo_url})"
            if r.repo_url
            else f"### `{repo_name}`"
        )
        md_lines.extend([
            repo_header,
            f"- **Files Scanned:** `{r.total_files_scanned}` | **Files with Usages:** `{r.files_with_usages}` | **Total Usages:** `{r.total_usages_found}`",
            "",
        ])
        if not r.usages:
            md_lines.append("No direct filesystem / fsspec usages detected in this target.\n")
        else:
            # Group usages by target method for structured search & navigation
            usages_by_method: Dict[str, List[Any]] = defaultdict(list)
            for u in r.usages:
                usages_by_method[u.target_name].append(u)

            for method_name, method_usages in sorted(
                usages_by_method.items(), key=lambda item: len(item[1]), reverse=True
            ):
                method_slug = _slugify(method_name)
                anchor = f"{repo_slug}-{method_slug}"
                count_str = f"{len(method_usages)} occurrence{'s' if len(method_usages) > 1 else ''}"

                md_lines.extend([
                    f"#### <a id=\"{anchor}\"></a>🔹 `{method_name}` ({count_str})",
                    "",
                    f"<details open>",
                    f"<summary><b>Click to expand/collapse {count_str} for <code>{method_name}</code> in {repo_name}</b></summary>",
                    "",
                ])

                for idx, usage in enumerate(method_usages, start=1):
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
                    cache_info = f" | **Cache Strategy:** `{usage.cache_type}`" if usage.is_specified_cache_keyword else ""
                    md_lines.extend([
                        f"##### {idx}. {file_link_str} (Line {usage.line_number})",
                        f"- **Line Link:** {usage.file_url or 'N/A'}",
                        f"- **Target Call:** `{usage.target_name}`{cache_info}",
                        f"- **Context:** {func_info}",
                        f"- **Arguments:** `{', '.join(usage.args)}`",
                        f"- **Keywords:** `{usage.kwargs}`",
                        "",
                        "```python",
                        f"{usage.code_snippet}",
                        "```",
                        "",
                    ])

                md_lines.extend([
                    "</details>",
                    "",
                ])

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("\n".join(md_lines), encoding="utf-8")
    return str(out_file)
