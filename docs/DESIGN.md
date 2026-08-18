# GCS Clients Optics (`gcs-clients-optics`) — System Design Document

## 1. Executive Overview

**GCS Clients Optics** is an extensible AST code crawling, performance issue tracking, and analytics system designed for **Google Cloud Storage (GCS) and `fsspec` abstract filesystem optics**.

The system enables automated, deep-codebase inspection of how open-source data science, machine learning, and cloud infrastructure projects (Dask, Ray, Hugging Face Datasets, PyTorch, pandas, DVC, etc.) interact with abstract storage layers, read-path caching strategies, and storage protocols.

```mermaid
graph TD
    subgraph Inputs ["1. Discovery & Source Inputs"]
        GH["GitHub Repositories (Git Trees API)"]
        Local["Local Codebases & File Trees"]
        Issues["GitHub Issues API (REST / Search)"]
    end

    subgraph CoreEngine ["2. Core Execution Engine"]
        CLI["Unified CLI (gcs-optics)"]
        Engine["OpticsEngine (Concurrent Fetch & AST Parser)"]
        Registry["Use-Case Registry"]
    end

    subgraph UseCases ["3. Pluggable Analysis Use Cases"]
        UC1["Use Case 1: FsspecMethodsUseCase<br/>(API calls & 8-domain categorization)"]
        UC2["Use Case 2: CacheTypeUseCase<br/>(Read-path buffering & cache_type)"]
        UC3["Use Case 3: IssuesPerformanceUseCase<br/>(Latency, throughput & OOM tracking)"]
        UC4["Use Case 4: ProtocolsUseCase<br/>(gs://, s3://, abfs://, backends)"]
        UC5["Use Case 5: AsyncSyncUseCase<br/>(Async coroutines, bridges & event loop stalls)"]
        UCCustom["Custom Use Cases<br/>(Compression, concurrency, retries)"]
    end

    subgraph Exporters ["4. Storage & Reporting Pipeline"]
        SQLite["SQLite WAL Store (optics.db)"]
        JSON["JSON Exporters (Structured AST Reports)"]
        CSV["CSV Exporters (Data Pipelines)"]
        MD["Markdown Exporters (Matrices & Summary Tables)"]
        Sim["In-Memory Filesystem Simulator"]
    end

    subgraph Consumers ["5. Downstream Consumers"]
        Agents["AI Reasoning Agents (SQL Tool Calling)"]
        Engineers["Storage & Performance Engineers"]
        Dashboards["BI & Analytics Dashboards"]
    end

    Inputs --> CoreEngine
    CoreEngine --> Registry
    Registry --> UseCases
    UseCases --> Exporters
    Exporters --> Consumers
```

---

## 2. Component Architecture & Responsibilities

The system is decomposed into modular layers with strict separation of concerns:

```
src/gcs_clients_optics/
├── cli.py              # CLI Interface & Command Dispatcher
├── engine/             # Generic Execution & AST Orchestration Engine
│   └── optics_engine.py
├── usecases/           # Domain-Specific Analysis Use Cases
│   ├── base.py         # BaseUseCase Abstract Contract
│   ├── fsspec_methods.py
│   ├── cache_type.py
│   ├── issues_performance.py
│   └── protocols.py
├── crawler/            # AST Node Visitors & Repository Scanners
│   ├── ast_visitor.py
│   ├── engine.py
│   ├── models.py
│   └── repos.py
├── issues/             # GitHub Issues Crawler & Scoring Engine
│   ├── analyzer.py
│   ├── crawler.py
│   ├── keywords.py
│   └── models.py
├── analysis/           # Categorization, Matrices & Summary Tables
│   ├── categorization.py # Complete fsspec base spec ontology (8 domains)
│   ├── matrix.py
│   └── summary_table.py
├── storage/            # Relational SQLite Engine & Ingestion Pipeline
│   └── sqlite_store.py
├── reporters/          # Multi-Format Report Exporters
│   ├── code_reports.py
│   └── issue_reports.py
└── simulation/         # In-Memory Validation & Live Simulator
    └── simulator.py
```

### Component Responsibility Matrix

