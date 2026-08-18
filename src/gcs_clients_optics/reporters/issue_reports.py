"""
Export formatters (CSV, JSON, Markdown) for GitHub issue crawl reports.
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Union

from gcs_clients_optics.issues.models import IssueCrawlReport


def export_issues_csv(
    reports: Union[IssueCrawlReport, List[IssueCrawlReport]], output_path: str
) -> str:
    """Export matched issues across reports to CSV format."""
    if not isinstance(reports, list):
        reports = [reports]

    rows = []
    for r in reports:
        for issue in r.issues:
            rows.append([
                issue.repo_name,
                issue.issue_number,
                issue.title,
                issue.html_url,
                issue.state,
                issue.relevance_score,
                ", ".join(issue.labels),
                ", ".join(issue.matched_fs_keywords),
                ", ".join(issue.matched_perf_keywords),
                issue.author,
                issue.created_at,
                issue.body_snippet,
            ])

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)

    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([
            "repository",
            "issue_number",
            "title",
            "html_url",
            "state",
            "relevance_score",
            "labels",
            "matched_fs_keywords",
            "matched_perf_keywords",
            "author",
            "created_at",
            "body_snippet",
        ])
        writer.writerows(rows)

    return str(out_file)


def export_issues_json(
    reports: Union[IssueCrawlReport, List[IssueCrawlReport]],
    output_path: str,
    elapsed_seconds: float = 0.0,
) -> str:
    """Export matched issues across reports to JSON format."""
    if not isinstance(reports, list):
        reports = [reports]

    json_payload: Dict[str, Any] = {
        "summary": {
            "total_repositories": len(reports),
            "total_issues_scanned": sum(r.total_issues_scanned for r in reports),
            "matched_issues_count": sum(r.matched_issues_count for r in reports),
            "elapsed_seconds": round(elapsed_seconds, 2),
        },
        "per_repository": [r.to_dict() for r in reports],
    }

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text(json.dumps(json_payload, indent=2), encoding="utf-8")
    return str(out_file)


def export_issues_markdown(
    reports: Union[IssueCrawlReport, List[IssueCrawlReport]], output_path: str
) -> str:
    """Generate a clean Markdown summary report of fsspec/performance issues."""
    if not isinstance(reports, list):
        reports = [reports]

    total_scanned = sum(r.total_issues_scanned for r in reports)
    total_matched = sum(r.matched_issues_count for r in reports)

    md_lines = [
        "# GitHub Issues Performance & FSSPEC Crawl Report",
        "",
        f"- **Repositories Crawled:** `{len(reports)}`",
        f"- **Total Issues Scanned:** `{total_scanned}`",
        f"- **Matched Performance / FSSPEC Issues:** `{total_matched}`",
        "",
        "---",
        "",
        "## 📊 Repository Issue Breakdown",
        "",
        "| Repository | Issues Scanned | Matched Perf/FSSPEC Issues | Top Issue Link |",
        "| :--- | :--- | :--- | :--- |",
    ]

    for r in reports:
        top_link = (
            f"[#{r.issues[0].issue_number}]({r.issues[0].html_url})"
            if r.issues
            else "N/A"
        )
        md_lines.append(
            f"| [{r.target_repo}]({r.repo_url}) | `{r.total_issues_scanned}` | `{r.matched_issues_count}` | {top_link} |"
        )

    md_lines.extend([
        "",
        "---",
        "",
        "## 🔍 Detailed Matched Issues",
        "",
    ])

    idx = 1
    for r in reports:
        if not r.issues:
            continue
        md_lines.append(
            f"### [{r.target_repo}]({r.repo_url}) ({r.matched_issues_count} issues)"
        )
        md_lines.append("")
        for issue in r.issues:
            labels_str = (
                ", ".join([f"`{lbl}`" for lbl in issue.labels])
                if issue.labels
                else "None"
            )
            fs_str = ", ".join([f"`{k}`" for k in issue.matched_fs_keywords])
            perf_str = ", ".join([f"`{k}`" for k in issue.matched_perf_keywords])

            md_lines.extend([
                f"#### {idx}. [{issue.title}]({issue.html_url}) (#{issue.issue_number})",
                f"- **URL:** {issue.html_url}",
                f"- **Relevance Score:** `{issue.relevance_score}` | **State:** `{issue.state}` | **Author:** `{issue.author}`",
                f"- **Labels:** {labels_str}",
                f"- **FS Keywords:** {fs_str}",
                f"- **Perf Keywords:** {perf_str}",
                f"- **Excerpt:** *\"{issue.body_snippet}\"*",
                "",
            ])
            idx += 1

    out_file = Path(output_path)
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("\n".join(md_lines), encoding="utf-8")
    return str(out_file)
