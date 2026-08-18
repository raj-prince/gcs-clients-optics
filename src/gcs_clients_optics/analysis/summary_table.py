"""
Comprehensive 4-column method summary table generator with automated functional categorization.
"""

import collections
import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from gcs_clients_optics.analysis.categorization import (
    USAGE_PATTERNS,
    categorize_method,
)


def generate_summary_table(
    report_data_or_path: Union[str, Path, Dict[str, Any]],
    output_path: Optional[Union[str, Path]] = None,
) -> str:
    """
    Generate a 4-column markdown summary table of all detected methods.
    Columns: Target Call | Occurrences | Major Repositories | Primary Usage Pattern
    """
    if isinstance(report_data_or_path, (str, Path)):
        p = Path(report_data_or_path)
        with open(p, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = report_data_or_path

    all_usages: List[Dict[str, Any]] = []
    for repo_data in data.get("per_repository", []):
        repo_name = repo_data.get("target_source", "")
        short_repo = (
            repo_name.replace("GitHub:", "").replace("Local:", "").split()[0]
        )
        for usage in repo_data.get("usages", []):
            u_copy = dict(usage)
            u_copy["short_repo"] = short_repo
            all_usages.append(u_copy)

    # Map method name -> count, repos Counter, snippets
    method_info: Dict[str, Dict[str, Any]] = collections.defaultdict(
        lambda: {"count": 0, "repos": collections.Counter(), "snippets": []}
    )

    for u in all_usages:
        name = u["target_name"]
        method_info[name]["count"] += 1
        method_info[name]["repos"][u["short_repo"]] += 1
        if len(method_info[name]["snippets"]) < 3 and u.get("code_snippet"):
            method_info[name]["snippets"].append(u["code_snippet"].strip())

    sorted_methods = sorted(
        method_info.items(), key=lambda x: -x[1]["count"]
    )

    table_lines: List[str] = [
        f"# Complete 4-Column Summary Table of All {len(sorted_methods)} FSSPEC & Filesystem Methods\n",
        "This reference summary table documents **every single distinct method call** identified by the AST crawler across scanned codebases, matching the summary format (`Target Call` | `Occurrences` | `Major Repositories` | `Usage Pattern`).\n",
        "| Target Call | Occurrences | Major Repositories | Primary Usage Pattern |",
        "| :--- | :---: | :--- | :--- |",
    ]

    for name, m_data in sorted_methods:
        cnt = m_data["count"]
        top_repos = ", ".join([f"`{r}`" for r, _ in m_data["repos"].most_common(3)])
        pattern = USAGE_PATTERNS.get(name)
        if not pattern:
            cat = categorize_method(name)
            pattern = f"{cat} API method detected across repository storage interactions"
        table_lines.append(
            f"| **`{name}`** | **{cnt}** | {top_repos} | {pattern} |"
        )

    content = "\n".join(table_lines) + "\n"

    if output_path:
        out_file = Path(output_path)
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(content, encoding="utf-8")

    return content
