# ⚡ Async vs Sync Filesystem Method Usage Report

> Comparative analysis of asynchronous coroutines (`await fs._cat_file()`, `open_async`, `asynchronous=True`) versus synchronous blocking calls (`fs.open()`, `fs.ls()`, `fs.exists()`) across cloud storage codebases.

## 📊 Executive Summary

- **Total Target Repositories**: 24
- **Total Files Scanned**: 9,472
- **Total Method Calls**: 33,914
- **Asynchronous Calls**: 933 (2.8%)
- **Synchronous Calls**: 32,900 (97.0%)
- **Potential Event Loop Blocking Calls**: 659

---

## 🏢 Repository Breakdown

| Repository / Target | Files Scanned | Total Calls | Async Calls | Sync Calls | Async % | Event Loop Warnings |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GitHub:pytorch/pytorch (main)` | 2,554 | 10,259 | 118 | 10,141 | **1.2%** | 0 |
| `GitHub:pandas-dev/pandas (main)` | 300 | 1,289 | 6 | 1,283 | **0.5%** | 0 |
| `GitHub:ray-project/ray (master)` | 2,018 | 7,118 | 173 | 6,914 | **2.4%** | 321 |
| `GitHub:pola-rs/polars (main)` | 212 | 300 | 9 | 291 | **3.0%** | 0 |
| `GitHub:Lightning-AI/pytorch-lightning (main)` | 457 | 996 | 18 | 978 | **1.8%** | 19 |
| `GitHub:duckdb/duckdb (main)` | 15 | 20 | 0 | 20 | **0.0%** | 0 |
| `GitHub:huggingface/datasets (main)` | 141 | 723 | 4 | 719 | **0.6%** | 1 |
| `GitHub:mlflow/mlflow (master)` | 1,300 | 5,427 | 30 | 5,366 | **0.6%** | 149 |
| `GitHub:apache/arrow (main)` | 80 | 249 | 4 | 245 | **1.6%** | 0 |
| `GitHub:iterative/dvc (main)` | 258 | 1,047 | 12 | 1,035 | **1.1%** | 0 |
| `GitHub:dask/dask (main)` | 184 | 644 | 10 | 634 | **1.6%** | 0 |
| `great-expectations/great_expectations` | 0 | 0 | 0 | 0 | **0.0%** | 0 |
| `GitHub:modin-project/modin (main)` | 283 | 996 | 11 | 985 | **1.1%** | 0 |
| `GitHub:flyteorg/flyte (main)` | 242 | 0 | 0 | 0 | **0.0%** | 0 |
| `GitHub:feast-dev/feast (master)` | 599 | 1,771 | 39 | 1,731 | **2.2%** | 38 |
| `GitHub:pydata/xarray (main)` | 123 | 470 | 30 | 440 | **6.4%** | 0 |
| `GitHub:kedro-org/kedro (main)` | 104 | 257 | 6 | 251 | **2.3%** | 1 |
| `GitHub:pytorch/torchtitan (main)` | 313 | 910 | 15 | 894 | **1.6%** | 1 |
| `GitHub:delta-io/delta-rs (main)` | 18 | 4 | 0 | 4 | **0.0%** | 0 |
| `GitHub:zarr-developers/zarr-python (main)` | 173 | 422 | 226 | 195 | **53.6%** | 25 |
| `GitHub:intake/intake (master)` | 52 | 368 | 2 | 366 | **0.5%** | 0 |
| `GitHub:fsspec/s3fs (main)` | 10 | 217 | 53 | 163 | **24.4%** | 39 |
| `GitHub:fsspec/gcsfs (main)` | 30 | 325 | 117 | 197 | **36.0%** | 49 |
| `GitHub:fsspec/adlfs (main)` | 6 | 102 | 50 | 48 | **49.0%** | 16 |

---

## 🛠️ Async Mechanisms & Patterns

| Mechanism | Description | Count |
| :--- | :--- | :--- |
| `sync_blocking` | Standard synchronous blocking call in sync function | 32,029 |
| `sync_in_async_context` | Synchronous call inside `async def` function | 952 |
| `await_expression` | Direct `await` invocation (`await fs._cat_file()`, `await f.read()`) | 414 |
| `async_coroutine_method` | Direct coroutine method reference (`_cat_file`, `_ls`, `_info`) | 335 |
| `async_bridge` | Event loop runner bridge (`fsspec.asyn.sync()`, `sync_wrapper()`) | 182 |
| `async_with` | Asynchronous context manager (`async with fsspec.open_async()`) | 2 |

---

