# ⚡ Async vs Sync Filesystem Method Usage Report

> Comparative analysis of asynchronous coroutines (`await fs._cat_file()`, `open_async`, `asynchronous=True`) versus synchronous blocking calls (`fs.open()`, `fs.ls()`, `fs.exists()`) across cloud storage codebases.

## 📊 Executive Summary

- **Total Target Repositories**: 1
- **Total Files Scanned**: 201
- **Total Method Calls**: 669
- **Asynchronous Calls**: 10 (1.5%)
- **Synchronous Calls**: 659 (98.5%)
- **Potential Event Loop Blocking Calls**: 0

---

## 🏢 Repository Breakdown

| Repository / Target | Files Scanned | Total Calls | Async Calls | Sync Calls | Async % | Event Loop Warnings |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `GitHub:dask/dask (main)` | 201 | 669 | 10 | 659 | **1.5%** | 0 |

---

## 🛠️ Async Mechanisms & Patterns

| Mechanism | Description | Count |
| :--- | :--- | :--- |
| `sync_blocking` | Standard synchronous blocking call in sync function | 659 |
| `async_coroutine_method` | Direct coroutine method reference (`_cat_file`, `_ls`, `_info`) | 9 |
| `async_bridge` | Event loop runner bridge (`fsspec.asyn.sync()`, `sync_wrapper()`) | 1 |

---

