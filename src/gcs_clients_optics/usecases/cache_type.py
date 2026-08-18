"""
Use Case 2: Cache-Type & Caching Strategy Analysis in the Read / Stream Path.
"""

import ast
import csv
import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

from gcs_clients_optics.crawler.ast_visitor import FsspecASTVisitor
from gcs_clients_optics.crawler.models import SPECIFIED_CACHE_KEYWORDS
from gcs_clients_optics.usecases.base import BaseUseCase

READ_METHODS = {
    "open",
    "open_files",
    "open_local",
    "open_parquet_file",
    "read_block",
    "cat",
    "cat_ranges",
    "cat_file",
    "head",
    "tail",
    "read_text",
    "read_bytes",
    "open_input_stream",
    "open_input_file",
}

CACHE_STRATEGY_DESCRIPTIONS: Dict[str, Dict[str, str]] = {
    "readahead": {
        "category": "Sequential Prefetching",
        "description": "Prefetches chunks ahead of reader cursor for sequential streaming",
        "recommendation": "Optimal for sequential CSV/Parquet scans and sequential dataset streaming.",
    },
    "mmap": {
        "category": "Memory-Mapped File",
        "description": "Spools byte ranges to a temporary local file and memory-maps it",
        "recommendation": "Optimal for random-access binary formats (Parquet/ORC) where small ranges are repeatedly accessed.",
    },
    "block": {
        "category": "Fixed Block Cache",
        "description": "Caches fixed-size blocks in RAM (block_size)",
        "recommendation": "Useful when access pattern exhibits spatial locality across chunk boundaries.",
    },
    "blockcache": {
        "category": "Fixed Block Cache",
        "description": "Alias for block cache in RAM",
        "recommendation": "Useful for spatial locality in chunked access.",
    },
    "parts": {
        "category": "Columnar / Section Caching",
        "description": "Parquet section/column block caching for selective column reads",
        "recommendation": "Required for fsspec.parquet precaching and columnar pruning.",
    },
    "none": {
        "category": "Direct Unbuffered",
        "description": "Disables caching completely; direct HTTP Range GET requests",
        "recommendation": "Optimal when reading data only once or in ultra-low RAM environments.",
    },
    "bytes": {
        "category": "In-Memory Byte Store",
        "description": "Caches exact requested byte ranges in a memory dictionary",
        "recommendation": "Best for small files or repeated identical range reads.",
    },
    "background": {
        "category": "Async Background Prefetch",
        "description": "Asynchronously prefetches data blocks in background threads",
        "recommendation": "Ideal for hiding network latency during compute-heavy batch processing.",
    },
    "file": {
        "category": "Local Disk Cache",
        "description": "Downloads complete file or chunks to local disk cache",
        "recommendation": "Best for immutable datasets reused across multiple training epochs.",
    },
    "NOT_EXPLICIT": {
        "category": "Implicit Default",
        "description": "cache_type keyword omitted (delegates to fsspec/backend default)",
        "recommendation": "Uses fsspec default ('readahead'). Explicit configuration recommended for high-performance workloads.",
    },
}


@dataclass
class CacheUsageItem:
    """Represents a detected caching usage in the read/stream path."""

    file_path: str
    line_number: int
    target_name: str
    cache_type: str
    is_explicit: bool
    cache_options: Optional[str] = None
    enclosing_function: Optional[str] = None
    enclosing_class: Optional[str] = None
    repo_url: Optional[str] = None
    file_url: Optional[str] = None
    code_snippet: str = ""
    strategy_category: str = "Implicit Default"

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CacheReport:
    """Aggregated cache usage report for a repository or target."""

    target_source: str
    total_files_scanned: int
    files_with_read_calls: int
    total_read_calls: int
    explicit_cache_count: int
    implicit_default_count: int
    cache_type_breakdown: Dict[str, int] = field(default_factory=dict)
    strategy_breakdown: Dict[str, int] = field(default_factory=dict)
    repo_url: Optional[str] = None
    items: List[CacheUsageItem] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["items"] = [i.to_dict() for i in self.items]
        return data