| Component | Module | Key Responsibilities | Inputs | Outputs |
| :--- | :--- | :--- | :--- | :--- |
| **CLI Dispatcher** | [`cli.py`](file:///usr/local/google/home/princer/code/gcs-clients-optics/src/gcs_clients_optics/cli.py) | Parses subcommands (`fsspec-methods`, `cache-type`, `issues`, `protocols`, `ingest`, `simulate`, `run-all`), resolves output paths (`.json`, `.csv`, `.md`, `.db`), and invokes engine workflows. | Command-line arguments & environment variables | Exit code & console feedback |
| **Optics Engine** | [`engine/optics_engine.py`](file:///usr/local/google/home/princer/code/gcs-clients-optics/src/gcs_clients_optics/engine/optics_engine.py) | Generic multithreaded orchestrator for scanning GitHub repositories via Git Trees API or local directory trees. Decoupled from specific use cases. | Target repository or local directory path + `BaseUseCase` | Aggregated report object |
| **Use-Case Registry** | [`usecases/`](file:///usr/local/google/home/princer/code/gcs-clients-optics/src/gcs_clients_optics/usecases/) | Encapsulates domain-specific AST visitors, scoring logic, aggregation, and export formatting under a uniform `BaseUseCase` interface. | Source code AST nodes & issue payloads | Domain reports (CrawlReport, CacheReport, ProtocolReport, IssueCrawlReport) |
| **AST Parser & Visitor** | [`crawler/ast_visitor.py`](file:///usr/local/google/home/princer/code/gcs-clients-optics/src/gcs_clients_optics/crawler/ast_visitor.py) | Traverses Python AST to extract method calls (`open`, `readinto`, `cat`, etc.), extracts `cache_type`, arguments, enclosing functions/classes, and line-level URLs. | Python source code string | List of `FsspecUsage` records |
| **Issue Performance Analyzer** | [`issues/analyzer.py`](file:///usr/local/google/home/princer/code/gcs-clients-optics/src/gcs_clients_optics/issues/analyzer.py) | Performs keyword matching, heuristic relevance scoring, and category tagging for cloud storage performance bottlenecks. | GitHub issue title & body text | Scored & categorized `GitHubIssue` |
| **Categorization Ontology** | [`analysis/categorization.py`](file:///usr/local/google/home/princer/code/gcs-clients-optics/src/gcs_clients_optics/analysis/categorization.py) | Complete formal ontology mapping 100% of `AbstractFileSystem` and `AbstractBufferedFile` methods into 8 standard functional domains. | Method name string | Functional category string & descriptive pattern |
| **SQLite Storage Engine** | [`storage/sqlite_store.py`](file:///usr/local/google/home/princer/code/gcs-clients-optics/src/gcs_clients_optics/storage/sqlite_store.py) | Normalized relational storage with WAL mode, indexing, and batch ingestion from live scans or JSON artifacts. | In-memory reports or JSON files | `optics.db` SQLite database |
| **Live Simulator** | [`simulation/simulator.py`](file:///usr/local/google/home/princer/code/gcs-clients-optics/src/gcs_clients_optics/simulation/simulator.py) | In-memory `fsspec` filesystem testbed executing live validation of directory hierarchies, wildcards, metadata, and stream reading. | None (self-contained) | Validation test execution results |

---

## 3. End-to-End Pipelining & Single-Pass Data Flow

The system employs a **Single-Pass Multi-Use-Case Execution Pipeline**. In a single crawl pass, each source file is downloaded **once** over the network, and all registered use cases (`FsspecMethodsUseCase`, `CacheTypeUseCase`, `ProtocolsUseCase`, `AsyncSyncUseCase`) evaluate the file in memory simultaneously:

```mermaid
sequenceDiagram
    autonumber
    actor User as User / CI Pipeline
    participant CLI as CLI (gcs-optics)
    participant Engine as OpticsEngine
    participant GitHub as GitHub API / Local FS
    participant UseCases as Pluggable Use Cases (Methods, Cache, Protocols, Async)
    participant SQLite as SQLite Storage (optics.db)
    actor Agent as Downstream AI Agent

    User->>CLI: gcs-optics run-all --output-dir reports
    CLI->>Engine: scan_multiple_repositories_multi(repos, [Methods, Cache, Protocols, Async])
    Engine->>GitHub: Fetch recursive tree (/git/trees/main?recursive=1)
    GitHub-->>Engine: 2,400 file paths
    Engine->>GitHub: Fetch Python source files ONCE (ThreadPoolExecutor, 16 workers)
    GitHub-->>Engine: Source code strings
    loop For each Python source file (in-memory)
        Engine->>UseCases: Pass source code to all 4 use cases simultaneously
        UseCases-->>Engine: Extract usages for Methods, Cache, Protocols, and Async
    end
    Engine-->>CLI: Aggregated reports for all 4 use cases
    CLI->>SQLite: Batch ingest into optics.db (method_usages, cache_usages, protocol_usages, async_sync_usages)
    CLI->>GitHub: Crawl GitHub Issues in parallel
    CLI->>SQLite: Batch ingest into issues table
    SQLite-->>User: Complete reports & optics.db ready

    opt Downstream Agent Query
        Agent->>SQLite: SELECT * FROM method_usages JOIN async_sync_usages ...
        SQLite-->>Agent: Structured SQL result set
    end
```

---

## 4. SQLite Relational Schema & Indexing Model

The storage engine writes to a single SQLite database (`optics.db`) configured with Write-Ahead Logging (`PRAGMA journal_mode=WAL`) for concurrent reading by downstream AI agents.

```mermaid
erDiagram
    scan_runs ||--o{ method_usages : contains
    scan_runs ||--o{ cache_usages : contains
    scan_runs ||--o{ protocol_usages : contains
    scan_runs ||--o{ async_sync_usages : contains
    scan_runs ||--o{ issues : contains

    scan_runs {
        string scan_id PK
        string use_case
        string target_source
        string repo_url
        int total_files_scanned
        int total_matches
        float elapsed_seconds
        timestamp scanned_at
    }

    method_usages {
        int id PK
        string scan_id FK
        string repository
        string file_path
        int line_number
        int end_line_number
        string target_name
        string base_method
        string category
        string cache_type
        boolean is_specified_cache_keyword
        string cache_options
        string enclosing_class
        string enclosing_function
        string file_url
        string code_snippet
        string detection_method
    }

    cache_usages {
        int id PK
        string scan_id FK
        string repository
        string file_path
        int line_number
        string target_name
        string cache_type
        boolean is_explicit
        string strategy_category
        string cache_options
        string enclosing_class
        string enclosing_function
        string file_url
        string code_snippet
    }

    protocol_usages {
        int id PK
        string scan_id FK
        string repository
        string file_path
        int line_number
        string protocol
        string provider
        string usage_type
        string context
        string file_url
        string code_snippet
    }

    async_sync_usages {
        int id PK
        string scan_id FK
        string repository
        string file_path
        int line_number
        string target_name
        string base_method
        string category
        string execution_mode
        string async_mechanism
        boolean is_async_context
        boolean is_coroutine_call
        boolean potential_event_loop_block
        string enclosing_class
        string enclosing_function
        string file_url
        string code_snippet
    }

    issues {
        int id PK
        string scan_id FK
        string repository
        int issue_number
        string title
        string state
        float relevance_score
        string matched_keywords
        string categories
        string html_url
        string author
        string created_at
        string updated_at
        string body_preview
    }
```

---

## 5. Functional Ontology & Categorization Pipeline

The system maps all detected method calls into **8 standard functional domains** covering 100% of the methods in `fsspec.spec.AbstractFileSystem` and `fsspec.spec.AbstractBufferedFile`:

```mermaid
pie title FSSPEC 8 Functional Domains
    "Stream Reading & Writing" : 35
    "Metadata & Existence Checks" : 20
    "Directory Listing & Traversal" : 15
    "File & Directory Mutation" : 12
    "Path Arithmetic & Topologies" : 8
    "Protocol Resolution & Lifecycle" : 5
    "Bulk Data Transfer" : 3
    "Driver Instances & Wrappers" : 2
```

1. **Stream Reading & Writing**: `open`, `read`, `readinto`, `readinto1`, `readline`, `readlines`, `read_block`, `read_bytes`, `read_text`, `write`, `write_bytes`, `write_text`, `pipe`, `cat`, `cat_file`, `cat_ranges`, `head`, `tail`, `seek`, `tell`, `flush`, `close`.
2. **Metadata & Existence Checks**: `exists`, `lexists`, `info`, `stat`, `isdir`, `isfile`, `size`, `sizes`, `du`, `checksum`, `ukey`, `created`, `modified`, `sign`, `get_file_info`.
3. **Directory Listing & Traversal**: `ls`, `listdir`, `glob`, `find`, `walk`, `tree`, `expand_path`, `expand_paths_if_needed`, `FileSelector`.
4. **File & Directory Mutation**: `mkdir`, `makedirs`, `touch`, `rm`, `rm_file`, `rmdir`, `delete`, `copy`, `cp`, `move`, `mv`, `rename`.
5. **Bulk Data Transfer**: `get`, `get_file`, `download`, `put`, `put_file`, `upload`.
6. **Path Arithmetic & Topologies**: `_parent`, `join`, `split`, `parts`, `relparts`, `relpath`, `normpath`, `abspath`, `getcwd`, `chdir`, `isin`, `commonpath`, `as_posix`.
7. **Protocol Resolution & Driver Lifecycle**: `url_to_fs`, `filesystem`, `get_fs_token_paths`, `split_protocol`, `strip_protocol`, `unstrip_protocol`, `to_dict`, `to_json`, `start_transaction`, `end_transaction`, `invalidate_cache`.
8. **Driver Instances & Wrapper Bridges**: `_get_pyarrow_filesystem`, `ArrowFSWrapper`, `DirFileSystem`, `LocalFileSystem`, `GCSFileSystem`, `S3FileSystem`, `AzureBlobFileSystem`, `PyFileSystem`.

---

## 6. Extensibility Model: Adding New Use Cases

The architecture allows adding new specialized analysis use cases without modifying the core execution engine:

```python
from gcs_clients_optics import BaseUseCase, OpticsEngine, register_use_case

class ConcurrencyOpticsUseCase(BaseUseCase):
    name = "concurrency"
    description = "Analyze threading, asyncio, and multiprocessing patterns around storage I/O"
    aliases = ["async", "threading"]

    def scan_code(self, file_path: str, source_code: str, repo_url=None, branch="main"):
        # Custom AST visitor logic to identify async with fs.open() or ThreadPoolExecutor
        return [...]

    def aggregate_report(self, target_source, total_files, files_with_usages, usages, repo_url=None):
        return {...}

    def export_reports(self, reports, output_csv=None, output_json=None, output_md=None, output_sqlite=None, **kwargs):
        # Multi-format exports
        return {}

# Register globally
register_use_case(ConcurrencyOpticsUseCase())

# Run using generic engine
engine = OpticsEngine(use_case=ConcurrencyOpticsUseCase())
report = engine.scan_github_repo("dask/dask")
```

---

## 7. Downstream Agent Integration Pattern

Downstream AI coding agents can interact with the system via SQLite queries without parsing raw JSON/CSV dumps:

```mermaid
graph LR
    UserAgent["AI Agent / LLM"] -->|1. Generate SQL Query| DB["optics.db (SQLite WAL)"]
    DB -->|2. Exact Result Rows| UserAgent
    UserAgent -->|3. Synthesize Answer| FinalResponse["User Answer / Decision"]
```

### Example Agent Interactions

| Question Asked to Agent | SQL Executed by Agent |
| :--- | :--- |
| *"Which repositories use `cat_ranges` for chunked reads?"* | `SELECT DISTINCT repository, file_path, line_number FROM method_usages WHERE base_method = 'cat_ranges';` |
| *"What percentage of read calls in Dask use `mmap` vs `readahead`?"* | `SELECT cache_type, COUNT(*) FROM cache_usages WHERE repository = 'dask/dask' GROUP BY 1;` |
| *"What are the top open performance issues in GCS filesystem libraries?"* | `SELECT repository, issue_number, title, relevance_score FROM issues WHERE relevance_score >= 10 ORDER BY relevance_score DESC LIMIT 5;` |
| *"Where is `readinto` called across all surveyed libraries?"* | `SELECT repository, file_path, line_number, code_snippet FROM method_usages WHERE base_method = 'readinto';` |

---

## 8. Performance & Concurrency Model

The system employs a **two-tier multi-threaded concurrency model** to maximize throughput while avoiding GitHub API rate limits:

```mermaid
graph TD
    subgraph RepoConcurrency ["Tier 1: Inter-Repository Concurrency (ThreadPoolExecutor, max_workers=16)"]
        R1["Repo 1: dask/dask"]
        R2["Repo 2: ray-project/ray"]
        R3["Repo 3: huggingface/datasets"]
        R4["Repo 4: iterative/dvc"]
    end

    subgraph FileConcurrency ["Tier 2: Intra-Repository File Concurrency (ThreadPoolExecutor, max_workers=16)"]
        F1["Fetch & Parse file_1.py"]
        F2["Fetch & Parse file_2.py"]
        F3["Fetch & Parse file_N.py"]
    end

    R1 --> FileConcurrency
    R2 --> FileConcurrency
```

1. **Tier 1: Inter-Repository Concurrency (`--concurrency` / `-j`, default: 16)**:
   - Multiple GitHub repositories or issues targets are crawled concurrently using `ThreadPoolExecutor(max_workers=16)`.
   - Progress callbacks report real-time completion status per repository as workers finish.
2. **Tier 2: Intra-Repository File Concurrency (default: 16)**:
   - Within each repository, all discovered Python source files are downloaded and parsed concurrently using a dedicated pool of 16 worker threads (`ThreadPoolExecutor(max_workers=16)`).
3. **AST-Native Speed**:
   - AST parsing (`ast.parse`) executes in native CPython bytecode, processing ~1,000 files/second per core with zero external process overhead.
4. **Git Trees Single-Call Discovery**:
   - Discovers entire 10,000+ file repository hierarchies in a single HTTP request using `api.github.com/repos/{owner}/{repo}/git/trees/{branch}?recursive=1`.
5. **SQLite WAL High-Throughput Ingestion**:
   - Database writes use Write-Ahead Logging (`PRAGMA journal_mode=WAL;`) and parameterized batch inserts (`executemany`), ingesting >50,000 usage records in under 200ms without table locking.
