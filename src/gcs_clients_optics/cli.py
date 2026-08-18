"""
Unified Command Line Interface for GCS Clients Optics with pluggable use cases.
"""

import argparse
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from gcs_clients_optics.analysis.matrix import generate_method_matrix
from gcs_clients_optics.analysis.summary_table import generate_summary_table
from gcs_clients_optics.crawler.dependents import (
    fetch_github_dependents_html,
    load_repos_from_file,
)
from gcs_clients_optics.crawler.repos import (
    DEFAULT_TARGET_REPOS as CODE_REPOS,
    get_default_target_repos,
)
from gcs_clients_optics.engine.optics_engine import OpticsEngine
from gcs_clients_optics.issues.crawler import GitHubIssuesCrawler
from gcs_clients_optics.issues.keywords import (
    DEFAULT_TARGET_REPOS as ISSUES_REPOS,
)
from gcs_clients_optics.issues.models import IssueCrawlReport
from gcs_clients_optics.reporters.issue_reports import (
    export_issues_csv,
    export_issues_json,
    export_issues_markdown,
)
from gcs_clients_optics.simulation.simulator import run_fsspec_simulation
from gcs_clients_optics.storage.sqlite_store import (
    ingest_issue_reports,
    ingest_json_report,
)
from gcs_clients_optics.usecases import (
    AsyncSyncUseCase,
    CacheTypeUseCase,
    FsspecMethodsUseCase,
    ProtocolsUseCase,
    get_use_case,
    list_use_cases,
)


def _resolve_output_paths(
    args: argparse.Namespace, default_basename: str
) -> Tuple[Optional[str], Optional[str], Optional[str], Optional[str]]:
    """
    Resolve output paths based on --format (json/csv/md/sqlite/db/all), --output (-o),
    and specific flags (--output-csv, --output-json, --output-md, --output-sqlite).
    """
    out_csv = getattr(args, "output_csv", None)
    out_json = getattr(args, "output_json", None)
    out_md = getattr(args, "output_md", None)
    out_sqlite = getattr(args, "output_sqlite", None)
    fmt = getattr(args, "format", None)
    out_target = getattr(args, "output", None)

    out_dir = Path("reports")
    if out_target:
        p = Path(out_target)
        if p.suffix.lower() == ".json":
            out_json = str(p)
        elif p.suffix.lower() == ".csv":
            out_csv = str(p)
        elif p.suffix.lower() == ".md":
            out_md = str(p)
        elif p.suffix.lower() in (".db", ".sqlite", ".sqlite3"):
            out_sqlite = str(p)
        else:
            out_dir = p

    if fmt:
        fmt = fmt.lower()
        if fmt in ("json", "all") and not out_json:
            out_json = str(out_dir / f"{default_basename}.json")
        if fmt in ("csv", "all") and not out_csv:
            out_csv = str(out_dir / f"{default_basename}.csv")
        if fmt in ("md", "markdown", "all") and not out_md:
            out_md = str(out_dir / f"{default_basename}.md")
        if fmt in ("sqlite", "db", "all") and not out_sqlite:
            out_sqlite = str(out_dir / "optics.db")

    # If neither format nor specific output is given, default to markdown
    if not (out_csv or out_json or out_md or out_sqlite):
        out_md = str(out_dir / f"{default_basename}.md")

    return out_csv, out_json, out_md, out_sqlite


