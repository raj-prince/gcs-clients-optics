"""
SQLite storage engine for ingesting and storing GCS Clients Optics analysis data.
"""

import json
import sqlite3
import uuid
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

from gcs_clients_optics.analysis.categorization import categorize_method


def init_db(db_path: Union[str, Path]) -> sqlite3.Connection:
    """Initialize SQLite database schema and indexes."""
    p = Path(db_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(p))
    conn.execute("PRAGMA journal_mode=WAL;")
    conn.execute("PRAGMA synchronous=NORMAL;")

    with conn:
        # 1. Scan Runs & Target Metadata
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS scan_runs (
                scan_id TEXT PRIMARY KEY,
                use_case TEXT NOT NULL,
                target_source TEXT NOT NULL,
                repo_url TEXT,
                total_files_scanned INTEGER,
                total_matches INTEGER,
                elapsed_seconds REAL,
                scanned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
        )

        # 2. FSSPEC Method Usages
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS method_usages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id TEXT,
                repository TEXT NOT NULL,
                file_path TEXT NOT NULL,
                line_number INTEGER,
                end_line_number INTEGER,
                target_name TEXT NOT NULL,
                base_method TEXT NOT NULL,
                category TEXT NOT NULL,
                cache_type TEXT,
                is_specified_cache_keyword BOOLEAN,
                cache_options TEXT,
                enclosing_class TEXT,
                enclosing_function TEXT,
                file_url TEXT,
                code_snippet TEXT,
                detection_method TEXT,
                FOREIGN KEY(scan_id) REFERENCES scan_runs(scan_id)
            );
            """
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_methods_repo ON method_usages(repository);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_methods_target ON method_usages(target_name);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_methods_base ON method_usages(base_method);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_methods_category ON method_usages(category);"
        )

        # 3. Read-Path Cache Usages
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS cache_usages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id TEXT,
                repository TEXT NOT NULL,
                file_path TEXT NOT NULL,
                line_number INTEGER,
                target_name TEXT NOT NULL,
                cache_type TEXT NOT NULL,
                is_explicit BOOLEAN,
                strategy_category TEXT,
                cache_options TEXT,
                enclosing_class TEXT,
                enclosing_function TEXT,
                file_url TEXT,
                code_snippet TEXT,
                FOREIGN KEY(scan_id) REFERENCES scan_runs(scan_id)
            );
            """
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_cache_repo ON cache_usages(repository);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_cache_type ON cache_usages(cache_type);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_cache_strategy ON cache_usages(strategy_category);"
        )

        # 4. Storage Protocols & Cloud Backends
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS protocol_usages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id TEXT,
                repository TEXT NOT NULL,
                file_path TEXT NOT NULL,
                line_number INTEGER,
                protocol TEXT NOT NULL,
                provider TEXT NOT NULL,
                usage_type TEXT NOT NULL,
                context TEXT,
                file_url TEXT,
                code_snippet TEXT,
                FOREIGN KEY(scan_id) REFERENCES scan_runs(scan_id)
            );
            """
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_proto_repo ON protocol_usages(repository);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_proto_protocol ON protocol_usages(protocol);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_proto_provider ON protocol_usages(provider);"
        )

        # 5. GitHub Performance Issues
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS issues (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                scan_id TEXT,
                repository TEXT NOT NULL,
                issue_number INTEGER NOT NULL,
                title TEXT NOT NULL,
                state TEXT NOT NULL,
                relevance_score REAL,
                matched_keywords TEXT,
                categories TEXT,
                html_url TEXT,
                author TEXT,
                created_at TEXT,
                updated_at TEXT,
                body_preview TEXT,
                FOREIGN KEY(scan_id) REFERENCES scan_runs(scan_id)
            );
            """
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_issues_repo ON issues(repository);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_issues_score ON issues(relevance_score);"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_issues_number ON issues(repository, issue_number);"
        )

    return conn


