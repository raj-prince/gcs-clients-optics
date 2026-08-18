"""
Unified Command Line Interface for GCS Clients Optics.
"""

import argparse
import sys
import time
from pathlib import Path
from typing import List, Optional

from gcs_clients_optics.analysis.matrix import generate_method_matrix
from gcs_clients_optics.analysis.summary_table import generate_summary_table
from gcs_clients_optics.crawler.engine import FsspecCrawlerEngine
from gcs_clients_optics.crawler.models import CrawlReport
from gcs_clients_optics.crawler.repos import DEFAULT_TARGET_REPOS as CODE_REPOS
from gcs_clients_optics.issues.crawler import GitHubIssuesCrawler
from gcs_clients_optics.issues.keywords import (
    DEFAULT_TARGET_REPOS as ISSUES_REPOS,
)
from gcs_clients_optics.issues.models import IssueCrawlReport
from gcs_clients_optics.reporters.code_reports import (
    export_csv_report,
    export_json_report,
    export_markdown_report,
)
from gcs_clients_optics.reporters.issue_reports import (
    export_issues_csv,
    export_issues_json,
    export_issues_markdown,
)
from gcs_clients_optics.simulation.simulator import run_fsspec_simulation


def _handle_crawl_code(args: argparse.Namespace) -> int:
    """Handle crawl-code command."""
    engine = FsspecCrawlerEngine(
        include_tests=args.include_tests,
        github_token=args.github_token,
    )
    reports: List[CrawlReport] = []
    start_time = time.time()

    if args.local_dir:
        print(f"\n[+] Scanning local directory: {args.local_dir}...")
        report = engine.scan_local_directory(args.local_dir)
        print(
            f"    - Scanned {report.total_files_scanned} files | "
            f"Found {report.total_usages_found} usages in {report.files_with_usages} files."
        )
        reports.append(report)

    elif args.local_file:
        print(f"\n[+] Scanning local file: {args.local_file}...")
        usages = engine.scan_local_file(args.local_file)
        summary = engine._build_cache_type_summary(usages)
        report = CrawlReport(
            target_source=f"Local:{Path(args.local_file).name}",
            total_files_scanned=1,
            files_with_usages=1 if usages else 0,
            total_usages_found=len(usages),
            cache_type_summary=summary,
            usages=usages,
        )
        print(f"    - Found {len(usages)} usages.")
        reports.append(report)

    elif args.all or args.repo:
        target_repos = (
            [repo for _, repo in CODE_REPOS]
            if args.all
            else (args.repo or [])
        )
        for repo in target_repos:
            print(f"\n[+] Crawling GitHub repo: {repo}...")
            report = engine.scan_github_repo(repo, branch=args.branch)
            print(
                f"    - Scanned {report.total_files_scanned} files | "
                f"Found {report.total_usages_found} usages in {report.files_with_usages} files."
            )
            if report.cache_type_summary:
                print(f"    - Cache_Type Summary: {report.cache_type_summary}")
            reports.append(report)
    else:
        print(
            "Error: Must specify --repo <owner/repo...>, --all, --local-dir, or --local-file",
            file=sys.stderr,
        )
        return 1

    elapsed = time.time() - start_time
    print(
        f"\nCompleted code scan across {len(reports)} target(s) in {elapsed:.2f} seconds."
    )

    if args.output_csv:
        export_csv_report(reports, args.output_csv)
        print(f"CSV report exported to: {args.output_csv}")

    if args.output_json:
        export_json_report(reports, args.output_json, elapsed_seconds=elapsed)
        print(f"JSON report exported to: {args.output_json}")

    if args.output_md:
        export_markdown_report(
            reports, args.output_md, include_tests=args.include_tests
        )
        print(f"Markdown report exported to: {args.output_md}")

    return 0