def _resolve_target_repos(
    args: argparse.Namespace, default_repos: List[Tuple[str, str]]
) -> List[str]:
    """
    Resolve target repositories from:
    1. --repo <owner/repo... or path/to/dependents.json / repos.txt>
    2. --dependents-file / --repos-file
    3. --dependents-of <owner/repo>
    4. --all or default repo list (from get_default_target_repos)
    """
    min_stars = getattr(args, "min_stars", 0)
    limit = getattr(args, "limit", None)

    # 1. Check explicit --repo arguments (which may contain repo names or file paths)
    repo_args = getattr(args, "repo", None)
    if repo_args:
        resolved: List[str] = []
        for item in repo_args:
            item_path = Path(item)
            if item_path.is_file() or item.endswith((".json", ".txt", ".csv")):
                if item_path.exists():
                    loaded = load_repos_from_file(
                        item_path, min_stars=min_stars, limit=limit
                    )
                    print(
                        f"\n[+] Loaded {len(loaded)} repositories from file: {item} (min_stars={min_stars})"
                    )
                    resolved.extend([repo for _, repo in loaded])
                else:
                    print(
                        f"Error: File '{item}' specified in --repo does not exist.",
                        file=sys.stderr,
                    )
            else:
                resolved.append(item)
        if resolved:
            return resolved

    # 2. Check --dependents-file / --repos-file
    dep_file = getattr(args, "dependents_file", None) or getattr(
        args, "repos_file", None
    )
    if dep_file:
        loaded = load_repos_from_file(dep_file, min_stars=min_stars, limit=limit)
        print(
            f"\n[+] Loaded {len(loaded)} repositories from file: {dep_file} (min_stars={min_stars})"
        )
        return [repo for _, repo in loaded]

    # 3. Check --dependents-of
    dep_of = getattr(args, "dependents_of", None)
    if dep_of:
        dep_limit = limit or 50
        print(
            f"\n[+] Discovering dependents of '{dep_of}' on GitHub (min_stars={min_stars}, limit={dep_limit})..."
        )
        loaded = fetch_github_dependents_html(
            dep_of,
            min_stars=min_stars,
            limit=dep_limit,
            github_token=getattr(args, "github_token", None),
        )
        print(f"    ✔ Discovered {len(loaded)} dependent repositories.")
        return [repo for _, repo in loaded]

    # 4. Check --all (or default repos)
    if getattr(args, "all", False):
        loaded_defaults = get_default_target_repos(
            min_stars=min_stars, limit=limit
        )
        return [repo for _, repo in loaded_defaults]

    return []


def _handle_discover_dependents(args: argparse.Namespace) -> int:
    """Discover dependents for a repository and output JSON or text."""
    repo = args.repo or "fsspec/filesystem_spec"
    min_stars = getattr(args, "min_stars", 10)
    limit = getattr(args, "limit", 50) or 50
    print(
        f"\n[+] Discovering dependents of '{repo}' on GitHub (min_stars={min_stars}, limit={limit})..."
    )
    dependents = fetch_github_dependents_html(
        repo,
        min_stars=min_stars,
        limit=limit,
        github_token=args.github_token,
    )
    print(f"    ✔ Found {len(dependents)} dependent repositories:")
    for name, full_repo in dependents:
        print(f"      - {full_repo}")

    if args.output:
        out_p = Path(args.output)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        if out_p.suffix.lower() == ".json":
            data = [{"name": r, "stars": 0} for _, r in dependents]
            out_p.write_text(json.dumps(data, indent=2), encoding="utf-8")
        else:
            out_p.write_text(
                "\n".join(r for _, r in dependents) + "\n", encoding="utf-8"
            )
        print(f"\n  • Saved dependents list to: {args.output}")
    return 0


