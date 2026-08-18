# GCS Clients Optics (`gcs-clients-optics`)

A simple, extensible CLI and analysis engine for **Google Cloud Storage (GCS) and `fsspec` filesystem optics**.

`gcs-clients-optics` scans Python codebases (via AST) and GitHub issues across open-source ecosystems (Dask, Ray, Hugging Face Datasets, PyTorch, etc.) using a **generic engine with pluggable use cases**.

---

## ⚡ Quick Start & Installation

```bash
git clone https://github.com/raj-prince/gcs-clients-optics.git
cd gcs-clients-optics

# Option 1: Install globally via uv tool (available directly in your PATH):
uv tool install --editable .

# Option 2: Install with standard pip in a virtual environment:
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

---

## 🚀 CLI Commands & Use Cases

List all available use cases:
```bash
gcs-optics list-usecases
```

### 1. FSSPEC Method Usage Across Repos (`fsspec-methods` / `methods`)
Scans code for all abstract filesystem calls (`open`, `exists`, `info`, `ls`, `glob`, `find`, `walk`, `makedirs`, `get`, `put`, etc.):

```bash
# Output as JSON
gcs-optics fsspec-methods --repo dask/dask --format json -o dask_methods.json

# Output as CSV
gcs-optics fsspec-methods --all --format csv -o reports/fsspec_methods.csv

# Output directly into SQLite database
gcs-optics fsspec-methods --all --format sqlite -o reports/optics.db

# Scan local code directory as JSON
gcs-optics fsspec-methods --local-dir /path/to/project --format json -o local_methods.json
```

---

### 2. Cache-Type Usage in the Read Path (`cache-type` / `caching`)
Analyzes `cache_type` (`readahead`, `mmap`, `block`, `parts`, `none`, `bytes`, `background`, `file`), `cache_options`, and read-path buffering:

```bash
# Output as JSON
gcs-optics cache-type --all --format json -o reports/cache_analysis.json

# Output as CSV
gcs-optics cache-type --all --format csv -o reports/cache_analysis.csv

# Output directly into SQLite database
gcs-optics cache-type --all --format sqlite -o reports/optics.db
```

---

### 3. GitHub Issues Performance Tracker (`issues` / `crawl-issues`)
Crawls and scores open GitHub issues for storage performance bottlenecks (latency, throughput, OOM, prefetching, chunk size):

```bash
# Output as JSON
gcs-optics issues --repo fsspec/gcsfs fsspec/s3fs --format json -o storage_issues.json

# Output as CSV
gcs-optics issues --all --format csv -o reports/all_issues.csv

# Output directly into SQLite database
gcs-optics issues --all --format sqlite -o reports/optics.db
```

---

### 4. Storage Protocols & Cloud Backends (`protocols` / `storage`)
Analyzes cloud protocol URIs (`gs://`, `s3://`, `abfs://`, `hdfs://`, `memory://`, `file://`) and backend driver instantiations (`gcsfs`, `s3fs`, etc.):

```bash
# Output as JSON
gcs-optics protocols --all --format json -o reports/protocols.json

# Output as CSV
gcs-optics protocols --all --format csv -o reports/protocols.csv

# Output directly into SQLite database
gcs-optics protocols --all --format sqlite -o reports/optics.db
```

---

### 5. Ingesting Existing JSON Reports into SQLite (`ingest`)
If you already have generated JSON reports, you can ingest them into SQLite at any time:

```bash
gcs-optics ingest --input reports/combined_fsspec_report.json --db reports/optics.db
gcs-optics ingest --input reports/all_issues.json --db reports/optics.db
```

---

### 6. In-Memory Filesystem Simulation (`simulate`)
Runs a live in-memory verification of directory traversal, wildcards, metadata, and stream reading:

```bash
gcs-optics simulate
```

---

### 7. Full Pipeline (`run-all`)
Runs all use cases and exports reports to a directory (including `optics.db`):

```bash
gcs-optics run-all --output-dir reports
```

---

## 💾 Output Formats: JSON, CSV, Markdown, SQLite

You can specify the output format using `--format` (`-t`) and the output path with `--output` (`-o`):

