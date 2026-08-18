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

# Scan a single local file
gcs-optics cache-type --local-file src/data_reader.py --format json -o reader_cache.json
```

---

### 3. GitHub Issues Performance Tracker (`issues` / `crawl-issues`)
Crawls and scores open GitHub issues for storage performance bottlenecks (latency, throughput, OOM, prefetching, chunk size):

```bash
# Output as JSON
gcs-optics issues --repo fsspec/gcsfs fsspec/s3fs --format json -o storage_issues.json

# Output as CSV
gcs-optics issues --all --format csv -o reports/all_issues.csv
```

---

### 4. Storage Protocols & Cloud Backends (`protocols` / `storage`)
Analyzes cloud protocol URIs (`gs://`, `s3://`, `abfs://`, `hdfs://`, `memory://`, `file://`) and backend driver instantiations (`gcsfs`, `s3fs`, etc.):

```bash
# Output as JSON
gcs-optics protocols --all --format json -o reports/protocols.json

# Output as CSV
gcs-optics protocols --all --format csv -o reports/protocols.csv
```

---

### 5. In-Memory Filesystem Simulation (`simulate`)
Runs a live in-memory verification of directory traversal, wildcards, metadata, and stream reading:

```bash
gcs-optics simulate
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
| `-o <path>` / `--output <path>` | Destination file or directory | `-o my_report.json` or `-o reports/` |

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