def _handle_use_case_scan(
    use_case, args: argparse.Namespace, default_basename: str
) -> int:
    """Generic handler for running code-scanning use cases."""
    file_workers = getattr(args, "file_workers", 32)
    subpath = getattr(args, "subpath", None)
    engine = OpticsEngine(
        use_case=use_case,
        include_tests=args.include_tests,
        github_token=args.github_token,
        max_workers=file_workers,
    )
    reports = []
    start_time = time.time()

    if args.local_dir:
        target_desc = f"{args.local_dir} (subpath: {subpath})" if subpath else args.local_dir
        print(f"\n[+] [{use_case.name}] Scanning local directory: {target_desc}...")
        report = engine.scan_local_directory(args.local_dir, subpath=subpath)
        matches_count = getattr(
            report,
            "total_usages_found",
            getattr(
                report,
                "total_read_calls",
                getattr(report, "total_protocol_usages", 0),
            ),
        )
        files_count = getattr(
            report,
            "files_with_usages",
            getattr(
                report,
                "files_with_read_calls",
                getattr(report, "files_with_protocols", 0),
            ),
        )
        print(
            f"    - Scanned {report.total_files_scanned} files | "
            f"Found {matches_count} matches in {files_count} files."
        )
        reports.append(report)

    elif args.local_file:
        print(f"\n[+] [{use_case.name}] Scanning local file: {args.local_file}...")
        report = engine.scan_local_file(args.local_file)
        print(f"    - Completed scan for {args.local_file}.")
        reports.append(report)

    elif (
        getattr(args, "all", False)
        or getattr(args, "repo", None)
        or getattr(args, "dependents_file", None)
        or getattr(args, "repos_file", None)
        or getattr(args, "dependents_of", None)
    ):
        target_repos = _resolve_target_repos(args, CODE_REPOS)
        if not target_repos:
            print("Error: No target repositories resolved.", file=sys.stderr)
            return 1

        concurrency = getattr(args, "concurrency", 16)
        subpath_desc = f", subpath={subpath}" if subpath else ""
        print(
            f"\n[+] [{use_case.name}] Scanning {len(target_repos)} repository target(s) (repo_workers={concurrency}, file_workers={file_workers}{subpath_desc})..."
        )

        def _progress(repo: str, rep: Any):
            matches_count = getattr(
                rep,
                "total_usages_found",
                getattr(
                    rep,
                    "total_read_calls",
                    getattr(rep, "total_protocol_usages", 0),
                ),
            )
            files_count = getattr(
                rep,
                "files_with_usages",
                getattr(
                    rep,
                    "files_with_read_calls",
                    getattr(rep, "files_with_protocols", 0),
                ),
            )
            print(
                f"    ✔ [{use_case.name}] {repo:<30s} | Scanned {rep.total_files_scanned} files | "
                f"Found {matches_count} matches in {files_count} files."
            )

        reports = engine.scan_multiple_repositories(
            target_repos,
            branch=args.branch,
            max_repo_workers=concurrency,
            progress_callback=_progress,
            subpath=subpath,
        )
    else:
        print(
            "Error: Must specify --repo <owner/repo...>, --all, --dependents-file, --dependents-of, --local-dir, or --local-file",
            file=sys.stderr,
        )
        return 1

    elapsed = time.time() - start_time
    use_case.print_summary(reports)
    print(f"\nScan completed across {len(reports)} target(s) in {elapsed:.2f} seconds.")

    out_csv, out_json, out_md, out_sqlite = _resolve_output_paths(
        args, default_basename
    )
    matrix_md = getattr(args, "matrix_md", None)
    summary_md = getattr(args, "summary_md", None)

    use_case.export_reports(
        reports,
        output_csv=out_csv,
        output_json=out_json,
        output_md=out_md,
        output_sqlite=out_sqlite,
        matrix_md=matrix_md,
        summary_md=summary_md,
        elapsed_seconds=elapsed,
        include_tests=args.include_tests,
    )

    if out_sqlite:
        print(f"  • SQLite database updated:  {out_sqlite}")
    if out_csv:
        print(f"  • CSV report exported:      {out_csv}")
    if out_json:
        print(f"  • JSON report exported:     {out_json}")
    if out_md:
        print(f"  • Markdown report exported: {out_md}")
    if matrix_md:
        print(f"  • Matrix exported:          {matrix_md}")
    if summary_md:
        print(f"  • Summary Table exported:   {summary_md}")

    return 0


def _handle_issues(args: argparse.Namespace) -> int:
    """Handle issues crawling command."""
    crawler = GitHubIssuesCrawler(
        github_token=args.github_token,
        max_issues_per_repo=args.max_issues,
    )

    target_repos = _resolve_target_repos(args, ISSUES_REPOS)
    if not target_repos:
        print(
            "Error: Must specify --repo <owner/repo...>, --all, --dependents-file, or --dependents-of",
            file=sys.stderr,
        )
        return 1

    start_time = time.time()

    def _progress(repo: str, report: IssueCrawlReport):
        print(f"[+] Crawled issues for {repo}:")
        print(
            f"    - Scanned {report.total_issues_scanned} issues | "
            f"Found {report.matched_issues_count} matches."
        )

    concurrency = getattr(args, "concurrency", 16)
    reports = crawler.crawl_multiple_repositories(
        target_repos=target_repos,
        state=args.state,
        max_workers=concurrency,
        progress_callback=_progress,
    )

    elapsed = time.time() - start_time
    print(
        f"\nCompleted issue crawling across {len(reports)} repository target(s) in {elapsed:.2f} seconds."
    )

    out_csv, out_json, out_md, out_sqlite = _resolve_output_paths(
        args, "all_issues"
    )

    if out_sqlite:
        ingest_issue_reports(reports, out_sqlite, elapsed_seconds=elapsed)
        print(f"  • SQLite database updated:  {out_sqlite}")

    if out_csv:
        export_issues_csv(reports, out_csv)
        print(f"  • CSV report exported:      {out_csv}")

    if out_json:
        export_issues_json(reports, out_json, elapsed_seconds=elapsed)
        print(f"  • JSON report exported:     {out_json}")

    if out_md:
        export_issues_markdown(reports, out_md)
        print(f"  • Markdown report exported: {out_md}")

    return 0