class CacheTypeUseCase(BaseUseCase):
    """
    Analyzes cache_type and cache_options configurations across the read / stream path.
    """

    name = "cache-type"
    description = (
        "Analyze cache_type and cache_options usage patterns in the read/stream path."
    )
    aliases = ["caching", "cache-usage", "cache"]

    def scan_code(
        self,
        file_path: str,
        source_code: str,
        repo_url: Optional[str] = None,
        branch: str = "main",
    ) -> List[CacheUsageItem]:
        """Scan Python code specifically for read-path caching configurations."""
        try:
            tree = ast.parse(source_code, filename=file_path)
            visitor = FsspecASTVisitor(
                file_path, source_code, repo_url=repo_url, branch=branch
            )
            visitor.visit(tree)
        except Exception:
            return []

        cache_items: List[CacheUsageItem] = []
        for u in visitor.usages:
            # Filter for read / stream path methods
            method_name = u.target_name.split(".")[-1]
            if method_name in READ_METHODS or "open" in u.target_name.lower():
                is_explicit = (
                    u.cache_type != "NOT_EXPLICIT"
                    and u.cache_type.lower() in SPECIFIED_CACHE_KEYWORDS
                )
                strategy_info = CACHE_STRATEGY_DESCRIPTIONS.get(
                    u.cache_type,
                    {
                        "category": "Custom Cache Strategy",
                        "description": "Custom user-defined cache configuration",
                    },
                )
                cache_items.append(
                    CacheUsageItem(
                        file_path=u.file_path,
                        line_number=u.line_number,
                        target_name=u.target_name,
                        cache_type=u.cache_type,
                        is_explicit=is_explicit,
                        cache_options=u.cache_options,
                        enclosing_function=u.enclosing_function,
                        enclosing_class=u.enclosing_class,
                        repo_url=u.repo_url,
                        file_url=u.file_url,
                        code_snippet=u.code_snippet,
                        strategy_category=strategy_info.get(
                            "category", "Custom"
                        ),
                    )
                )

        return cache_items

    def aggregate_report(
        self,
        target_source: str,
        total_files_scanned: int,
        files_with_usages: int,
        usages: List[CacheUsageItem],
        repo_url: Optional[str] = None,
    ) -> CacheReport:
        """Aggregate cache usage items into a CacheReport."""
        ct_breakdown: Dict[str, int] = {}
        strategy_breakdown: Dict[str, int] = {}
        explicit_count = 0
        implicit_count = 0

        for item in usages:
            ct_breakdown[item.cache_type] = (
                ct_breakdown.get(item.cache_type, 0) + 1
            )
            strategy_breakdown[item.strategy_category] = (
                strategy_breakdown.get(item.strategy_category, 0) + 1
            )
            if item.is_explicit:
                explicit_count += 1
            else:
                implicit_count += 1

        return CacheReport(
            target_source=target_source,
            total_files_scanned=total_files_scanned,
            files_with_read_calls=files_with_usages,
            total_read_calls=len(usages),
            explicit_cache_count=explicit_count,
            implicit_default_count=implicit_count,
            cache_type_breakdown=ct_breakdown,
            strategy_breakdown=strategy_breakdown,
            repo_url=repo_url,
            items=usages,
        )

    def export_reports(
        self,
        reports: List[CacheReport],
        output_csv: Optional[str] = None,
        output_json: Optional[str] = None,
        output_md: Optional[str] = None,
        **kwargs,
    ) -> Dict[str, str]:
        """Export cache analysis in CSV, JSON, and Markdown formats."""
        generated: Dict[str, str] = {}

        if output_csv:
            self._export_csv(reports, output_csv)
            generated["csv"] = output_csv

        if output_json:
            self._export_json(reports, output_json, kwargs.get("elapsed_seconds", 0.0))
            generated["json"] = output_json

        if output_md:
            self._export_markdown(reports, output_md)
            generated["markdown"] = output_md

        return generated

    def _export_csv(self, reports: List[CacheReport], output_path: str):
        rows = []
        for r in reports:
            repo_name = (
                r.target_source.replace("GitHub:", "")
                .replace("Local:", "")
                .split()[0]
            )
            for item in r.items:
                rows.append([
                    repo_name,
                    item.file_path,
                    item.line_number,
                    item.target_name,
                    item.cache_type,
                    item.is_explicit,
                    item.strategy_category,
                    item.cache_options or "None",
                    item.enclosing_class or "None",
                    item.enclosing_function or "global",
                    item.file_url or "",
                    item.code_snippet.replace("\n", " "),
                ])

        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        with open(p, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "repository",
                "file_path",
                "line_number",
                "target_name",
                "cache_type",
                "is_explicit",
                "strategy_category",
                "cache_options",
                "enclosing_class",
                "enclosing_function",
                "file_url",
                "code_snippet",
            ])
            writer.writerows(rows)

    def _export_json(
        self, reports: List[CacheReport], output_path: str, elapsed_seconds: float
    ):
        global_ct: Dict[str, int] = {}
        global_strat: Dict[str, int] = {}
        for r in reports:
            for k, v in r.cache_type_breakdown.items():
                global_ct[k] = global_ct.get(k, 0) + v
            for k, v in r.strategy_breakdown.items():
                global_strat[k] = global_strat.get(k, 0) + v

        json_data = {
            "summary": {
                "total_targets": len(reports),
                "total_files_scanned": sum(r.total_files_scanned for r in reports),
                "total_read_calls": sum(r.total_read_calls for r in reports),
                "explicit_cache_count": sum(
                    r.explicit_cache_count for r in reports
                ),
                "implicit_default_count": sum(
                    r.implicit_default_count for r in reports
                ),
                "global_cache_types": global_ct,
                "global_strategies": global_strat,
                "elapsed_seconds": round(elapsed_seconds, 2),
            },
            "per_repository": [r.to_dict() for r in reports],
        }

        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(json_data, indent=2), encoding="utf-8")

    def _export_markdown(self, reports: List[CacheReport], output_path: str):
        total_files = sum(r.total_files_scanned for r in reports)
        total_calls = sum(r.total_read_calls for r in reports)
        total_explicit = sum(r.explicit_cache_count for r in reports)
        total_implicit = sum(r.implicit_default_count for r in reports)

        global_ct: Dict[str, int] = {}
        for r in reports:
            for k, v in r.cache_type_breakdown.items():
                global_ct[k] = global_ct.get(k, 0) + v

        lines = [
            "# Read-Path Caching Strategy & Cache_Type Optics Report",
            "",
            "This report analyzes **caching strategies and `cache_type` configurations** in the file reading/streaming path across open-source ecosystems.",
            "",
            "---",
            "",
            "## 📊 Global Cache Strategy Summary",
            "",
            f"- **Repositories/Targets Scanned:** `{len(reports)}`",
            f"- **Total Files Scanned:** `{total_files}`",
            f"- **Total Read/Stream Calls Detected:** `{total_calls}`",
            f"- **Explicit Cache Configurations:** `{total_explicit}` ({((total_explicit / total_calls) * 100) if total_calls else 0:.1f}%)",
            f"- **Implicit Default Caching:** `{total_implicit}` ({((total_implicit / total_calls) * 100) if total_calls else 0:.1f}%)",
            "",
            "---",
            "",
            "## 📈 Cache_Type Distribution & Performance Guidelines",
            "",
            "| Cache_Type | Occurrences | % Share | Category | Workload Recommendation |",
            "| :--- | :---: | :---: | :--- | :--- |",
        ]

        for ct, cnt in sorted(global_ct.items(), key=lambda x: -x[1]):
            pct = (cnt / total_calls * 100) if total_calls else 0.0
            info = CACHE_STRATEGY_DESCRIPTIONS.get(
                ct,
                {
                    "category": "Custom Strategy",
                    "recommendation": "Custom application caching strategy",
                },
            )
            lines.append(
                f"| **`{ct}`** | **{cnt}** | `{pct:.1f}%` | {info['category']} | {info['recommendation']} |"
            )

        lines.extend([
            "",
            "---",
            "",
            "## 🏛️ Repository-by-Repository Cache Strategy Matrix",
            "",
            "| Repository | Total Reads | Explicit Cache Calls | Implicit Default | Dominant Strategy |",
            "| :--- | :---: | :---: | :---: | :--- |",
        ])

        for r in reports:
            repo_name = (
                r.target_source.replace("GitHub:", "")
                .replace("Local:", "")
                .split()[0]
            )
            repo_link = (
                f"[{repo_name}]({r.repo_url})"
                if r.repo_url
                else f"`{repo_name}`"
            )
            top_strat = (
                max(r.strategy_breakdown.items(), key=lambda x: x[1])[0]
                if r.strategy_breakdown
                else "None"
            )
            lines.append(
                f"| {repo_link} | `{r.total_read_calls}` | `{r.explicit_cache_count}` | `{r.implicit_default_count}` | `{top_strat}` |"
            )

        lines.extend([
            "",
            "---",
            "",
            "## 💡 Cloud Storage (GCS/S3) Read Optimization Best Practices",
            "",
            "1. **Sequential Parquet & CSV Streaming:**",
            "   - Use `cache_type='readahead'` with `block_size` tuned between 8MB and 64MB depending on bandwidth and memory availability.",
            "2. **Random Access & Point Queries (Arrow / Parquet Column Scanning):**",
            "   - Use `cache_type='mmap'` or `cache_type='block'` to minimize redundant HTTP Range GET requests on shared chunk headers.",
            "3. **Selective Columnar Reading with fsspec.parquet:**",
            "   - Specify `cache_type='parts'` to precache Parquet footer and dictionary pages across worker nodes.",
            "4. **High Concurrency / Distributed Workers:**",
            "   - Use `cache_type='none'` when memory is constrained and streams are read in single passes without seeking.",
            "",
        ])

        p = Path(output_path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\n".join(lines), encoding="utf-8")

    def print_summary(self, reports: List[CacheReport]) -> None:
        """Print console summary."""
        total_calls = sum(r.total_read_calls for r in reports)
        total_explicit = sum(r.explicit_cache_count for r in reports)
        total_implicit = sum(r.implicit_default_count for r in reports)

        print("\n" + "=" * 70)
        print("  ⚡ READ-PATH CACHING & CACHE_TYPE OPTICS SUMMARY")
        print("=" * 70)
        print(f"  • Total Targets Scanned:     {len(reports)}")
        print(f"  • Total Read Calls Analyzed: {total_calls}")
        print(
            f"  • Explicit Cache Configs:    {total_explicit} ({((total_explicit / total_calls) * 100) if total_calls else 0:.1f}%)"
        )
        print(
            f"  • Implicit Default Caching:  {total_implicit} ({((total_implicit / total_calls) * 100) if total_calls else 0:.1f}%)"
        )
        print("=" * 70)