| Flag / Option | Description | Example |
| :--- | :--- | :--- |
| `--format json` | Output report in JSON format | `gcs-optics fsspec-methods --all --format json -o output.json` |
| `--format csv` | Output report in CSV format | `gcs-optics cache-type --all --format csv -o output.csv` |
| `--format md` | Output report in Markdown format | `gcs-optics cache-type --all --format md -o output.md` |
| `--format sqlite` | Ingest and store data in SQLite database | `gcs-optics fsspec-methods --all --format sqlite -o reports/optics.db` |
| `--format all` | Output all formats (JSON, CSV, MD, SQLite) | `gcs-optics fsspec-methods --all --format all -o reports/` |
| `-o <path>` / `--output <path>` | Destination file (`.json`, `.csv`, `.md`, `.db`) or directory | `-o my_report.json` or `-o reports/optics.db` |

---

## 🗄️ Querying the SQLite Database (`.db`)

When data is exported to SQLite (`optics.db`), other agents, scripts, or analytics tools can directly query the normalized relational tables without parsing JSON or CSV files.

### 📋 Database Tables Schema

- **`method_usages`**: Every AST method call (`repository`, `file_path`, `line_number`, `target_name`, `base_method`, `category`, `cache_type`, `code_snippet`, `file_url`)
- **`cache_usages`**: Read-path caching strategies (`repository`, `file_path`, `line_number`, `target_name`, `cache_type`, `is_explicit`, `strategy_category`, `cache_options`, `code_snippet`)
- **`protocol_usages`**: Storage protocols (`repository`, `file_path`, `line_number`, `protocol`, `provider`, `usage_type`, `context`, `code_snippet`)
- **`issues`**: GitHub performance issues (`repository`, `issue_number`, `title`, `state`, `relevance_score`, `matched_keywords`, `categories`, `html_url`, `body_preview`)
- **`scan_runs`**: Metadata for every scan (`scan_id`, `use_case`, `target_source`, `total_files_scanned`, `total_matches`, `elapsed_seconds`, `scanned_at`)

---

### 🐍 Python Example (for Downstream Agents)

```python
import sqlite3

# Connect to database
conn = sqlite3.connect("reports/optics.db")
conn.row_factory = sqlite3.Row  # Dict-like row access
cursor = conn.cursor()

# 1. Query Top 10 Most Used Methods
cursor.execute("""
    SELECT target_name, category, COUNT(*) as call_count
    FROM method_usages
    GROUP BY target_name, category
    ORDER BY call_count DESC
    LIMIT 10;
""")
for row in cursor.fetchall():
    print(f"{row['target_name']:20s} | {row['category']:30s} | {row['call_count']} calls")

# 2. Query Read-Path Caching Distribution
cursor.execute("""
    SELECT cache_type, strategy_category, COUNT(*) as count
    FROM cache_usages
    GROUP BY cache_type, strategy_category
    ORDER BY count DESC;
""")
for row in cursor.fetchall():
    print(f"{row['cache_type']:15s} | {row['strategy_category']:25s} | {row['count']}")

# 3. Find High-Relevance Performance Issues
cursor.execute("""
    SELECT repository, issue_number, title, relevance_score, html_url
    FROM issues
    WHERE relevance_score >= 0.6
    ORDER BY relevance_score DESC
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(f"[{row['repository']} #{row['issue_number']}] {row['title']} (Score: {row['relevance_score']})")

conn.close()
```

---

### 💻 Command Line SQLite Query Example

```bash
# Top 5 methods across repositories
sqlite3 reports/optics.db "SELECT target_name, count(*) FROM method_usages GROUP BY 1 ORDER BY 2 DESC LIMIT 5;"

# All readahead or mmap usages in Dask
sqlite3 -header -column reports/optics.db \
  "SELECT file_path, line_number, cache_type, code_snippet FROM cache_usages WHERE repository = 'dask/dask' AND cache_type != 'NOT_EXPLICIT';"
```

---

## 🧩 Adding a Custom Use Case

Any new use case plugs directly into the generic `OpticsEngine`:

```python
from gcs_clients_optics import BaseUseCase, OpticsEngine, register_use_case

class CompressionUseCase(BaseUseCase):
    name = "compression"
    description = "Analyze compression codec usage (gzip, snappy, zstd, lz4)"

    def scan_code(self, file_path, source_code, repo_url=None, branch="main"):
        # Custom AST or regex inspection logic
        return [...]

    def aggregate_report(self, target_source, total_files_scanned, files_with_usages, usages, repo_url=None):
        return {...}

    def export_reports(self, reports, output_csv=None, output_json=None, output_md=None, output_sqlite=None, **kwargs):
        # Export JSON/CSV/MD/SQLite
        return {}

# Register globally
register_use_case(CompressionUseCase())

# Run with generic engine
engine = OpticsEngine(use_case=CompressionUseCase())
report = engine.scan_local_directory("src/")
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📄 License

Apache 2.0