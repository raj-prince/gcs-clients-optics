# GitHub Issues Performance & FSSPEC Crawl Report

- **Repositories Crawled:** `24`
- **Total Issues Scanned:** `2634`
- **Matched Performance / FSSPEC Issues:** `195`

---

## 📊 Repository Issue Breakdown

| Repository | Issues Scanned | Matched Perf/FSSPEC Issues | Top Issue Link |
| :--- | :--- | :--- | :--- |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | `200` | `2` | [#193915](https://github.com/pytorch/pytorch/issues/193915) |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | `200` | `17` | [#66615](https://github.com/pandas-dev/pandas/issues/66615) |
| [ray-project/ray](https://github.com/ray-project/ray) | `100` | `1` | [#65557](https://github.com/ray-project/ray/issues/65557) |
| [pola-rs/polars](https://github.com/pola-rs/polars) | `200` | `30` | [#28647](https://github.com/pola-rs/polars/issues/28647) |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | `100` | `6` | [#21868](https://github.com/Lightning-AI/pytorch-lightning/issues/21868) |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | `200` | `5` | [#24848](https://github.com/duckdb/duckdb/issues/24848) |
| [huggingface/datasets](https://github.com/huggingface/datasets) | `200` | `4` | [#8242](https://github.com/huggingface/datasets/issues/8242) |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | `200` | `7` | [#24461](https://github.com/mlflow/mlflow/issues/24461) |
| [apache/arrow](https://github.com/apache/arrow) | `200` | `7` | [#50667](https://github.com/apache/arrow/issues/50667) |
| [iterative/dvc](https://github.com/iterative/dvc) | `100` | `28` | [#10417](https://github.com/treeverse/dvc/issues/10417) |
| [dask/dask](https://github.com/dask/dask) | `200` | `2` | [#12060](https://github.com/dask/dask/issues/12060) |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | `34` | `3` | [#10896](https://github.com/fivetran/great_expectations/issues/10896) |
| [modin-project/modin](https://github.com/modin-project/modin) | `100` | `39` | [#7403](https://github.com/modin-project/modin/issues/7403) |
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | `100` | `2` | [#7558](https://github.com/flyteorg/flyte/issues/7558) |
| [feast-dev/feast](https://github.com/feast-dev/feast) | `200` | `1` | [#6665](https://github.com/feast-dev/feast/issues/6665) |
| [pydata/xarray](https://github.com/pydata/xarray) | `200` | `37` | [#11455](https://github.com/pydata/xarray/issues/11455) |
| [kedro-org/kedro](https://github.com/kedro-org/kedro) | `100` | `4` | [#4690](https://github.com/kedro-org/kedro/issues/4690) |
| [pytorch/torchtitan](https://github.com/pytorch/torchtitan) | `0` | `0` | N/A |
| [delta-io/delta-rs](https://github.com/delta-io/delta-rs) | `0` | `0` | N/A |
| [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) | `0` | `0` | N/A |
| [intake/intake](https://github.com/intake/intake) | `0` | `0` | N/A |
| [fsspec/s3fs](https://github.com/fsspec/s3fs) | `0` | `0` | N/A |
| [fsspec/gcsfs](https://github.com/fsspec/gcsfs) | `0` | `0` | N/A |
| [fsspec/adlfs](https://github.com/fsspec/adlfs) | `0` | `0` | N/A |

---

## 🔍 Detailed Matched Issues

### [pytorch/pytorch](https://github.com/pytorch/pytorch) (2 issues)

#### 1. [[AOTInductor] mmap-backed constant mappings survive runner destruction](https://github.com/pytorch/pytorch/issues/193915) (#193915)
- **URL:** https://github.com/pytorch/pytorch/issues/193915
- **Relevance Score:** `27` | **State:** `open` | **Author:** `sujuyu`
- **Labels:** `module: memory usage`, `triaged`, `oncall: pt2`, `oncall: export`, `module: aotinductor`, `bot-triaged`
- **FS Keywords:** `mmap`
- **Perf Keywords:** `cache`, `caching`, `hang`, `io`, `prefetch`
- **Excerpt:** *"### 🐛 Describe the bug <!-- Suggested title: [AOTInductor] mmap-backed constant mappings survive runner destruction --> I reproduced this behavior in a rolling AOTInductor model-loading workload. I reviewed the report below and confirmed that the `/proc/self/maps` behavior matches my local testing. ..."*

#### 2. [[DCP] Dynamic `thread_count` auto-tuning for Distributed Checkpoint writers](https://github.com/pytorch/pytorch/issues/193804) (#193804)
- **URL:** https://github.com/pytorch/pytorch/issues/193804
- **Relevance Score:** `10` | **State:** `open` | **Author:** `Yonghui-Lee`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`, `latency`
- **Excerpt:** *"### 🚀 The feature, motivation and pitch PyTorch Distributed Checkpoint (DCP) supports multi-threaded parallel file writing via `FileSystemWriter(thread_count=...)` and `FsspecWriter(thread_count=...)`. When saving sharded state dicts (e.g. in FSDP / TP / ModelParallel), `_split_by_size_and_type` par..."*

### [pandas-dev/pandas](https://github.com/pandas-dev/pandas) (17 issues)

#### 3. [BUG: Inconsistent date time handling with serialized data](https://github.com/pandas-dev/pandas/issues/66615) (#66615)
- **URL:** https://github.com/pandas-dev/pandas/issues/66615
- **Relevance Score:** `34` | **State:** `open` | **Author:** `nanthony007`
- **Labels:** `Bug`, `IO JSON`, `Needs Triage`, `Closing Candidate`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `i/o`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 4. [BUG: object of type 'list_iterator' has no len()](https://github.com/pandas-dev/pandas/issues/66514) (#66514)
- **URL:** https://github.com/pandas-dev/pandas/issues/66514
- **Relevance Score:** `31` | **State:** `open` | **Author:** `loicdiridollou`
- **Labels:** `Bug`, `Needs Discussion`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 5. [BUG: Plotting with timezone-aware and normalized `DatetimeIndex` drops tz-info](https://github.com/pandas-dev/pandas/issues/65915) (#65915)
- **URL:** https://github.com/pandas-dev/pandas/issues/65915
- **Relevance Score:** `31` | **State:** `open` | **Author:** `Julian-Harbeck`
- **Labels:** `Bug`, `Visualization`, `Needs Discussion`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 6. [DOC: `read_{csv,excel}` skip rows (columns) above (before) header (index columns)](https://github.com/pandas-dev/pandas/issues/66378) (#66378)
- **URL:** https://github.com/pandas-dev/pandas/issues/66378
- **Relevance Score:** `28` | **State:** `open` | **Author:** `kuraga`
- **Labels:** `Docs`, `IO CSV`, `IO Excel`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"- [x] I have checked that the issue still exists on the latest versions of the docs on main [here](https://pandas.pydata.org/docs/dev/). (Part of #34766.) [test.csv](https://github.com/user-attachments/files/30165155/test.csv) [test.xlsx](https://github.com/user-attachments/files/30165203/test.xlsx)..."*

#### 7. [API: `read_excel`: `.index.names` vs `.columns.names`](https://github.com/pandas-dev/pandas/issues/66377) (#66377)
- **URL:** https://github.com/pandas-dev/pandas/issues/66377
- **Relevance Score:** `28` | **State:** `open` | **Author:** `kuraga`
- **Labels:** `API Design`, `IO CSV`, `IO Excel`, `API - Consistency`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 8. [BUG: `read_{csv,excel}(<...>, header=[0,1], index_col=[0,1])` take different `.columns.names`](https://github.com/pandas-dev/pandas/issues/66376) (#66376)
- **URL:** https://github.com/pandas-dev/pandas/issues/66376
- **Relevance Score:** `28` | **State:** `open` | **Author:** `kuraga`
- **Labels:** `Bug`, `IO CSV`, `IO Excel`, `MultiIndex`, `API - Consistency`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 9. [BUG: `read_excel`: `ValueError: Length of new names must be 1, got 2`](https://github.com/pandas-dev/pandas/issues/66372) (#66372)
- **URL:** https://github.com/pandas-dev/pandas/issues/66372
- **Relevance Score:** `28` | **State:** `open` | **Author:** `kuraga`
- **Labels:** `Bug`, `IO Excel`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 10. [BUG: cumsum/cumprod raises ArrowInvalid: overflow on integer ArrowDtypes instead of upcasting](https://github.com/pandas-dev/pandas/issues/66605) (#66605)
- **URL:** https://github.com/pandas-dev/pandas/issues/66605
- **Relevance Score:** `24` | **State:** `open` | **Author:** `arunkpe`
- **Labels:** `Bug`, `Needs Discussion`, `Arrow`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 11. [BUG: `factorize(use_na_sentinel=True)` ignores `use_na_sentinel` for pre-encoded PyArrow `DictionaryArray`s](https://github.com/pandas-dev/pandas/issues/66490) (#66490)
- **URL:** https://github.com/pandas-dev/pandas/issues/66490
- **Relevance Score:** `21` | **State:** `open` | **Author:** `camriddell`
- **Labels:** `Bug`, `Algos`, `Arrow`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 12. [BUG: Inconsistent nan to None behaviour in replace() with scalar vs list value](https://github.com/pandas-dev/pandas/issues/65892) (#65892)
- **URL:** https://github.com/pandas-dev/pandas/issues/65892
- **Relevance Score:** `21` | **State:** `open` | **Author:** `veenstrajelmer`
- **Labels:** `Bug`, `Missing-data`, `Strings`, `replace`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 13. [BUG: coerce empty-string IEEE NaN to null for pyarrow floats](https://github.com/pandas-dev/pandas/issues/66834) (#66834)
- **URL:** https://github.com/pandas-dev/pandas/issues/66834
- **Relevance Score:** `18` | **State:** `open` | **Author:** `hebian1994`
- **Labels:** `Bug`, `Needs Triage`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 14. [BUG: Passing a tuple at creation for 1-d  index in df is fine but rename_axis with tuple fails](https://github.com/pandas-dev/pandas/issues/66656) (#66656)
- **URL:** https://github.com/pandas-dev/pandas/issues/66656
- **Relevance Score:** `18` | **State:** `open` | **Author:** `loicdiridollou`
- **Labels:** `Bug`, `Indexing`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 15. [BUG: DataFrame.loc assignment with boolean column indexer raises NotImplementedError for single-column DataFrame](https://github.com/pandas-dev/pandas/issues/66527) (#66527)
- **URL:** https://github.com/pandas-dev/pandas/issues/66527
- **Relevance Score:** `18` | **State:** `open` | **Author:** `kanade-ao`
- **Labels:** `Bug`, `Needs Triage`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 16. [BUG: DataFrame.eq() incorrectly rejects scalar strings in type annotations](https://github.com/pandas-dev/pandas/issues/66499) (#66499)
- **URL:** https://github.com/pandas-dev/pandas/issues/66499
- **Relevance Score:** `18` | **State:** `open` | **Author:** `Sascha1505`
- **Labels:** `Docs`, `Typing`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 17. [BUG: `MultiIndex.__repr__`: inconsistent output](https://github.com/pandas-dev/pandas/issues/66374) (#66374)
- **URL:** https://github.com/pandas-dev/pandas/issues/66374
- **Relevance Score:** `18` | **State:** `open` | **Author:** `kuraga`
- **Labels:** `Output-Formatting`, `MultiIndex`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 18. [BUG: `str.split()`/`rsplit()` with no separator on `ArrowDtype` keeps empty whitespace tokens](https://github.com/pandas-dev/pandas/issues/66368) (#66368)
- **URL:** https://github.com/pandas-dev/pandas/issues/66368
- **Relevance Score:** `18` | **State:** `open` | **Author:** `gautamvarmadatla`
- **Labels:** `Bug`, `Strings`, `Arrow`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 19. [BUG: Float64 vs float64 incorrect result when using empty slice](https://github.com/pandas-dev/pandas/issues/66255) (#66255)
- **URL:** https://github.com/pandas-dev/pandas/issues/66255
- **Relevance Score:** `18` | **State:** `open` | **Author:** `konvica`
- **Labels:** `Bug`, `Needs Triage`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

### [ray-project/ray](https://github.com/ray-project/ray) (1 issues)

#### 20. [[Data] Parquet Datasource V2 - regression problem - file extension filtering broken](https://github.com/ray-project/ray/issues/65557) (#65557)
- **URL:** https://github.com/ray-project/ray/issues/65557
- **Relevance Score:** `5` | **State:** `open` | **Author:** `pierrebelzile`
- **Labels:** `bug`, `triage`, `usability`, `data`, `stability`, `community-backlog`
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"### What happened + What you expected to happen It appears that with 2.57, parquet_datasource_v2 is now the default. This broke our code that uses: ``` ray_data.read_parquet( paths, filesystem=filesystem, schema=schema, file_extensions=None, ) ) ``` ParquetDatasourceV2::__init__ now does: `self._fil..."*

### [pola-rs/polars](https://github.com/pola-rs/polars) (30 issues)

#### 21. [Speed up datetime parsing from NDJSON](https://github.com/pola-rs/polars/issues/28647) (#28647)
- **URL:** https://github.com/pola-rs/polars/issues/28647
- **Relevance Score:** `33` | **State:** `open` | **Author:** `0guban0v`
- **Labels:** `enhancement`, `A-io-json`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `benchmark`, `cache`, `io`, `slow`, `speed`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this issue on latest release `polars==1.43.2`. ### Reproducible example Given `mgbench2.csv` from public [Brown University/MgBench dataset](https://clickhouse.com/docs/get-started/sample-datasets/br..."*

#### 22. [read_parquet fails on a Parquet data page with concatenated gzip members](https://github.com/pola-rs/polars/issues/28787) (#28787)
- **URL:** https://github.com/pola-rs/polars/issues/28787
- **Relevance Score:** `30` | **State:** `open` | **Author:** `sovsparrow`
- **Labels:** `bug`, `python`, `accepted`, `P-medium`, `A-io-parquet`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `chunk_size`, `concurrent`, `io`, `prefetch`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python from hashlib import sha256 from io import BytesIO from urllib.request import u..."*

#### 23. [FilterExec's parallelism gate is inverted, leading to significant slowdown](https://github.com/pola-rs/polars/issues/28593) (#28593)
- **URL:** https://github.com/pola-rs/polars/issues/28593
- **Relevance Score:** `30` | **State:** `open` | **Author:** `matthewbayer`
- **Labels:** `python`, `performance`, `accepted`, `P-medium`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `slow`, `stall`, `stalled`, `throughput`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import time import numpy as np import polars as pl def t(f): f(); ts = [] for ..."*

#### 24. [parquet scan/reads fail over HTTP for small files hosted with miniserve](https://github.com/pola-rs/polars/issues/28400) (#28400)
- **URL:** https://github.com/pola-rs/polars/issues/28400
- **Relevance Score:** `30` | **State:** `open` | **Author:** `wahsmail`
- **Labels:** `bug`, `python`, `P-medium`, `A-io-parquet`, `upstream issue`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `cache`, `chunk_size`, `io`, `range request`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example The below is run with `uv run --script script.py` and requires miniserve 0.29.0 on path ..."*

#### 25. [`Categorical.sort()` is slower than the equivalent `String.sort()` since the 1.32 lexical rework](https://github.com/pola-rs/polars/issues/28774) (#28774)
- **URL:** https://github.com/pola-rs/polars/issues/28774
- **Relevance Score:** `27` | **State:** `open` | **Author:** `tommycarstensen`
- **Labels:** `python`, `enhancement`, `performance`, `A-dtype-categorical`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `cache`, `io`, `slow`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python #!/usr/bin/env python3 """Repro: polars Categorical.sort() is slower than the ..."*

#### 26. [.rolling(...).agg(...)  ~20–40x slower ≥ 64 threads](https://github.com/pola-rs/polars/issues/28597) (#28597)
- **URL:** https://github.com/pola-rs/polars/issues/28597
- **Relevance Score:** `27` | **State:** `open` | **Author:** `rcliu623`
- **Labels:** `bug`, `python`, `performance`, `P-medium`, `A-rolling`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `performance`, `slow`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import time import polars as pl # 250_000 rows: 1_000 groups x 250 rows. Group..."*

#### 27. [Docs: clarify meaning of `ambiguous` in `str.to_datetime` (and other docstrings where `ambiguous` appears)](https://github.com/pola-rs/polars/issues/28833) (#28833)
- **URL:** https://github.com/pola-rs/polars/issues/28833
- **Relevance Score:** `24` | **State:** `open` | **Author:** `gim-am`
- **Labels:** `documentation`, `python`, `P-low`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `concurrent`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl df = pl.DataFrame({"value": [31216]}) df.filter( pl.col("v..."*

#### 28. [Checking the emptyness of a lazyframe with pl.String as first column can cause OOM](https://github.com/pola-rs/polars/issues/28582) (#28582)
- **URL:** https://github.com/pola-rs/polars/issues/28582
- **Relevance Score:** `24` | **State:** `open` | **Author:** `Hunterlige`
- **Labels:** `python`, `enhancement`, `performance`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `oom`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python """Repro: "does this frame have rows" reads a data column on a union of cast s..."*

#### 29. [ComputeError reading Parquet files with VARIANT LogicalType (field_id=16) entire file unreadable](https://github.com/pola-rs/polars/issues/28627) (#28627)
- **URL:** https://github.com/pola-rs/polars/issues/28627
- **Relevance Score:** `21` | **State:** `open` | **Author:** `SzymonCogiel`
- **Labels:** `bug`, `python`, `needs triage`, `A-io-parquet`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python """ Generates a minimal Parquet file with a VARIANT LogicalType annotation by ..."*

#### 30. [`json_decode` parses invalid json](https://github.com/pola-rs/polars/issues/28552) (#28552)
- **URL:** https://github.com/pola-rs/polars/issues/28552
- **Relevance Score:** `21` | **State:** `open` | **Author:** `erikbrinkman`
- **Labels:** `bug`, `python`, `accepted`, `P-medium`, `A-io-json`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python pl.Series(["1,2", "3"]).str.json_decode(dtype=pl.Int64) ``` ### Log output ```..."*

#### 31. [Oracle database connection regression in 1.43.0](https://github.com/pola-rs/polars/issues/28463) (#28463)
- **URL:** https://github.com/pola-rs/polars/issues/28463
- **Relevance Score:** `21` | **State:** `open` | **Author:** `lmocsi`
- **Labels:** `bug`, `python`, `regression`, `needs triage`, `A-io-database`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python # 1.42.1 ok # 1.43.0 error import polars as pl import oracledb from my_config ..."*

#### 32. [Nested CSPE prevents predicate pushdown to scans](https://github.com/pola-rs/polars/issues/28860) (#28860)
- **URL:** https://github.com/pola-rs/polars/issues/28860
- **Relevance Score:** `17` | **State:** `open` | **Author:** `dancsi`
- **Labels:** `bug`, `python`, `accepted`, `A-optimizer`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `cache`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl import os os.environ['POLARS_ALLOW_NESTED_CSPE'] = '1' buf..."*

#### 33. [Datatypes have an inconsistent repr (not PEP 585-complaint?)](https://github.com/pola-rs/polars/issues/28766) (#28766)
- **URL:** https://github.com/pola-rs/polars/issues/28766
- **Relevance Score:** `14` | **State:** `open` | **Author:** `Fufs`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl repr(pl.DataType) # DataType repr(pl.DataType | str) # pol..."*

#### 34. [Non-monotonic tz-aware temporal conversions keep a stale sorted flag, so `sort()`/`min()` return wrong results](https://github.com/pola-rs/polars/issues/28560) (#28560)
- **URL:** https://github.com/pola-rs/polars/issues/28560
- **Relevance Score:** `14` | **State:** `open` | **Author:** `matthewbayer`
- **Labels:** `bug`, `python`, `A-temporal`, `accepted`, `P-high`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example **Part A — `dt.date()`** ```python import datetime as dt import polars as pl utc = ( pl...."*

#### 35. [`~expr.is_nan()` raises `InvalidOperationError` on dtype `Null` since 1.43.1](https://github.com/pola-rs/polars/issues/28845) (#28845)
- **URL:** https://github.com/pola-rs/polars/issues/28845
- **Relevance Score:** `11` | **State:** `open` | **Author:** `knowecho`
- **Labels:** `bug`, `python`, `accepted`, `P-high`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl print(pl.select(~pl.lit(None).is_nan())) ``` On 1.43.2 thi..."*

#### 36. [`collect_async` and `collect_batches` silently run on the CPU when GPU is selected](https://github.com/pola-rs/polars/issues/28842) (#28842)
- **URL:** https://github.com/pola-rs/polars/issues/28842
- **Relevance Score:** `11` | **State:** `open` | **Author:** `dancsi`
- **Labels:** `bug`, `python`, `needs triage`, `A-gpu`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import asyncio import polars as pl engine = pl.GPUEngine(raise_on_fail=True) #..."*

#### 37. [LazyFrame.set_sorted() with multiple columns returns wrong results with in-memory engine](https://github.com/pola-rs/polars/issues/28831) (#28831)
- **URL:** https://github.com/pola-rs/polars/issues/28831
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ndaskalovic`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl # Lexicographically sorted by (a, b): `b` is sorted *withi..."*

#### 38. [Inconsistent behavior when exporting to Arrow schema](https://github.com/pola-rs/polars/issues/28777) (#28777)
- **URL:** https://github.com/pola-rs/polars/issues/28777
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ng-23`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import csv import tempfile import polars as pl import pyarrow as pa import pya..."*

#### 39. [CSE of list](https://github.com/pola-rs/polars/issues/28706) (#28706)
- **URL:** https://github.com/pola-rs/polars/issues/28706
- **Relevance Score:** `11` | **State:** `open` | **Author:** `matthieubulte`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl CALLS: list[int] = [] def instrumented_scalar_udf(s: pl.Se..."*

#### 40. [Bug: `cum_sum` panics on Int64 overflow test_confirmed_bugswhile `sum()` and binary `+` wrap](https://github.com/pola-rs/polars/issues/28660) (#28660)
- **URL:** https://github.com/pola-rs/polars/issues/28660
- **Relevance Score:** `11` | **State:** `open` | **Author:** `JasonHonKL`
- **Labels:** `bug`, `python`, `P-medium`, `A-arithmetic`, `A-panic`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl s = pl.Series([9223372036854775807, 1], dtype=pl.Int64) # ..."*

#### 41. [`write_csv(quote_style="always")` writes nulls as `""`, silently turning them into empty strings on read](https://github.com/pola-rs/polars/issues/28589) (#28589)
- **URL:** https://github.com/pola-rs/polars/issues/28589
- **Relevance Score:** `11` | **State:** `open` | **Author:** `matthewbayer`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import io import polars as pl buf = io.BytesIO() pl.DataFrame({"s": ["a", None..."*

#### 42. [`cast(Struct{...}, strict=True)` to renamed fields silently nulls every value](https://github.com/pola-rs/polars/issues/28587) (#28587)
- **URL:** https://github.com/pola-rs/polars/issues/28587
- **Relevance Score:** `11` | **State:** `open` | **Author:** `matthewbayer`
- **Labels:** `bug`, `python`, `accepted`, `P-high`, `A-dtype-struct`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl s = pl.Series([{"a": 1, "b": 2}]) s.cast(pl.Struct({"x": p..."*

#### 43. [Inconsistencies between `collect_schema()` and `collect()` with extension types](https://github.com/pola-rs/polars/issues/28542) (#28542)
- **URL:** https://github.com/pola-rs/polars/issues/28542
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ManuelF-Hexagon`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python from __future__ import annotations import polars as pl class IPv4(pl.BaseExten..."*

#### 44. [Polars expression context masks Python exceptions with keyword-only constructors](https://github.com/pola-rs/polars/issues/28535) (#28535)
- **URL:** https://github.com/pola-rs/polars/issues/28535
- **Relevance Score:** `11` | **State:** `open` | **Author:** `bcallender`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl class RequiresContext(Exception): def __init__(self, messa..."*

#### 45. [show_graph does not render row limiting functions when applied to the root lazyframe](https://github.com/pola-rs/polars/issues/28511) (#28511)
- **URL:** https://github.com/pola-rs/polars/issues/28511
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ohmdelta`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python >>> import polars as pl >>> pl.LazyFrame({"a": range(20)}).head(10).show_graph..."*

#### 46. [collect_schema returns type Unknown for Boolean * pl.lit(some_float)](https://github.com/pola-rs/polars/issues/28505) (#28505)
- **URL:** https://github.com/pola-rs/polars/issues/28505
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ph-ll-pp`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl lf = pl.LazyFrame({"bool": [True, False]}) result = lf.wit..."*

#### 47. [Arguments to show are ignored (except for limit)](https://github.com/pola-rs/polars/issues/28501) (#28501)
- **URL:** https://github.com/pola-rs/polars/issues/28501
- **Relevance Score:** `11` | **State:** `open` | **Author:** `memeplex`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import polars as pl test_df = pl.DataFrame(dict(a=[1.0, 2.0, 3.0])) test_df.sh..."*

#### 48. [replace_strict infers replacement value dtype from dictionary insertion order](https://github.com/pola-rs/polars/issues/28422) (#28422)
- **URL:** https://github.com/pola-rs/polars/issues/28422
- **Relevance Score:** `11` | **State:** `open` | **Author:** `rhug123`
- **Labels:** `bug`, `python`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python starting df df = pl.DataFrame( { "color": ["Green", "Red", "Yellow"], } ) ┌───..."*

#### 49. [`pl.DataFrame` fails on `datetime.datetime` in 3.15 Betas](https://github.com/pola-rs/polars/issues/28347) (#28347)
- **URL:** https://github.com/pola-rs/polars/issues/28347
- **Relevance Score:** `11` | **State:** `open` | **Author:** `sco1`
- **Labels:** `bug`, `python`, `A-temporal`, `accepted`, `P-high`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pypi.org/project/polars/) of Polars. ### Reproducible example ```python import datetime as dt import polars as pl df = pl.DataFrame( { "utc_timestamp"..."*

#### 50. [Improve PR Template](https://github.com/pola-rs/polars/issues/28534) (#28534)
- **URL:** https://github.com/pola-rs/polars/issues/28534
- **Relevance Score:** `5` | **State:** `open` | **Author:** `Kevin-Patyk`
- **Labels:** None
- **FS Keywords:** `parts`
- **Perf Keywords:** `io`
- **Excerpt:** *"Currently, the [PR template](https://github.com/pola-rs/polars/blob/main/.github/pull_request_template.md?plain=1) is a single HTML comment, and I think that it is often overlooked, skimmed, and/or deleted. Based on the AI policy, contribution guidelines, and the existing PR template, I suggest some..."*

### [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) (6 issues)

#### 51. [Optimize remote checkpoint loading with parallel multiprocess downloads and zero-copy mmap](https://github.com/Lightning-AI/pytorch-lightning/issues/21868) (#21868)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21868
- **Relevance Score:** `31` | **State:** `open` | **Author:** `yuxin00j`
- **Labels:** `feature`, `needs triage`
- **FS Keywords:** `filesystem`, `mmap`
- **Perf Keywords:** `bottleneck`, `cache`, `caching`, `concurrent`, `i/o`, `io`, `latency`, `oom`, `throughput`
- **Excerpt:** *"### Description & Motivation Currently, loading monolithic, multi-gigabyte checkpoints from remote object stores (such as Google Cloud Storage gs://) via _load() suffers from two significant bottlenecks: 1. Sequential Main-Thread Streaming I/O: Upstream Lightning streams remote checkpoints sequentia..."*

#### 52. [Unified storage_options support for FSDPStrategy, ModelParallelStrategy, and TorchCheckpointIO](https://github.com/Lightning-AI/pytorch-lightning/issues/21905) (#21905)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21905
- **Relevance Score:** `19` | **State:** `open` | **Author:** `Yonghui-Lee`
- **Labels:** `feature`, `needs triage`
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `caching`, `concurrent`, `i/o`, `io`, `performance`
- **Excerpt:** *"### Description & Motivation When saving and loading distributed checkpoints (e.g., via PyTorch Distributed Checkpoint / DCP with `FSDPStrategy` or `ModelParallelStrategy`), PyTorch allows configuring storage backend parameters such as: - `thread_count`: Number of concurrent I/O threads per rank to ..."*

#### 53. [Deprecation warnings in lightning.pytorch.cli with jsonargparse 4.49+](https://github.com/Lightning-AI/pytorch-lightning/issues/21900) (#21900)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21900
- **Relevance Score:** `11` | **State:** `open` | **Author:** `adamjstewart`
- **Labels:** `bug`, `needs triage`, `ver: 2.6.x`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `cache`, `hang`, `io`
- **Excerpt:** *"### Bug description `lightning/pytorch/cli.py` uses a few features from jsonargparse that have recently been deprecated. ### What version are you seeing the problem on? v2.6 ### Reproduced in studio _No response_ ### How to reproduce the bug ```python ``` ### Error messages and logs ``` /Users/Adam/..."*

#### 54. [Checkpoints silently fail to save due to swallowed PermissionError in `_atomic_save`](https://github.com/Lightning-AI/pytorch-lightning/issues/21800) (#21800)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21800
- **Relevance Score:** `11` | **State:** `open` | **Author:** `zhixiangli`
- **Labels:** `bug`, `checkpointing`, `ver: 2.6.x`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Bug description `_atomic_save` was silently swallowing non-cross-device PermissionErrors, causing saves to report success while failing to write any checkpoints. Because training continues as if the process were successful, this is a data-loss risk. ### What version are you seeing the problem on..."*

#### 55. [`ModelCheckpoint` deletes *previous run's* checkpoint when remote filesystem](https://github.com/Lightning-AI/pytorch-lightning/issues/21813) (#21813)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21813
- **Relevance Score:** `10` | **State:** `open` | **Author:** `parhamfh`
- **Labels:** `bug`, `callback: model checkpoint`, `ver: 2.6.x`
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"### Bug description `ModelCheckpoint` deletes the *previous run's* checkpoint, including the exact file the trainer resumed from, when the checkpoint dirpath is on a remote (fsspec) filesystem. Authored with the help of an agent but I detected the bug myself. I continued a training using `Trainer.fi..."*

#### 56. [Transformer Engine plugin fails to check weight exists for LayerNorm](https://github.com/Lightning-AI/pytorch-lightning/issues/21755) (#21755)
- **URL:** https://github.com/Lightning-AI/pytorch-lightning/issues/21755
- **Relevance Score:** `10` | **State:** `open` | **Author:** `HenryJia`
- **Labels:** `bug`, `ver: 2.6.x`
- **FS Keywords:** `fsspec`, `mmap`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"### Bug description At https://github.com/Lightning-AI/pytorch-lightning/blob/master/src/lightning/fabric/plugins/precision/transformer_engine.py#L173 There is no check that the weights of the LayerNorm layer are not None This means that if a LayerNorm layer is created using `elementwise_affine=Fals..."*

### [duckdb/duckdb](https://github.com/duckdb/duckdb) (5 issues)

#### 57. [Sustained inserts into a uniquely-indexed table degrade with table size; automatic checkpoints appear to re-serialize the whole ART index](https://github.com/duckdb/duckdb/issues/24848) (#24848)
- **URL:** https://github.com/duckdb/duckdb/issues/24848
- **Relevance Score:** `11` | **State:** `open` | **Author:** `skuirrels`
- **Labels:** None
- **FS Keywords:** `parts`
- **Perf Keywords:** `cache`, `io`, `oom`
- **Excerpt:** *"### What happens? Per-batch insert cost into a table with a unique index on a random-UUID column grows steadily as the table grows, independent of batch size. Profiling the per-batch timings shows two components: 1. A periodic spike whose cost grows **linearly with total table size** and whose caden..."*

#### 58. [Windows: WAL recovery after crash mid-checkpoint always fails with "Could not move file: Access is denied" (main WAL handle still open during recovery rename)](https://github.com/duckdb/duckdb/issues/24767) (#24767)
- **URL:** https://github.com/duckdb/duckdb/issues/24767
- **Relevance Score:** `11` | **State:** `open` | **Author:** `bryanliew-heptix`
- **Labels:** `needs triage`
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `concurrent`, `hang`, `io`
- **Excerpt:** *"### What happens? If the host crashes (power loss / hard reset) while a checkpoint is in progress, the database is left with both `<db>.wal` and `<db>.wal.checkpoint` on disk — a state DuckDB's recovery path is designed to handle. On **Windows**, however, that recovery deterministically fails on eve..."*

#### 59. [Sandboxing untrusted SQL forces a choice between fencing file access and out-of-core execution](https://github.com/duckdb/duckdb/issues/24695) (#24695)
- **URL:** https://github.com/duckdb/duckdb/issues/24695
- **Relevance Score:** `5` | **State:** `open` | **Author:** `rubenfiszel`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"### The problem When DuckDB is embedded and runs **untrusted SQL in-process**, there is no way to express: the engine may spill to disk, but queries may not otherwise touch the filesystem. `disabled_filesystems='LocalFileSystem'` is the natural fence, and it works well for user-facing file access. B..."*

#### 60. [FILE_FLAGS_EXCLUSIVE_CREATE is silently ignored on Windows](https://github.com/duckdb/duckdb/issues/24610) (#24610)
- **URL:** https://github.com/duckdb/duckdb/issues/24610
- **Relevance Score:** `5` | **State:** `open` | **Author:** `cmettler`
- **Labels:** `PR submitted`
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"### What happens? On Windows, LocalFileSystem::OpenFile never consults FileOpenFlags::ExclusiveCreate(). ExclusiveCreate() is read in exactly one place in the tree. The POSIX branch of the same function, where it becomes O_EXCL. CREATE_NEW, the Win32 disposition that fails with ERROR_FILE_EXISTS, ap..."*

#### 61. [current_timestamp not listed in duckdb_functions()](https://github.com/duckdb/duckdb/issues/24446) (#24446)
- **URL:** https://github.com/duckdb/duckdb/issues/24446
- **Relevance Score:** `5` | **State:** `open` | **Author:** `rpbouman`
- **Labels:** `PR submitted`
- **FS Keywords:** `parts`
- **Perf Keywords:** `io`
- **Excerpt:** *"### What happens? I just noticed current_timestamp appears not to have an entry in duckdb_functions(). It probably ought to be in there considering current_date is also in there. Also, I believe parts of the documentation are generated using info from duckdb_functions() so missing entries could affe..."*

### [huggingface/datasets](https://github.com/huggingface/datasets) (4 issues)

#### 62. ["eval_strategy": "no" perform evaluation](https://github.com/huggingface/datasets/issues/8242) (#8242)
- **URL:** https://github.com/huggingface/datasets/issues/8242
- **Relevance Score:** `23` | **State:** `open` | **Author:** `SamuelLarkin`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`, `mmap`, `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`, `performance`, `speed`
- **Excerpt:** *"### Describe the bug Hi, I'm trying to train a diffusion model and I getting stuck with ``` strace -p 967873 strace: Process 967873 attached ioctl(9, _IOC(_IOC_READ|_IOC_WRITE, 0x46, 0x2a, 0x20), 0x7fff18579d90) = 0 ioctl(9, _IOC(_IOC_READ|_IOC_WRITE, 0x46, 0x2a, 0x20), 0x7fff18579d90) = 0 ``` But m..."*

#### 63. [`Dataset.map(num_proc=N)` worker crashes with `ValueError: I/O operation on closed file` when `finalize()` is interrupted](https://github.com/huggingface/datasets/issues/8491) (#8491)
- **URL:** https://github.com/huggingface/datasets/issues/8491
- **Relevance Score:** `11` | **State:** `open` | **Author:** `HowardZorn`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `i/o`, `io`
- **Excerpt:** *"### Describe the bug We hit this while running Megatron-LM training through ms-swift, which uses `datasets` under the hood for preprocessing. Our preprocessing step calls `Dataset.map()` with a fairly aggressive `num_proc=512` on a ~25k-example JSONL file: ```bash swift --dataset_num_proc 512 --data..."*

#### 64. [Dataset Viewer fails on TSFile datasets](https://github.com/huggingface/datasets/issues/8256) (#8256)
- **URL:** https://github.com/huggingface/datasets/issues/8256
- **Relevance Score:** `8` | **State:** `open` | **Author:** `gengziyand`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"### Describe the bug ## Description The Dataset Viewer fails when trying to display a dataset stored in TSFile format. The error shown by the viewer is: ```python ModuleNotFoundError: No module named 'tsfile' ### Steps to reproduce the bug # Dataset Viewer fails to load TSFile dataset due to missing..."*

#### 65. [`PandasArrayExtensionDtype._metadata` should be a tuple, not a string](https://github.com/huggingface/datasets/issues/8375) (#8375)
- **URL:** https://github.com/huggingface/datasets/issues/8375
- **Relevance Score:** `5` | **State:** `open` | **Author:** `kohankhaki`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"### Describe the bug There's a small typo in `PandasArrayExtensionDtype` (`src/datasets/features/features.py`): ```python _metadata = "value_type" ``` Pandas expects `_metadata` to be a tuple of attribute names, like `("value_type",)`, not a plain string ([API documentation ref](https://pandas.pydat..."*

### [mlflow/mlflow](https://github.com/mlflow/mlflow) (7 issues)

#### 66. [[BUG] Silent loss of per-iteration logging in `GepaPromptOptimizer` when `valset` is passed via `gepa_kwargs`](https://github.com/mlflow/mlflow/issues/24461) (#24461)
- **URL:** https://github.com/mlflow/mlflow/issues/24461
- **Relevance Score:** `24` | **State:** `open` | **Author:** `sugoma11`
- **Labels:** `bug`, `has-closing-pr`, `area/evaluation`, `ready`
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `i/o`, `io`, `stall`, `stalled`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. ### Issues Policy a..."*

#### 67. [[BUG] Eager trace span loading causes UI crash and API timeout on large TRACKING_STORE traces](https://github.com/mlflow/mlflow/issues/24314) (#24314)
- **URL:** https://github.com/mlflow/mlflow/issues/24314
- **Relevance Score:** `20` | **State:** `open` | **Author:** `mprahl`
- **Labels:** `bug`, `area/uiux`, `area/tracking`, `has-closing-pr`, `area/tracing`, `ready`
- **FS Keywords:** `parts`
- **Perf Keywords:** `bottleneck`, `hang`, `i/o`, `io`, `slow`, `timeout`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. ### Issues Policy a..."*

#### 68. [[FR] Static (fixed message) Multi-turn DSL and Conversation Simulation support](https://github.com/mlflow/mlflow/issues/24453) (#24453)
- **URL:** https://github.com/mlflow/mlflow/issues/24453
- **Relevance Score:** `15` | **State:** `open` | **Author:** `ajjajjajjajjajj`
- **Labels:** `enhancement`, `area/evaluation`, `domain/genai`
- **FS Keywords:** `parts`
- **Perf Keywords:** `io`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. ### Willingness to ..."*

#### 69. [[BUG] A single unparseable filename in images/ silently discards every logged image for that run](https://github.com/mlflow/mlflow/issues/24789) (#24789)
- **URL:** https://github.com/mlflow/mlflow/issues/24789
- **Relevance Score:** `8` | **State:** `open` | **Author:** `sirzzang`
- **Labels:** `Acknowledged`
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. ### MLflow version ..."*

#### 70. [[BUG] AI Gateway passthrough forwards the client Authorization header, shadowing the Vertex AI OAuth Bearer (401)](https://github.com/mlflow/mlflow/issues/25108) (#25108)
- **URL:** https://github.com/mlflow/mlflow/issues/25108
- **Relevance Score:** `5` | **State:** `open` | **Author:** `Nantina`
- **Labels:** `bug`, `has-closing-pr`, `ready`, `area/gateway`
- **FS Keywords:** `parts`
- **Perf Keywords:** `io`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. ### Issues Policy a..."*

#### 71. [[FR] Support Hugging Face Storage Buckets as an artifact store](https://github.com/mlflow/mlflow/issues/24848) (#24848)
- **URL:** https://github.com/mlflow/mlflow/issues/24848
- **Relevance Score:** `5` | **State:** `open` | **Author:** `abidlabs`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. MLflow already supp..."*

#### 72. [[BUG] Adding a trace with array-shaped inputs (OTel GenAI convention) to an evaluation dataset fails with a 500 INTERNAL_ERROR](https://github.com/mlflow/mlflow/issues/24709) (#24709)
- **URL:** https://github.com/mlflow/mlflow/issues/24709
- **Relevance Score:** `5` | **State:** `open` | **Author:** `sebnow`
- **Labels:** None
- **FS Keywords:** `parts`
- **Perf Keywords:** `io`
- **Excerpt:** *"<!-- issue-warning --> > [!WARNING] > Before submitting a PR, please make sure that: > - A maintainer has triaged this issue and applied the `ready` label > - This issue has no assignee > - No duplicate PR exists > > PRs not meeting these requirements may be automatically closed. ### Issues Policy a..."*

### [apache/arrow](https://github.com/apache/arrow) (7 issues)

#### 73. [[C++][Python] Significant performance degradation after pyarrow 24.0.0 to 25.0.0 upgrade](https://github.com/apache/arrow/issues/50667) (#50667)
- **URL:** https://github.com/apache/arrow/issues/50667
- **Relevance Score:** `21` | **State:** `open` | **Author:** `ghaarsma`
- **Labels:** `Type: bug`, `Component: C++`, `Component: Python`
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `s3filesystem`
- **Perf Keywords:** `caching`, `hang`, `io`, `performance`, `stall`
- **Excerpt:** *"### Describe the bug, including details regarding any error messages, version, and platform. In our application we implement a local TimeSeries caching implementation that stores TimeSeries data into Parquet files. We heavily read/write parquet files via the pandas to_parquet(engine="pyarrow") and r..."*

#### 74. [[Python] Bindings for GcsFileSystem FromServiceAccountCredentials](https://github.com/apache/arrow/issues/50888) (#50888)
- **URL:** https://github.com/apache/arrow/issues/50888
- **Relevance Score:** `16` | **State:** `open` | **Author:** `hampsterx`
- **Labels:** None
- **FS Keywords:** `filesystem`, `gcsfilesystem`, `gcsfs`, `pyarrow.fs`, `s3fs`
- **Perf Keywords:** `io`, `latency`
- **Excerpt:** *"### Describe the enhancement requested `GcsOptions::FromServiceAccountCredentials` (`cpp/src/arrow/filesystem/gcsfs.h:146`) is the one credential factory on `GcsOptions` with no Python binding, so a caller holding [aip/4112] service-account JSON has no way to construct a `GcsFileSystem` from it. `py..."*

#### 75. [[C++][Compute] unique, value_counts and dictionary_encode have no kernel for float16 (halffloat)](https://github.com/apache/arrow/issues/50512) (#50512)
- **URL:** https://github.com/apache/arrow/issues/50512
- **Relevance Score:** `11` | **State:** `open` | **Author:** `fornwall`
- **Labels:** `Type: enhancement`, `Component: C++`
- **FS Keywords:** `parts`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Describe the enhancement requested The hash-based vector functions do not support `halffloat` input, while supporting all other numeric types: ```python >>> import pyarrow as pa >>> pa.array([1.5, 2.5], type=pa.float16()).dictionary_encode() ArrowNotImplementedError: Function 'dictionary_encode'..."*

#### 76. [[C++] deprecated-declarations warnings in bundled google-cloud-cpp](https://github.com/apache/arrow/issues/50868) (#50868)
- **URL:** https://github.com/apache/arrow/issues/50868
- **Relevance Score:** `10` | **State:** `open` | **Author:** `kou`
- **Labels:** `Type: bug`, `Component: C++`
- **FS Keywords:** `filesystem`, `gcsfs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"### Describe the bug, including details regarding any error messages, version, and platform. ARM64 macOS GLib & Ruby https://github.com/apache/arrow/actions/runs/31872547761/job/94983313575?pr=50799 : ```text [382/662] Building CXX object src/arrow/CMakeFiles/arrow_filesystem.dir/filesystem/gcsfs.cc..."*

#### 77. [[Python] s3fs selector count is not asserted](https://github.com/apache/arrow/issues/50665) (#50665)
- **URL:** https://github.com/apache/arrow/issues/50665
- **Relevance Score:** `9` | **State:** `open` | **Author:** `anxkhn`
- **Labels:** `Component: Python`
- **FS Keywords:** `filesystem`, `fsspec`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"### Describe the bug, including details regarding any error messages, version, and platform. `test_get_file_info_with_selector` in `python/pyarrow/tests/test_fs.py` evaluates `len(infos) == 4` without asserting it for recursive listings through the fsspec S3 backend. The comparison result is discard..."*

#### 78. [[Python] Debian job on i386 segfaults when running Python tests](https://github.com/apache/arrow/issues/50599) (#50599)
- **URL:** https://github.com/apache/arrow/issues/50599
- **Relevance Score:** `8` | **State:** `open` | **Author:** `raulcd`
- **Labels:** `Type: bug`, `Component: Python`
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"### Describe the bug, including details regarding any error messages, version, and platform. The [test-debian-13-python-3-i386](https://github.com/ursacomputing/crossbow/actions/runs/29889191727/job/88826043097) nightly job is segfaulting with the following error when running tests: ``` + pytest -r ..."*

#### 79. [[C++][FS][Azure] Azurite tests can race service startup](https://github.com/apache/arrow/issues/50876) (#50876)
- **URL:** https://github.com/apache/arrow/issues/50876
- **Relevance Score:** `5` | **State:** `open` | **Author:** `booxter`
- **Labels:** `Component: C++`
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"`AzuriteEnv::Make()` returns immediately after spawning Azurite, without waiting for the Blob service to become ready. The first test setup request can therefore fail with: Fail to get a new connection for: http://127.0.0.1:10000. Could not connect to server Observed with Arrow 23.0.0 on aarch64 mac..."*

### [iterative/dvc](https://github.com/iterative/dvc) (28 issues)

#### 80. [import: hangs when pulling many files from GCS remote and one fails](https://github.com/treeverse/dvc/issues/10417) (#10417)
- **URL:** https://github.com/treeverse/dvc/issues/10417
- **Relevance Score:** `38` | **State:** `open` | **Author:** `dluks`
- **Labels:** `performance`, `A: data-sync`
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `benchmark`, `cache`, `concurrent`, `hang`, `hanging`, `io`, `performance`, `timeout`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> ## import/pull: hangs when pullin..."*

#### 81. [dvc stage: params section with variable](https://github.com/treeverse/dvc/issues/10528) (#10528)
- **URL:** https://github.com/treeverse/dvc/issues/10528
- **Relevance Score:** `27` | **State:** `open` | **Author:** `ermolaev94`
- **Labels:** `question`, `A: pipelines`
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `benchmark`, `cache`, `hang`, `io`, `performance`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> ## Description I have the followi..."*

#### 82. [Incomplete copy of repo in cloud versioning after dvc push](https://github.com/treeverse/dvc/issues/10747) (#10747)
- **URL:** https://github.com/treeverse/dvc/issues/10747
- **Relevance Score:** `25` | **State:** `open` | **Author:** `chris-rapson-formus`
- **Labels:** `cloud-versioning`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`
- **Excerpt:** *"# Bug Report dvc push: when using google cloud storage with cloud versioning enabled, some files are missing after pushing, despite no error messages being shown. The files are present on my local system, and both `dvc status` and `git status` show that everything is updated and committed. ## Descri..."*

#### 83. [dvc pull crashing on a FSx Lustre file system](https://github.com/treeverse/dvc/issues/10502) (#10502)
- **URL:** https://github.com/treeverse/dvc/issues/10502
- **Relevance Score:** `25` | **State:** `open` | **Author:** `rrazavipour`
- **Labels:** `triage`, `A: data-sync`
- **FS Keywords:** `filesystem`, `s3fs`
- **Perf Keywords:** `benchmark`, `cache`, `hang`, `i/o`, `io`, `performance`, `timeout`
- **Excerpt:** *"# Bug Report dvc pull <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> ## Description dvc pull ..."*

#### 84. [dvc push hangs silently](https://github.com/treeverse/dvc/issues/10483) (#10483)
- **URL:** https://github.com/treeverse/dvc/issues/10483
- **Relevance Score:** `22` | **State:** `open` | **Author:** `davies-w`
- **Labels:** `triage`, `fs: s3`, `A: data-sync`
- **FS Keywords:** `fsspec`, `s3fs`
- **Perf Keywords:** `benchmark`, `cache`, `hang`, `io`, `performance`, `timeout`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> dvc pull hangs silently ## Descri..."*

#### 85. [`dvc repro`: dvc.lock records dependency hashes from after cmd finishes, allowing the recorded code↔output linkage to be falsified](https://github.com/treeverse/dvc/issues/11058) (#11058)
- **URL:** https://github.com/treeverse/dvc/issues/11058
- **Relevance Score:** `21` | **State:** `open` | **Author:** `TimOliverMaier`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"# Bug Report ## Description Hello, I discovered today that with `dvc repro` of a pipeline the hash sums of a stage's dependency are calculated and stored after execution. Which lets DVC record a false code <-> output linkage, if a dependency is changed mid-run. ### Reproduce In a DVC repository plac..."*

#### 86. [DVC do not cache output of pipeline properly](https://github.com/treeverse/dvc/issues/10549) (#10549)
- **URL:** https://github.com/treeverse/dvc/issues/10549
- **Relevance Score:** `21` | **State:** `open` | **Author:** `imyhxy`
- **Labels:** `optimize`, `A: pipelines`, `A: data-management`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `benchmark`, `cache`, `hang`, `io`, `performance`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> repro: doesn't cache output prope..."*

#### 87. [pull: stale data when converted from "imported" to pipeline-local file](https://github.com/treeverse/dvc/issues/10457) (#10457)
- **URL:** https://github.com/treeverse/dvc/issues/10457
- **Relevance Score:** `21` | **State:** `open` | **Author:** `bakaleks`
- **Labels:** `bug`, `p3-nice-to-have`, `triage`, `A: data-sync`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `benchmark`, `cache`, `hang`, `io`, `performance`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> ## Description Imagine scenario w..."*

#### 88. [Add `multipart_chunksize` / `multipart_threshold` to the `s3` remote config schema](https://github.com/treeverse/dvc/issues/11034) (#11034)
- **URL:** https://github.com/treeverse/dvc/issues/11034
- **Relevance Score:** `17` | **State:** `open` | **Author:** `Chouffe`
- **Labels:** None
- **FS Keywords:** `parts`
- **Perf Keywords:** `chunk_size`, `concurrent`, `hang`, `io`, `timeout`
- **Excerpt:** *"## Problem `dvc-s3` already maps `multipart_chunksize` and `multipart_threshold` into boto3's `TransferConfig` via `_TRANSFER_CONFIG_ALIASES` (see [`dvc_s3/__init__.py` lines 59–60, 117](https://github.com/iterative/dvc-s3/blob/main/dvc_s3/__init__.py)), but `dvc/config_schema.py`'s `s3` block (line..."*

#### 89. [dvc pull cannot be stopped by Ctrl+C (at least on Windows)](https://github.com/treeverse/dvc/issues/10658) (#10658)
- **URL:** https://github.com/treeverse/dvc/issues/10658
- **Relevance Score:** `17` | **State:** `open` | **Author:** `a18`
- **Labels:** `triage`, `P: windows`, `A: data-sync`
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `benchmark`, `cache`, `hang`, `io`, `performance`
- **Excerpt:** *"# Bug Report pull: cannot be stopped by Ctrl+C <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` -->..."*

#### 90. [dvc exp run --run-all: One or two experiments are executed, than it hangs (JSONDecodeError) (similar to #10398)](https://github.com/treeverse/dvc/issues/10428) (#10428)
- **URL:** https://github.com/treeverse/dvc/issues/10428
- **Relevance Score:** `16` | **State:** `open` | **Author:** `AljoSt`
- **Labels:** `A: experiments`
- **FS Keywords:** `filesystem`, `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`, `timeout`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> ## Description When executing `dv..."*

#### 91. [config: allow filesystem plugins to declare their own remote config schema via entry points](https://github.com/treeverse/dvc/issues/10993) (#10993)
- **URL:** https://github.com/treeverse/dvc/issues/10993
- **Relevance Score:** `14` | **State:** `open` | **Author:** `adamlabadorf`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"## Problem Third-party DVC filesystem plugins (installed via the `dvc.fs` entry point group) cannot be used as DVC remotes without modifying DVC core. The config validator in `dvc/config_schema.py` maintains a hardcoded list of URL schemes in `REMOTE_SCHEMAS`, so any plugin with a custom scheme gets..."*

#### 92. [repro:  --pull option stopped working since last Friday](https://github.com/treeverse/dvc/issues/10991) (#10991)
- **URL:** https://github.com/treeverse/dvc/issues/10991
- **Relevance Score:** `14` | **State:** `open` | **Author:** `eng-ts`
- **Labels:** None
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `benchmark`, `cache`, `io`, `performance`
- **Excerpt:** *"# Bug Report ## Description the `--pull` option is not working anymore since Friday. We observed on several project, when data are not present and must be downloaded (fresh remote instances). We got this message: `ERROR: failed to reproduce '[...].parquet.dvc': missing data 'source': [...]` Solution..."*

#### 93. [`dvc run exp --queue` gives unclear error without committed pipeline files](https://github.com/treeverse/dvc/issues/10697) (#10697)
- **URL:** https://github.com/treeverse/dvc/issues/10697
- **Relevance Score:** `14` | **State:** `open` | **Author:** `pwithams`
- **Labels:** None
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`, `slow`
- **Excerpt:** *"# Bug Report ## `dvc exp run --queue`: fails with "No such file or directory" on a cache path similar to .dvc/tmp/exps ## Description 1. It appears that `dvc exp run --queue` only works on DVC pipelines that have been previously committed to git 2. The error from this is not clear When running a que..."*

#### 94. [`dvc pull`: git credentials consumed and stripped from git credential-helper makes clone of `import`ed data impossibe](https://github.com/treeverse/dvc/issues/10999) (#10999)
- **URL:** https://github.com/treeverse/dvc/issues/10999
- **Relevance Score:** `11` | **State:** `open` | **Author:** `vigarov`
- **Labels:** None
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`
- **Excerpt:** *"# Bug Report ## Description When using git credential helpers similarly to as suggested [here](https://github.com/treeverse/dvc/issues/8068#issuecomment-1243783489), `dvc pull` does not manage to clone a repository that needs such credentials, and strips the cached credentials. My use case is automa..."*

#### 95. [dvc experiment queue error: output does not exist](https://github.com/treeverse/dvc/issues/10654) (#10654)
- **URL:** https://github.com/treeverse/dvc/issues/10654
- **Relevance Score:** `11` | **State:** `open` | **Author:** `OS-leonardopratesi`
- **Labels:** `awaiting response`, `triage`
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> ## Description <!-- A clear and c..."*

#### 96. [DVC post-checkout hook: complains about unsaved files (which have not changed)](https://github.com/treeverse/dvc/issues/10584) (#10584)
- **URL:** https://github.com/treeverse/dvc/issues/10584
- **Relevance Score:** `11` | **State:** `open` | **Author:** `JulianoLagana`
- **Labels:** `triage`
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> ## Description DVC post-checkout ..."*

#### 97. [dvc push not updating Push %](https://github.com/treeverse/dvc/issues/10556) (#10556)
- **URL:** https://github.com/treeverse/dvc/issues/10556
- **Relevance Score:** `11` | **State:** `open` | **Author:** `danshome`
- **Labels:** `p2-medium`, `ui`, `triage`, `A: data-sync`
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`
- **Excerpt:** *"# Bug Report ## Issue name dvc push -v -j 4: Doesn't update Pushing %, B/s transferred, or transfer times. ## Description When I run dvc push to an S3 bucket the % always reports 0%. I think it's pushing because I can see my outbound network traffic spike, but the percentage never changes. dvc push ..."*

#### 98. [dvc pull/fetch: corrupted cache with GDrive](https://github.com/treeverse/dvc/issues/10525) (#10525)
- **URL:** https://github.com/treeverse/dvc/issues/10525
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ermolaev94`
- **Labels:** `A: data-sync`
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`
- **Excerpt:** *"# Bug Report <!-- ## Issue name Issue names must follow the pattern `command: description` where the command is the dvc command that you are trying to run. The description should describe the consequence of the bug. Example: `repro: doesn't detect input changes` --> ## Description <!-- A clear and c..."*

#### 99. [Feature Request: Add support for Rclone as a remote storage backend](https://github.com/treeverse/dvc/issues/10878) (#10878)
- **URL:** https://github.com/treeverse/dvc/issues/10878
- **Relevance Score:** `10` | **State:** `open` | **Author:** `liblaf`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`, `performance`
- **Excerpt:** *"### Summary This is a feature request to add support for [Rclone](https://rclone.org/) as a remote storage backend in DVC. Rclone is a powerful command-line program to manage files on over 70 cloud storage providers. Integrating Rclone would vastly expand the number of supported storage backends for..."*

#### 100. [DVC Pull is not working with EFS and it is taking around 2 hours for 2.3GB files](https://github.com/treeverse/dvc/issues/10680) (#10680)
- **URL:** https://github.com/treeverse/dvc/issues/10680
- **Relevance Score:** `9` | **State:** `open` | **Author:** `shmubara`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"dvc pull is taking around 2 hours to pull 2.3 GB file amazon s3 when using EFS based PVC in the pods. dvc doctor DVC version: 3.59.0 (deb) ------------------------- Platform: Python 3.12.7 on Linux-5.10.225-213.878.amzn2.x86_64-x86_64-with-glibc2.36 Subprojects: Supports: azure (adlfs = 2024.12.0, k..."*

#### 101. [pull: KeyError crash (or silently skipped target) when mixing .dvc-file targets with granular paths inside a tracked directory](https://github.com/treeverse/dvc/issues/11075) (#11075)
- **URL:** https://github.com/treeverse/dvc/issues/11075
- **Relevance Score:** `8` | **State:** `open` | **Author:** `sfgartland`
- **Labels:** None
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"# Bug Report ## Description `dvc pull` with a target list that mixes a **`.dvc`-file target** with **granular paths inside a tracked directory** misbehaves in two ways, depending on workspace state: 1. **Crash:** if the tracked directory contains any untracked (drifted) file, pull dies with `ERROR: ..."*

#### 102. [`dvc exp show -A` does not show all experiments](https://github.com/treeverse/dvc/issues/10707) (#10707)
- **URL:** https://github.com/treeverse/dvc/issues/10707
- **Relevance Score:** `8` | **State:** `open` | **Author:** `kblissett`
- **Labels:** `A: experiments`
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"# Bug Report ## exp show: doesn't show all experiments. ## Description I have a slightly non-conventional git workflow that involves frequent rebasing and re-writing of history. I have found during this workflow that experiments can be lost from the `dvc exp show -A` view though they can still be in..."*

#### 103. [DVCFileSystem: inconsistent behavior of DVCFileSystem](https://github.com/treeverse/dvc/issues/10647) (#10647)
- **URL:** https://github.com/treeverse/dvc/issues/10647
- **Relevance Score:** `8` | **State:** `open` | **Author:** `adamliter`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"# Bug Report ## Description `DVCFileSystem` exhibits some inconsistent behavior (I think, based on my understanding of the documentation), and I'm not sure what the intended behavior is. In particular, `DVCFileSystem`'s `get_file` raises an error with `rpath=lpath` and `rev=None` from a non-default ..."*

#### 104. [dvc metrics diff --all: on same branch is empty](https://github.com/treeverse/dvc/issues/10429) (#10429)
- **URL:** https://github.com/treeverse/dvc/issues/10429
- **Relevance Score:** `8` | **State:** `open` | **Author:** `MaximilianTunk`
- **Labels:** `bug`, `p3-nice-to-have`
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `cache`, `io`
- **Excerpt:** *"# Bug Report ## Description Hello, we found that `dvc metrics diff --all`outputs nothing, if `a_rev`and `b_rev` refer to the same git commit. No matter if they are exactly the same or different types of references (HEAD vs branch_name, etc.) ### Reproduce * setup any dvc stage with metrics. * run `d..."*

#### 105. [`dvc.api.get_url()` throws error when working directory is a subdirectory of repo path](https://github.com/treeverse/dvc/issues/11029) (#11029)
- **URL:** https://github.com/treeverse/dvc/issues/11029
- **Relevance Score:** `5` | **State:** `open` | **Author:** `rgoya`
- **Labels:** None
- **FS Keywords:** `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"# Bug Report ## Description `dvc.api.get_url()` throws an error when the current working path is a subdirectory inside the dvc repository. ### Reproduce ```bash cat > setup.sh << EOF mkdir -p test_repo cd test_repo dvc init --no-scm mkdir -p /tmp/dvc_remote/ dvc remote add -d storage_name /tmp/dvc_r..."*

#### 106. [Security issue with pickle.load - dvc 3.67.1](https://github.com/treeverse/dvc/issues/11022) (#11022)
- **URL:** https://github.com/treeverse/dvc/issues/11022
- **Relevance Score:** `5` | **State:** `open` | **Author:** `Mounira-RM`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hello! My CICD on Github blocks because of a security issue related to dvc 3.67.1 using pickle.load. I din't have this issue in the version 3.66.1. This is the report: Potential security risk (AI signal): pypi dvc is 68.0% likely risky Notes: The fragment contains a major security risk: it uses pick..."*

#### 107. [Proposal: Docs/example on RAG pipeline failure modes and versioning, using WFGY ProblemMap](https://github.com/treeverse/dvc/issues/10996) (#10996)
- **URL:** https://github.com/treeverse/dvc/issues/10996
- **Relevance Score:** `5` | **State:** `open` | **Author:** `onestardao`
- **Labels:** None
- **FS Keywords:** `mmap`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, and thanks for DVC – versioning data and models properly has been essential for many teams I talk to. I maintain an open-source project called **WFGY** (MIT-licensed, ~1.5k GitHub stars). We publish a **16-problem “ProblemMap”** that focuses on typical **RAG / LLM pipeline failure modes**, inclu..."*

### [dask/dask](https://github.com/dask/dask) (2 issues)

#### 108. [Significant slowdown in loading remote xarray dataset since 2025.5.0](https://github.com/dask/dask/issues/12060) (#12060)
- **URL:** https://github.com/dask/dask/issues/12060
- **Relevance Score:** `24` | **State:** `open` | **Author:** `Metamess`
- **Labels:** `needs attention`, `needs triage`
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `i/o`, `io`, `slow`, `stall`
- **Excerpt:** *"**Describe the issue**: Calling `.load()` or `.compute()` on an xarray dataset created by concatenating and slicing zarr datasets from a cloud bucket has seen a severe (factor ~50) slowdown between dask 2025.4.1 and 2025.5.0. I have not been able to replicate this slowdown with zarrs stored locally,..."*

#### 109. ['cumsum' results differ from 'cumsum' on a pure numpy array](https://github.com/dask/dask/issues/12359) (#12359)
- **URL:** https://github.com/dask/dask/issues/12359
- **Relevance Score:** `21` | **State:** `open` | **Author:** `muttener`
- **Labels:** `array`, `needs attention`, `bug`
- **FS Keywords:** `mmap`
- **Perf Keywords:** `chunk_size`, `io`, `stall`
- **Excerpt:** *"<!-- Please include a self-contained copy-pastable example that generates the issue if possible. Please be concise with code posted. See guidelines below on how to provide a good bug report: - Craft Minimal Bug Reports http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports - Minimal Comp..."*

### [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) (3 issues)

#### 110. [[ISSUE] Backends using TupleFilesystemStoreBackend constantly request new Azure credentials](https://github.com/fivetran/great_expectations/issues/10896) (#10896)
- **URL:** https://github.com/fivetran/great_expectations/issues/10896
- **Relevance Score:** `11` | **State:** `open` | **Author:** `jschra`
- **Labels:** `feature-request`
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `cache`, `io`, `performance`
- **Excerpt:** *"**Is your feature request related to a problem? Please describe.** We are using GX Core with our backends configured to an Azure Storage Account over multiple containers for each of the stores. Whenever we run our validation jobs, the logs show that connections with our backend are reinitialised con..."*

#### 111. [recursive_file_lookup doesn't read files from subdirectories when set to True in add_parquet_asset](https://github.com/fivetran/great_expectations/issues/11017) (#11017)
- **URL:** https://github.com/fivetran/great_expectations/issues/11017
- **Relevance Score:** `5` | **State:** `open` | **Author:** `jagpsz`
- **Labels:** None
- **FS Keywords:** `parts`
- **Perf Keywords:** `io`
- **Excerpt:** *"**Describe the bug** I would like to read all parquet files from subdirectories from s3. I am doing that in databricks. My data is partitioned by yyyy, mm, dd, hh but I want to validate the whole day at once. `recursive_file_lookup` doesn't seem to work as expected, I get `TestConnectionError: No fi..."*

#### 112. [Why is `validation_definition_store_name` not part of the `great_expectations.yaml` spec?](https://github.com/fivetran/great_expectations/issues/10958) (#10958)
- **URL:** https://github.com/fivetran/great_expectations/issues/10958
- **Relevance Score:** `5` | **State:** `open` | **Author:** `CrossNox`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"I'm trying to set up GX in such a way that I can use a single `yaml` to run both `production` and `development` environments. On `config_variables` I have `env` for this purpose. Then, e.g. `expectations_store_name` could be `${env}_expectations_store`, with `dev_expectations_store` and `prd_expecta..."*

### [modin-project/modin](https://github.com/modin-project/modin) (39 issues)

#### 113. [Low Physical Core Utilization](https://github.com/modin-project/modin/issues/7403) (#7403)
- **URL:** https://github.com/modin-project/modin/issues/7403
- **Relevance Score:** `40` | **State:** `open` | **Author:** `azhuvath`
- **Labels:** `question ❓`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `concurrent`, `hang`, `hanging`, `io`, `performance`, `stall`, `stalled`
- **Excerpt:** *"We are optimizing a pandas pipeline which process 300 million records on a Intel Xeon machine with 2 sockets and each socket having 32 physical cores. The cores are hyper threaded and hence the system has an overall logical cores of 128 (2*32*2). The physical core utilization while executing the wor..."*

#### 114. [BUG: Series.compare with differently named series raises ValueError, but should not](https://github.com/modin-project/modin/issues/7334) (#7334)
- **URL:** https://github.com/modin-project/modin/issues/7334
- **Relevance Score:** `34` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`, `P2`, `Interfaces and abstractions`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`, `timeout`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 115. [BUG: QueryCompilerCaster breaks NamedTuple arguments](https://github.com/modin-project/modin/issues/7594) (#7594)
- **URL:** https://github.com/modin-project/modin/issues/7594
- **Relevance Score:** `28` | **State:** `open` | **Author:** `sfc-gh-joshi`
- **Labels:** `bug 🦗`, `P1`, `hybrid-execution`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 116. [BUG: jupyter loading of serialized modin objects from ray tasks converts to pandas objects](https://github.com/modin-project/modin/issues/7408) (#7408)
- **URL:** https://github.com/modin-project/modin/issues/7408
- **Relevance Score:** `27` | **State:** `open` | **Author:** `eyadgaran`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `hanging`, `io`, `oom`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 117. [BUG: can't handle `df.groupby('a').agg(c=('b', 'mean'), d=('b', 'mean'))`](https://github.com/modin-project/modin/issues/7414) (#7414)
- **URL:** https://github.com/modin-project/modin/issues/7414
- **Relevance Score:** `26` | **State:** `open` | **Author:** `MarcoGorelli`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `parts`, `s3fs`
- **Perf Keywords:** `benchmark`, `block_size`, `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 118. [Possible issue with `dropna(how="all")` not deleting data from partition on ray.](https://github.com/modin-project/modin/issues/7350) (#7350)
- **URL:** https://github.com/modin-project/modin/issues/7350
- **Relevance Score:** `24` | **State:** `open` | **Author:** `brunojensen`
- **Labels:** `bug 🦗`, `P0`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`, `timeout`
- **Excerpt:** *"When processing a large dataframe with modin running on ray, if I had previously dropped invalid rows, it runs into an issue by accessing data from the new dataframe (after dropna). It looks like the data is not released from ray, or maybe modin `dropna` operation is not removing it properly. It wor..."*

#### 119. [BUG: groupby().apply() raise numpy ValueError when Series has multi index](https://github.com/modin-project/modin/issues/7344) (#7344)
- **URL:** https://github.com/modin-project/modin/issues/7344
- **Relevance Score:** `24` | **State:** `open` | **Author:** `Pekton`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`, `timeout`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 120. [BUG: SeriesGroupBy.apply applies function to pandas DataFrame instead of to pandas Series](https://github.com/modin-project/modin/issues/7096) (#7096)
- **URL:** https://github.com/modin-project/modin/issues/7096
- **Relevance Score:** `24` | **State:** `open` | **Author:** `mvashishtha`
- **Labels:** `bug 🦗`, `P2`, `pandas.groupby`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`, `timeout`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 121. [BUG: setting some config variables to invalid values makes them permanently unwriteable and unreadable](https://github.com/modin-project/modin/issues/7454) (#7454)
- **URL:** https://github.com/modin-project/modin/issues/7454
- **Relevance Score:** `23` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`, `P2`
- **FS Keywords:** `fsspec`, `gcsfs`, `parts`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 122. [BUG: df[col].replace(dict, inplace=True) is brutally slow, while .apply which does the same is blazing fast](https://github.com/modin-project/modin/issues/7377) (#7377)
- **URL:** https://github.com/modin-project/modin/issues/7377
- **Relevance Score:** `23` | **State:** `open` | **Author:** `Liquidmasl`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `parts`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `slow`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [ ] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 123. [BUG: `Resample.mean()` raises error on pandas 2.3.3 with native execution](https://github.com/modin-project/modin/issues/7697) (#7697)
- **URL:** https://github.com/modin-project/modin/issues/7697
- **Relevance Score:** `21` | **State:** `open` | **Author:** `sfc-gh-joshi`
- **Labels:** `bug 🦗`, `P3`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 124. [BUG: 'nrows' parameter do not seem to be honoured in read_excel()](https://github.com/modin-project/modin/issues/7651) (#7651)
- **URL:** https://github.com/modin-project/modin/issues/7651
- **Relevance Score:** `21` | **State:** `open` | **Author:** `deathstalkr`
- **Labels:** `bug 🦗`, `pandas concordance 🐼`, `P2`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 125. [BUG: SeriesGroupBy.diff() raises TypeError for datetime64[ns] column with Pandas backend](https://github.com/modin-project/modin/issues/7631) (#7631)
- **URL:** https://github.com/modin-project/modin/issues/7631
- **Relevance Score:** `21` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `i/o`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 126. [BUG: Creating empty unidist dataframes in benchmarkmode makes Modin get stuck](https://github.com/modin-project/modin/issues/7516) (#7516)
- **URL:** https://github.com/modin-project/modin/issues/7516
- **Relevance Score:** `21` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `benchmark`, `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 127. [BUG: engine_kwargs do not seem to be honoured in read_excel()](https://github.com/modin-project/modin/issues/7450) (#7450)
- **URL:** https://github.com/modin-project/modin/issues/7450
- **Relevance Score:** `21` | **State:** `open` | **Author:** `whoward`
- **Labels:** `bug 🦗`, `pandas concordance 🐼`, `P2`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 128. [BUG: Pass Groupby kwargs to panads grouper](https://github.com/modin-project/modin/issues/7412) (#7412)
- **URL:** https://github.com/modin-project/modin/issues/7412
- **Relevance Score:** `21` | **State:** `open` | **Author:** `Servinjesus1`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. ### Reproducible Example ```python import modin.pandas as pd import numpy as np import warnings warnings.filterwarnings("error"..."*

#### 129. [BUG: Modin with Ray not scaling across multiple CPUs](https://github.com/modin-project/modin/issues/7411) (#7411)
- **URL:** https://github.com/modin-project/modin/issues/7411
- **Relevance Score:** `21` | **State:** `open` | **Author:** `simone-macri`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `performance`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 130. [BUG: extra row gets inserted when using `.iloc` on Series](https://github.com/modin-project/modin/issues/7392) (#7392)
- **URL:** https://github.com/modin-project/modin/issues/7392
- **Relevance Score:** `21` | **State:** `open` | **Author:** `MarcoGorelli`
- **Labels:** `bug 🦗`, `pandas concordance 🐼`, `P3`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 131. [BUG: `groupby().agg(<constant>)` lead to inconsistencies with Pandas](https://github.com/modin-project/modin/issues/7694) (#7694)
- **URL:** https://github.com/modin-project/modin/issues/7694
- **Relevance Score:** `18` | **State:** `open` | **Author:** `asddfl`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 132. [BUG:  `groupby()` and `max()` lead to inconsistencies with Pandas](https://github.com/modin-project/modin/issues/7693) (#7693)
- **URL:** https://github.com/modin-project/modin/issues/7693
- **Relevance Score:** `18` | **State:** `open` | **Author:** `asddfl`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 133. [BUG: Expressions combining `.loc[]` and `.fillna()` causes inconsistencies with Pandas](https://github.com/modin-project/modin/issues/7692) (#7692)
- **URL:** https://github.com/modin-project/modin/issues/7692
- **Relevance Score:** `18` | **State:** `open` | **Author:** `asddfl`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 134. [BUG: Data types reading from csv file differ from those of Pandas](https://github.com/modin-project/modin/issues/7690) (#7690)
- **URL:** https://github.com/modin-project/modin/issues/7690
- **Relevance Score:** `18` | **State:** `open` | **Author:** `asddfl`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 135. [BUG: series with tuple name has a column multiindex in internal pandas frame](https://github.com/modin-project/modin/issues/7689) (#7689)
- **URL:** https://github.com/modin-project/modin/issues/7689
- **Relevance Score:** `18` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 136. [BUG: modin.pandas.eval() does not work at all](https://github.com/modin-project/modin/issues/7656) (#7656)
- **URL:** https://github.com/modin-project/modin/issues/7656
- **Relevance Score:** `18` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`, `P2`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 137. [BUG: combine_first casts dtypes, pandas does not](https://github.com/modin-project/modin/issues/7642) (#7642)
- **URL:** https://github.com/modin-project/modin/issues/7642
- **Relevance Score:** `18` | **State:** `open` | **Author:** `Liquidmasl`
- **Labels:** `bug 🦗`, `P2`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 138. [BUG: We do not respect semantics of to_numpy(copy=False) and np.array(copy=False) (the latter only available on numpy >= 2.1)](https://github.com/modin-project/modin/issues/7583) (#7583)
- **URL:** https://github.com/modin-project/modin/issues/7583
- **Relevance Score:** `18` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`, `P2`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 139. [BUG: `modin.pandas.concat` on dict of dataframes behaves different from default `pandas.concat` if the dict keys are tuples](https://github.com/modin-project/modin/issues/7568) (#7568)
- **URL:** https://github.com/modin-project/modin/issues/7568
- **Relevance Score:** `18` | **State:** `open` | **Author:** `jlbosse`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 140. [BUG: assigning series to certain rows of a dataframe with row or iloc incorrectly assigns NaN](https://github.com/modin-project/modin/issues/7484) (#7484)
- **URL:** https://github.com/modin-project/modin/issues/7484
- **Relevance Score:** `18` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`, `P1`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 141. [BUG: DataFrame.__setitem__ on empty frame switches engines](https://github.com/modin-project/modin/issues/7428) (#7428)
- **URL:** https://github.com/modin-project/modin/issues/7428
- **Relevance Score:** `18` | **State:** `open` | **Author:** `sfc-gh-mvashishtha`
- **Labels:** `bug 🦗`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 142. [BUG: modin.pandas.read_csv: "FileNotFoundError: [Errno 2] No such file or directory"](https://github.com/modin-project/modin/issues/7416) (#7416)
- **URL:** https://github.com/modin-project/modin/issues/7416
- **Relevance Score:** `18` | **State:** `open` | **Author:** `frank0532`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 143. [BUG: can't use list of tuples of select multiple columns when columns are multiindex](https://github.com/modin-project/modin/issues/7409) (#7409)
- **URL:** https://github.com/modin-project/modin/issues/7409
- **Relevance Score:** `18` | **State:** `open` | **Author:** `MarcoGorelli`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 144. [BUG: Cannot insert lists into individual cells with `at` or `loc`. Works in pandas.](https://github.com/modin-project/modin/issues/7406) (#7406)
- **URL:** https://github.com/modin-project/modin/issues/7406
- **Relevance Score:** `18` | **State:** `open` | **Author:** `bdalal`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 145. [BUG: Writes to `DataFrame.attrs` are not preserved](https://github.com/modin-project/modin/issues/7401) (#7401)
- **URL:** https://github.com/modin-project/modin/issues/7401
- **Relevance Score:** `18` | **State:** `open` | **Author:** `noloerino`
- **Labels:** `bug 🦗`, `pandas concordance 🐼`, `P2`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 146. [BUG: Merge on Ray Engine does not produce the column "_merge" when indicator is True](https://github.com/modin-project/modin/issues/7384) (#7384)
- **URL:** https://github.com/modin-project/modin/issues/7384
- **Relevance Score:** `18` | **State:** `open` | **Author:** `castelojb`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [x] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 147. [BUG: [RAY] ray initialisation sets _memory and object_store_memory to the same value, leading to crashes and less flexibility](https://github.com/modin-project/modin/issues/7361) (#7361)
- **URL:** https://github.com/modin-project/modin/issues/7361
- **Relevance Score:** `18` | **State:** `open` | **Author:** `Liquidmasl`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [ ] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 148. [BUG: Series + DataFrame result is different object type depending on order of operands](https://github.com/modin-project/modin/issues/7236) (#7236)
- **URL:** https://github.com/modin-project/modin/issues/7236
- **Relevance Score:** `18` | **State:** `open` | **Author:** `sfc-gh-rdurrani`
- **Labels:** `bug 🦗`, `P1`, `Enable plugin`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 149. [BUG: SeriesGroupBy for aggregations returns unnamed series instead of series named after aggregated column](https://github.com/modin-project/modin/issues/7097) (#7097)
- **URL:** https://github.com/modin-project/modin/issues/7097
- **Relevance Score:** `18` | **State:** `open` | **Author:** `mvashishtha`
- **Labels:** `bug 🦗`, `P2`, `pandas.groupby`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [X] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 150. [BUG: `Series.clip` raises with pyarrow dtype backend](https://github.com/modin-project/modin/issues/7415) (#7415)
- **URL:** https://github.com/modin-project/modin/issues/7415
- **Relevance Score:** `14` | **State:** `open` | **Author:** `FBruzzesi`
- **Labels:** `bug 🦗`, `Triage 🩹`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `i/o`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Modin version checks - [X] I have checked that this issue has not already been reported. - [X] I have confirmed this bug exists on the latest released version of Modin. - [ ] I have confirmed this bug exists on the main branch of Modin. (In order to do this you can follow [this guide](https://mo..."*

#### 151. [Suggestion: reference WFGY Problem Map (RAG / LLM debugging checklist) for Modin users](https://github.com/modin-project/modin/issues/7696) (#7696)
- **URL:** https://github.com/modin-project/modin/issues/7696
- **Relevance Score:** `5` | **State:** `open` | **Author:** `onestardao`
- **Labels:** None
- **FS Keywords:** `mmap`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi Modin team, thank you for making it easier to scale pandas-style workloads. I see Modin being used more and more in pipelines where people prepare large corpora, logs, and features that eventually feed into vector stores and LLM / RAG systems. I maintain an MIT-licensed project called **WFGY Prob..."*

### [flyteorg/flyte](https://github.com/flyteorg/flyte) (2 issues)

#### 152. [Fix typo: rename ActionMetadata.funtion_name → function_name (proto, backend, SDK stubs)](https://github.com/flyteorg/flyte/issues/7558) (#7558)
- **URL:** https://github.com/flyteorg/flyte/issues/7558
- **Relevance Score:** `14` | **State:** `open` | **Author:** `pingsutw`
- **Labels:** `good first issue`, `flyte2`
- **FS Keywords:** `parts`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"## Summary There's a typo in one of our protobuf fields: `funtion_name` should be `function_name` (missing the **c**). It lives on the `ActionMetadata` message and flows through the generated code in every language, the Go backend, and the published `flyteidl2` package that the Python SDK depends on..."*

#### 153. [Proposal: RAG workflow failure taxonomy guide using WFGY ProblemMap](https://github.com/flyteorg/flyte/issues/6930) (#6930)
- **URL:** https://github.com/flyteorg/flyte/issues/6930
- **Relevance Score:** `5` | **State:** `open` | **Author:** `onestardao`
- **Labels:** None
- **FS Keywords:** `mmap`
- **Perf Keywords:** `io`
- **Excerpt:** *"Hi, and thanks for Flyte – the emphasis on strong typing and reproducible workflows is very helpful for production ML. I maintain an open-source project called **WFGY** (MIT-licensed, ~1.5k GitHub stars). We maintain a **16-problem “ProblemMap”** that focuses on **RAG / LLM failure modes** across re..."*

### [feast-dev/feast](https://github.com/feast-dev/feast) (1 issues)

#### 154. [Remote registry gRPC client sets no deadline and no keepalive, and neither is configurable: a blackholed connection hangs the caller indefinitely](https://github.com/feast-dev/feast/issues/6665) (#6665)
- **URL:** https://github.com/feast-dev/feast/issues/6665
- **Relevance Score:** `14` | **State:** `open` | **Author:** `BigyaPradhan`
- **Labels:** None
- **FS Keywords:** `parts`
- **Perf Keywords:** `hang`, `io`, `stall`, `timeout`
- **Excerpt:** *"## Expected Behavior A registry RPC issued by `RemoteRegistry` should fail within a bounded time when the connection to the registry server stops making progress, and the bound should be configurable through `RemoteRegistryConfig`. ## Current Behavior `RemoteRegistry` builds a channel with no keepal..."*

### [pydata/xarray](https://github.com/pydata/xarray) (37 issues)

#### 155. [unstack is slow for regular data](https://github.com/pydata/xarray/issues/11455) (#11455)
- **URL:** https://github.com/pydata/xarray/issues/11455
- **Relevance Score:** `36` | **State:** `open` | **Author:** `takluyver`
- **Labels:** `bug`, `topic-performance`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `performance`, `slow`, `speed`, `speedup`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Unstacking an array with a 'regular' MultiIndex, i.e. a cartesian product which doesn't need any missing value handling, is unexpectedly slow. E.g. unstacking (300_000, 1024) -> (10_000, 30, 1024) takes ~660 ms in my test, whereas reshaping the numpy array is massively quicker. ##..."*

#### 156. [2026.4.0 breaks pickling with backends.scipy_](https://github.com/pydata/xarray/issues/11323) (#11323)
- **URL:** https://github.com/pydata/xarray/issues/11323
- **Relevance Score:** `30` | **State:** `open` | **Author:** `SoundDesignerToBe`
- **Labels:** `bug`, `topic-backends`, `contrib-good-first-issue`, `regression`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `concurrent`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Switching from 2026.2.0 to 2026.4.0 breaks some pickling backend for netcdf files in multi-processing (concurrent.future.ProcessPoolExecutor). Quoting Claude: > The error is a classic pickle-identity mismatch: the instance's class qualname is `xarray.backends.scipy_._PickleWorkaro..."*

#### 157. [Construction of arrays with `object` dtype very slow when Pandas `future.infer_string` is enabled](https://github.com/pydata/xarray/issues/11470) (#11470)
- **URL:** https://github.com/pydata/xarray/issues/11470
- **Relevance Score:** `27` | **State:** `open` | **Author:** `y4n9squared`
- **Labels:** `bug`, `topic-performance`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `slow`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Constructing a `Variable` (or `Dataset`/`DataArray`) from an object-dtype numpy array of strings takes ~0.1ms per 10M elements under pandas' default settings, but **~500–620ms** with `pd.options.future.infer_string = True` — the setting that becomes the default in pandas 3.0. Why:..."*

#### 158. [to_zarr with regions does not respect dim names -- only order.](https://github.com/pydata/xarray/issues/10891) (#10891)
- **URL:** https://github.com/pydata/xarray/issues/10891
- **Relevance Score:** `27` | **State:** `open` | **Author:** `oxinabox`
- **Labels:** `topic-documentation`, `topic-zarr`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? If i have 2 datasets with the same set of coords but in different orders then `to_zarr` writes them to a file in that order, rather than ensuring that the names agree. So reading them out things get swapped around. Oerhaps I am wrong and actually I am explictly opting out of this ..."*

#### 159. [xarray.load_dataarray fails when loading a DataArray with coordinates via zarr-fsspec](https://github.com/pydata/xarray/issues/10950) (#10950)
- **URL:** https://github.com/pydata/xarray/issues/10950
- **Relevance Score:** `26` | **State:** `open` | **Author:** `csubich`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `block_size`, `bottleneck`, `cache`, `concurrent`, `io`, `stall`, `stalled`, `timeout`
- **Excerpt:** *"### What happened? When loading a zarr-backed DataArray via a fsspec URL, if the DataArray has coordinates xarray appears to treat the load as a request for a Dataset, not a DataArray. It then seeks to load the coordinate as a distinct variable within the file, where it is not present. This issue do..."*

#### 160. [Units and calendar attributes of time_bnds are dropped by to_netcdf](https://github.com/pydata/xarray/issues/11275) (#11275)
- **URL:** https://github.com/pydata/xarray/issues/11275
- **Relevance Score:** `24` | **State:** `open` | **Author:** `briardew`
- **Labels:** `topic-CF conventions`, `plan to close`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? If I define a `time_bnds` variable and denote it with the `bounds` attribute to the `time` variable, sometimes `to_netcdf` will drop the `units` and `calendar` attributes of the `time_bnds` variable. This seems like a bug to me. ### What did you expect to happen? I expected writte..."*

#### 161. [groupby multiple variables should include observed groups only](https://github.com/pydata/xarray/issues/11178) (#11178)
- **URL:** https://github.com/pydata/xarray/issues/11178
- **Relevance Score:** `24` | **State:** `open` | **Author:** `joshua-gould`
- **Labels:** `topic-groupby`, `usage question`, `plan to close`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Grouping more more than one variable includes combinations with no observations ### What did you expect to happen? Empty groups are not included ### Minimal Complete Verifiable Example ```Python # /// script # requires-python = ">=3.11" # dependencies = [ # "xarray[complete]@git+h..."*

#### 162. [Scalars coordinates have no memory on their DataArray](https://github.com/pydata/xarray/issues/11176) (#11176)
- **URL:** https://github.com/pydata/xarray/issues/11176
- **Relevance Score:** `24` | **State:** `open` | **Author:** `oloapinivad`
- **Labels:** `design question`, `usage question`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I am noticing an issue which might be a bug or a feature, but leaves me quite puzzled. I understand that scalar coordinates are transported all together when slicing/selection is operated to make smooth operations across datasets. However, when I have a dataset with two variables ..."*

#### 163. [In open_zarr, decode_timedelta does not behave as documented](https://github.com/pydata/xarray/issues/11507) (#11507)
- **URL:** https://github.com/pydata/xarray/issues/11507
- **Relevance Score:** `19` | **State:** `open` | **Author:** `theo-xirouchaki`
- **Labels:** `bug`, `topic-zarr`
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `bottleneck`, `io`, `speed`, `stall`, `stalled`
- **Excerpt:** *"### What happened? [The documentation](https://docs.xarray.dev/en/stable/generated/xarray.open_zarr.html#xarray.open_zarr) states that, for open_zarr, if decode_timedelta is None it will take the value of decode_times which is True by default. That isn't the behaviour I'm seeing, timedeltas are not ..."*

#### 164. [DataSetRolling and DatasetGroupBy silently accept `keepdims`, which modifes shape of the GroupBy output](https://github.com/pydata/xarray/issues/11518) (#11518)
- **URL:** https://github.com/pydata/xarray/issues/11518
- **Relevance Score:** `17` | **State:** `open` | **Author:** `charles-turner-1`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? > [!NOTE] > I've edited this a bit since I've opened it since I've discovered a bit of a can of worms. I'm trying to figure out if this is a duplicate of other issues now - it wasn't when I started. tldr; `ds.rolling({'time' : 12}).mean(keepdims=False|True)` makes no difference an..."*

#### 165. [StringDType does not roundtrip through zarr](https://github.com/pydata/xarray/issues/11466) (#11466)
- **URL:** https://github.com/pydata/xarray/issues/11466
- **Relevance Score:** `17` | **State:** `open` | **Author:** `jacksonriley`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Hi there, I noticed today that in `xarray>=2026.4.0`, a `Dataset` with a variable of type `np.dtypes.StringDType` does not roundtrip via zarr (you end up with fixed-length UTF32), and this also triggers a warning in Zarr: ``` /usr/local/lib/python3.12/site-packages/zarr/core/dtype..."*

#### 166. [FutureCancelledError (lost dependencies) during `dask.compute` with `optimize_graph=True` when chaining Dataset.assign](https://github.com/pydata/xarray/issues/11329) (#11329)
- **URL:** https://github.com/pydata/xarray/issues/11329
- **Relevance Score:** `17` | **State:** `open` | **Author:** `maneesh29s`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? It appears that the High-Level Graph (HLG) optimization fails to correctly resolve dependencies when a variable (like `new_weight` in the example) is used both as an input for a subsequent calculation and as a replacement variable in an intermediate Dataset state. Raised exception..."*

#### 167. [Cannot call .chunk('auto') on DataTree.](https://github.com/pydata/xarray/issues/11315) (#11315)
- **URL:** https://github.com/pydata/xarray/issues/11315
- **Relevance Score:** `17` | **State:** `open` | **Author:** `BorisTheBrave`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Got an error when calling data_tree.chunk('auto') This is pretty frustrating, when `xr.open_datatree` supports it. I would expect both to be equivalent. ### What did you expect to happen? I expect it to succeed, and be equivalent to chunking the dataset, or opening the datatree wi..."*

#### 168. [`.idxmax()` fails if coordinates are intervals](https://github.com/pydata/xarray/issues/11300) (#11300)
- **URL:** https://github.com/pydata/xarray/issues/11300
- **Relevance Score:** `17` | **State:** `open` | **Author:** `j-haacker`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? `<operation including groupby_bins>.idxmax()` raised `TypeError: len() of unsized object` ### What did you expect to happen? It should return the index of the greatest value. ### Minimal Complete Verifiable Example ```Python # /// script # requires-python = ">=3.11" # dependencies..."*

#### 169. [Unable to run groupby, map after shuffle_to_chunks](https://github.com/pydata/xarray/issues/11212) (#11212)
- **URL:** https://github.com/pydata/xarray/issues/11212
- **Relevance Score:** `17` | **State:** `open` | **Author:** `joshua-gould`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `chunk_size`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? ValueError: Array chunk size or shape is unknown. Possible solution with x.compute_chunk_sizes() ### What did you expect to happen? Able to successfully iterate over groups and apply a function ### Minimal Complete Verifiable Example ```Python # /// script # requires-python = ">=3..."*

#### 170. [DataArray.groupby drops empty coordinates](https://github.com/pydata/xarray/issues/11188) (#11188)
- **URL:** https://github.com/pydata/xarray/issues/11188
- **Relevance Score:** `17` | **State:** `open` | **Author:** `eugene57`
- **Labels:** `bug`, `topic-groupby`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When I run groupby on an empty `DataArray`, empty coordinates are dropped. This is is xarray version 2024.10.0. ``` import numpy as np import xarray as xr data = xr.DataArray(np.empty((0, 2)), dims=['x', 'y'], coords={'x': [], 'y': [1, 1]}) print(data.groupby('y').sum()) <xarray.D..."*

#### 171. [Appending to Zarr store on disk changes dimension metadata](https://github.com/pydata/xarray/issues/11101) (#11101)
- **URL:** https://github.com/pydata/xarray/issues/11101
- **Relevance Score:** `17` | **State:** `open` | **Author:** `jacobbieker`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I am writing lots of geo data to disk in Zarr and Icechunk, usually through appending to a given Zarr store on disk. I noticed that recently, some of the data values have seemed flipped compared to what the dimension says they should be. I've made a minimal example to show this, t..."*

#### 172. [String type casting error during concatenating](https://github.com/pydata/xarray/issues/10968) (#10968)
- **URL:** https://github.com/pydata/xarray/issues/10968
- **Relevance Score:** `17` | **State:** `open` | **Author:** `Pietervanhalem`
- **Labels:** `bug`, `needs triage`, `topic-combine`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I have a very large number of data sets (6840) that I want to concat over 3 dimensions. An example of one of the dataset is showed below: <img width="1127" height="633" alt="Image" src="https://github.com/user-attachments/assets/63673f8d-b769-4b55-81ee-9befc6dd8177" /> I concat wi..."*

#### 173. [DataTree constructor error message says dict even though dict is not accepted](https://github.com/pydata/xarray/issues/11514) (#11514)
- **URL:** https://github.com/pydata/xarray/issues/11514
- **Relevance Score:** `14` | **State:** `open` | **Author:** `mgunyho`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When I try to create a `DataTree` with a `dict` as the first argument, I get a TypeError: ``` >>> xr.DataTree(dict()) ... TypeError: data object is not an xarray.Dataset, dict, or None: {} ``` ### What did you expect to happen? A dictionary should be accepted, or the error message..."*

#### 174. [Unable to roundtrip sharded zarr](https://github.com/pydata/xarray/issues/11460) (#11460)
- **URL:** https://github.com/pydata/xarray/issues/11460
- **Relevance Score:** `14` | **State:** `open` | **Author:** `taus`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When creating a sharded zarr data set, reopening the dataset looses the sharding information. Shard and chunk sizes are set using `encoding` in to_zarr. When the dataset is reopened the sharding information is disregarded and the zarr chunks are used instead. This results in issue..."*

#### 175. [Latex labels not rendered under very specific conditions](https://github.com/pydata/xarray/issues/11452) (#11452)
- **URL:** https://github.com/pydata/xarray/issues/11452
- **Relevance Score:** `14` | **State:** `open` | **Author:** `mtrocadomoreira`
- **Labels:** `bug`, `topic-plotting`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I was plotting some Datasets with fairly complicated labels and units, and I noticed a very strange behaviour when using the `plot()` method. When both `attrs["long_name"]` and `attrs["units"]` contain `\mathrm`'s or `\text`'s, and at least one of them contains a `\frac`, and if t..."*

#### 176. [np.linalg.pinv of a DataArray results in mismatched coordinates](https://github.com/pydata/xarray/issues/11396) (#11396)
- **URL:** https://github.com/pydata/xarray/issues/11396
- **Relevance Score:** `14` | **State:** `open` | **Author:** `brsr`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? In general, `np.linalg.pinv` takes an array of shape (..., n, m) and returns an array of shape (..., m, n). Something isn't recognizing that the last two axes get switched around, so it incorrectly retains the coordinates in the same order. In the attached example, `m1` is an Data..."*

#### 177. [Cannot reindex onto a stacked MultiIndex via indexers — only reindex_like works](https://github.com/pydata/xarray/issues/11368) (#11368)
- **URL:** https://github.com/pydata/xarray/issues/11368
- **Relevance Score:** `14` | **State:** `open` | **Author:** `FBumann`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Reindexing a DataArray whose dimension is backed by a stacked `pd.MultiIndex` onto a *different* MultiIndex (e.g. the full index, where the array covers a subset) fails for **every** indexer form: 1. a raw `pd.MultiIndex` as indexer value → `ValueError: unmatched keys found in ind..."*

#### 178. [Corrupted data when Xarray writes to Zarr Datetime64 dtype](https://github.com/pydata/xarray/issues/11350) (#11350)
- **URL:** https://github.com/pydata/xarray/issues/11350
- **Relevance Score:** `14` | **State:** `open` | **Author:** `vladidobro`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Hi, when using the new Zarr v3 DateTime64 dtype, I have trouble correctly writing to it with xarray - I have not found a way to write the correct values. I believe it is probably related to some CF coding enabled when it should not be, or something like that. Am I doing something ..."*

#### 179. [A single nested tuple MultiIndex key is located correctly but preserves the dimension](https://github.com/pydata/xarray/issues/11341) (#11341)
- **URL:** https://github.com/pydata/xarray/issues/11341
- **Relevance Score:** `14` | **State:** `open` | **Author:** `cfriedland5`
- **Labels:** `bug`, `topic-indexing`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When selecting from an xarray MultiIndex that has a tuple-valued level, a nested tuple key corresponding to a single location can be located correctly, but the result keeps a length-1 dimension instead of behaving like scalar selection. It is inconsistent that xarray correctly und..."*

#### 180. [cumulate+argmax uses padded index instead of absolute index](https://github.com/pydata/xarray/issues/11336) (#11336)
- **URL:** https://github.com/pydata/xarray/issues/11336
- **Relevance Score:** `14` | **State:** `open` | **Author:** `saschahofmann`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? The combination of cumulative + argmax does not lead to the (at least from me) expected result. Example: ```python import numpy as np import xarray as xr da = xr.DataArray([1,2,1.5,3.5,4], coords={'time': ('time', np.arange(5))}) da.cumulative('time').argmax() # [4., 4., 3., 4., 4..."*

#### 181. [concat fails due to StringDtype introduced by pd.Index](https://github.com/pydata/xarray/issues/11317) (#11317)
- **URL:** https://github.com/pydata/xarray/issues/11317
- **Relevance Score:** `14` | **State:** `open` | **Author:** `vincentschut`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? This used to work (a few releases of xarray and/or pandas ago): ```python import xarray as xr import pandas as pd da = xr.DataArray([0], dims=["dim_a"], coords=dict(dim_a=["a"])) db = xr.DataArray([0]) # use concat to add a new dimension with coordinate db2 = xr.concat([db], pd.In..."*

#### 182. [Inconsistent and unexpected results when grouping by more than one coordinate](https://github.com/pydata/xarray/issues/11264) (#11264)
- **URL:** https://github.com/pydata/xarray/issues/11264
- **Relevance Score:** `14` | **State:** `open` | **Author:** `joshua-gould`
- **Labels:** `bug`, `API design`, `topic-groupby`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Grouping by more than one coordinate uses all combinations of coordinates. ### What did you expect to happen? I would expect only the observed combinations to be used. ### Minimal Complete Verifiable Example ```Python # /// script # requires-python = ">=3.11" # dependencies = [ # ..."*

#### 183. [`chunks` argument is typed incorrected in `open_zarr`](https://github.com/pydata/xarray/issues/11221) (#11221)
- **URL:** https://github.com/pydata/xarray/issues/11221
- **Relevance Score:** `14` | **State:** `open` | **Author:** `C-Loftus`
- **Labels:** `contrib-good-first-issue`, `topic-typing`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? If you try to type check a project that is using xarray there will be a failure when checking `open_zarr`. It is a best practice not to ignore this since if you do you generally have to ignore all type checking info on the open call which is otherwise useful. This error I believe ..."*

#### 184. [.swap_dims() loses indexes of non-dimension variables](https://github.com/pydata/xarray/issues/11099) (#11099)
- **URL:** https://github.com/pydata/xarray/issues/11099
- **Relevance Score:** `14` | **State:** `open` | **Author:** `Reshief`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? A rather obscure issue this time: When trying to rename a few dimensions and variable names of an old dataset, the resulting xarray lost all attributes on other variables in the dataset. More specifically, I could narrow it down to a very specific sequence of steps: 1. We need a d..."*

#### 185. [`expand_dims` creates `object` dtype for string coordinates instead of inferring string dtype](https://github.com/pydata/xarray/issues/11061) (#11061)
- **URL:** https://github.com/pydata/xarray/issues/11061
- **Relevance Score:** `14` | **State:** `open` | **Author:** `dcherian`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Discussed in https://github.com/pydata/xarray/discussions/11038 <div type='discussions-op-text'> <sup>Originally posted by **etienneschalk** December 19, 2025</sup> # `expand_dims` creates `object` dtype for string coordinates instead of inferring string dtype ## Summary When creating string coo..."*

#### 186. [Inconsistent behavior for `hue` between scatter and line](https://github.com/pydata/xarray/issues/10998) (#10998)
- **URL:** https://github.com/pydata/xarray/issues/10998
- **Relevance Score:** `14` | **State:** `open` | **Author:** `ianhi`
- **Labels:** `bug`, `topic-plotting`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? The behavior of `hue` results in different colors `ds.plot.scatter` vs `ds.plot.line` Both docstrings describe hue as: > hue (Hashable, optional) – Dimension or coordinate for which you want multiple lines plotted. If plotting against a 2D coordinate, hue must be a dimension. Whic..."*

#### 187. [`.sel()` fails on `datetime64[s]` object](https://github.com/pydata/xarray/issues/10975) (#10975)
- **URL:** https://github.com/pydata/xarray/issues/10975
- **Relevance Score:** `14` | **State:** `open` | **Author:** `oloapinivad`
- **Labels:** `bug`, `upstream issue`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Hi there, sorry if this might be a duplicate, but I have been browsing the repo without finding anything specific which resemble this. So, I am exploring to the possibility of calling xarray with `CFDatetimeDecoder` on time period overshooting `pandas` threshold year 2262 Running ..."*

#### 188. [Variious tests fail on x86 (32-bit issues)?](https://github.com/pydata/xarray/issues/10956) (#10956)
- **URL:** https://github.com/pydata/xarray/issues/10956
- **Relevance Score:** `14` | **State:** `open` | **Author:** `eli-schwartz`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? ``` FAILED xarray/tests/test_formatting.py::TestFormatting::test_diff_datatree_repr_equals - assert "Left and right DataTree objects are not equal\n\nData at node 'node' does not match:\n Differing dimensions:\n (y: 2) != (x: 1, y: 2)\n Differing data variables:\n L data (y) i... ..."*

#### 189. [Memory overflow when concatenating Dask-backed DataArrays with mixed dtypes (Boolean and Float)](https://github.com/pydata/xarray/issues/10928) (#10928)
- **URL:** https://github.com/pydata/xarray/issues/10928
- **Relevance Score:** `14` | **State:** `open` | **Author:** `josephnowak`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I had a process that needed to concatenate a Boolean matrix with a 3D float tensor, and every time I try to run a sum operation over it, it killed all the workers of my cluster. After investigation, I found that the boolean matrix was being converted into an integer before being c..."*

#### 190. [Maximum value not always included in pcolormesh output when levels are requested](https://github.com/pydata/xarray/issues/10911) (#10911)
- **URL:** https://github.com/pydata/xarray/issues/10911
- **Relevance Score:** `14` | **State:** `open` | **Author:** `aulemahal`
- **Labels:** `bug`, `contrib-help-wanted`, `topic-plotting`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When plotting data with "pcolormesh" and requesting levels, if the calculated "vmax" if equal to the upper bound of the last bin, it is not included in the map, as if it was "over" or "missing". ### What did you expect to happen? I expected `values == vmax` to be painted with the ..."*

#### 191. [open_mfdataset segfaults when using engine="netcdf4" and Prallel=Tru](https://github.com/pydata/xarray/issues/11088) (#11088)
- **URL:** https://github.com/pydata/xarray/issues/11088
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ArielDeVora`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`
- **Excerpt:** *"### What happened? When opening a mf_dataset using netcdf4 engine and parallel=True a segmentation fault arises. The whole open_mfdataset and all operations are wrapped in a class inheriting from xr.Dataset. I would like to know whether netcdf4 engine is compatible with parallel=True, or if there ar..."*

### [kedro-org/kedro](https://github.com/kedro-org/kedro) (4 issues)

#### 192. [Prevent serialization/pickling errors when using cloud-based datasets (e.g., S3).](https://github.com/kedro-org/kedro/issues/4690) (#4690)
- **URL:** https://github.com/kedro-org/kedro/issues/4690
- **Relevance Score:** `9` | **State:** `open` | **Author:** `SajidAlamQB`
- **Labels:** None
- **FS Keywords:** `filesystem`, `s3filesystem`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"### Description Related to: #2162 Datasets backed by cloud storage (e.g., S3 via s3fs) often hold non-picklable internal references (e.g., `S3FileSystem._glob`), which cause `ParallelRunner` to fail during multiprocessing pickling. Potential Fix: - Add a validation layer in `ParallelRunner._validate..."*

#### 193. [Feature request: RAG / LLM pipeline debugging tutorial using 16-problem ProblemMap](https://github.com/kedro-org/kedro/issues/5396) (#5396)
- **URL:** https://github.com/kedro-org/kedro/issues/5396
- **Relevance Score:** `8` | **State:** `open` | **Author:** `onestardao`
- **Labels:** None
- **FS Keywords:** `mmap`
- **Perf Keywords:** `hang`, `io`
- **Excerpt:** *"## Description Add an official tutorial or guide that shows how to debug RAG / LLM pipelines built with Kedro using a structured 16-problem failure map (WFGY ProblemMap). The guide would help users locate whether a failing RAG system is due to chunking, embeddings, vector stores, retrieval, routing ..."*

#### 194. [Identify Kedro in the S3 client user agent, and document endpoint_url generally](https://github.com/kedro-org/kedro/issues/5711) (#5711)
- **URL:** https://github.com/kedro-org/kedro/issues/5711
- **Relevance Score:** `7` | **State:** `open` | **Author:** `goanpeca`
- **Labels:** `Community`, `support: needs more info`
- **FS Keywords:** `fsspec`, `s3fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"## Description Kedro datasets reach `s3://` paths through `fsspec`/`s3fs`, and credentials entries already accept `client_kwargs.endpoint_url`, so Kedro works against Amazon S3 and other S3-compatible object stores today. Two small gaps follow: 1. **The S3 client does not identify Kedro.** The s3fs/..."*

#### 195. [Add opt-in URL scheme/host allowlist to `OmegaConfigLoader` for remote `conf_source`](https://github.com/kedro-org/kedro/issues/5636) (#5636)
- **URL:** https://github.com/kedro-org/kedro/issues/5636
- **Relevance Score:** `7` | **State:** `open` | **Author:** `merelcht`
- **Labels:** `Issue: Feature Request`
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"## Description `OmegaConfigLoader` accepts any fsspec-compatible URL as `conf_source`, including `http://` and `https://` targets, without any scheme or host validation. As a defence-in-depth measure, add an **opt-in** allowlist mechanism so teams running Kedro in multi-tenant or network-facing serv..."*
