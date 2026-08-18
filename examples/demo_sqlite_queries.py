"""
Demo Script: Querying the GCS Clients Optics SQLite Database.

This demo illustrates how downstream AI agents, automated analysis tools,
or data engineers can query `optics.db` directly using standard SQLite / Python.

Usage:
    python examples/demo_sqlite_queries.py [--db reports/optics.db]
"""

import argparse
import sqlite3
import sys
from pathlib import Path


def run_demo(db_path: str) -> None:
    """Execute sample agent queries against the Optics SQLite database."""
    p = Path(db_path)
    if not p.exists():
        print(f"[-] Database not found at '{db_path}'.")
        print("[+] Creating and populating database from existing reports...")
        from gcs_clients_optics.storage.sqlite_store import ingest_json_report

        json_reports = [
            "reports/combined_fsspec_report.json",
            "reports/all_issues.json",
        ]
        for r in json_reports:
            if Path(r).exists():
                ingest_json_report(r, db_path)

    if not p.exists():
        print(f"Error: Could not locate or create database at {db_path}", file=sys.stderr)
        return

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print("\n" + "=" * 80)
    print("  🚀 GCS CLIENTS OPTICS - SQLITE AGENT QUERY DEMO")
    print(f"  Database File: {db_path}")
    print("=" * 80)

    # --------------------------------------------------------------------------
    # Query 1: Top 10 Most Frequently Called Methods & Functional Categories
    # --------------------------------------------------------------------------
    print("\n📊 1. Top 10 Most Frequently Called FSSPEC Methods:")
    print("-" * 80)
    query_1 = """
        SELECT
            target_name,
            category,
            COUNT(*) AS total_calls,
            COUNT(DISTINCT repository) AS repo_spread
        FROM method_usages
        GROUP BY target_name, category
        ORDER BY total_calls DESC
        LIMIT 10;
    """
    cursor.execute(query_1)
    print(f"{'Target Call':<25} | {'Category':<35} | {'Calls':<6} | {'Repos'}")
    print("-" * 80)
    for row in cursor.fetchall():
        print(
            f"{row['target_name']:<25} | {row['category']:<35} | {row['total_calls']:<6} | {row['repo_spread']}"
        )

    # --------------------------------------------------------------------------
    # Query 2: Read-Path Caching Strategy Distribution
    # --------------------------------------------------------------------------
    print("\n⚡ 2. Read-Path Caching Strategy Distribution (`cache_type`):")
    print("-" * 80)
    query_2 = """
        SELECT
            cache_type,
            COUNT(*) AS occurrences,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM method_usages WHERE category = 'Stream Reading & Writing'), 1) AS pct_share
        FROM method_usages
        WHERE category = 'Stream Reading & Writing'
        GROUP BY cache_type
        ORDER BY occurrences DESC;
    """
    cursor.execute(query_2)
    print(f"{'Cache Strategy':<25} | {'Occurrences':<12} | {'% of Read Path'}")
    print("-" * 80)
    for row in cursor.fetchall():
        print(f"{row['cache_type']:<25} | {row['occurrences']:<12} | {row['pct_share']}%")

    # --------------------------------------------------------------------------
    # Query 3: Cross-Repository Core Method Usage Matrix
    # --------------------------------------------------------------------------
    print("\n🏢 3. Cross-Repository Method Usage Breakdown (Top Repositories):")
    print("-" * 80)
    query_3 = """
        SELECT
            repository,
            SUM(CASE WHEN base_method = 'open' THEN 1 ELSE 0 END) AS open_calls,
            SUM(CASE WHEN base_method = 'exists' THEN 1 ELSE 0 END) AS exists_calls,
            SUM(CASE WHEN base_method = 'info' THEN 1 ELSE 0 END) AS info_calls,
            SUM(CASE WHEN base_method = 'ls' THEN 1 ELSE 0 END) AS ls_calls,
            SUM(CASE WHEN base_method = 'glob' THEN 1 ELSE 0 END) AS glob_calls,
            SUM(CASE WHEN base_method = 'get' THEN 1 ELSE 0 END) AS get_calls,
            COUNT(*) AS total_calls
        FROM method_usages
        GROUP BY repository
        ORDER BY total_calls DESC
        LIMIT 6;
    """
    cursor.execute(query_3)
    print(f"{'Repository':<24} | {'open':<5} | {'exists':<6} | {'info':<5} | {'ls':<4} | {'glob':<5} | {'get':<4} | {'Total'}")
    print("-" * 80)
    for row in cursor.fetchall():
        print(
            f"{row['repository']:<24} | {row['open_calls']:<5} | {row['exists_calls']:<6} | "
            f"{row['info_calls']:<5} | {row['ls_calls']:<4} | {row['glob_calls']:<5} | "
            f"{row['get_calls']:<4} | {row['total_calls']}"
        )

    # --------------------------------------------------------------------------
    # Query 4: High-Relevance GitHub Storage Performance Issues
    # --------------------------------------------------------------------------
    print("\n🐛 4. Top 5 High-Relevance GitHub Filesystem Performance Issues:")
    print("-" * 80)
    query_4 = """
        SELECT
            repository,
            issue_number,
            title,
            relevance_score,
            html_url
        FROM issues
        ORDER BY relevance_score DESC
        LIMIT 5;
    """
    cursor.execute(query_4)
    for idx, row in enumerate(cursor.fetchall(), start=1):
        print(f"{idx}. [{row['repository']} #{row['issue_number']}] (Score: {row['relevance_score']})")
        print(f"   Title: {row['title']}")
        print(f"   URL:   {row['html_url']}\n")

    # --------------------------------------------------------------------------
    # Query 5: Code Snippet Search (Explicit Cache Configurations)
    # --------------------------------------------------------------------------
    print("🔍 5. Sample Code Snippets with Explicit `cache_type` Configurations:")
    print("-" * 80)
    query_5 = """
        SELECT
            repository,
            file_path,
            line_number,
            target_name,
            cache_type,
            code_snippet
        FROM method_usages
        WHERE cache_type != 'NOT_EXPLICIT'
        LIMIT 3;
    """
    cursor.execute(query_5)
    for row in cursor.fetchall():
        print(f"• {row['repository']} -> {row['file_path']}:{row['line_number']} (cache_type='{row['cache_type']}')")
        print(f"  Snippet: {row['code_snippet'].strip()}\n")

    # --------------------------------------------------------------------------
    # Query 6: Async vs Sync Execution & Potential Event Loop Blocks
    # --------------------------------------------------------------------------
    print("\n⚡ 6. Async vs Sync Execution Breakdown & Anti-Pattern Warnings:")
    print("-" * 80)
    cursor.execute("""
        SELECT
            execution_mode,
            async_mechanism,
            COUNT(*) AS count,
            SUM(potential_event_loop_block) AS event_loop_blocks
        FROM async_sync_usages
        GROUP BY execution_mode, async_mechanism
        ORDER BY count DESC;
    """)
    rows = cursor.fetchall()
    if rows:
        print(f"{'Execution Mode':<15} | {'Mechanism':<28} | {'Calls':<8} | {'Event Loop Blocks'}")
        print("-" * 80)
        for row in rows:
            print(f"{row['execution_mode']:<15} | {row['async_mechanism']:<28} | {row['count']:<8} | {row['event_loop_blocks']}")
    else:
        print("  (Run `gcs-optics async-sync --all --format sqlite -o reports/optics.db` to populate async_sync_usages)")

    print("=" * 80)
    print("  ✅ Demo complete! Agents can execute any arbitrary SQL against the database.")
    print("=" * 80)
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Demo queries on GCS Clients Optics SQLite database.")
    parser.add_argument(
        "--db",
        "-d",
        default="reports/optics.db",
        help="Path to SQLite database (default: reports/optics.db)",
    )
    args = parser.parse_args()
    run_demo(args.db)
