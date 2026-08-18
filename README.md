# GCS Clients Optics (`gcs-clients-optics`)

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A modular, production-grade Python analysis suite and crawler tool designed for **Google Cloud Storage (GCS) and `fsspec` abstract filesystem optics**.

`gcs-clients-optics` inspects AST codebases, tracks GitHub performance issues, generates cross-repository method usage matrices, and simulates filesystem operations across top Python data science, machine learning, and MLOps open-source ecosystems (e.g., Dask, Ray, Hugging Face Datasets, PyTorch, pandas, DVC, etc.).

---

## 🏗️ Architecture & Modules

```
gcs-clients-optics/
├── pyproject.toml              # Packaging, build system & CLI entry point
├── README.md                   # Repository documentation
├── reports/                    # Generated datasets, matrices & markdown reports
│   ├── all_issues.csv / .json / .md
│   ├── all_methods_summary_table.md
│   ├── combined_fsspec_report.json / .md
│   ├── fsspec_crawl_results.csv
│   └── method_distribution_matrix.md
├── src/
│   └── gcs_clients_optics/     # Core Python package
│       ├── __init__.py         # Package exports & version
│       ├── cli.py              # Unified CLI (`gcs-optics`)
│       ├── crawler/            # AST Code Crawler & GitHub Trees API scanner
│       │   ├── ast_visitor.py  # FsspecASTVisitor (AST parsing & cache_type extraction)
│       │   ├── engine.py       # FsspecCrawlerEngine (local & remote scanner)
│       │   ├── models.py       # FsspecUsage, CrawlReport dataclasses
│       │   ├── regex_scanner.py# Fallback regex scanner
│       │   └── repos.py        # Default target repositories configuration
│       ├── issues/             # GitHub Issues Crawler & Performance Analyzer
│       │   ├── analyzer.py     # IssuePerformanceAnalyzer (scoring & filtering)
│       │   ├── crawler.py      # GitHubIssuesCrawler (REST API pagination)
│       │   ├── keywords.py     # Filesystem & performance keyword sets
│       │   └── models.py       # GitHubIssue, IssueCrawlReport dataclasses
│       ├── analysis/           # Analytics, Matrices & Summary Tables
│       │   ├── categorization.py# 8 functional categories & pattern dictionary
│       │   ├── matrix.py       # Cross-repository occurrence matrix generator
│       │   └── summary_table.py# 4-column method summary table generator
│       ├── reporters/          # Export Formatters
│       │   ├── code_reports.py # CSV, JSON, Markdown exporters for AST crawl
│       │   └── issue_reports.py# CSV, JSON, Markdown exporters for issues crawl
│       └── simulation/         # In-Memory Simulation Suite
│           └── simulator.py    # Live in-memory filesystem validation engine
└── tests/                      # Comprehensive pytest test suite
    ├── test_ast_visitor.py
    ├── test_crawler_engine.py
    ├── test_issues_analyzer.py
    ├── test_issues_crawler.py
    ├── test_reports_and_matrix.py
    ├── test_simulation.py
    └── test_cli.py
```

---

## ⚡ Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/raj-prince/gcs-clients-optics.git
cd gcs-clients-optics

# Option A: Install globally to ~/.local/bin via uv tool (available everywhere):
uv tool install --editable .

# Option B: Install inside a virtual environment:
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"

# Option C: Using standard pip:
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

---

## 🚀 CLI Usage (`gcs-optics`)

The package provides a unified CLI `gcs-optics` (or `python -m gcs_clients_optics`):

### 1. AST Code Crawler (`crawl-code` / `code`)
Crawl remote GitHub repositories or local directories to detect filesystem/fsspec calls, extract `cache_type` options, and build line-level GitHub links:

```bash
# Crawl all 12 default open-source repositories
gcs-optics crawl-code --all \
  --output-csv reports/fsspec_crawl_results.csv \
  --output-json reports/combined_fsspec_report.json \
  --output-md reports/combined_fsspec_report.md

# Crawl specific repositories
gcs-optics crawl-code --repo dask/dask huggingface/datasets --output-md dask_report.md

# Scan a local repository or directory tree
gcs-optics crawl-code --local-dir /path/to/repo --output-md local_report.md
```

### 2. GitHub Issues Tracker (`crawl-issues` / `issues`)
Scan and score open GitHub issues related to filesystem performance, latency, and cloud storage bottlenecks:

```bash
# Crawl open issues across all default repositories
gcs-optics crawl-issues --all \
  --output-csv reports/all_issues.csv \
  --output-json reports/all_issues.json \
  --output-md reports/all_issues.md

# Crawl specific storage repositories
gcs-optics crawl-issues --repo fsspec/gcsfs fsspec/s3fs --output-md gcs_issues.md
```

### 3. Generate Distribution Matrix (`matrix`)
Generate a markdown cross-repository distribution matrix from crawl results:

```bash
gcs-optics matrix \
  --input-json reports/combined_fsspec_report.json \
  --output-md reports/method_distribution_matrix.md
```

### 4. Generate Method Summary Table (`summary`)
Generate a 4-column summary table categorized across 8 functional domains:

```bash
gcs-optics summary \
  --input-json reports/combined_fsspec_report.json \
  --output-md reports/all_methods_summary_table.md
```

### 5. In-Memory Simulation (`simulate`)
Execute a live in-memory simulation of all core filesystem operations:

```bash
gcs-optics simulate
```

### 6. Full Pipeline (`run-all`)
Run code crawl, issue crawl, matrix, summary tables, and simulation in one command:

```bash
gcs-optics run-all --output-dir reports
```

---

## 🐍 Python API Usage

You can also import and use `gcs_clients_optics` programmatically:

```python
from gcs_clients_optics import (
    FsspecCrawlerEngine,
    GitHubIssuesCrawler,
    generate_method_matrix,
    generate_summary_table,
    run_fsspec_simulation,
)

# 1. Scan code snippet or file
engine = FsspecCrawlerEngine()
usages = engine.scan_code("sample.py", "with fsspec.open('gs://bucket/data.parquet', 'rb', cache_type='mmap') as f: pass")
for u in usages:
    print(f"Call: {u.target_name}, cache_type: {u.cache_type}")

# 2. Crawl GitHub issues
crawler = GitHubIssuesCrawler()
report = crawler.crawl_repository_issues("fsspec/gcsfs")
print(f"Found {report.matched_issues_count} performance issues in {report.target_repo}")

# 3. Run in-memory simulation
results = run_fsspec_simulation(verbose=True)
```

---

## 🧪 Running Tests

Run the test suite with `pytest`:

```bash
pytest
```

---

## 📄 License

This project is licensed under the Apache 2.0 License.