def _clean_repo_name(target_source: Optional[str]) -> str:
    """Extract clean repository name (e.g. 'GitHub:dask/dask (main)' -> 'dask/dask')."""
    if not target_source:
        return "unknown"
    cleaned = target_source.replace("GitHub:", "").replace("Local:", "").strip()
    parts = cleaned.split()
    return parts[0] if parts else cleaned


def ingest_fsspec_reports(
    reports: List[Any],
    db_path: Union[str, Path],
    elapsed_seconds: float = 0.0,
) -> int:
    """Ingest Fsspec method usage reports into SQLite."""
    conn = init_db(db_path)
    total_inserted = 0

    with conn:
        for r in reports:
            scan_id = str(uuid.uuid4())
            repo_name = _clean_repo_name(r.target_source)
            conn.execute(
                """
                INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                (
                    scan_id,
                    "fsspec-methods",
                    r.target_source,
                    r.repo_url,
                    r.total_files_scanned,
                    r.total_usages_found,
                    elapsed_seconds,
                ),
            )

            rows = []
            for u in r.usages:
                target_name = getattr(u, "target_name", "")
                base_method = target_name.split(".")[-1].strip()
                cat = categorize_method(target_name)
                cache_opts = getattr(u, "cache_options", None)
                opts_str = json.dumps(cache_opts) if cache_opts else None

                rows.append((
                    scan_id,
                    repo_name,
                    getattr(u, "file_path", ""),
                    getattr(u, "line_number", 0),
                    getattr(u, "end_line_number", getattr(u, "line_number", 0)),
                    target_name,
                    base_method,
                    cat,
                    getattr(u, "cache_type", "NOT_EXPLICIT"),
                    getattr(u, "is_specified_cache_keyword", False),
                    opts_str,
                    getattr(u, "enclosing_class", None),
                    getattr(u, "enclosing_function", None),
                    getattr(u, "file_url", None),
                    getattr(u, "code_snippet", ""),
                    getattr(u, "detection_method", "ast"),
                ))

            if rows:
                conn.executemany(
                    """
                    INSERT INTO method_usages (
                        scan_id, repository, file_path, line_number, end_line_number,
                        target_name, base_method, category, cache_type,
                        is_specified_cache_keyword, cache_options, enclosing_class,
                        enclosing_function, file_url, code_snippet, detection_method
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                    """,
                    rows,
                )
                total_inserted += len(rows)

    conn.close()
    return total_inserted


def ingest_cache_reports(
    reports: List[Any],
    db_path: Union[str, Path],
    elapsed_seconds: float = 0.0,
) -> int:
    """Ingest read-path cache strategy reports into SQLite."""
    conn = init_db(db_path)
    total_inserted = 0

    with conn:
        for r in reports:
            scan_id = str(uuid.uuid4())
            repo_name = _clean_repo_name(r.target_source)
            conn.execute(
                """
                INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                (
                    scan_id,
                    "cache-type",
                    r.target_source,
                    r.repo_url,
                    r.total_files_scanned,
                    r.total_read_calls,
                    elapsed_seconds,
                ),
            )

            rows = []
            for item in r.items:
                cache_opts = getattr(item, "cache_options", None)
                opts_str = json.dumps(cache_opts) if cache_opts else None
                rows.append((
                    scan_id,
                    repo_name,
                    getattr(item, "file_path", ""),
                    getattr(item, "line_number", 0),
                    getattr(item, "target_name", ""),
                    getattr(item, "cache_type", "NOT_EXPLICIT"),
                    getattr(item, "is_explicit", False),
                    getattr(item, "strategy_category", "Implicit Default"),
                    opts_str,
                    getattr(item, "enclosing_class", None),
                    getattr(item, "enclosing_function", None),
                    getattr(item, "file_url", None),
                    getattr(item, "code_snippet", ""),
                ))

            if rows:
                conn.executemany(
                    """
                    INSERT INTO cache_usages (
                        scan_id, repository, file_path, line_number, target_name,
                        cache_type, is_explicit, strategy_category, cache_options,
                        enclosing_class, enclosing_function, file_url, code_snippet
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                    """,
                    rows,
                )
                total_inserted += len(rows)

    conn.close()
    return total_inserted


def ingest_protocol_reports(
    reports: List[Any],
    db_path: Union[str, Path],
    elapsed_seconds: float = 0.0,
) -> int:
    """Ingest storage protocol and driver reports into SQLite."""
    conn = init_db(db_path)
    total_inserted = 0

    with conn:
        for r in reports:
            scan_id = str(uuid.uuid4())
            repo_name = _clean_repo_name(r.target_source)
            conn.execute(
                """
                INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                (
                    scan_id,
                    "protocols",
                    r.target_source,
                    r.repo_url,
                    r.total_files_scanned,
                    r.total_protocol_usages,
                    elapsed_seconds,
                ),
            )

            rows = []
            for item in r.items:
                rows.append((
                    scan_id,
                    repo_name,
                    getattr(item, "file_path", ""),
                    getattr(item, "line_number", 0),
                    getattr(item, "protocol", ""),
                    getattr(item, "provider", ""),
                    getattr(item, "usage_type", ""),
                    getattr(item, "context", ""),
                    getattr(item, "file_url", None),
                    getattr(item, "code_snippet", ""),
                ))

            if rows:
                conn.executemany(
                    """
                    INSERT INTO protocol_usages (
                        scan_id, repository, file_path, line_number, protocol,
                        provider, usage_type, context, file_url, code_snippet
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                    """,
                    rows,
                )
                total_inserted += len(rows)

    conn.close()
    return total_inserted


def ingest_issue_reports(
    reports: List[Any],
    db_path: Union[str, Path],
    elapsed_seconds: float = 0.0,
) -> int:
    """Ingest GitHub issues into SQLite."""
    conn = init_db(db_path)
    total_inserted = 0

    with conn:
        for r in reports:
            scan_id = str(uuid.uuid4())
            repo_name = _clean_repo_name(r.target_repo)
            conn.execute(
                """
                INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                (
                    scan_id,
                    "issues",
                    r.target_repo,
                    r.repo_url,
                    r.total_issues_scanned,
                    r.matched_issues_count,
                    elapsed_seconds,
                ),
            )

            rows = []
            for issue in r.issues:
                keywords_str = json.dumps(getattr(issue, "matched_keywords", []))
                cat_str = json.dumps(getattr(issue, "categories", []))
                rows.append((
                    scan_id,
                    repo_name,
                    getattr(issue, "number", 0),
                    getattr(issue, "title", ""),
                    getattr(issue, "state", "open"),
                    getattr(issue, "relevance_score", 0.0),
                    keywords_str,
                    cat_str,
                    getattr(issue, "html_url", ""),
                    getattr(issue, "author", ""),
                    getattr(issue, "created_at", ""),
                    getattr(issue, "updated_at", ""),
                    getattr(issue, "body_preview", ""),
                ))

            if rows:
                conn.executemany(
                    """
                    INSERT INTO issues (
                        scan_id, repository, issue_number, title, state,
                        relevance_score, matched_keywords, categories,
                        html_url, author, created_at, updated_at, body_preview
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                    """,
                    rows,
                )
                total_inserted += len(rows)

    conn.close()
    return total_inserted


def ingest_json_report(
    json_path: Union[str, Path], db_path: Union[str, Path]
) -> int:
    """Ingest any pre-existing JSON report file into the SQLite database."""
    p = Path(json_path)
    if not p.exists():
        raise FileNotFoundError(f"JSON file not found: {json_path}")

    data = json.loads(p.read_text(encoding="utf-8"))
    conn = init_db(db_path)
    total_inserted = 0

    # Case 1: Code / FSSPEC report with 'per_repository' or 'usages'
    if "per_repository" in data:
        with conn:
            for repo_data in data["per_repository"]:
                scan_id = str(uuid.uuid4())
                target_source = repo_data.get("target_source", "")
                repo_name = _clean_repo_name(target_source)
                repo_url = repo_data.get("repo_url")

                # Check if it's fsspec usages or cache usages or protocols or issues
                if "usages" in repo_data:
                    usages = repo_data.get("usages", [])
                    conn.execute(
                        """
                        INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                        VALUES (?, ?, ?, ?, ?, ?, ?);
                        """,
                        (
                            scan_id,
                            "fsspec-methods",
                            target_source,
                            repo_url,
                            repo_data.get("total_files_scanned", 0),
                            len(usages),
                            0.0,
                        ),
                    )
                    rows = []
                    for u in usages:
                        target_name = u.get("target_name", "")
                        base_method = target_name.split(".")[-1].strip()
                        cat = categorize_method(target_name)
                        cache_opts = u.get("cache_options")
                        opts_str = (
                            json.dumps(cache_opts) if cache_opts else None
                        )
                        rows.append((
                            scan_id,
                            repo_name,
                            u.get("file_path", ""),
                            u.get("line_number", 0),
                            u.get("end_line_number", u.get("line_number", 0)),
                            target_name,
                            base_method,
                            cat,
                            u.get("cache_type", "NOT_EXPLICIT"),
                            u.get("is_specified_cache_keyword", False),
                            opts_str,
                            u.get("enclosing_class"),
                            u.get("enclosing_function"),
                            u.get("file_url"),
                            u.get("code_snippet", ""),
                            u.get("detection_method", "ast"),
                        ))
                    if rows:
                        conn.executemany(
                            """
                            INSERT INTO method_usages (
                                scan_id, repository, file_path, line_number, end_line_number,
                                target_name, base_method, category, cache_type,
                                is_specified_cache_keyword, cache_options, enclosing_class,
                                enclosing_function, file_url, code_snippet, detection_method
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                            """,
                            rows,
                        )
                        total_inserted += len(rows)

                elif "issues" in repo_data:
                    issues = repo_data.get("issues", [])
                    target_repo = repo_data.get("target_repo") or target_source
                    repo_clean = _clean_repo_name(target_repo)
                    conn.execute(
                        """
                        INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                        VALUES (?, ?, ?, ?, ?, ?, ?);
                        """,
                        (
                            scan_id,
                            "issues",
                            target_repo,
                            repo_url,
                            repo_data.get("total_issues_scanned", 0),
                            len(issues),
                            0.0,
                        ),
                    )
                    rows = []
                    for issue in issues:
                        keywords = issue.get("matched_keywords") or (
                            issue.get("matched_fs_keywords", [])
                            + issue.get("matched_perf_keywords", [])
                        )
                        keywords_str = json.dumps(keywords)
                        cat_str = json.dumps(issue.get("categories", []))
                        rows.append((
                            scan_id,
                            repo_clean,
                            issue.get("issue_number") or issue.get("number", 0),
                            issue.get("title", ""),
                            issue.get("state", "open"),
                            float(issue.get("relevance_score", 0.0)),
                            keywords_str,
                            cat_str,
                            issue.get("html_url", ""),
                            issue.get("author", ""),
                            issue.get("created_at", ""),
                            issue.get("updated_at", ""),
                            issue.get("body_snippet") or issue.get("body_preview", ""),
                        ))
                    if rows:
                        conn.executemany(
                            """
                            INSERT INTO issues (
                                scan_id, repository, issue_number, title, state,
                                relevance_score, matched_keywords, categories,
                                html_url, author, created_at, updated_at, body_preview
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                            """,
                            rows,
                        )
                        total_inserted += len(rows)

                elif "items" in repo_data:
                    items = repo_data.get("items", [])
                    # Check if items are cache or protocol
                    if items and "strategy_category" in items[0]:
                        conn.execute(
                            """
                            INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                            VALUES (?, ?, ?, ?, ?, ?, ?);
                            """,
                            (
                                scan_id,
                                "cache-type",
                                target_source,
                                repo_url,
                                repo_data.get("total_files_scanned", 0),
                                len(items),
                                0.0,
                            ),
                        )
                        rows = []
                        for it in items:
                            cache_opts = it.get("cache_options")
                            opts_str = (
                                json.dumps(cache_opts) if cache_opts else None
                            )
                            rows.append((
                                scan_id,
                                repo_name,
                                it.get("file_path", ""),
                                it.get("line_number", 0),
                                it.get("target_name", ""),
                                it.get("cache_type", "NOT_EXPLICIT"),
                                it.get("is_explicit", False),
                                it.get("strategy_category", "Implicit Default"),
                                opts_str,
                                it.get("enclosing_class"),
                                it.get("enclosing_function"),
                                it.get("file_url"),
                                it.get("code_snippet", ""),
                            ))
                        if rows:
                            conn.executemany(
                                """
                                INSERT INTO cache_usages (
                                    scan_id, repository, file_path, line_number, target_name,
                                    cache_type, is_explicit, strategy_category, cache_options,
                                    enclosing_class, enclosing_function, file_url, code_snippet
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                                """,
                                rows,
                            )
                            total_inserted += len(rows)

                    elif items and "protocol" in items[0]:
                        conn.execute(
                            """
                            INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                            VALUES (?, ?, ?, ?, ?, ?, ?);
                            """,
                            (
                                scan_id,
                                "protocols",
                                target_source,
                                repo_url,
                                repo_data.get("total_files_scanned", 0),
                                len(items),
                                0.0,
                            ),
                        )
                        rows = []
                        for it in items:
                            rows.append((
                                scan_id,
                                repo_name,
                                it.get("file_path", ""),
                                it.get("line_number", 0),
                                it.get("protocol", ""),
                                it.get("provider", ""),
                                it.get("usage_type", ""),
                                it.get("context", ""),
                                it.get("file_url"),
                                it.get("code_snippet", ""),
                            ))
                        if rows:
                            conn.executemany(
                                """
                                INSERT INTO protocol_usages (
                                    scan_id, repository, file_path, line_number, protocol,
                                    provider, usage_type, context, file_url, code_snippet
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                                """,
                                rows,
                            )
                            total_inserted += len(rows)

    # Case 2: Issues report
    elif "per_repository_issues" in data or isinstance(data, list):
        reports_list = (
            data.get("per_repository_issues", [])
            if isinstance(data, dict)
            else data
        )
        with conn:
            for rep in reports_list:
                scan_id = str(uuid.uuid4())
                target_repo = rep.get("target_repo", "")
                repo_name = _clean_repo_name(target_repo)
                issues_list = rep.get("issues", [])

                conn.execute(
                    """
                    INSERT INTO scan_runs (scan_id, use_case, target_source, repo_url, total_files_scanned, total_matches, elapsed_seconds)
                    VALUES (?, ?, ?, ?, ?, ?, ?);
                    """,
                    (
                        scan_id,
                        "issues",
                        target_repo,
                        rep.get("repo_url"),
                        rep.get("total_issues_scanned", 0),
                        len(issues_list),
                        0.0,
                    ),
                )
                rows = []
                for issue in issues_list:
                    keywords_str = json.dumps(issue.get("matched_keywords", []))
                    cat_str = json.dumps(issue.get("categories", []))
                    rows.append((
                        scan_id,
                        repo_name,
                        issue.get("number", 0),
                        issue.get("title", ""),
                        issue.get("state", "open"),
                        issue.get("relevance_score", 0.0),
                        keywords_str,
                        cat_str,
                        issue.get("html_url", ""),
                        issue.get("author", ""),
                        issue.get("created_at", ""),
                        issue.get("updated_at", ""),
                        issue.get("body_preview", ""),
                    ))
                if rows:
                    conn.executemany(
                        """
                        INSERT INTO issues (
                            scan_id, repository, issue_number, title, state,
                            relevance_score, matched_keywords, categories,
                            html_url, author, created_at, updated_at, body_preview
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                        """,
                        rows,
                    )
                    total_inserted += len(rows)

    conn.close()
    return total_inserted
