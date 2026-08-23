# GCS Clients Optics (`gcs-clients-optics`)

A simple, extensible CLI and analysis engine for **Google Cloud Storage (GCS) clients**.

`gcs-clients-optics` supports [fsspec](https://github.com/fsspec/)/[gcsfs](https://github.com/fsspec/gcsfs) which is pythonic filesystem client. It scans the client's upstream python codebases (via AST) and GitHub issues across open-source ecosystems (Dask, Ray, Hugging Face Datasets, PyTorch, etc.) using a **generic engine with pluggable use cases**.

📖 **[System Design Document](docs/DESIGN.md)**: High-level component diagrams, responsibilities, pipelining, and SQLite schema.

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

# Output as Markdown
gcs-optics fsspec-methods --all --format md -o reports/combined_fsspec_report.md

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

# Output as Markdown
gcs-optics cache-type --all --format md -o reports/cache_analysis.md
```

---

### 3. Storage Protocols & Cloud Backends (`protocols` / `storage`)
Analyzes cloud protocol URIs (`gs://`, `s3://`, `abfs://`, `hdfs://`, `memory://`, `file://`) and backend driver instantiations (`gcsfs`, `s3fs`, etc.):

```bash
# Output as JSON
gcs-optics protocols --all --format json -o reports/protocols.json

# Output as CSV
gcs-optics protocols --all --format csv -o reports/protocols.csv

# Output as Markdown
gcs-optics protocols --all --format md -o reports/protocols.md
```

---

### 4. Async vs Sync Filesystem Method Usage (`async-sync` / `async`)
Analyzes asynchronous coroutines (`await fs._cat_file()`, `open_async`, `asynchronous=True`, `fsspec.asyn.sync()`) versus synchronous blocking calls (`fs.open()`, `fs.ls()`, `fs.exists()`, `f.readinto()`), and detects potential event loop blocking anti-patterns:

```bash
# Output as JSON
gcs-optics async-sync --all --format json -o reports/async_sync.json

# Output as CSV
gcs-optics async-sync --all --format csv -o reports/async_sync.csv

# Output as Markdown
gcs-optics async-sync --all --format md -o reports/async_sync.md
```

### 5. Targeting Downstream Dependents (`github-dependents-info` & `discover-dependents`)

You can scan the hundreds of downstream projects that depend on `fsspec` or `gcsfs`:

#### Option A: Ingest `github-dependents-info` JSON:
```bash
# 1. Collect dependents of fsspec or gcsfs
github-dependents-info --repo fsspec/filesystem_spec --minstars 100 --json > dependents.json
github-dependents-info --repo fsspec/gcsfs --minstars 50 --json > gcsfs_dependents.json

# 2. Run single-pass scan across all discovered dependents:
gcs-optics run-all --dependents-file dependents.json --min-stars 100 --output-dir reports/

# 3. Or run specific use case on dependents:
gcs-optics fsspec-methods -D dependents.json --min-stars 100 --format all -o reports/
gcs-optics async-sync -D gcsfs_dependents.json --format md -o reports/gcsfs_dependents_async.md
```

#### Option B: Built-in Dependents Discovery:
```bash
# Discover top dependents and save to file:
gcs-optics discover-dependents --repo fsspec/filesystem_spec --min-stars 100 --limit 50 -o dependents.json

# Or scan discovered dependents directly on the fly:
gcs-optics fsspec-methods --dependents-of fsspec/filesystem_spec --limit 30 --format md -o reports/fsspec_deps.md
```

---

### 6. Full Pipeline (`run-all`)
Runs all use cases and exports reports to a directory:

```bash
gcs-optics run-all --output-dir reports
```

---

## 💾 Output Formats: JSON, CSV, Markdown

You can specify the output format using `--format` (`-t`) and the output path with `--output` (`-o`):

| Flag / Option | Description | Example |
| :--- | :--- | :--- |
| `--format json` | Output report in JSON format | `gcs-optics fsspec-methods --all --format json -o output.json` |
| `--format csv` | Output report in CSV format | `gcs-optics cache-type --all --format csv -o output.csv` |
| `--format md` | Output report in Markdown format | `gcs-optics cache-type --all --format md -o output.md` |
| `--format all` | Output all formats (JSON, CSV, MD) | `gcs-optics fsspec-methods --all --format all -o reports/` |
| `--dependents-file <file>` / `-D` | Load target repositories from dependents JSON / text file | `gcs-optics fsspec-methods -D dependents.json --min-stars 100` |
| `--dependents-of <owner/repo>` | Discover & scan downstream dependents from GitHub | `gcs-optics fsspec-methods --dependents-of fsspec/filesystem_spec` |
| `--min-stars <N>` | Filter repositories by minimum GitHub stars | `gcs-optics run-all -D dependents.json --min-stars 100` |
| `--limit <N>` / `-n` | Limit number of repositories to scan from dependents | `gcs-optics fsspec-methods -D dependents.json -n 50` |
| `--subpath <path>` / `-p` | Scope scan to a specific subdirectory in repo | `gcs-optics fsspec-methods --repo ray-project/ray -p python/ray/data` |
| `--file-workers <N>` / `-w` | File download/parsing worker threads (default: 32) | `gcs-optics fsspec-methods --repo ray-project/ray -w 32` |
| `--concurrency <N>` / `-j` | Concurrent repositories to crawl (default: 16) | `gcs-optics fsspec-methods --all -j 16` |
| `-o <path>` / `--output <path>` | Destination file (`.json`, `.csv`, `.md`) or directory | `-o my_report.json` or `-o reports/` |

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

    def export_reports(self, reports, output_csv=None, output_json=None, output_md=None, **kwargs):
        # Export JSON/CSV/MD
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