def _handle_ingest(args: argparse.Namespace) -> int:
    """Ingest existing JSON report into SQLite database."""
    input_file = args.input or getattr(args, "input_json", None)
    db_file = args.db or args.output or "reports/optics.db"

    if not input_file:
        print("Error: Must specify --input <report.json>", file=sys.stderr)
        return 1

    print(f"\n[+] Ingesting {input_file} into SQLite database: {db_file}...")
    try:
        count = ingest_json_report(input_file, db_file)
        print(f"🎉 Successfully ingested {count} record(s) into {db_file}.\n")
        return 0
    except Exception as e:
        print(f"Error ingesting into SQLite: {e}", file=sys.stderr)
        return 1


def _handle_list_usecases(args: argparse.Namespace) -> int:
    """Print all available registered use-cases."""
    usecases = list_use_cases()
    print("\n" + "=" * 75)
    print("  🚀 GCS CLIENTS OPTICS - REGISTERED USE CASES")
    print("=" * 75)
    for idx, uc in enumerate(usecases, start=1):
        aliases_str = ", ".join([f"`{a}`" for a in uc.aliases]) if uc.aliases else "None"
        print(f"\n{idx}. Command: gcs-optics {uc.name}")
        print(f"   Aliases:     {aliases_str}")
        print(f"   Description: {uc.description}")
    print("\n" + "=" * 75)
    return 0


def _handle_matrix(args: argparse.Namespace) -> int:
    input_path = args.input_json or "reports/combined_fsspec_report.json"
    output_path = args.output_md or "reports/method_distribution_matrix.md"
    if not Path(input_path).exists():
        print(f"Error: Input JSON report '{input_path}' not found.", file=sys.stderr)
        return 1
    generate_method_matrix(input_path, output_path=output_path)
    print(f"Matrix report written to: {output_path}")
    return 0


def _handle_summary(args: argparse.Namespace) -> int:
    input_path = args.input_json or "reports/combined_fsspec_report.json"
    output_path = args.output_md or "reports/all_methods_summary_table.md"
    if not Path(input_path).exists():
        print(f"Error: Input JSON report '{input_path}' not found.", file=sys.stderr)
        return 1
    generate_summary_table(input_path, output_path=output_path)
    print(f"Summary table report written to: {output_path}")
    return 0


def _handle_simulate(args: argparse.Namespace) -> int:
    results = run_fsspec_simulation(verbose=not args.quiet)
    if args.quiet:
        print(f"Simulation completed successfully: {results}")
    return 0


