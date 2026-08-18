# GitHub Issues Performance & FSSPEC Crawl Report

- **Repositories Crawled:** `8`
- **Total Issues Scanned:** `1600`
- **Matched Performance / FSSPEC Issues:** `85`

---

## 📊 Repository Issue Breakdown

| Repository | Issues Scanned | Matched Perf/FSSPEC Issues | Top Issue Link |
| :--- | :--- | :--- | :--- |
| [dask/dask](https://github.com/dask/dask) | `200` | `2` | [#12060](https://github.com/dask/dask/issues/12060) |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | `200` | `17` | [#66615](https://github.com/pandas-dev/pandas/issues/66615) |
| [pydata/xarray](https://github.com/pydata/xarray) | `200` | `37` | [#11455](https://github.com/pydata/xarray/issues/11455) |
| [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) | `200` | `16` | [#4029](https://github.com/zarr-developers/zarr-python/issues/4029) |
| [apache/arrow](https://github.com/apache/arrow) | `200` | `7` | [#50667](https://github.com/apache/arrow/issues/50667) |
| [huggingface/datasets](https://github.com/huggingface/datasets) | `200` | `4` | [#8242](https://github.com/huggingface/datasets/issues/8242) |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | `200` | `2` | [#193915](https://github.com/pytorch/pytorch/issues/193915) |
| [ray-project/ray](https://github.com/ray-project/ray) | `200` | `0` | N/A |

---

## 🔍 Detailed Matched Issues

### [dask/dask](https://github.com/dask/dask) (2 issues)

#### 1. [Significant slowdown in loading remote xarray dataset since 2025.5.0](https://github.com/dask/dask/issues/12060) (#12060)
- **URL:** https://github.com/dask/dask/issues/12060
- **Relevance Score:** `24` | **State:** `open` | **Author:** `Metamess`
- **Labels:** `needs attention`, `needs triage`
- **FS Keywords:** `gcsfs`
- **Perf Keywords:** `i/o`, `io`, `slow`, `stall`
- **Excerpt:** *"**Describe the issue**: Calling `.load()` or `.compute()` on an xarray dataset created by concatenating and slicing zarr datasets from a cloud bucket has seen a severe (factor ~50) slowdown between dask 2025.4.1 and 2025.5.0. I have not been able to replicate this slowdown with zarrs stored locally,..."*

#### 2. ['cumsum' results differ from 'cumsum' on a pure numpy array](https://github.com/dask/dask/issues/12359) (#12359)
- **URL:** https://github.com/dask/dask/issues/12359
- **Relevance Score:** `21` | **State:** `open` | **Author:** `muttener`
- **Labels:** `array`, `needs attention`, `bug`
- **FS Keywords:** `mmap`
- **Perf Keywords:** `chunk_size`, `io`, `stall`
- **Excerpt:** *"<!-- Please include a self-contained copy-pastable example that generates the issue if possible. Please be concise with code posted. See guidelines below on how to provide a good bug report: - Craft Minimal Bug Reports http://matthewrocklin.com/blog/work/2018/02/28/minimal-bug-reports - Minimal Comp..."*

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

#### 10. [BUG:  DataFrame.add(fill_value=...) promotes nullable integer dtypes to Float64, inconsistent with Series](https://github.com/pandas-dev/pandas/issues/65805) (#65805)
- **URL:** https://github.com/pandas-dev/pandas/issues/65805
- **Relevance Score:** `28` | **State:** `open` | **Author:** `arnaudlegout`
- **Labels:** `Bug`, `Dtype Conversions`, `Numeric Operations`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [ ] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 11. [BUG: cumsum/cumprod raises ArrowInvalid: overflow on integer ArrowDtypes instead of upcasting](https://github.com/pandas-dev/pandas/issues/66605) (#66605)
- **URL:** https://github.com/pandas-dev/pandas/issues/66605
- **Relevance Score:** `24` | **State:** `open` | **Author:** `arunkpe`
- **Labels:** `Bug`, `Needs Discussion`, `Arrow`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 12. [BUG: `factorize(use_na_sentinel=True)` ignores `use_na_sentinel` for pre-encoded PyArrow `DictionaryArray`s](https://github.com/pandas-dev/pandas/issues/66490) (#66490)
- **URL:** https://github.com/pandas-dev/pandas/issues/66490
- **Relevance Score:** `21` | **State:** `open` | **Author:** `camriddell`
- **Labels:** `Bug`, `Algos`, `Arrow`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Pandas version checks - [x] I have checked that this issue has not already been reported. - [x] I have confirmed this bug exists on the [latest version](https://pandas.pydata.org/docs/whatsnew/index.html) of pandas. - [x] I have confirmed this bug exists on the [main branch](https://pandas.pydat..."*

#### 13. [BUG: Inconsistent nan to None behaviour in replace() with scalar vs list value](https://github.com/pandas-dev/pandas/issues/65892) (#65892)
- **URL:** https://github.com/pandas-dev/pandas/issues/65892
- **Relevance Score:** `21` | **State:** `open` | **Author:** `veenstrajelmer`
- **Labels:** `Bug`, `Missing-data`, `Strings`, `replace`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
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

### [pydata/xarray](https://github.com/pydata/xarray) (37 issues)

#### 20. [unstack is slow for regular data](https://github.com/pydata/xarray/issues/11455) (#11455)
- **URL:** https://github.com/pydata/xarray/issues/11455
- **Relevance Score:** `36` | **State:** `open` | **Author:** `takluyver`
- **Labels:** `bug`, `topic-performance`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `performance`, `slow`, `speed`, `speedup`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Unstacking an array with a 'regular' MultiIndex, i.e. a cartesian product which doesn't need any missing value handling, is unexpectedly slow. E.g. unstacking (300_000, 1024) -> (10_000, 30, 1024) takes ~660 ms in my test, whereas reshaping the numpy array is massively quicker. ##..."*

#### 21. [2026.4.0 breaks pickling with backends.scipy_](https://github.com/pydata/xarray/issues/11323) (#11323)
- **URL:** https://github.com/pydata/xarray/issues/11323
- **Relevance Score:** `30` | **State:** `open` | **Author:** `SoundDesignerToBe`
- **Labels:** `bug`, `topic-backends`, `contrib-good-first-issue`, `regression`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `concurrent`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Switching from 2026.2.0 to 2026.4.0 breaks some pickling backend for netcdf files in multi-processing (concurrent.future.ProcessPoolExecutor). Quoting Claude: > The error is a classic pickle-identity mismatch: the instance's class qualname is `xarray.backends.scipy_._PickleWorkaro..."*

#### 22. [Construction of arrays with `object` dtype very slow when Pandas `future.infer_string` is enabled](https://github.com/pydata/xarray/issues/11470) (#11470)
- **URL:** https://github.com/pydata/xarray/issues/11470
- **Relevance Score:** `27` | **State:** `open` | **Author:** `y4n9squared`
- **Labels:** `bug`, `topic-performance`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `slow`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Constructing a `Variable` (or `Dataset`/`DataArray`) from an object-dtype numpy array of strings takes ~0.1ms per 10M elements under pandas' default settings, but **~500–620ms** with `pd.options.future.infer_string = True` — the setting that becomes the default in pandas 3.0. Why:..."*

#### 23. [to_zarr with regions does not respect dim names -- only order.](https://github.com/pydata/xarray/issues/10891) (#10891)
- **URL:** https://github.com/pydata/xarray/issues/10891
- **Relevance Score:** `27` | **State:** `open` | **Author:** `oxinabox`
- **Labels:** `topic-documentation`, `topic-zarr`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? If i have 2 datasets with the same set of coords but in different orders then `to_zarr` writes them to a file in that order, rather than ensuring that the names agree. So reading them out things get swapped around. Oerhaps I am wrong and actually I am explictly opting out of this ..."*

#### 24. [xarray.load_dataarray fails when loading a DataArray with coordinates via zarr-fsspec](https://github.com/pydata/xarray/issues/10950) (#10950)
- **URL:** https://github.com/pydata/xarray/issues/10950
- **Relevance Score:** `26` | **State:** `open` | **Author:** `csubich`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `block_size`, `bottleneck`, `cache`, `concurrent`, `io`, `stall`, `stalled`, `timeout`
- **Excerpt:** *"### What happened? When loading a zarr-backed DataArray via a fsspec URL, if the DataArray has coordinates xarray appears to treat the load as a request for a Dataset, not a DataArray. It then seeks to load the coordinate as a distinct variable within the file, where it is not present. This issue do..."*

#### 25. [Units and calendar attributes of time_bnds are dropped by to_netcdf](https://github.com/pydata/xarray/issues/11275) (#11275)
- **URL:** https://github.com/pydata/xarray/issues/11275
- **Relevance Score:** `24` | **State:** `open` | **Author:** `briardew`
- **Labels:** `topic-CF conventions`, `plan to close`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? If I define a `time_bnds` variable and denote it with the `bounds` attribute to the `time` variable, sometimes `to_netcdf` will drop the `units` and `calendar` attributes of the `time_bnds` variable. This seems like a bug to me. ### What did you expect to happen? I expected writte..."*

#### 26. [groupby multiple variables should include observed groups only](https://github.com/pydata/xarray/issues/11178) (#11178)
- **URL:** https://github.com/pydata/xarray/issues/11178
- **Relevance Score:** `24` | **State:** `open` | **Author:** `joshua-gould`
- **Labels:** `topic-groupby`, `usage question`, `plan to close`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Grouping more more than one variable includes combinations with no observations ### What did you expect to happen? Empty groups are not included ### Minimal Complete Verifiable Example ```Python # /// script # requires-python = ">=3.11" # dependencies = [ # "xarray[complete]@git+h..."*

#### 27. [Scalars coordinates have no memory on their DataArray](https://github.com/pydata/xarray/issues/11176) (#11176)
- **URL:** https://github.com/pydata/xarray/issues/11176
- **Relevance Score:** `24` | **State:** `open` | **Author:** `oloapinivad`
- **Labels:** `design question`, `usage question`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I am noticing an issue which might be a bug or a feature, but leaves me quite puzzled. I understand that scalar coordinates are transported all together when slicing/selection is operated to make smooth operations across datasets. However, when I have a dataset with two variables ..."*

#### 28. [In open_zarr, decode_timedelta does not behave as documented](https://github.com/pydata/xarray/issues/11507) (#11507)
- **URL:** https://github.com/pydata/xarray/issues/11507
- **Relevance Score:** `19` | **State:** `open` | **Author:** `theo-xirouchaki`
- **Labels:** `bug`, `topic-zarr`
- **FS Keywords:** `fsspec`, `gcsfs`
- **Perf Keywords:** `bottleneck`, `io`, `speed`, `stall`, `stalled`
- **Excerpt:** *"### What happened? [The documentation](https://docs.xarray.dev/en/stable/generated/xarray.open_zarr.html#xarray.open_zarr) states that, for open_zarr, if decode_timedelta is None it will take the value of decode_times which is True by default. That isn't the behaviour I'm seeing, timedeltas are not ..."*

#### 29. [DataSetRolling and DatasetGroupBy silently accept `keepdims`, which modifes shape of the GroupBy output](https://github.com/pydata/xarray/issues/11518) (#11518)
- **URL:** https://github.com/pydata/xarray/issues/11518
- **Relevance Score:** `17` | **State:** `open` | **Author:** `charles-turner-1`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? > [!NOTE] > I've edited this a bit since I've opened it since I've discovered a bit of a can of worms. I'm trying to figure out if this is a duplicate of other issues now - it wasn't when I started. tldr; `ds.rolling({'time' : 12}).mean(keepdims=False|True)` makes no difference an..."*

#### 30. [StringDType does not roundtrip through zarr](https://github.com/pydata/xarray/issues/11466) (#11466)
- **URL:** https://github.com/pydata/xarray/issues/11466
- **Relevance Score:** `17` | **State:** `open` | **Author:** `jacksonriley`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Hi there, I noticed today that in `xarray>=2026.4.0`, a `Dataset` with a variable of type `np.dtypes.StringDType` does not roundtrip via zarr (you end up with fixed-length UTF32), and this also triggers a warning in Zarr: ``` /usr/local/lib/python3.12/site-packages/zarr/core/dtype..."*

#### 31. [FutureCancelledError (lost dependencies) during `dask.compute` with `optimize_graph=True` when chaining Dataset.assign](https://github.com/pydata/xarray/issues/11329) (#11329)
- **URL:** https://github.com/pydata/xarray/issues/11329
- **Relevance Score:** `17` | **State:** `open` | **Author:** `maneesh29s`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? It appears that the High-Level Graph (HLG) optimization fails to correctly resolve dependencies when a variable (like `new_weight` in the example) is used both as an input for a subsequent calculation and as a replacement variable in an intermediate Dataset state. Raised exception..."*

#### 32. [Cannot call .chunk('auto') on DataTree.](https://github.com/pydata/xarray/issues/11315) (#11315)
- **URL:** https://github.com/pydata/xarray/issues/11315
- **Relevance Score:** `17` | **State:** `open` | **Author:** `BorisTheBrave`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Got an error when calling data_tree.chunk('auto') This is pretty frustrating, when `xr.open_datatree` supports it. I would expect both to be equivalent. ### What did you expect to happen? I expect it to succeed, and be equivalent to chunking the dataset, or opening the datatree wi..."*

#### 33. [`.idxmax()` fails if coordinates are intervals](https://github.com/pydata/xarray/issues/11300) (#11300)
- **URL:** https://github.com/pydata/xarray/issues/11300
- **Relevance Score:** `17` | **State:** `open` | **Author:** `j-haacker`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `cache`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? `<operation including groupby_bins>.idxmax()` raised `TypeError: len() of unsized object` ### What did you expect to happen? It should return the index of the greatest value. ### Minimal Complete Verifiable Example ```Python # /// script # requires-python = ">=3.11" # dependencies..."*

#### 34. [Unable to run groupby, map after shuffle_to_chunks](https://github.com/pydata/xarray/issues/11212) (#11212)
- **URL:** https://github.com/pydata/xarray/issues/11212
- **Relevance Score:** `17` | **State:** `open` | **Author:** `joshua-gould`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `chunk_size`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? ValueError: Array chunk size or shape is unknown. Possible solution with x.compute_chunk_sizes() ### What did you expect to happen? Able to successfully iterate over groups and apply a function ### Minimal Complete Verifiable Example ```Python # /// script # requires-python = ">=3..."*

#### 35. [DataArray.groupby drops empty coordinates](https://github.com/pydata/xarray/issues/11188) (#11188)
- **URL:** https://github.com/pydata/xarray/issues/11188
- **Relevance Score:** `17` | **State:** `open` | **Author:** `eugene57`
- **Labels:** `bug`, `topic-groupby`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When I run groupby on an empty `DataArray`, empty coordinates are dropped. This is is xarray version 2024.10.0. ``` import numpy as np import xarray as xr data = xr.DataArray(np.empty((0, 2)), dims=['x', 'y'], coords={'x': [], 'y': [1, 1]}) print(data.groupby('y').sum()) <xarray.D..."*

#### 36. [Appending to Zarr store on disk changes dimension metadata](https://github.com/pydata/xarray/issues/11101) (#11101)
- **URL:** https://github.com/pydata/xarray/issues/11101
- **Relevance Score:** `17` | **State:** `open` | **Author:** `jacobbieker`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I am writing lots of geo data to disk in Zarr and Icechunk, usually through appending to a given Zarr store on disk. I noticed that recently, some of the data values have seemed flipped compared to what the dimension says they should be. I've made a minimal example to show this, t..."*

#### 37. [String type casting error during concatenating](https://github.com/pydata/xarray/issues/10968) (#10968)
- **URL:** https://github.com/pydata/xarray/issues/10968
- **Relevance Score:** `17` | **State:** `open` | **Author:** `Pietervanhalem`
- **Labels:** `bug`, `needs triage`, `topic-combine`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I have a very large number of data sets (6840) that I want to concat over 3 dimensions. An example of one of the dataset is showed below: <img width="1127" height="633" alt="Image" src="https://github.com/user-attachments/assets/63673f8d-b769-4b55-81ee-9befc6dd8177" /> I concat wi..."*

#### 38. [DataTree constructor error message says dict even though dict is not accepted](https://github.com/pydata/xarray/issues/11514) (#11514)
- **URL:** https://github.com/pydata/xarray/issues/11514
- **Relevance Score:** `14` | **State:** `open` | **Author:** `mgunyho`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When I try to create a `DataTree` with a `dict` as the first argument, I get a TypeError: ``` >>> xr.DataTree(dict()) ... TypeError: data object is not an xarray.Dataset, dict, or None: {} ``` ### What did you expect to happen? A dictionary should be accepted, or the error message..."*

#### 39. [Unable to roundtrip sharded zarr](https://github.com/pydata/xarray/issues/11460) (#11460)
- **URL:** https://github.com/pydata/xarray/issues/11460
- **Relevance Score:** `14` | **State:** `open` | **Author:** `taus`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When creating a sharded zarr data set, reopening the dataset looses the sharding information. Shard and chunk sizes are set using `encoding` in to_zarr. When the dataset is reopened the sharding information is disregarded and the zarr chunks are used instead. This results in issue..."*

#### 40. [Latex labels not rendered under very specific conditions](https://github.com/pydata/xarray/issues/11452) (#11452)
- **URL:** https://github.com/pydata/xarray/issues/11452
- **Relevance Score:** `14` | **State:** `open` | **Author:** `mtrocadomoreira`
- **Labels:** `bug`, `topic-plotting`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I was plotting some Datasets with fairly complicated labels and units, and I noticed a very strange behaviour when using the `plot()` method. When both `attrs["long_name"]` and `attrs["units"]` contain `\mathrm`'s or `\text`'s, and at least one of them contains a `\frac`, and if t..."*

#### 41. [np.linalg.pinv of a DataArray results in mismatched coordinates](https://github.com/pydata/xarray/issues/11396) (#11396)
- **URL:** https://github.com/pydata/xarray/issues/11396
- **Relevance Score:** `14` | **State:** `open` | **Author:** `brsr`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? In general, `np.linalg.pinv` takes an array of shape (..., n, m) and returns an array of shape (..., m, n). Something isn't recognizing that the last two axes get switched around, so it incorrectly retains the coordinates in the same order. In the attached example, `m1` is an Data..."*

#### 42. [Cannot reindex onto a stacked MultiIndex via indexers — only reindex_like works](https://github.com/pydata/xarray/issues/11368) (#11368)
- **URL:** https://github.com/pydata/xarray/issues/11368
- **Relevance Score:** `14` | **State:** `open` | **Author:** `FBumann`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Reindexing a DataArray whose dimension is backed by a stacked `pd.MultiIndex` onto a *different* MultiIndex (e.g. the full index, where the array covers a subset) fails for **every** indexer form: 1. a raw `pd.MultiIndex` as indexer value → `ValueError: unmatched keys found in ind..."*

#### 43. [Corrupted data when Xarray writes to Zarr Datetime64 dtype](https://github.com/pydata/xarray/issues/11350) (#11350)
- **URL:** https://github.com/pydata/xarray/issues/11350
- **Relevance Score:** `14` | **State:** `open` | **Author:** `vladidobro`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Hi, when using the new Zarr v3 DateTime64 dtype, I have trouble correctly writing to it with xarray - I have not found a way to write the correct values. I believe it is probably related to some CF coding enabled when it should not be, or something like that. Am I doing something ..."*

#### 44. [A single nested tuple MultiIndex key is located correctly but preserves the dimension](https://github.com/pydata/xarray/issues/11341) (#11341)
- **URL:** https://github.com/pydata/xarray/issues/11341
- **Relevance Score:** `14` | **State:** `open` | **Author:** `cfriedland5`
- **Labels:** `bug`, `topic-indexing`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When selecting from an xarray MultiIndex that has a tuple-valued level, a nested tuple key corresponding to a single location can be located correctly, but the result keeps a length-1 dimension instead of behaving like scalar selection. It is inconsistent that xarray correctly und..."*

#### 45. [cumulate+argmax uses padded index instead of absolute index](https://github.com/pydata/xarray/issues/11336) (#11336)
- **URL:** https://github.com/pydata/xarray/issues/11336
- **Relevance Score:** `14` | **State:** `open` | **Author:** `saschahofmann`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? The combination of cumulative + argmax does not lead to the (at least from me) expected result. Example: ```python import numpy as np import xarray as xr da = xr.DataArray([1,2,1.5,3.5,4], coords={'time': ('time', np.arange(5))}) da.cumulative('time').argmax() # [4., 4., 3., 4., 4..."*

#### 46. [concat fails due to StringDtype introduced by pd.Index](https://github.com/pydata/xarray/issues/11317) (#11317)
- **URL:** https://github.com/pydata/xarray/issues/11317
- **Relevance Score:** `14` | **State:** `open` | **Author:** `vincentschut`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? This used to work (a few releases of xarray and/or pandas ago): ```python import xarray as xr import pandas as pd da = xr.DataArray([0], dims=["dim_a"], coords=dict(dim_a=["a"])) db = xr.DataArray([0]) # use concat to add a new dimension with coordinate db2 = xr.concat([db], pd.In..."*

#### 47. [Inconsistent and unexpected results when grouping by more than one coordinate](https://github.com/pydata/xarray/issues/11264) (#11264)
- **URL:** https://github.com/pydata/xarray/issues/11264
- **Relevance Score:** `14` | **State:** `open` | **Author:** `joshua-gould`
- **Labels:** `bug`, `API design`, `topic-groupby`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Grouping by more than one coordinate uses all combinations of coordinates. ### What did you expect to happen? I would expect only the observed combinations to be used. ### Minimal Complete Verifiable Example ```Python # /// script # requires-python = ">=3.11" # dependencies = [ # ..."*

#### 48. [`chunks` argument is typed incorrected in `open_zarr`](https://github.com/pydata/xarray/issues/11221) (#11221)
- **URL:** https://github.com/pydata/xarray/issues/11221
- **Relevance Score:** `14` | **State:** `open` | **Author:** `C-Loftus`
- **Labels:** `contrib-good-first-issue`, `topic-typing`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? If you try to type check a project that is using xarray there will be a failure when checking `open_zarr`. It is a best practice not to ignore this since if you do you generally have to ignore all type checking info on the open call which is otherwise useful. This error I believe ..."*

#### 49. [.swap_dims() loses indexes of non-dimension variables](https://github.com/pydata/xarray/issues/11099) (#11099)
- **URL:** https://github.com/pydata/xarray/issues/11099
- **Relevance Score:** `14` | **State:** `open` | **Author:** `Reshief`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? A rather obscure issue this time: When trying to rename a few dimensions and variable names of an old dataset, the resulting xarray lost all attributes on other variables in the dataset. More specifically, I could narrow it down to a very specific sequence of steps: 1. We need a d..."*

#### 50. [`expand_dims` creates `object` dtype for string coordinates instead of inferring string dtype](https://github.com/pydata/xarray/issues/11061) (#11061)
- **URL:** https://github.com/pydata/xarray/issues/11061
- **Relevance Score:** `14` | **State:** `open` | **Author:** `dcherian`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Discussed in https://github.com/pydata/xarray/discussions/11038 <div type='discussions-op-text'> <sup>Originally posted by **etienneschalk** December 19, 2025</sup> # `expand_dims` creates `object` dtype for string coordinates instead of inferring string dtype ## Summary When creating string coo..."*

#### 51. [Inconsistent behavior for `hue` between scatter and line](https://github.com/pydata/xarray/issues/10998) (#10998)
- **URL:** https://github.com/pydata/xarray/issues/10998
- **Relevance Score:** `14` | **State:** `open` | **Author:** `ianhi`
- **Labels:** `bug`, `topic-plotting`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? The behavior of `hue` results in different colors `ds.plot.scatter` vs `ds.plot.line` Both docstrings describe hue as: > hue (Hashable, optional) – Dimension or coordinate for which you want multiple lines plotted. If plotting against a 2D coordinate, hue must be a dimension. Whic..."*

#### 52. [`.sel()` fails on `datetime64[s]` object](https://github.com/pydata/xarray/issues/10975) (#10975)
- **URL:** https://github.com/pydata/xarray/issues/10975
- **Relevance Score:** `14` | **State:** `open` | **Author:** `oloapinivad`
- **Labels:** `bug`, `upstream issue`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? Hi there, sorry if this might be a duplicate, but I have been browsing the repo without finding anything specific which resemble this. So, I am exploring to the possibility of calling xarray with `CFDatetimeDecoder` on time period overshooting `pandas` threshold year 2262 Running ..."*

#### 53. [Variious tests fail on x86 (32-bit issues)?](https://github.com/pydata/xarray/issues/10956) (#10956)
- **URL:** https://github.com/pydata/xarray/issues/10956
- **Relevance Score:** `14` | **State:** `open` | **Author:** `eli-schwartz`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? ``` FAILED xarray/tests/test_formatting.py::TestFormatting::test_diff_datatree_repr_equals - assert "Left and right DataTree objects are not equal\n\nData at node 'node' does not match:\n Differing dimensions:\n (y: 2) != (x: 1, y: 2)\n Differing data variables:\n L data (y) i... ..."*

#### 54. [Memory overflow when concatenating Dask-backed DataArrays with mixed dtypes (Boolean and Float)](https://github.com/pydata/xarray/issues/10928) (#10928)
- **URL:** https://github.com/pydata/xarray/issues/10928
- **Relevance Score:** `14` | **State:** `open` | **Author:** `josephnowak`
- **Labels:** `bug`, `needs triage`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? I had a process that needed to concatenate a Boolean matrix with a 3D float tensor, and every time I try to run a sum operation over it, it killed all the workers of my cluster. After investigation, I found that the boolean matrix was being converted into an integer before being c..."*

#### 55. [Maximum value not always included in pcolormesh output when levels are requested](https://github.com/pydata/xarray/issues/10911) (#10911)
- **URL:** https://github.com/pydata/xarray/issues/10911
- **Relevance Score:** `14` | **State:** `open` | **Author:** `aulemahal`
- **Labels:** `bug`, `contrib-help-wanted`, `topic-plotting`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `io`, `stall`, `stalled`
- **Excerpt:** *"### What happened? When plotting data with "pcolormesh" and requesting levels, if the calculated "vmax" if equal to the upper bound of the last bin, it is not included in the map, as if it was "over" or "missing". ### What did you expect to happen? I expected `values == vmax` to be painted with the ..."*

#### 56. [open_mfdataset segfaults when using engine="netcdf4" and Prallel=Tru](https://github.com/pydata/xarray/issues/11088) (#11088)
- **URL:** https://github.com/pydata/xarray/issues/11088
- **Relevance Score:** `11` | **State:** `open` | **Author:** `ArielDeVora`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `bottleneck`, `hang`, `io`
- **Excerpt:** *"### What happened? When opening a mf_dataset using netcdf4 engine and parallel=True a segmentation fault arises. The whole open_mfdataset and all operations are wrapped in a class inheriting from xr.Dataset. I would like to know whether netcdf4 engine is compatible with parallel=True, or if there ar..."*

### [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) (16 issues)

#### 57. [VerboseModule cannot be pickled](https://github.com/zarr-developers/zarr-python/issues/4029) (#4029)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/4029
- **Relevance Score:** `21` | **State:** `open` | **Author:** `vladidobro`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`, `stall`, `stalled`
- **Excerpt:** *"### Zarr version 3.2.1 ### Numcodecs version 0.16.5 ### Python Version 3.12.12 ### Operating System Mac ### Installation using uv run ### Description Hi, I was trying to send zarr.storage.ObjectStore-backed Dask arrays to Dask, and I hit this error. Apparently `zarr.storage`, the module, cannot be p..."*

#### 58. [fully separate sync and async internal APIs](https://github.com/zarr-developers/zarr-python/issues/4217) (#4217)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/4217
- **Relevance Score:** `17` | **State:** `open` | **Author:** `d-v-b`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `io`, `latency`, `performance`, `slow`
- **Excerpt:** *"## current state our `Store` API uses _async_ methods for doing IO. In Python today, this is ergonomic for high-latency storage (stuff stored on a server far away), and unergonomic for low-latency storage (stuff stored in memory). similarly, our `Codec` API uses async methods for encoding and decodi..."*

#### 59. [Divergent behavior of memory store and localstore list prefix](https://github.com/zarr-developers/zarr-python/issues/3773) (#3773)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3773
- **Relevance Score:** `15` | **State:** `open` | **Author:** `ianhi`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`, `gcsfs`, `s3fs`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Zarr version main ### Numcodecs version main ### Python Version 3.11 ### Operating System Mac ### Installation uv ### Description Memory Store and Fsspec file system store return different results for `list_prefix` I think that the localstore matches what I would expect ### Steps to reproduce ``..."*

#### 60. [Explicitly using fsspec and zarr FsspecStore causes RuntimeError "Task attached to a different loop"](https://github.com/zarr-developers/zarr-python/issues/3487) (#3487)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3487
- **Relevance Score:** `13` | **State:** `open` | **Author:** `dmitriyrepin`
- **Labels:** None
- **FS Keywords:** `abstractfilesystem`, `filesystem`, `fsspec`, `gcsfs`, `url_to_fs`
- **Perf Keywords:** `io`
- **Excerpt:** *"## Summary Mixing explicit use of fsspec and zarr FsspecStore produces the following error: ```'RuntimeError: Task <Task pending ... > attached to a different loop. Task was destroyed but it is pending!'``` ## Reproducers: 1. When one explicitly creates fsspec.AbstractFileSystem and then uses it in ..."*

#### 61. [Zarr over ssh fails with `unexpected keyword argument`](https://github.com/zarr-developers/zarr-python/issues/3576) (#3576)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3576
- **Relevance Score:** `11` | **State:** `open` | **Author:** `b8raoult`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`, `stalled`
- **Excerpt:** *"### Zarr version 3.1.3 ### Numcodecs version 0.15.1 ### Python Version 3.12.9 ### Operating System Linux ### Installation uv pip install ### Description Calling `zarr.open` with an `ssh://...` url fails with the following error: ``` File ".../python3.12/site-packages/fsspec/implementations/sftp.py",..."*

#### 62. [Monthly issue metrics report](https://github.com/zarr-developers/zarr-python/issues/4223) (#4223)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/4223
- **Relevance Score:** `10` | **State:** `open` | **Author:** `github-actions[bot]`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `benchmark`, `io`
- **Excerpt:** *"# Issue Metrics | Metric | Average | Median | 90th percentile | | --- | --- | --- | ---: | | Time to first response | 11:44:43 | 4:18:47 | 1 day, 0:31:45 | | Time to first review | None | None | None | | Time to close | 5 days, 18:12:44 | 5 days, 19:32:26 | 11 days, 10:07:42 | | Time to answer | Non..."*

#### 63. [FsspecStore.from_url() raises "RuntimeError: Loop is not running" during interpreter shutdown](https://github.com/zarr-developers/zarr-python/issues/4221) (#4221)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/4221
- **Relevance Score:** `8` | **State:** `open` | **Author:** `hginzel`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"### Zarr version v3.3.0 ### Numcodecs version v0.16.5 ### Python Version 3.12.11 ### Operating System Ubuntu 26.04 ### Installation uv add zarr ### Environment Python 3.12.11 zarr 3.3.0 fsspec 2026.7.0 adlfs 2026.5.0 azure-identity 1.25.3 ### Description Creating a FsspecStore backed by Azure Blob S..."*

#### 64. [Regression in support for indexing into structured arrays within a Zarr store (v2 -> v3)](https://github.com/zarr-developers/zarr-python/issues/3983) (#3983)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3983
- **Relevance Score:** `8` | **State:** `open` | **Author:** `rachitk`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"### Zarr version v3.2.1 ### Numcodecs version 0.16.5 ### Python Version 3.12.7 ### Operating System Linux ### Installation Pip into virtual environment ### Description In Zarr-Python 2, saving a structured array into a Zarr store enabled one to load the store and index into the structured array to l..."*

#### 65. [Proposal: Make Obstore backend the default for s3/gcs/azure/https](https://github.com/zarr-developers/zarr-python/issues/3520) (#3520)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3520
- **Relevance Score:** `8` | **State:** `open` | **Author:** `jhamman`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `benchmark`, `performance`
- **Excerpt:** *"The Obstore backend in Zarr for about 6 months. Its working great and is significantly more performant that the fsspec alternatives. See [maxrjones/zarr-obstore-performance](https://github.com/maxrjones/zarr-obstore-performance) for performance benchmarks. With this in mind, I'm proposing that we sw..."*

#### 66. [Failure to list keys on remote HTTP store](https://github.com/zarr-developers/zarr-python/issues/3495) (#3495)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3495
- **Relevance Score:** `8` | **State:** `open` | **Author:** `ianhi`
- **Labels:** `bug`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"### Zarr version main ### Numcodecs version 0.16.3 ### Python Version 3.13 ### Operating System mac ### Installation pep-723 ### Description Opening a remote zarr store over https can silently fails to list keys ### Steps to reproduce ```python # /// script # requires-python = ">=3.11" # dependencie..."*

#### 67. [make `remote` dependencies more precise](https://github.com/zarr-developers/zarr-python/issues/3453) (#3453)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3453
- **Relevance Score:** `8` | **State:** `open` | **Author:** `d-v-b`
- **Labels:** `chore`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"We have an optional dependency called [`remote`](https://github.com/zarr-developers/zarr-python/blob/bce30dd3cc92a35038b88f80c4c42130670d4100/pyproject.toml#L64) that includes fsspec and obstore. But fsspec doesn't support http or s3 by default, so users who install `zarr[remote]` and try to open ht..."*

#### 68. [newtype pattern to protect against sloppy path normalization](https://github.com/zarr-developers/zarr-python/issues/3923) (#3923)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3923
- **Relevance Score:** `5` | **State:** `open` | **Author:** `d-v-b`
- **Labels:** `enhancement`
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"#3922 revealed that we don't normalize the `path` parameter when creating an instance of `FSSpecStore`. So `Store(path="foo/")` and `Store(path="foo")` end up with different `.path` attributes. One way to guard against this type of bug would be to introduce a new type that models "strings that have ..."*

#### 69. [Tolerate 403 HTTP codes in S3 stores as "non existing" objects](https://github.com/zarr-developers/zarr-python/issues/3617) (#3617)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3617
- **Relevance Score:** `5` | **State:** `open` | **Author:** `jordi-domingo`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"Dear all, I have a request for Zarr-Python related to their S3 stores (fsspec, obstore). Under certain circumstances, accessing a Zarr datacube in S3 can lead to 403 responses, which is an expected and correct behaviour: 1. During the creation of the datacube, chunk files with no data are directly n..."*

#### 70. [should the default path for the `FsspecStore` be `"/"` or `""`](https://github.com/zarr-developers/zarr-python/issues/3471) (#3471)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3471
- **Relevance Score:** `5` | **State:** `open` | **Author:** `d-v-b`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"The default path for `FsspecStore` is currently "/". I feel like this is less correct than the empty string "", and I suspect the leading "/" is removed internally by many of our path normalization routines."*

#### 71. [Opening Icechunk using Zarr 3.0 in a flask context](https://github.com/zarr-developers/zarr-python/issues/3463) (#3463)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3463
- **Relevance Score:** `5` | **State:** `open` | **Author:** `adanb13`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"I am trying to open a local `.icechunk` via: ``` import xarray as xr import logging from pathlib import Path logger = logging.getLogger(__name__) import icechunk import zarr def open_icechunk_dataset(file_path: Path, **kwargs) -> xr.Dataset: """ Load an Icechunk dataset using the Icechunk Python API..."*

#### 72. [Certain extension points of zarr are not implemented](https://github.com/zarr-developers/zarr-python/issues/3433) (#3433)
- **URL:** https://github.com/zarr-developers/zarr-python/issues/3433
- **Relevance Score:** `5` | **State:** `open` | **Author:** `remcofl`
- **Labels:** None
- **FS Keywords:** `filesystem`
- **Perf Keywords:** `io`
- **Excerpt:** *"Zarr is built with extensibility in mind with several extension points defined in the spec. However, zarr-python does not yet implement all these extension points. Notably, chunk grid and chunk key encoding are not extendable yet, and I believe storage transformers aren't even implemented altogether..."*

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

### [huggingface/datasets](https://github.com/huggingface/datasets) (4 issues)

#### 80. ["eval_strategy": "no" perform evaluation](https://github.com/huggingface/datasets/issues/8242) (#8242)
- **URL:** https://github.com/huggingface/datasets/issues/8242
- **Relevance Score:** `23` | **State:** `open` | **Author:** `SamuelLarkin`
- **Labels:** None
- **FS Keywords:** `fsspec`, `gcsfs`, `mmap`, `s3fs`
- **Perf Keywords:** `cache`, `hang`, `io`, `performance`, `speed`
- **Excerpt:** *"### Describe the bug Hi, I'm trying to train a diffusion model and I getting stuck with ``` strace -p 967873 strace: Process 967873 attached ioctl(9, _IOC(_IOC_READ|_IOC_WRITE, 0x46, 0x2a, 0x20), 0x7fff18579d90) = 0 ioctl(9, _IOC(_IOC_READ|_IOC_WRITE, 0x46, 0x2a, 0x20), 0x7fff18579d90) = 0 ``` But m..."*

#### 81. [`Dataset.map(num_proc=N)` worker crashes with `ValueError: I/O operation on closed file` when `finalize()` is interrupted](https://github.com/huggingface/datasets/issues/8491) (#8491)
- **URL:** https://github.com/huggingface/datasets/issues/8491
- **Relevance Score:** `11` | **State:** `open` | **Author:** `HowardZorn`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `hang`, `i/o`, `io`
- **Excerpt:** *"### Describe the bug We hit this while running Megatron-LM training through ms-swift, which uses `datasets` under the hood for preprocessing. Our preprocessing step calls `Dataset.map()` with a fairly aggressive `num_proc=512` on a ~25k-example JSONL file: ```bash swift --dataset_num_proc 512 --data..."*

#### 82. [Dataset Viewer fails on TSFile datasets](https://github.com/huggingface/datasets/issues/8256) (#8256)
- **URL:** https://github.com/huggingface/datasets/issues/8256
- **Relevance Score:** `8` | **State:** `open` | **Author:** `gengziyand`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`, `stall`
- **Excerpt:** *"### Describe the bug ## Description The Dataset Viewer fails when trying to display a dataset stored in TSFile format. The error shown by the viewer is: ```python ModuleNotFoundError: No module named 'tsfile' ### Steps to reproduce the bug # Dataset Viewer fails to load TSFile dataset due to missing..."*

#### 83. [`PandasArrayExtensionDtype._metadata` should be a tuple, not a string](https://github.com/huggingface/datasets/issues/8375) (#8375)
- **URL:** https://github.com/huggingface/datasets/issues/8375
- **Relevance Score:** `5` | **State:** `open` | **Author:** `kohankhaki`
- **Labels:** None
- **FS Keywords:** `fsspec`
- **Perf Keywords:** `io`
- **Excerpt:** *"### Describe the bug There's a small typo in `PandasArrayExtensionDtype` (`src/datasets/features/features.py`): ```python _metadata = "value_type" ``` Pandas expects `_metadata` to be a tuple of attribute names, like `("value_type",)`, not a plain string ([API documentation ref](https://pandas.pydat..."*

### [pytorch/pytorch](https://github.com/pytorch/pytorch) (2 issues)

#### 84. [[AOTInductor] mmap-backed constant mappings survive runner destruction](https://github.com/pytorch/pytorch/issues/193915) (#193915)
- **URL:** https://github.com/pytorch/pytorch/issues/193915
- **Relevance Score:** `27` | **State:** `open` | **Author:** `sujuyu`
- **Labels:** `module: memory usage`, `triaged`, `oncall: pt2`, `oncall: export`, `module: aotinductor`, `bot-triaged`
- **FS Keywords:** `mmap`
- **Perf Keywords:** `cache`, `caching`, `hang`, `io`, `prefetch`
- **Excerpt:** *"### 🐛 Describe the bug <!-- Suggested title: [AOTInductor] mmap-backed constant mappings survive runner destruction --> I reproduced this behavior in a rolling AOTInductor model-loading workload. I reviewed the report below and confirmed that the `/proc/self/maps` behavior matches my local testing. ..."*

#### 85. [[DCP] Dynamic `thread_count` auto-tuning for Distributed Checkpoint writers](https://github.com/pytorch/pytorch/issues/193804) (#193804)
- **URL:** https://github.com/pytorch/pytorch/issues/193804
- **Relevance Score:** `10` | **State:** `open` | **Author:** `Yonghui-Lee`
- **Labels:** None
- **FS Keywords:** `filesystem`, `fsspec`
- **Perf Keywords:** `io`, `latency`
- **Excerpt:** *"### 🚀 The feature, motivation and pitch PyTorch Distributed Checkpoint (DCP) supports multi-threaded parallel file writing via `FileSystemWriter(thread_count=...)` and `FsspecWriter(thread_count=...)`. When saving sharded state dicts (e.g. in FSDP / TP / ModelParallel), `_split_by_size_and_type` par..."*
