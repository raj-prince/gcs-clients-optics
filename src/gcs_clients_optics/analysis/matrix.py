"""
Cross-repository method occurrence matrix generator.
"""

import collections
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union


def generate_method_matrix(
    report_data_or_path: Union[str, Path, Dict[str, Any]],
    output_path: Optional[Union[str, Path]] = None,
    target_repos: Optional[List[str]] = None,
) -> str:
    """
    Generate a markdown cross-repository distribution matrix from crawl report data.
    """
    if isinstance(report_data_or_path, (str, Path)):
        p = Path(report_data_or_path)
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = report_data_or_path

    all_usages: List[Dict[str, Any]] = []
    detected_repos: List[str] = []

    for repo_data in data.get("per_repository", []):
        repo_name = repo_data.get("target_source", "")
        short_repo = (
            repo_name.replace("GitHub:", "").replace("Local:", "").split()[0]
        )
        if short_repo and short_repo not in detected_repos:
            detected_repos.append(short_repo)

        for usage in repo_data.get("usages", []):
            u_copy = dict(usage)
            u_copy["short_repo"] = short_repo
            all_usages.append(u_copy)

    repos = target_repos or detected_repos
    methods = collections.Counter(u["target_name"] for u in all_usages)

    matrix: Dict[str, collections.Counter] = collections.defaultdict(
        collections.Counter
    )
    for u in all_usages:
        matrix[u["target_name"]][u["short_repo"]] += 1

    lines: List[str] = [
        f"# Complete Cross-Repository Method Distribution Matrix (All {len(methods)} Methods)\n",
        f"This document provides the exact occurrence count of **every single filesystem/fsspec method call** across all {len(repos)} repositories scanned by the AST crawler.\n",
    ]

    header_cols = ["Rank", "Target Method Name", "Total Calls"] + [
        r.split("/")[-1] for r in repos
    ]
    lines.append("| " + " | ".join(header_cols) + " |")
    lines.append(
        "| "
        + " | ".join(
            [":---" if i < 2 else ":---:" for i in range(len(header_cols))]
        )
        + " |"
    )

    for idx, (method, total) in enumerate(methods.most_common(), 1):
        row = [f"**{idx}**", f"`{method}`", f"**{total}**"]
        for r in repos:
            cnt = matrix[method].get(r, 0)
            row.append(str(cnt) if cnt > 0 else "-")
        lines.append("| " + " | ".join(row) + " |")

    content = "\n".join(lines) + "\n"

    if output_path:
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(content, encoding="utf-8")

    return content