def _handle_run_all(args: argparse.Namespace) -> int:
    out_dir = Path(args.output_dir or "reports")
    out_dir.mkdir(parents=True, exist_ok=True)
    db_path = str(out_dir / "optics.db")
    target_repos = _resolve_target_repos(args, CODE_REPOS)
    if not target_repos:
        target_repos = [
            repo
            for _, repo in get_default_target_repos(
                min_stars=getattr(args, "min_stars", 0),
                limit=getattr(args, "limit", None),
            )
        ]

    print("🚀 Running GCS Clients Optics Unified Single-Pass Multi-Use-Case Pipeline...")
    print(
        f"   Target Repositories: {len(target_repos)} | Output Dir: {out_dir}/ | SQLite: {db_path}"
    )

    # 1. Initialize all code analysis use cases
    methods_uc = FsspecMethodsUseCase()
    cache_uc = CacheTypeUseCase()
    proto_uc = ProtocolsUseCase()
    async_uc = AsyncSyncUseCase()
    code_use_cases = [methods_uc, cache_uc, proto_uc, async_uc]

    file_workers = getattr(args, "file_workers", 32)
    engine = OpticsEngine(
        use_case=methods_uc,
        include_tests=False,
        github_token=args.github_token,
        max_workers=file_workers,
    )

    print(
        f"\n[+] [Single-Pass Crawl] Scanning {len(target_repos)} repositories for 4 use cases simultaneously..."
    )
    start_time = time.time()

    def _progress(repo: str, repo_reports: Dict[str, Any]):
        fsspec_rep = repo_reports.get("fsspec-methods")
        files = fsspec_rep.total_files_scanned if fsspec_rep else 0
        matches = fsspec_rep.total_usages_found if fsspec_rep else 0
        print(
            f"    ✔ {repo:<30s} | Scanned {files} files | Found {matches} FSSPEC method calls"
        )

    concurrency = getattr(args, "concurrency", 16)
    subpath = getattr(args, "subpath", None)
    multi_reports = engine.scan_multiple_repositories_multi(
        target_repos,
        code_use_cases,
        branch="main",
        max_repo_workers=concurrency,
        progress_callback=_progress,
        subpath=subpath,
    )
    crawl_elapsed = time.time() - start_time
    print(
        f"\n🎉 Completed single-pass code scan across all {len(target_repos)} repositories in {crawl_elapsed:.2f} seconds!"
    )

    # Export Use Case 1: fsspec-methods
    print("\n[+] Exporting Use Case 1: FSSPEC Method Usages...")
    methods_uc.export_reports(
        multi_reports["fsspec-methods"],
        output_csv=str(out_dir / "fsspec_crawl_results.csv"),
        output_json=str(out_dir / "combined_fsspec_report.json"),
        output_md=str(out_dir / "combined_fsspec_report.md"),
        output_sqlite=db_path,
        matrix_md=str(out_dir / "method_distribution_matrix.md"),
        summary_md=str(out_dir / "all_methods_summary_table.md"),
        elapsed_seconds=crawl_elapsed,
    )

    # Export Use Case 2: cache-type
    print("[+] Exporting Use Case 2: Read-Path Caching & Cache_Type...")
    cache_uc.export_reports(
        multi_reports["cache-type"],
        output_csv=str(out_dir / "cache_analysis.csv"),
        output_json=str(out_dir / "cache_analysis.json"),
        output_md=str(out_dir / "cache_analysis.md"),
        output_sqlite=db_path,
        elapsed_seconds=crawl_elapsed,
    )

    # Export Use Case 3: protocols
    print("[+] Exporting Use Case 3: Storage Protocols & Cloud Backends...")
    proto_uc.export_reports(
        multi_reports["protocols"],
        output_csv=str(out_dir / "protocols_analysis.csv"),
        output_json=str(out_dir / "protocols_analysis.json"),
        output_md=str(out_dir / "protocols_analysis.md"),
        output_sqlite=db_path,
        elapsed_seconds=crawl_elapsed,
    )

    # Export Use Case 4: async-sync
    print("[+] Exporting Use Case 4: Async vs Sync Method Usages...")
    async_uc.export_reports(
        multi_reports["async-sync"],
        output_csv=str(out_dir / "async_sync_analysis.csv"),
        output_json=str(out_dir / "async_sync_analysis.json"),
        output_md=str(out_dir / "async_sync_analysis.md"),
        output_sqlite=db_path,
        elapsed_seconds=crawl_elapsed,
    )

    # 5. issues
    print("\n=== Use Case 5: GitHub Performance & Filesystem Issues ===")
    issues_args = argparse.Namespace(
        all=True,
        repo=None,
        state="open",
        max_issues=200,
        github_token=args.github_token,
        format="all",
        output=str(out_dir),
        output_sqlite=db_path,
        output_csv=str(out_dir / "all_issues.csv"),
        output_json=str(out_dir / "all_issues.json"),
        output_md=str(out_dir / "all_issues.md"),
    )
    _handle_issues(issues_args)

    # 6. simulate
    print("\n=== Use Case 6: In-Memory Filesystem Simulation ===")
    run_fsspec_simulation(verbose=True)

    total_elapsed = time.time() - start_time
    print(
        f"\n🎉 Full single-pass pipeline completed in {total_elapsed:.2f} seconds! All reports and optics.db generated in: {out_dir}/"
    )
    return 0


