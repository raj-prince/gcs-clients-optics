"""
Unified Command Line Interface for GCS Clients Optics with pluggable use cases.
"""

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from gcs_clients_optics.crawler.dependents import (
    DEFAULT_TARGET_REPOS as CODE_REPOS,
    fetch_github_dependents_html,
    get_default_target_repos,
    load_repos_from_file,
)
from gcs_clients_optics.crawler.engine import OpticsEngine
from gcs_clients_optics.usecases import (
    FsspecMethodsUseCase,
    get_use_case,
    list_use_cases,
)


def _resolve_output_paths(
    args: argparse.Namespace, default_basename: str
) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Resolve output paths based on --format (json/csv/md/all), --output (-o),
    and specific flags (--output-csv, --output-json, --output-md).
    """
    out_csv = getattr(args, "output_csv", None)
    out_json = getattr(args, "output_json", None)
    out_md = getattr(args, "output_md", None)
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

    # If neither format nor specific output is given, default to markdown
    if not (out_csv or out_json or out_md):
        out_md = str(out_dir / f"{default_basename}.md")

    return out_csv, out_json, out_md


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

    if getattr(args, "local_file", None):
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
            "Error: Must specify --repo <owner/repo...>, --all, --dependents-file, --dependents-of, or --local-file",
            file=sys.stderr,
        )
        return 1

    elapsed = time.time() - start_time
    use_case.print_summary(reports)
    print(f"\nScan completed across {len(reports)} target(s) in {elapsed:.2f} seconds.")

    out_csv, out_json, out_md = _resolve_output_paths(
        args, default_basename
    )
    matrix_md = getattr(args, "matrix_md", None)
    summary_md = getattr(args, "summary_md", None)

    use_case.export_reports(
        reports,
        output_csv=out_csv,
        output_json=out_json,
        output_md=out_md,
        matrix_md=matrix_md,
        summary_md=summary_md,
        elapsed_seconds=elapsed,
        include_tests=args.include_tests,
    )

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





def _add_common_code_args(parser: argparse.ArgumentParser):
    """Add standard arguments for code-crawling commands."""
    parser.add_argument(
        "--repo",
        "-r",
        nargs="+",
        help="One or more GitHub repositories (e.g. --repo pytorch/pytorch dask/dask)",
    )
    parser.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Crawl all default open-source repositories",
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
        choices=["json", "csv", "md", "all"],
        help="Output format: json, csv, md, or all (default: md)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output file path (e.g. -o report.json / -o report.md) or output directory",
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
        "--matrix-md", help="Path to write method distribution matrix markdown"
    )
    parser.add_argument(
        "--summary-md", help="Path to write method summary table markdown"
    )
    parser.add_argument(
        "--subpath",
        "--path",
        "-p",
        help="Subdirectory or subpath to scan within repository (e.g. --subpath python/ray)",
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
    """Build root CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="gcs-optics",
        description="GCS Clients Optics - FSSPEC & cloud filesystem method usage analyzer.",
    )
    subparsers = parser.add_subparsers(
        dest="command", title="commands", help="Available subcommands"
    )

    # 1. scan command
    p_scan = subparsers.add_parser(
        "scan",
        help="Scan GitHub repositories for fsspec method usage (default command).",
    )
    _add_common_code_args(p_scan)

    # 2. dependents discovery command
    p_dep = subparsers.add_parser(
        "dependents",
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

    return parser


def main(args: Optional[List[str]] = None) -> int:
    """CLI Entry Point."""
    raw_args = list(sys.argv[1:] if args is None else args)

    # If flags are passed without a subcommand, default to 'scan'
    if raw_args and raw_args[0] not in ("scan", "dependents", "-h", "--help"):
        raw_args.insert(0, "scan")

    parser = build_parser()
    parsed = parser.parse_args(raw_args)

    if not parsed.command:
        parser.print_help()
        return 0

    if parsed.command == "scan":
        use_case = get_use_case("fsspec-methods")
        return _handle_use_case_scan(use_case, parsed, "fsspec_methods")

    elif parsed.command == "dependents":
        return _handle_discover_dependents(parsed)

    else:
        uc = get_use_case(parsed.command)
        if uc:
            return _handle_use_case_scan(uc, parsed, uc.name)
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