def _handle_crawl_issues(args: argparse.Namespace) -> int:
    """Handle crawl-issues command."""
    crawler = GitHubIssuesCrawler(
        github_token=args.github_token,
        max_issues_per_repo=args.max_issues,
    )

    if args.all:
        target_repos = [repo for _, repo in ISSUES_REPOS]
    elif args.repo:
        target_repos = args.repo
    else:
        print(
            "Error: Must specify --repo <owner/repo...> or --all",
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

    reports = crawler.crawl_multiple_repositories(
        target_repos=target_repos,
        state=args.state,
        max_workers=5,
        progress_callback=_progress,
    )

    elapsed = time.time() - start_time
    print(
        f"\nCompleted issue crawling across {len(reports)} repository target(s) in {elapsed:.2f} seconds."
    )

    if args.output_csv:
        export_issues_csv(reports, args.output_csv)
        print(f"CSV report exported to: {args.output_csv}")

    if args.output_json:
        export_issues_json(reports, args.output_json, elapsed_seconds=elapsed)
        print(f"JSON report exported to: {args.output_json}")

    if args.output_md:
        export_issues_markdown(reports, args.output_md)
        print(f"Markdown report exported to: {args.output_md}")

    return 0


def _handle_matrix(args: argparse.Namespace) -> int:
    """Handle matrix generation command."""
    input_path = args.input_json or "reports/combined_fsspec_report.json"
    output_path = args.output_md or "reports/method_distribution_matrix.md"

    if not Path(input_path).exists():
        print(
            f"Error: Input JSON report '{input_path}' not found.",
            file=sys.stderr,
        )
        return 1

    generate_method_matrix(input_path, output_path=output_path)
    print(f"Matrix report written to: {output_path}")
    return 0


def _handle_summary(args: argparse.Namespace) -> int:
    """Handle summary table generation command."""
    input_path = args.input_json or "reports/combined_fsspec_report.json"
    output_path = args.output_md or "reports/all_methods_summary_table.md"

    if not Path(input_path).exists():
        print(
            f"Error: Input JSON report '{input_path}' not found.",
            file=sys.stderr,
        )
        return 1

    generate_summary_table(input_path, output_path=output_path)
    print(f"Summary table report written to: {output_path}")
    return 0


def _handle_simulate(args: argparse.Namespace) -> int:
    """Handle simulation command."""
    results = run_fsspec_simulation(verbose=not args.quiet)
    if args.quiet:
        print(f"Simulation completed successfully: {results}")
    return 0


def _handle_run_all(args: argparse.Namespace) -> int:
    """Handle run-all pipeline command."""
    out_dir = Path(args.output_dir or "reports")
    out_dir.mkdir(parents=True, exist_ok=True)

    print("🚀 Running full GCS Clients Optics analysis pipeline...")

    # Step 1: Code Crawl
    print("\n--- Step 1: Crawling Code Usages ---")
    code_args = argparse.Namespace(
        all=True,
        repo=None,
        local_dir=None,
        local_file=None,
        branch="main",
        include_tests=False,
        github_token=args.github_token,
        output_csv=str(out_dir / "fsspec_crawl_results.csv"),
        output_json=str(out_dir / "combined_fsspec_report.json"),
        output_md=str(out_dir / "combined_fsspec_report.md"),
    )
    _handle_crawl_code(code_args)

    # Step 2: Matrix & Summary
    print("\n--- Step 2: Generating Matrix & Summary Tables ---")
    generate_method_matrix(
        out_dir / "combined_fsspec_report.json",
        output_path=out_dir / "method_distribution_matrix.md",
    )
    generate_summary_table(
        out_dir / "combined_fsspec_report.json",
        output_path=out_dir / "all_methods_summary_table.md",
    )

    # Step 3: Issues Crawl
    print("\n--- Step 3: Crawling Performance & Filesystem Issues ---")
    issues_args = argparse.Namespace(
        all=True,
        repo=None,
        state="open",
        max_issues=200,
        github_token=args.github_token,
        output_csv=str(out_dir / "all_issues.csv"),
        output_json=str(out_dir / "all_issues.json"),
        output_md=str(out_dir / "all_issues.md"),
    )
    _handle_crawl_issues(issues_args)

    # Step 4: Simulation
    print("\n--- Step 4: Running In-Memory Verification Simulation ---")
    run_fsspec_simulation(verbose=True)

    print(f"\n🎉 Full pipeline completed! All reports generated in: {out_dir}/")
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build root CLI argument parser with subcommands."""
    parser = argparse.ArgumentParser(
        prog="gcs-optics",
        description="GCS Clients Optics - AST code crawler, GitHub issues tracker, and filesystem analytics.",
    )
    subparsers = parser.add_subparsers(
        dest="command", title="Commands", help="Available subcommands"
    )

    # crawl-code
    p_code = subparsers.add_parser(
        "crawl-code",
        aliases=["code"],
        help="Crawl repositories or local files for filesystem / fsspec AST usages.",
    )
    p_code.add_argument(
        "--repo",
        "-r",
        nargs="+",
        help="One or more GitHub repositories (e.g. --repo dask/dask)",
    )
    p_code.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Crawl all default open-source repositories",
    )
    p_code.add_argument(
        "--local-dir",
        "-d",
        help="Path to local directory to scan recursively",
    )
    p_code.add_argument(
        "--local-file",
        "-f",
        help="Path to a single local Python file to scan",
    )
    p_code.add_argument(
        "--branch",
        "-b",
        default="main",
        help="GitHub branch (default: main)",
    )
    p_code.add_argument(
        "--include-tests",
        action="store_true",
        help="Include test Python files",
    )
    p_code.add_argument(
        "--github-token",
        help="GitHub API token (or set GITHUB_TOKEN env var)",
    )
    p_code.add_argument(
        "--output-csv", "-c", help="Path to write output CSV report"
    )
    p_code.add_argument(
        "--output-json", "-o", help="Path to write output JSON report"
    )
    p_code.add_argument(
        "--output-md", "-m", help="Path to write output Markdown report"
    )

    # crawl-issues
    p_issues = subparsers.add_parser(
        "crawl-issues",
        aliases=["issues"],
        help="Crawl GitHub issues for performance bottlenecks and filesystem topics.",
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
        "--output-csv", "-c", help="Path to write output CSV report"
    )
    p_issues.add_argument(
        "--output-json", "-o", help="Path to write output JSON report"
    )
    p_issues.add_argument(
        "--output-md", "-m", help="Path to write output Markdown report"
    )

    # matrix
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

    # summary
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

    # simulate
    p_sim = subparsers.add_parser(
        "simulate",
        aliases=["sim"],
        help="Run live in-memory simulation of all fsspec / abstract filesystem methods.",
    )
    p_sim.add_argument(
        "--quiet", "-q", action="store_true", help="Suppress verbose logs"
    )

    # run-all
    p_all = subparsers.add_parser(
        "run-all",
        help="Run complete pipeline: code crawl + issues crawl + matrix + summary + simulation.",
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

    if parsed.command in ("crawl-code", "code"):
        return _handle_crawl_code(parsed)
    elif parsed.command in ("crawl-issues", "issues"):
        return _handle_crawl_issues(parsed)
    elif parsed.command == "matrix":
        return _handle_matrix(parsed)
    elif parsed.command == "summary":
        return _handle_summary(parsed)
    elif parsed.command in ("simulate", "sim"):
        return _handle_simulate(parsed)
    elif parsed.command == "run-all":
        return _handle_run_all(parsed)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