def _add_common_code_args(parser: argparse.ArgumentParser):
    """Add standard arguments for code-crawling commands."""
    parser.add_argument(
        "--repo",
        "-r",
        nargs="+",
        help="One or more GitHub repositories (e.g. --repo dask/dask)",
    )
    parser.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Crawl all default open-source repositories",
    )
    parser.add_argument(
        "--local-dir",
        "-d",
        help="Path to local directory to scan recursively",
    )
    parser.add_argument(
        "--local-file",
        "-f",
        help="Path to a single local Python file to scan",
    )
    parser.add_argument(
        "--branch",
        "-b",
        default="main",
        help="GitHub branch (default: main)",
    )
    parser.add_argument(
        "--include-tests",
        action="store_true",
        help="Include test Python files",
    )
    parser.add_argument(
        "--github-token",
        help="GitHub API token (or set GITHUB_TOKEN env var)",
    )
    parser.add_argument(
        "--format",
        "-t",
        choices=["json", "csv", "md", "sqlite", "db", "all"],
        help="Output format: json, csv, md, sqlite, or all (default: md)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file path (e.g. -o report.json / -o optics.db) or output directory",
    )
    parser.add_argument(
        "--output-csv", "-c", help="Specific path to write output CSV report"
    )
    parser.add_argument(
        "--output-json", help="Specific path to write output JSON report"
    )
    parser.add_argument(
        "--output-md", "-m", help="Specific path to write output Markdown report"
    )
    parser.add_argument(
        "--output-sqlite", help="Specific path to write SQLite database file"
    )
    parser.add_argument(
        "--subpath",
        "--path",
        "-p",
        help="Subdirectory or subpath to scan within repository or local dir (e.g. --subpath python/ray)",
    )
    parser.add_argument(
        "--dependents-file",
        "--repos-file",
        "-D",
        help="Path to JSON or text file containing repository dependents (e.g. from github-dependents-info)",
    )
    parser.add_argument(
        "--dependents-of",
        help="Discover downstream dependents directly from GitHub (e.g. --dependents-of fsspec/filesystem_spec)",
    )
    parser.add_argument(
        "--min-stars",
        type=int,
        default=0,
        help="Minimum GitHub stars threshold when loading dependents (default: 0)",
    )
    parser.add_argument(
        "--limit",
        "-n",
        type=int,
        default=None,
        help="Maximum number of repositories to scan from dependents",
    )
    parser.add_argument(
        "--file-workers",
        "-w",
        type=int,
        default=32,
        help="Number of concurrent file download/parsing workers per repository (default: 32)",
    )
    parser.add_argument(
        "--concurrency",
        "-j",
        type=int,
        default=16,
        help="Number of concurrent repositories to crawl (default: 16)",
    )


