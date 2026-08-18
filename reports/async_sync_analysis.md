# ⚡ Async vs Sync Filesystem Method Usage Report

> Comparative analysis of asynchronous coroutines (`await fs._cat_file()`, `open_async`, `asynchronous=True`) versus synchronous blocking calls (`fs.open()`, `fs.ls()`, `fs.exists()`) across cloud storage codebases.

## 📊 Executive Summary

- **Total Target Repositories**: 13
- **Total Files Scanned**: 9,944
- **Total Method Calls**: 31,707
- **Asynchronous Calls**: 939 (3.0%)
- **Synchronous Calls**: 30,695 (96.8%)
- **Potential Event Loop Blocking Calls**: 440

---

## 🏢 Repository Breakdown

| Repository / Target | Files Scanned | Total Calls | Async Calls | Sync Calls | Async % | Event Loop Warnings |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GitHub:dask/dask (main)` | 201 | 667 | 10 | 657 | **1.5%** | 0 |
| `GitHub:intake/intake (master)` | 71 | 375 | 2 | 371 | **0.5%** | 0 |
| `GitHub:pandas-dev/pandas (main)` | 544 | 1,603 | 6 | 1,597 | **0.4%** | 0 |
| `GitHub:pydata/xarray (main)` | 164 | 504 | 29 | 475 | **5.8%** | 0 |
| `GitHub:zarr-developers/zarr-python (main)` | 264 | 510 | 278 | 231 | **54.5%** | 25 |
| `GitHub:iterative/dvc (main)` | 326 | 1,255 | 12 | 1,243 | **1.0%** | 0 |
| `GitHub:kedro-org/kedro (main)` | 152 | 288 | 6 | 282 | **2.1%** | 1 |
| `GitHub:huggingface/datasets (main)` | 162 | 837 | 6 | 831 | **0.7%** | 1 |
| `GitHub:pytorch/pytorch (main)` | 3,445 | 12,575 | 322 | 12,252 | **2.6%** | 7 |
| `GitHub:Lightning-AI/pytorch-lightning (main)` | 767 | 1,199 | 18 | 1,181 | **1.5%** | 20 |
| `GitHub:pytorch/torchtitan (main)` | 364 | 999 | 15 | 983 | **1.5%** | 5 |
| `GitHub:ray-project/ray (master)` | 3,342 | 10,431 | 231 | 10,132 | **2.2%** | 381 |
| `GitHub:apache/arrow (main)` | 142 | 464 | 4 | 460 | **0.9%** | 0 |

---

## 🛠️ Async Mechanisms & Patterns

| Mechanism | Description | Count |
| :--- | :--- | :--- |
| `sync_blocking` | Standard synchronous blocking call in sync function | 30,043 |
| `sync_in_async_context` | Synchronous call inside `async def` function | 725 |
| `async_coroutine_method` | Direct coroutine method reference (`_cat_file`, `_ls`, `_info`) | 471 |
| `await_expression` | Direct `await` invocation (`await fs._cat_file()`, `await f.read()`) | 340 |
| `async_bridge` | Event loop runner bridge (`fsspec.asyn.sync()`, `sync_wrapper()`) | 128 |

---

