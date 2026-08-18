# GitHub Issues Performance & FSSPEC Crawl Report

- **Repositories Crawled:** `24`
- **Total Issues Scanned:** `1000`
- **Matched Performance / FSSPEC Issues:** `52`

---

## 📊 Repository Issue Breakdown

| Repository | Issues Scanned | Matched Perf/FSSPEC Issues | Top Issue Link |
| :--- | :--- | :--- | :--- |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | `100` | `1` | [#193915](https://github.com/pytorch/pytorch/issues/193915) |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | `100` | `5` | [#66615](https://github.com/pandas-dev/pandas/issues/66615) |
| [ray-project/ray](https://github.com/ray-project/ray) | `100` | `0` | N/A |
| [pola-rs/polars](https://github.com/pola-rs/polars) | `100` | `17` | [#28647](https://github.com/pola-rs/polars/issues/28647) |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | `100` | `6` | [#21868](https://github.com/Lightning-AI/pytorch-lightning/issues/21868) |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | `0` | `0` | N/A |
| [huggingface/datasets](https://github.com/huggingface/datasets) | `0` | `0` | N/A |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | `100` | `3` | [#24789](https://github.com/mlflow/mlflow/issues/24789) |
| [apache/arrow](https://github.com/apache/arrow) | `0` | `0` | N/A |
| [iterative/dvc](https://github.com/iterative/dvc) | `0` | `0` | N/A |
| [dask/dask](https://github.com/dask/dask) | `100` | `1` | [#12359](https://github.com/dask/dask/issues/12359) |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | `0` | `0` | N/A |
| [modin-project/modin](https://github.com/modin-project/modin) | `0` | `0` | N/A |
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | `100` | `2` | [#7558](https://github.com/flyteorg/flyte/issues/7558) |
| [feast-dev/feast](https://github.com/feast-dev/feast) | `100` | `1` | [#6665](https://github.com/feast-dev/feast/issues/6665) |
| [pydata/xarray](https://github.com/pydata/xarray) | `100` | `16` | [#11455](https://github.com/pydata/xarray/issues/11455) |
| [kedro-org/kedro](https://github.com/kedro-org/kedro) | `0` | `0` | N/A |
| [pytorch/torchtitan](https://github.com/pytorch/torchtitan) | `0` | `0` | N/A |
| [delta-io/delta-rs](https://github.com/delta-io/delta-rs) | `0` | `0` | N/A |
| [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) | `0` | `0` | N/A |
| [intake/intake](https://github.com/intake/intake) | `0` | `0` | N/A |
| [fsspec/s3fs](https://github.com/fsspec/s3fs) | `0` | `0` | N/A |
| [fsspec/gcsfs](https://github.com/fsspec/gcsfs) | `0` | `0` | N/A |
| [fsspec/adlfs](https://github.com/fsspec/adlfs) | `0` | `0` | N/A |

---

## 🔍 Detailed Matched Issues

### [pytorch/pytorch](https://github.com/pytorch/pytorch) (1 issues)

#### 1. [[AOTInductor] mmap-backed constant mappings survive runner destruction](https://github.com/pytorch/pytorch/issues/193915) (#193915)
- **URL:** https://github.com/pytorch/pytorch/issues/193915
- **Relevance Score:** `27` | **State:** `open` | **Author:** `sujuyu`
- **Labels:** `module: memory usage`, `triaged`, `oncall: pt2`, `oncall: export`, `module: aotinductor`, `bot-triaged`
- **FS Keywords:** `mmap`
- **Perf Keywords:** `cache`, `caching`, `hang`, `io`, `prefetch`
- **Excerpt:** *"### 🐛 Describe the bug <!-- Suggested title: [AOTInductor] mmap-backed constant mappings survive runner destruction --> I reproduced this behavior in a rolling AOTInductor model-loading workload. I reviewed the report below and confirmed that the `/proc/self/maps` behavior matches my local testing. ..."*

### [pandas-dev/pandas](https://github.com/pandas-dev/pandas) (5 issues)

#### 2. [BUG: Inconsistent date time handling with serialized data](https://github.com/pandas-dev/pandas/issues/66615) (#66615)
- **URL:** https://github.com/pandas-dev/pandas/issues/66615
- **Relevance Score:** `34` | **State:** `open` | **Author:** `nanthony007`
- **Labels:** `Bug`, `IO JSON`, `Needs Triage`, `Closing Candidate`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `i/o`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 3. [BUG: object of type 'list_iterator' has no len()](https://github.com/pandas-dev/pandas/issues/66514) (#66514)
- **URL:** https://github.com/pandas-dev/pandas/issues/66514
- **Relevance Score:** `31` | **State:** `open` | **Author:** `loicdiridollou`
- **Labels:** `Bug`, `Needs Discussion`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 4. [BUG: cumsum/cumprod raises ArrowInvalid: overflow on integer ArrowDtypes instead of upcasting](https://github.com/pandas-dev/pandas/issues/66605) (#66605)
- **URL:** https://github.com/pandas-dev/pandas/issues/66605
- **Relevance Score:** `24` | **State:** `open` | **Author:** `arunkpe`
- **Labels:** `Bug`, `Needs Discussion`, `Arrow`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 5. [BUG: Passing a tuple at creation for 1-d  index in df is fine but rename_axis with tuple fails](https://github.com/pandas-dev/pandas/issues/66656) (#66656)
- **URL:** https://github.com/pandas-dev/pandas/issues/66656
- **Relevance Score:** `18` | **State:** `open` | **Author:** `loicdiridollou`
- **Labels:** `Bug`, `Indexing`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 6. [BUG: DataFrame.loc assignment with boolean column indexer raises NotImplementedError for single-column DataFrame](https://github.com/pandas-dev/pandas/issues/66527) (#66527)
- **URL:** https://github.com/pandas-dev/pandas/issues/66527
- **Relevance Score:** `18` | **State:** `open` | **Author:** `kanade-ao`
- **Labels:** `Bug`, `Needs Triage`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

### [pola-rs/polars](https://github.com/pola-rs/polars) (17 issues)

#### 7. [Speed up datetime parsing from NDJSON](https://github.com/pola-rs/polars/issues/28647) (#28647)
- **URL:** https://github.com/pola-rs/polars/issues/28647
- **Relevance Score:** `33` | **State:** `open` | **Author:** `0guban0v`
- **Labels:** `enhancement`, `A-io-json`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `benchmark`, `cache`, `io`, `slow`, `speed`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this issue on latest release `polars==1.43.2`. ### Reproducible example Given `mgbench2.csv` from public [Brown University/MgBench dataset](https://clickhouse.com/docs/get-started/sample-datasets/br..."*

#### 8. [read_parquet fails on a Parquet data page with concatenated gzip members](https://github.com/pola-rs/polars/issues/28787) (#28787)
- **URL:** https://github.com/pola-rs/polars/issues/28787
- **Relevance Score:** `30` | **State:** `open` | **Author:** `sovsparrow`
- **Labels:** `bug`, `python`, `accepted`, `P-medium`, `A-io-parquet`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `chunk_size`, `concurrent`, `io`, `prefetch`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python from hashlib import sha256 from io import BytesIO from urllib.request import u..."*

#### 9. [FilterExec's parallelism gate is inverted, leading to significant slowdown](https://github.com/pola-rs/polars/issues/28593) (#28593)
- **URL:** https://github.com/pola-rs/polars/issues/28593
- **Relevance Score:** `30` | **State:** `open` | **Author:** `matthewbayer`
- **Labels:** `python`, `performance`, `accepted`, `P-medium`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `slow`, `stall`, `stalled`, `throughput`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import time import numpy as np import polars as pl def t(f): f(); ts = [] for ..."*

#### 10. [`Categorical.sort()` is slower than the equivalent `String.sort()` since the 1.32 lexical rework](https://github.com/pola-rs/polars/issues/28774) (#28774)
- **URL:** https://github.com/pola-rs/polars/issues/28774
- **Relevance Score:** `27` | **State:** `open` | **Author:** `tommycarstensen`
- **Labels:** `python`, `enhancement`, `performance`, `A-dtype-categorical`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `cache`, `io`, `slow`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python #!/usr/bin/env python3 """Repro: polars Categorical.sort() is slower than the ..."*

#### 11. [.rolling(...).agg(...)  ~20–40x slower ≥ 64 threads](https://github.com/pola-rs/polars/issues/28597) (#28597)
- **URL:** https://github.com/pola-rs/polars/issues/28597
- **Relevance Score:** `27` | **State:** `open` | **Author:** `rcliu623`
- **Labels:** `bug`, `python`, `performance`, `P-medium`, `A-rolling`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `performance`, `slow`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import time import polars as pl # 250_000 rows: 1_000 groups x 250 rows. Group..."*

#### 12. [Docs: clarify meaning of `ambiguous` in `str.to_datetime` (and other docstrings where `ambiguous` appears)](https://github.com/pola-rs/polars/issues/28833) (#28833)
- **URL:** https://github.com/pola-rs/polars/issues/28833
- **Relevance Score:** `24` | **State:** `open` | **Author:** `gim-am`
- **Labels:** `documentation`, `python`, `P-low`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `concurrent`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl df = pl.DataFrame({"value": [31216]}) df.filter( pl.col("v..."*

#### 13. [Checking the emptyness of a lazyframe with pl.String as first column can cause OOM](https://github.com/pola-rs/polars/issues/28582) (#28582)
- **URL:** https://github.com/pola-rs/polars/issues/28582
- **Relevance Score:** `24` | **State:** `open` | **Author:** `Hunterlige`
- **Labels:** `python`, `enhancement`, `performance`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `oom`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python """Repro: "does this frame have rows" reads a data column on a union of cast s..."*

#### 14. [ComputeError reading Parquet files with VARIANT LogicalType (field_id=16) entire file unreadable](https://github.com/pola-rs/polars/issues/28627) (#28627)
- **URL:** https://github.com/pola-rs/polars/issues/28627
- **Relevance Score:** `21` | **State:** `open` | **Author:** `SzymonCogiel`
- **Labels:** `bug`, `python`, `needs triage`, `A-io-parquet`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python """ Generates a minimal Parquet file with a VARIANT LogicalType annotation by ..."*

#### 15. [Datatypes have an inconsistent repr (not PEP 585-complaint?)](https://github.com/pola-rs/polars/issues/28766) (#28766)
- **URL:** https://github.com/pola-rs/polars/issues/28766
- **Relevance Score:** `14` | **State:** `open` | **Author:** `Fufs`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl repr(pl.DataType) # DataType repr(pl.DataType | str) # pol..."*

#### 16. [`~expr.is_nan()` raises `InvalidOperationError` on dtype `Null` since 1.43.1](https://github.com/pola-rs/polars/issues/28845) (#28845)
- **URL:** https://github.com/pola-rs/polars/issues/28845
- **Relevance Score:** `11` | **State:** `open` | **Author:** `knowecho`
- **Labels:** `bug`, `python`, `accepted`, `P-high`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl print(pl.select(~pl.lit(None).is_nan())) ``` On 1.43.2 thi..."*

#### 17. [`collect_async` and `collect_batches` silently run on the CPU when GPU is selected](https://github.com/pola-rs/polars/issues/28842) (#28842)
- **URL:** https://github.com/pola-rs/polars/issues/28842
- **Relevance Score:** `11` | **State:** `open` | **Author:** `dancsi`
- **Labels:** `bug`, `python`, `needs triage`, `A-gpu`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import asyncio import polars as pl engine = pl.GPUEngine(raise_on_fail=True) #..."*

#### 18. [LazyFrame.set_sorted() with multiple columns returns wrong results with in-memory engine](https://github.com/pola-rs/polars/issues/28831) (#28831)
- **URL:** https://github.com/pola-rs/polars/issues/28831
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ndaskalovic`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl # Lexicographically sorted by (a, b): `b` is sorted *withi..."*

#### 19. [Inconsistent behavior when exporting to Arrow schema](https://github.com/pola-rs/polars/issues/28777) (#28777)
- **URL:** https://github.com/pola-rs/polars/issues/28777
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ng-23`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import csv import tempfile import polars as pl import pyarrow as pa import pya..."*

#### 20. [CSE of list](https://github.com/pola-rs/polars/issues/28706) (#28706)
- **URL:** https://github.com/pola-rs/polars/issues/28706
- **Relevance Score:** `11` | **State:** `open` | **Author:** `matthieubulte`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl CALLS: list[int] = [] def instrumented_scalar_udf(s: pl.Se..."*

#### 21. [Bug: `cum_sum` panics on Int64 overflow test_confirmed_bugswhile `sum()` and binary `+` wrap](https://github.com/pola-rs/polars/issues/28660) (#28660)
- **URL:** https://github.com/pola-rs/polars/issues/28660
- **Relevance Score:** `11` | **State:** `open` | **Author:** `JasonHonKL`
- **Labels:** `bug`, `python`, `P-medium`, `A-arithmetic`, `A-panic`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl s = pl.Series([9223372036854775807, 1], dtype=pl.Int64) # ..."*

#### 22. [`write_csv(quote_style="always")` writes nulls as `""`, silently turning them into empty strings on read](https://github.com/pola-rs/polars/issues/28589) (#28589)
- **URL:** https://github.com/pola-rs/polars/issues/28589
- **Relevance Score:** `11` | **State:** `open` | **Author:** `matthewbayer`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import io import polars as pl buf = io.BytesIO() pl.DataFrame({"s": ["a", None..."*

#### 23. [`cast(Struct{...}, strict=True)` to renamed fields silently nulls every value](https://github.com/pola-rs/polars/issues/28587) (#28587)
- **URL:** https://github.com/pola-rs/polars/issues/28587
- **Relevance Score:** `11` | **State:** `open` | **Author:** `matthewbayer`
- **Labels:** `bug`, `python`, `accepted`, `P-high`, `A-dtype-struct`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl s = pl.Series([{"a": 1, "b": 2}]) s.cast(pl.Struct({"x": p..."*

### [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) (6 issues)

#### 24. [Optimize remote checkpoint loading with parallel multiprocess downloads and zero-copy mmap](https://github.com/Lightning-AI/pytorch-lightning/issues/21868) (#21868)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21868
- **Relevance Score:** `31` | **State:** `open` | **Author:** `yuxin00j`
- **Labels:** `feature`, `needs triage`
- **FS Keywords:** `filesystem`, `mmap`
- **Perf Keywords:** `bottleneck`, `cache`, `caching`, `concurrent`, `i/o`, `io`, `latency`, `oom`, `throughput`
- **Excerpt:** *"### Description & Motivation Currently, loading monolithic, multi-gigabyte checkpoints from remote object stores (such as Google Cloud Storage gs://) via _load() suffers from two significant bottlenecks: 1. Sequential Main-Thread Streaming I/O: Upstream Lightning streams remote checkpoints sequentia..."*

#### 25. [Unified storage_options support for FSDPStrategy, ModelParallelStrategy, and TorchCheckpointIO](https://github.com/Lightning-AI/pytorch-lightning/issues/21905) (#21905)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21905
- **Relevance Score:** `19` | **State:** `open` | **Author:** `Yonghui-Lee`
- **Labels:** `feature`, `needs triage`
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `caching`, `concurrent`, `i/o`, `io`, `performance`
- **Excerpt:** *"### Description & Motivation When saving and loading distributed checkpoints (e.g., via PyTorch Distributed Checkpoint / DCP with `FSDPStrategy` or `ModelParallelStrategy`), PyTorch allows configuring storage backend parameters such as: - `thread_count`: Number of concurrent I/O threads per rank to ..."*

#### 26. [Deprecation warnings in lightning.pytorch.cli with jsonargparse 4.49+](https://github.com/Lightning-AI/pytorch-lightning/issues/21900) (#21900)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21900
- **Relevance Score:** `11` | **State:** `open` | **Author:** `adamjstewart`
- **Labels:** `bug`, `needs triage`, `ver: 2.6.x`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `cache`, `hang`, `io`
- **Excerpt:** *"### Bug description `lightning/pytorch/cli.py` uses a few features from jsonargparse that have recently been deprecated. ### What version are you seeing the problem on? v2.6 ### Reproduced in studio _No response_ ### How to reproduce the bug ```python ``` ### Error messages and logs ``` /Users/Adam/..."*

#### 27. [Checkpoints silently fail to save due to swallowed PermissionError in `_atomic_save`](https://github.com/Lightning-AI/pytorch-lightning/issues/21800) (#21800)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21800
- **Relevance Score:** `11` | **State:** `open` | **Author:** `zhixiangli`
- **Labels:** `bug`, `checkpointing`, `ver: 2.6.x`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Bug description `_atomic_save` was silently swallowing non-cross-device PermissionErrors, causing saves to report success while failing to write any checkpoints. Because training continues as if the process were successful, this is a data-loss risk. ### What version are you seeing the problem on..."*

#### 28. [`ModelCheckpoint` deletes *previous run's* checkpoint when remote filesystem](https://github.com/Lightning-AI/pytorch-lightning/issues/21813) (#21813)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21813
- **Relevance Score:** `10` | **State:** `open` | **Author:** `parhamfh`
- **Labels:** `bug`, `callback: model checkpoint`, `ver: 2.6.x`
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"### Bug description `ModelCheckpoint` deletes the *previous run's* checkpoint, including the exact file the trainer resumed from, when the checkpoint dirpath is on a remote (fsspec) filesystem. Authored with the help of an agent but I detected the bug myself. I continued a training using `Trainer.fi..."*

#### 29. [Transformer Engine plugin fails to check weight exists for LayerNorm](https://github.com/Lightning-AI/pytorch-lightning/issues/21755) (#21755)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21755
- **Relevance Score:** `10` | **State:** `open` | **Author:** `HenryJia`
- **Labels:** `bug`, `ver: 2.6.x`
- **FS Keywords:** `fsspec`, `mmap`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"### Bug description At https://github.com/Lightning-AI/pytorch-lightning/blob/master/src/lightning/fabric/plugins/precision/transformer_engine.py#L173 There is no check that the weights of the LayerNorm layer are not None This means that if a LayerNorm layer is created using `elementwise_affine=Fals..."*

### [mlflow/mlflow](https://github.com/mlflow/mlflow) (3 issues)

#### 30. [[BUG] A single unparseable filename in images/ silently discards every logged image for that run](https://github.com/mlflow/mlflow/issues/24789) (#24789)
- **URL:** https://github.com/mlflow/mlflow/issues/24789
- **Relevance Score:** `8` | **State:** `open` | **Author:** `sirzzang`
- **Labels:** `Acknowledged`
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. ### MLflow version ..."*

#### 31. [[BUG] AI Gateway passthrough forwards the client Authorization header, shadowing the Vertex AI OAuth Bearer (401)](https://github.com/mlflow/mlflow/issues/25108) (#25108)
- **URL:** https://github.com/mlflow/mlflow/issues/25108
- **Relevance Score:** `5` | **State:** `open` | **Author:** `Nantina`
- **Labels:** `bug`, `has-closing-pr`, `ready`, `area/gateway`
- **FS Keywords:** `parts`
- **Perf Keywords:** `io`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. ### Issues Policy a..."*

#### 32. [[FR] Support Hugging Face Storage Buckets as an artifact store](https://github.com/mlflow/mlflow/issues/24848) (#24848)
- **URL:** https://github.com/mlflow/mlflow/issues/24848
- **Relevance Score:** `5` | **State:** `open` | **Author:** `abidlabs`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. MLflow already supp..."*

### [dask/dask](https://github.com/dask/dask) (1 issues)

#### 33. ['cumsum' results differ from 'cumsum' on a pure numpy array](https://github.com/dask/dask/issues/12359) (#12359)
- **URL:** https://github.com/dask/dask/issues/12359
- **Relevance Score:** `21` | **State:** `open` | **Author:** `muttener`
- **Labels:** `array`, `needs attention`, `bug`
- **FS Keywords:** `mmap`
- **Perf Keywords:** `chunk_size`, `io`, `stall`
- **Excerpt:** *"<!-- Please include a self-contained copy-pastable example that generates the issue if possible. Please be concise with code posted. See guidelines below on how to provide a good bug report: - Craft Minimal Bug Reports http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports - Minimal Comp..."*

### [flyteorg/flyte](https://github.com/flyteorg/flyte) (2 issues)

#### 34. [Fix typo: rename ActionMetadata.funtion_name → function_name (proto, backend, SDK stubs)](https://github.com/flyteorg/flyte/issues/7558) (#7558)
- **URL:** https://github.com/flyteorg/flyte/issues/7558
- **Relevance Score:** `14` | **State:** `open` | **Author:** `pingsutw`
- **Labels:** `good first issue`, `flyte2`
- **FS Keywords:** `parts`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"## Summary There's a typo in one of our protobuf fields: `funtion_name` should be `function_name` (missing the **c**). It lives on the `ActionMetadata` message and flows through the generated code in every language, the Go backend, and the published `flyteidl2` package that the Python SDK depends on..."*

#### 35. [Proposal: RAG workflow failure taxonomy guide using WFGY ProblemMap](https://github.com/flyteorg/flyte/issues/6930) (#6930)
- **URL:** https://github.com/flyteorg/flyte/issues/6930
- **Relevance Score:** `5` | **State:** `open` | **Author:** `onestardao`
- **Labels:** None
- **FS Keywords:** `mmap`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, and thanks for Flyte – the emphasis on strong typing and reproducible workflows is very helpful for production ML. I maintain an open-source project called **WFGY** (MIT-licensed, ~1.5k GitHub stars). We maintain a **16-problem “ProblemMap”** that focuses on **RAG / LLM failure modes** across re..."*

### [feast-dev/feast](https://github.com/feast-dev/feast) (1 issues)

#### 36. [Remote registry gRPC client sets no deadline and no keepalive, and neither is configurable: a blackholed connection hangs the caller indefinitely](https://github.com/feast-dev/feast/issues/6665) (#6665)
- **URL:** https://github.com/feast-dev/feast/issues/6665
- **Relevance Score:** `14` | **State:** `open` | **Author:** `BigyaPradhan`
- **Labels:** None
- **FS Keywords:** `parts`
- **Perf Keywords:** `hang`, `io`, `stall`, `timeout`
- **Excerpt:** *"## Expected Behavior A registry RPC issued by `RemoteRegistry` should fail within a bounded time when the connection to the registry server stops making progress, and the bound should be configurable through `RemoteRegistryConfig`. ## Current Behavior `RemoteRegistry` builds a channel with no keepal..."*

### [pydata/xarray](https://github.com/pydata/xarray) (16 issues)

#### 37. [unstack is slow for regular data](https://github.com/pydata/xarray/issues/11455) (#11455)
- **URL:** https://github.com/pydata/xarray/issues/11455
- **Relevance Score:** `36` | **State:** `open` | **Author:** `takluyver`
- **Labels:** `bug`, `topic-performance`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `performance`, `slow`, `speed`, `speedup`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Unstacking an array with a 'regular' MultiIndex, i.e. a cartesian product which doesn't need any missing value handling, is unexpectedly slow. E.g. unstacking (300_000, 1024) -> (10_000, 30, 1024) takes ~660 ms in my test, whereas reshaping the numpy array is massively quicker. ##..."*

#### 38. [2026.4.0 breaks pickling with backends.scipy_](https://github.com/pydata/xarray/issues/11323) (#11323)
- **URL:** https://github.com/pydata/xarray/issues/11323
- **Relevance Score:** `30` | **State:** `open` | **Author:** `SoundDesignerToBe`
- **Labels:** `bug`, `topic-backends`, `contrib-good-first-issue`, `regression`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `concurrent`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Switching from 2026.2.0 to 2026.4.0 breaks some pickling backend for netcdf files in multi-processing (concurrent.future.ProcessPoolExecutor). Quoting Claude: > The error is a classic pickle-identity mismatch: the instance's class qualname is `xarray.backends.scipy_._PickleWorkaro..."*

#### 39. [Construction of arrays with `object` dtype very slow when Pandas `future.infer_string` is enabled](https://github.com/pydata/xarray/issues/11470) (#11470)
- **URL:** https://github.com/pydata/xarray/issues/11470
- **Relevance Score:** `27` | **State:** `open` | **Author:** `y4n9squared`
- **Labels:** `bug`, `topic-performance`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `slow`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Constructing a `Variable` (or `Dataset`/`DataArray`) from an object-dtype numpy array of strings takes ~0.1ms per 10M elements under pandas' default settings, but **~500–620ms** with `pd.options.future.infer_string = True` — the setting that becomes the default in pandas 3.0. Why:..."*

#### 40. [In open_zarr, decode_timedelta does not behave as documented](https://github.com/pydata/xarray/issues/11507) (#11507)
- **URL:** https://github.com/pydata/xarray/issues/11507
- **Relevance Score:** `19` | **State:** `open` | **Author:** `theo-xirouchaki`
- **Labels:** `bug`, `topic-zarr`
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `bottleneck`, `io`, `speed`, `stall`, `stalled`
- **Excerpt:** *"### What happened? [The documentation](https://docs.xarray.dev/en/stable/generated/xarray.open_zarr.html#xarray.open_zarr) states that, for open_zarr, if decode_timedelta is None it will take the value of decode_times which is True by default. That isn't the behaviour I'm seeing, timedeltas are not ..."*

#### 41. [DataSetRolling and DatasetGroupBy silently accept `keepdims`, which modifes shape of the GroupBy output](https://github.com/pydata/xarray/issues/11518) (#11518)
- **URL:** https://github.com/pydata/xarray/issues/11518
- **Relevance Score:** `17` | **State:** `open` | **Author:** `charles-turner-1`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? > [!NOTE] > I've edited this a bit since I've opened it since I've discovered a bit of a can of worms. I'm trying to figure out if this is a duplicate of other issues now - it wasn't when I started. tldr; `ds.rolling({'time' : 12}).mean(keepdims=False|True)` makes no difference an..."*

#### 42. [StringDType does not roundtrip through zarr](https://github.com/pydata/xarray/issues/11466) (#11466)
- **URL:** https://github.com/pydata/xarray/issues/11466
- **Relevance Score:** `17` | **State:** `open` | **Author:** `jacksonriley`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Hi there, I noticed today that in `xarray>=2026.4.0`, a `Dataset` with a variable of type `np.dtypes.StringDType` does not roundtrip via zarr (you end up with fixed-length UTF32), and this also triggers a warning in Zarr: ``` /usr/local/lib/python3.12/site-packages/zarr/core/dtype..."*

#### 43. [FutureCancelledError (lost dependencies) during `dask.compute` with `optimize_graph=True` when chaining Dataset.assign](https://github.com/pydata/xarray/issues/11329) (#11329)
- **URL:** https://github.com/pydata/xarray/issues/11329
- **Relevance Score:** `17` | **State:** `open` | **Author:** `maneesh29s`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? It appears that the High-Level Graph (HLG) optimization fails to correctly resolve dependencies when a variable (like `new_weight` in the example) is used both as an input for a subsequent calculation and as a replacement variable in an intermediate Dataset state. Raised exception..."*

#### 44. [DataTree constructor error message says dict even though dict is not accepted](https://github.com/pydata/xarray/issues/11514) (#11514)
- **URL:** https://github.com/pydata/xarray/issues/11514
- **Relevance Score:** `14` | **State:** `open` | **Author:** `mgunyho`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When I try to create a `DataTree` with a `dict` as the first argument, I get a TypeError: ``` >>> xr.DataTree(dict()) ... TypeError: data object is not an xarray.Dataset, dict, or None: {} ``` ### What did you expect to happen? A dictionary should be accepted, or the error message..."*

#### 45. [Unable to roundtrip sharded zarr](https://github.com/pydata/xarray/issues/11460) (#11460)
- **URL:** https://github.com/pydata/xarray/issues/11460
- **Relevance Score:** `14` | **State:** `open` | **Author:** `taus`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When creating a sharded zarr data set, reopening the dataset looses the sharding information. Shard and chunk sizes are set using `encoding` in to_zarr. When the dataset is reopened the sharding information is disregarded and the zarr chunks are used instead. This results in issue..."*

#### 46. [Latex labels not rendered under very specific conditions](https://github.com/pydata/xarray/issues/11452) (#11452)
- **URL:** https://github.com/pydata/xarray/issues/11452
- **Relevance Score:** `14` | **State:** `open` | **Author:** `mtrocadomoreira`
- **Labels:** `bug`, `topic-plotting`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I was plotting some Datasets with fairly complicated labels and units, and I noticed a very strange behaviour when using the `plot()` method. When both `attrs["long_name"]` and `attrs["units"]` contain `\mathrm`'s or `\text`'s, and at least one of them contains a `\frac`, and if t..."*

#### 47. [np.linalg.pinv of a DataArray results in mismatched coordinates](https://github.com/pydata/xarray/issues/11396) (#11396)
- **URL:** https://github.com/pydata/xarray/issues/11396
- **Relevance Score:** `14` | **State:** `open` | **Author:** `brsr`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? In general, `np.linalg.pinv` takes an array of shape (..., n, m) and returns an array of shape (..., m, n). Something isn't recognizing that the last two axes get switched around, so it incorrectly retains the coordinates in the same order. In the attached example, `m1` is an Data..."*

#### 48. [Cannot reindex onto a stacked MultiIndex via indexers — only reindex_like works](https://github.com/pydata/xarray/issues/11368) (#11368)
- **URL:** https://github.com/pydata/xarray/issues/11368
- **Relevance Score:** `14` | **State:** `open` | **Author:** `FBumann`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Reindexing a DataArray whose dimension is backed by a stacked `pd.MultiIndex` onto a *different* MultiIndex (e.g. the full index, where the array covers a subset) fails for **every** indexer form: 1. a raw `pd.MultiIndex` as indexer value → `ValueError: unmatched keys found in ind..."*

#### 49. [Corrupted data when Xarray writes to Zarr Datetime64 dtype](https://github.com/pydata/xarray/issues/11350) (#11350)
- **URL:** https://github.com/pydata/xarray/issues/11350
- **Relevance Score:** `14` | **State:** `open` | **Author:** `vladidobro`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Hi, when using the new Zarr v3 DateTime64 dtype, I have trouble correctly writing to it with xarray - I have not found a way to write the correct values. I believe it is probably related to some CF coding enabled when it should not be, or something like that. Am I doing something ..."*

#### 50. [A single nested tuple MultiIndex key is located correctly but preserves the dimension](https://github.com/pydata/xarray/issues/11341) (#11341)
- **URL:** https://github.com/pydata/xarray/issues/11341
- **Relevance Score:** `14` | **State:** `open` | **Author:** `cfriedland5`
- **Labels:** `bug`, `topic-indexing`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When selecting from an xarray MultiIndex that has a tuple-valued level, a nested tuple key corresponding to a single location can be located correctly, but the result keeps a length-1 dimension instead of behaving like scalar selection. It is inconsistent that xarray correctly und..."*

#### 51. [cumulate+argmax uses padded index instead of absolute index](https://github.com/pydata/xarray/issues/11336) (#11336)
- **URL:** https://github.com/pydata/xarray/issues/11336
- **Relevance Score:** `14` | **State:** `open` | **Author:** `saschahofmann`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? The combination of cumulative + argmax does not lead to the (at least from me) expected result. Example: ```python import numpy as np import xarray as xr da = xr.DataArray([1,2,1.5,3.5,4], coords={'time': ('time', np.arange(5))}) da.cumulative('time').argmax() # [4., 4., 3., 4., 4..."*

#### 52. [concat fails due to StringDtype introduced by pd.Index](https://github.com/pydata/xarray/issues/11317) (#11317)
- **URL:** https://github.com/pydata/xarray/issues/11317
- **Relevance Score:** `14` | **State:** `open` | **Author:** `vincentschut`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? This used to work (a few releases of xarray and/or pandas ago): ```python import xarray as xr import pandas as pd da = xr.DataArray([0], dims=["dim_a"], coords=dict(dim_a=["a"])) db = xr.DataArray([0]) # use concat to add a new dimension with coordinate db2 = xr.concat([db], pd.In..."*
