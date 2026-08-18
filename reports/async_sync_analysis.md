# ⚡ Async vs Sync Filesystem Method Usage Report

> Comparative analysis of asynchronous coroutines (`await fs._cat_file()`, `open_async`, `asynchronous=True`) versus synchronous blocking calls (`fs.open()`, `fs.ls()`, `fs.exists()`) across cloud storage codebases.

## 📊 Executive Summary

- **Total Target Repositories**: 24
- **Total Files Scanned**: 9,357
- **Total Method Calls**: 33,827
- **Asynchronous Calls**: 933 (2.8%)
- **Synchronous Calls**: 32,813 (97.0%)
- **Potential Event Loop Blocking Calls**: 659

---

## 🏢 Repository Breakdown

| Repository / Target | Files Scanned | Total Calls | Async Calls | Sync Calls | Async % | Event Loop Warnings |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GitHub:pytorch/pytorch (main)` | 2,546 | 10,258 | 118 | 10,140 | **1.2%** | 0 |
| `GitHub:pandas-dev/pandas (main)` | 297 | 1,289 | 6 | 1,283 | **0.5%** | 0 |
| `GitHub:ray-project/ray (master)` | 2,003 | 7,084 | 173 | 6,880 | **2.4%** | 321 |
| `GitHub:pola-rs/polars (main)` | 204 | 300 | 9 | 291 | **3.0%** | 0 |
| `GitHub:Lightning-AI/pytorch-lightning (main)` | 446 | 981 | 18 | 963 | **1.8%** | 19 |
| `GitHub:duckdb/duckdb (main)` | 14 | 20 | 0 | 20 | **0.0%** | 0 |
| `GitHub:huggingface/datasets (main)` | 139 | 721 | 4 | 717 | **0.6%** | 1 |
| `GitHub:mlflow/mlflow (master)` | 1,291 | 5,427 | 30 | 5,366 | **0.6%** | 149 |
| `GitHub:apache/arrow (main)` | 70 | 249 | 4 | 245 | **1.6%** | 0 |
| `GitHub:iterative/dvc (main)` | 257 | 1,047 | 12 | 1,035 | **1.1%** | 0 |
| `GitHub:dask/dask (main)` | 182 | 644 | 10 | 634 | **1.6%** | 0 |
| `great-expectations/great_expectations` | 0 | 0 | 0 | 0 | **0.0%** | 0 |
| `GitHub:modin-project/modin (main)` | 278 | 994 | 11 | 983 | **1.1%** | 0 |
| `GitHub:flyteorg/flyte (main)` | 236 | 0 | 0 | 0 | **0.0%** | 0 |
| `GitHub:feast-dev/feast (master)` | 593 | 1,740 | 39 | 1,700 | **2.2%** | 38 |
| `GitHub:pydata/xarray (main)` | 121 | 470 | 30 | 440 | **6.4%** | 0 |
| `GitHub:kedro-org/kedro (main)` | 98 | 257 | 6 | 251 | **2.3%** | 1 |
| `GitHub:pytorch/torchtitan (main)` | 308 | 910 | 15 | 894 | **1.6%** | 1 |
| `GitHub:delta-io/delta-rs (main)` | 17 | 4 | 0 | 4 | **0.0%** | 0 |
| `GitHub:zarr-developers/zarr-python (main)` | 169 | 422 | 226 | 195 | **53.6%** | 25 |
| `GitHub:intake/intake (master)` | 51 | 368 | 2 | 366 | **0.5%** | 0 |
| `GitHub:fsspec/s3fs (main)` | 7 | 215 | 53 | 161 | **24.7%** | 39 |
| `GitHub:fsspec/gcsfs (main)` | 27 | 325 | 117 | 197 | **36.0%** | 49 |
| `GitHub:fsspec/adlfs (main)` | 3 | 102 | 50 | 48 | **49.0%** | 16 |

---

## 🛠️ Async Mechanisms & Patterns

| Mechanism | Description | Count |
| :--- | :--- | :--- |
| `sync_blocking` | Standard synchronous blocking call in sync function | 31,942 |
| `sync_in_async_context` | Synchronous call inside `async def` function | 952 |
| `await_expression` | Direct `await` invocation (`await fs._cat_file()`, `await f.read()`) | 414 |
| `async_coroutine_method` | Direct coroutine method reference (`_cat_file`, `_ls`, `_info`) | 335 |
| `async_bridge` | Event loop runner bridge (`fsspec.asyn.sync()`, `sync_wrapper()`) | 182 |
| `async_with` | Asynchronous context manager (`async with fsspec.open_async()`) | 2 |

---