def build_parser() -> argparse.ArgumentParser:
    """Build root CLI argument parser with use-case subcommands."""
    parser = argparse.ArgumentParser(
        prog="gcs-optics",
        description="GCS Clients Optics - Extensible multi-use-case analysis suite for cloud filesystems.",
    )
    subparsers = parser.add_subparsers(
        dest="command", title="Commands", help="Available subcommands & use cases"
    )

    # 1. Use Case 1: fsspec-methods
    p_methods = subparsers.add_parser(
        "fsspec-methods",
        aliases=["methods", "crawl-code", "code"],
        help="[Use Case 1] Analyze abstract filesystem / fsspec method usage across codebases.",
    )
    _add_common_code_args(p_methods)
    p_methods.add_argument(
        "--matrix-md", help="Path to write method distribution matrix markdown"
    )
    p_methods.add_argument(
        "--summary-md", help="Path to write method summary table markdown"
    )

    # 2. Use Case 2: cache-type
    p_cache = subparsers.add_parser(
        "cache-type",
        aliases=["caching", "cache-usage", "cache"],
        help="[Use Case 2] Analyze cache_type and cache_options in the read/stream path.",
    )
    _add_common_code_args(p_cache)

    # 3. Use Case 3: issues
    p_issues = subparsers.add_parser(
        "issues",
        aliases=["crawl-issues", "issues-performance"],
        help="[Use Case 3] Crawl GitHub issues for performance bottlenecks and storage topics.",
    )
    p_issues.add_argument(
        "--repo",
        "-r",
        nargs="+",
        help="One or more GitHub repositories (e.g. --repo dask/dask fsspec/gcsfs)",
    )
    p_issues.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Crawl open issues across all default repositories",
    )
    p_issues.add_argument(
        "--dependents-file",
        "--repos-file",
        "-D",
        help="Path to JSON or text file containing repository dependents",
    )
    p_issues.add_argument(
        "--dependents-of",
        help="Discover downstream dependents directly from GitHub (e.g. --dependents-of fsspec/filesystem_spec)",
    )
    p_issues.add_argument(
        "--min-stars",
        type=int,
        default=0,
        help="Minimum GitHub stars threshold (default: 0)",
    )
    p_issues.add_argument(
        "--limit",
        "-n",
        type=int,
        default=None,
        help="Maximum number of repositories to scan from dependents",
    )
    p_issues.add_argument(
        "--state",
        default="open",
        choices=["open", "closed", "all"],
        help="Issue state to scan (default: open)",
    )
    p_issues.add_argument(
        "--max-issues",
        type=int,
        default=200,
        help="Max issues to scan per repository (default: 200)",
    )
    p_issues.add_argument(
        "--github-token",
        help="GitHub API token (or set GITHUB_TOKEN env var)",
    )
    p_issues.add_argument(
        "--format",
        "-t",
        choices=["json", "csv", "md", "sqlite", "db", "all"],
        help="Output format: json, csv, md, sqlite, or all (default: md)",
    )
    p_issues.add_argument(
        "--output",
        "-o",
        help="Output file path (e.g. -o issues.json / -o optics.db) or directory",
    )
    p_issues.add_argument(
        "--output-csv", "-c", help="Specific path to write output CSV report"
    )
    p_issues.add_argument(
        "--output-json", help="Specific path to write output JSON report"
    )
    p_issues.add_argument(
        "--output-md", "-m", help="Specific path to write output Markdown report"
    )
    p_issues.add_argument(
        "--output-sqlite", help="Specific path to write SQLite database file"
    )
    p_issues.add_argument(
        "--concurrency",
        "-j",
        type=int,
        default=16,
        help="Number of concurrent repositories to crawl (default: 16)",
    )

    # 4. Use Case 4: protocols
    p_proto = subparsers.add_parser(
        "protocols",
        aliases=["storage", "backends", "cloud-providers"],
        help="[Use Case 4] Analyze cloud storage protocols (gs://, s3://, abfs://) and drivers.",
    )
    _add_common_code_args(p_proto)

    # 5. Use Case 5: async-sync
    p_async = subparsers.add_parser(
        "async-sync",
        aliases=["async", "async-optics", "concurrency-modes", "sync-async"],
        help="[Use Case 5] Analyze async vs sync filesystem method usage, coroutines, and bridges.",
    )
    _add_common_code_args(p_async)

    # 6. Ingest JSON to SQLite
    p_ingest = subparsers.add_parser(
        "ingest",
        aliases=["load-db"],
        help="Ingest pre-existing JSON report into SQLite database.",
    )
    p_ingest.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to input JSON report file (e.g. reports/combined_fsspec_report.json)",
    )
    p_ingest.add_argument(
        "--db",
        "-d",
        default="reports/optics.db",
        help="Path to SQLite DB file (default: reports/optics.db)",
    )

    # 7. List use cases
    subparsers.add_parser(
        "list-usecases",
        aliases=["usecases", "list"],
        help="List all registered analysis use cases.",
    )

    # 8. Dependents discovery command
    p_dep = subparsers.add_parser(
        "discover-dependents",
        aliases=["dependents", "find-dependents"],
        help="Discover downstream dependents of a package/repository from GitHub.",
    )
    p_dep.add_argument(
        "--repo",
        "-r",
        default="fsspec/filesystem_spec",
        help="Repository to find dependents for (default: fsspec/filesystem_spec)",
    )
    p_dep.add_argument(
        "--min-stars",
        type=int,
        default=10,
        help="Minimum stars threshold (default: 10)",
    )
    p_dep.add_argument(
        "--limit",
        "-n",
        type=int,
        default=50,
        help="Maximum number of dependents to discover (default: 50)",
    )
    p_dep.add_argument(
        "--output",
        "-o",
        help="Path to save discovered dependents list (.json or .txt)",
    )
    p_dep.add_argument(
        "--github-token",
        help="GitHub API token (or set GITHUB_TOKEN env var)",
    )

    # 9. Matrix & Summary utilities
    p_matrix = subparsers.add_parser(
        "matrix",
        help="Generate cross-repository method occurrence matrix markdown.",
    )
    p_matrix.add_argument(
        "--input-json",
        "-i",
        help="Path to combined_fsspec_report.json (default: reports/combined_fsspec_report.json)",
    )
    p_matrix.add_argument(
        "--output-md",
        "-o",
        help="Path to write matrix markdown (default: reports/method_distribution_matrix.md)",
    )

    p_summary = subparsers.add_parser(
        "summary",
        help="Generate comprehensive 4-column method summary table markdown.",
    )
    p_summary.add_argument(
        "--input-json",
        "-i",
        help="Path to combined_fsspec_report.json (default: reports/combined_fsspec_report.json)",
    )
    p_summary.add_argument(
        "--output-md",
        "-o",
        help="Path to write summary markdown (default: reports/all_methods_summary_table.md)",
    )

    # 10. Simulation
    p_sim = subparsers.add_parser(
        "simulate",
        aliases=["sim"],
        help="Run live in-memory simulation of all fsspec / abstract filesystem methods.",
    )
    p_sim.add_argument(
        "--quiet", "-q", action="store_true", help="Suppress verbose logs"
    )

    # 11. Run All
    p_all = subparsers.add_parser(
        "run-all",
        help="Run complete multi-use-case pipeline across all targets.",
    )
    p_all.add_argument(
        "--repo",
        "-r",
        nargs="+",
        help="One or more GitHub repositories (e.g. --repo dask/dask fsspec/gcsfs)",
    )
    p_all.add_argument(
        "--dependents-file",
        "--repos-file",
        "-D",
        help="Path to JSON or text file containing repository dependents (e.g. from github-dependents-info)",
    )
    p_all.add_argument(
        "--dependents-of",
        help="Discover downstream dependents directly from GitHub (e.g. --dependents-of fsspec/filesystem_spec)",
    )
    p_all.add_argument(
        "--min-stars",
        type=int,
        default=0,
        help="Minimum GitHub stars threshold when loading dependents (default: 0)",
    )
    p_all.add_argument(
        "--limit",
        "-n",
        type=int,
        default=None,
        help="Maximum number of repositories to scan from dependents",
    )
    p_all.add_argument(
        "--subpath",
        "--path",
        "-p",
        help="Subdirectory or subpath to scan within repository (e.g. --subpath python/ray)",
    )
    p_all.add_argument(
        "--file-workers",
        "-w",
        type=int,
        default=32,
        help="Number of concurrent file download/parsing workers per repository (default: 32)",
    )
    p_all.add_argument(
        "--concurrency",
        "-j",
        type=int,
        default=16,
        help="Number of concurrent repositories to crawl (default: 16)",
    )
    p_all.add_argument(
        "--output-dir",
        "-o",
        default="reports",
        help="Output directory for reports (default: reports)",
    )
    p_all.add_argument(
        "--github-token",
        help="GitHub API token (or set GITHUB_TOKEN env var)",
    )

    return parser


