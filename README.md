# GCS Clients Optics (`gcs-clients-optics`)

A high-performance AST crawler and analysis engine for **Google Cloud Storage (GCS) and `fsspec` abstract filesystem optics**.

`gcs-clients-optics` analyzes upstream Python codebases across open-source ecosystems (PyTorch, Hugging Face Datasets, Dask, Ray, Pandas, DVC, etc.) using AST-based inspection to uncover how projects interact with storage layers, read streams, and abstract filesystems.

---

## ⚡ Quick Start & Installation

```bash
git clone https://github.com/raj-prince/gcs-clients-optics.git
cd gcs-clients-optics

# Virtual environment setup
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

---

## 🚀 CLI Commands & Usage

The CLI (`gcs-optics`) provides two streamlined commands: `scan` (default) and `dependents`.

### 1. Scan Repositories (`scan` or default)

Scan any GitHub repository or local directory for `fsspec` and filesystem method usages:

```bash
# Scan a single GitHub repository (exports Markdown report by default)
gcs-optics --repo pytorch/pytorch -o reports/pytorch_methods.md

# Scan multiple repositories
gcs-optics --repo pytorch/pytorch huggingface/datasets dask/dask

# Scan all curated ecosystem dependents
gcs-optics --all

# Scan dependents loaded from a JSON file
gcs-optics -D data/default_dependents.json --min-stars 5000

# Scope scan to a specific subpath in repository
gcs-optics --repo ray-project/ray -p python/ray/data -o reports/ray_data.md

# Adjust concurrency and worker threads
gcs-optics --all --concurrency 16 --file-workers 32
```

---

### 2. Discover Dependents (`dependents`)

Discover downstream GitHub repositories that depend on `fsspec` or `gcsfs`:

```bash
# Discover top dependents and save to JSON
gcs-optics dependents --repo fsspec/filesystem_spec --min-stars 100 --limit 50 -o data/dependents.json

# Discover gcsfs dependents
gcs-optics dependents --repo fsspec/gcsfs --min-stars 50 -o data/gcsfs_dependents.json
```

---

## 📊 Method Taxonomy & Canonicalization

`gcs-clients-optics` standardizes all call sites into an intuitive, clean 3-tier taxonomy:

| Layer Prefix | Type | Description | Examples |
| :--- | :--- | :--- | :--- |
| **`fs.*`** | **Filesystem Operations** | All abstract filesystem driver methods (whether called via `fs.open()`, `self.fs.makedirs()`, `dirfs.glob()`, or `fsspec.open()`). | `fs.open`, `fs.exists`, `fs.isfile`, `fs.glob`, `fs.makedirs`, `fs.ls`, `fs.cat_file`, `fs.info` |
| **`f.*`** | **Stream Buffer Operations** | Methods executed on an open file handle / stream buffer. | `f.read`, `f.write`, `f.close`, `f.flush`, `f.seek`, `f.tell`, `f.readline` |
| **Direct Helpers** | **Module Utilities** | Standalone URL resolvers and driver factory functions. | `url_to_fs`, `get_fs_token_paths`, `fsspec.filesystem` |

---

## 📋 8-Domain Functional Ontology

All detected methods are categorized into 8 standard functional domains:

1. **Stream Reading & Writing**: `fs.open`, `f.read`, `f.write`, `f.close`, `f.flush`, `f.seek`, `f.tell`, `fs.read_text`
2. **Metadata & Existence Checks**: `fs.exists`, `fs.isfile`, `fs.isdir`, `fs.info`, `fs.size`, `fs.checksum`, `fs.ukey`
3. **Directory Listing & Traversal**: `fs.ls`, `fs.listdir`, `fs.glob`, `fs.find`, `fs.walk`, `fs.tree`
4. **File & Directory Mutation**: `fs.makedirs`, `fs.mkdir`, `fs.rm`, `fs.rm_file`, `fs.mv`, `fs.rename`, `fs.touch`
5. **Bulk Data Transfer**: `fs.get`, `fs.get_file`, `fs.put`, `fs.put_file`, `fs.copy`
6. **Path Arithmetic & Topologies**: `fs.split`, `fs.join`, `fs.relpath`, `fs.normpath`, `fs.abspath`, `stringify_path`
7. **Protocol Resolution & Driver Lifecycle**: `url_to_fs`, `get_fs_token_paths`, `fsspec.filesystem`, `infer_compression`
8. **Driver Instances & Wrapper Bridges**: Transaction wrappers, caching bridges, and filesystem wrappers.

---

## 🛠️ CLI Options Reference

| Option | Flag | Description | Default |
| :--- | :--- | :--- | :--- |
| `--repo` | `-r` | GitHub repository (`owner/repo`) or list of repositories | None |
| `--all` | `-a` | Scan all default ecosystem dependents | `False` |
| `--dependents-file` | `-D` | Load target repositories from dependents JSON / text file | None |
| `--output` / `--output-md` | `-o` | Markdown report destination path | `reports/<basename>.md` |
| `--subpath` | `-p` | Scope scan to subdirectory within the repository | None |
| `--branch` | `-b` | Git branch to scan | `main` |
| `--concurrency` | `-j` | Concurrent repositories to scan in parallel | `16` |
| `--file-workers` | `-w` | Concurrent file downloading & AST parsing worker threads | `32` |
| `--min-stars` | `-s` | Minimum GitHub stars filter for dependents | `0` |
| `--limit` | `-n` | Maximum number of repositories to scan from dependents list | None |

---

## 🧩 Pluggable Use Case Architecture

The engine uses a pluggable architecture. Additional analyzers can be created by subclassing `BaseUseCase`:

```python
from gcs_clients_optics import BaseUseCase, OpticsEngine, register_use_case

class CompressionUseCase(BaseUseCase):
    name = "compression-optics"
    description = "Analyzes compression codec usage in storage pipelines"

    def scan_code(self, file_path, source_code, repo_url=None, branch="main"):
        # AST or regex inspection logic
        return [...]

    def aggregate_report(self, target_source, total_files_scanned, files_with_usages, usages, repo_url=None):
        return {...}

# Register use case
register_use_case(CompressionUseCase())

# Run with generic engine
engine = OpticsEngine(use_case=CompressionUseCase())
reports = engine.scan_github_repo("dask/dask")
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📄 License

Apache 2.0