def main(args: Optional[List[str]] = None) -> int:
    """CLI Entry Point."""
    parser = build_parser()
    parsed = parser.parse_args(args)

    if not parsed.command:
        parser.print_help()
        return 0

    if parsed.command in ("fsspec-methods", "methods", "crawl-code", "code"):
        use_case = get_use_case("fsspec-methods")
        return _handle_use_case_scan(use_case, parsed, "fsspec_methods")

    elif parsed.command in ("cache-type", "caching", "cache-usage", "cache"):
        use_case = get_use_case("cache-type")
        return _handle_use_case_scan(use_case, parsed, "cache_analysis")

    elif parsed.command in ("protocols", "storage", "backends", "cloud-providers"):
        use_case = get_use_case("protocols")
        return _handle_use_case_scan(use_case, parsed, "protocols_analysis")

    elif parsed.command in ("async-sync", "async", "async-optics", "concurrency-modes", "sync-async"):
        use_case = get_use_case("async-sync")
        return _handle_use_case_scan(use_case, parsed, "async_sync_analysis")

    elif parsed.command in ("issues", "crawl-issues", "issues-performance"):
        return _handle_issues(parsed)

    elif parsed.command in ("discover-dependents", "dependents", "find-dependents"):
        return _handle_discover_dependents(parsed)

    elif parsed.command in ("ingest", "load-db"):
        return _handle_ingest(parsed)

    elif parsed.command in ("list-usecases", "usecases", "list"):
        return _handle_list_usecases(parsed)

    elif parsed.command == "matrix":
        return _handle_matrix(parsed)

    elif parsed.command == "summary":
        return _handle_summary(parsed)

    elif parsed.command in ("simulate", "sim"):
        return _handle_simulate(parsed)

    elif parsed.command == "run-all":
        return _handle_run_all(parsed)

    else:
        # Check if it matches any other dynamically registered use case
        uc = get_use_case(parsed.command)
        if uc:
            return _handle_use_case_scan(uc, parsed, uc.name)
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
