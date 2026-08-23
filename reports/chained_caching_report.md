# FSSPEC Chained Filesystems & Caching Layer Usage Report

- **Repositories Analyzed:** `21`
- **Repositories with Chaining / Caching Findings:** `5`
- **Total Files Scanned:** `18452`

---

## 📊 Chained Filesystem & Cache Strategy Matrix

| Repository | Total Findings | `simplecache::` | `filecache::` | `blockcache` | `DirFileSystem` | `ZipFileSystem` | Other Cache / Chaining |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [iterative/dvc](https://github.com/iterative/dvc) | **0** | - | - | - | - | - | - |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | **0** | - | - | - | - | - | - |
| [pydata/xarray](https://github.com/pydata/xarray) | **2** | [**2**](#pydata-xarray-chained-urls) | - | - | - | - | - |
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | **0** | - | - | - | - | - | - |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | **7** | - | [**7**](#pandas-dev-pandas-chained-urls) | - | - | - | - |
| [dask/dask](https://github.com/dask/dask) | **0** | - | - | - | - | - | - |
| [pytorch/torchtitan](https://github.com/pytorch/torchtitan) | **0** | - | - | - | - | - | - |
| [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) | **0** | - | - | - | - | - | - |
| [pola-rs/polars](https://github.com/pola-rs/polars) | **0** | - | - | - | - | - | - |
| [delta-io/delta-rs](https://github.com/delta-io/delta-rs) | **0** | - | - | - | - | - | - |
| [intake/intake](https://github.com/intake/intake) | **3** | [**3**](#intake-intake-chained-urls) | - | - | - | - | - |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | **0** | - | - | - | - | - | - |
| [modin-project/modin](https://github.com/modin-project/modin) | **0** | - | - | - | - | - | - |
| [apache/arrow](https://github.com/apache/arrow) | **0** | - | - | - | - | - | - |
| [huggingface/datasets](https://github.com/huggingface/datasets) | **7** | - | - | - | [**3**](#huggingface-datasets-dirfs) | - | 4 |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | **0** | - | - | - | - | - | - |
| [feast-dev/feast](https://github.com/feast-dev/feast) | **0** | - | - | - | - | - | - |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | **0** | - | - | - | - | - | - |
| [ray-project/ray](https://github.com/ray-project/ray) | **6** | - | - | - | [**2**](#ray-project-ray-dirfs) | [**4**](#ray-project-ray-zipfs) | - |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | **0** | - | - | - | - | - | - |
| [kedro-org/kedro](https://github.com/kedro-org/kedro) | **0** | - | - | - | - | - | - |

---

## 🔍 Detailed Chaining & Caching Findings by Repository

### [pydata/xarray](https://github.com/pydata/xarray)

#### <a id="pydata-xarray-chained-urls"></a>🔹 Chained URL Patterns (`proto::target_url`) (2 occurrences)

<details open>
<summary><b>View 2 Chained URL Call Site(s) in pydata/xarray</b></summary>

##### 1. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L7216) (Line 7216)
- **Protocol:** `simplecache::`
- **Full Match:** `"simplecache::memory://out2.zarr"`

```python
url = "simplecache::memory://out2.zarr"
```

##### 2. [xarray/tests/test_backends.py](https://github.com/pydata/xarray/blob/main/xarray/tests/test_backends.py#L7228) (Line 7228)
- **Protocol:** `simplecache::`
- **Full Match:** `"simplecache::memory://out*.zarr"`

```python
url = "simplecache::memory://out*.zarr"
```

</details>

### [pandas-dev/pandas](https://github.com/pandas-dev/pandas)

#### <a id="pandas-dev-pandas-chained-urls"></a>🔹 Chained URL Patterns (`proto::target_url`) (7 occurrences)

<details open>
<summary><b>View 7 Chained URL Call Site(s) in pandas-dev/pandas</b></summary>

##### 1. [pandas/tests/io/json/test_pandas.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/json/test_pandas.py#L2046) (Line 2046)
- **Protocol:** `filecache::`
- **Full Match:** `"filecache::s3://yet-another-fsspec/file.json"`

```python
"filecache::s3://yet-another-fsspec/file.json",
```

##### 2. [pandas/tests/io/test_common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_common.py#L516) (Line 516)
- **Protocol:** `filecache::`
- **Full Match:** `"filecache::s3://pandas/test.csv"`

```python
assert icom.is_fsspec_url("filecache::s3://pandas/test.csv")
```

##### 3. [pandas/tests/io/test_common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_common.py#L517) (Line 517)
- **Protocol:** `filecache::`
- **Full Match:** `filecache::gcs://bucket/file.zip"`

```python
assert icom.is_fsspec_url("zip://test.csv::filecache::gcs://bucket/file.zip")
```

##### 4. [pandas/tests/io/test_common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_common.py#L518) (Line 518)
- **Protocol:** `filecache::`
- **Full Match:** `"filecache::zip://test.csv::gcs://bucket/file.zip"`

```python
assert icom.is_fsspec_url("filecache::zip://test.csv::gcs://bucket/file.zip")
```

##### 5. [pandas/tests/io/test_common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_common.py#L519) (Line 519)
- **Protocol:** `filecache::`
- **Full Match:** `"filecache::dask::s3://pandas/test.csv"`

```python
assert icom.is_fsspec_url("filecache::dask::s3://pandas/test.csv")
```

##### 6. [pandas/tests/io/test_common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_common.py#L521) (Line 521)
- **Protocol:** `filecache::`
- **Full Match:** `"filecache:::s3://pandas/test.csv"`

```python
assert not icom.is_fsspec_url("filecache:::s3://pandas/test.csv")
```

##### 7. [pandas/tests/io/test_common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/test_common.py#L522) (Line 522)
- **Protocol:** `filecache::`
- **Full Match:** `"filecache::://pandas/test.csv"`

```python
assert not icom.is_fsspec_url("filecache::://pandas/test.csv")
```

</details>

### [intake/intake](https://github.com/intake/intake)

#### <a id="intake-intake-chained-urls"></a>🔹 Chained URL Patterns (`proto::target_url`) (3 occurrences)

<details open>
<summary><b>View 3 Chained URL Call Site(s) in intake/intake</b></summary>

##### 1. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L693) (Line 693)
- **Protocol:** `simplecache::`
- **Full Match:** `f"simplecache::{data.url}"`

```python
fs, path = fsspec.core.url_to_fs(f"simplecache::{data.url}", **options)
```

##### 2. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L736) (Line 736)
- **Protocol:** `simplecache::`
- **Full Match:** `f"simplecache::{v}"`

```python
path = fsspec.open_local(f"simplecache::{v}")
```

##### 3. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3514) (Line 3514)
- **Protocol:** `simplecache::`
- **Full Match:** `f"simplecache::{url}"`

```python
f"simplecache::{url}", **{"simplecache": {}, **(data.storage_options or {})}
```

</details>

### [huggingface/datasets](https://github.com/huggingface/datasets)

#### <a id="huggingface-datasets-chained-urls"></a>🔹 Chained URL Patterns (`proto::target_url`) (4 occurrences)

<details open>
<summary><b>View 4 Chained URL Call Site(s) in huggingface/datasets</b></summary>

##### 1. [tests/test_file_utils.py](https://github.com/huggingface/datasets/blob/main/tests/test_file_utils.py#L502) (Line 502)
- **Protocol:** `dir::`
- **Full Match:** `dir::"`

```python
assert len(xlistdir("zip://main_dir::" + root_url, download_config=download_config)) == 2
```

##### 2. [tests/test_file_utils.py](https://github.com/huggingface/datasets/blob/main/tests/test_file_utils.py#L531) (Line 531)
- **Protocol:** `dir::`
- **Full Match:** `dir::"`

```python
assert xisdir("zip://main_dir::" + root_url, download_config=download_config) is True
```

##### 3. [tests/test_file_utils.py](https://github.com/huggingface/datasets/blob/main/tests/test_file_utils.py#L664) (Line 664)
- **Protocol:** `dir::`
- **Full Match:** `dir::"`

```python
assert len(list(xwalk("zip://main_dir::" + root_url, download_config=download_config))) == 1
```

##### 4. [tests/test_file_utils.py](https://github.com/huggingface/datasets/blob/main/tests/test_file_utils.py#L829) (Line 829)
- **Protocol:** `dir::`
- **Full Match:** `dir::https://host.com/archive.zip"`

```python
("zip://dir/file.txt::https://host.com/archive.zip", "zip://dir::https://host.com/archive.zip"),
```

</details>

#### <a id="huggingface-datasets-cached-classes"></a><a id="huggingface-datasets-dirfs"></a><a id="huggingface-datasets-zipfs"></a>🔹 Chained / Cached Class Implementations (3 occurrences)

<details open>
<summary><b>View 3 Class References in huggingface/datasets</b></summary>

##### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L63) (Line 63)
- **Class:** `DirFileSystem` (DirFileSystem (subtree directory prefix wrapper))

```python
from fsspec.implementations.dirfs import DirFileSystem
```

##### 2. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L17) (Line 17)
- **Class:** `DirFileSystem` (DirFileSystem (subtree directory prefix wrapper))

```python
from fsspec.implementations.dirfs import DirFileSystem
```

##### 3. [tests/test_buckets.py](https://github.com/huggingface/datasets/blob/main/tests/test_buckets.py#L6) (Line 6)
- **Class:** `DirFileSystem` (DirFileSystem (subtree directory prefix wrapper))

```python
from fsspec.implementations.dirfs import DirFileSystem
```

</details>

### [ray-project/ray](https://github.com/ray-project/ray)

#### <a id="ray-project-ray-caching-fs"></a>🔹 Caching / Wrapper Filesystem Instantiations (2 occurrences)

<details open>
<summary><b>View 2 Filesystem Calls in ray-project/ray</b></summary>

##### 1. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L317) (Line 317)
- **Protocol:** `zip`

```python
self._fs = fsspec.filesystem("zip", fo=self.paths[0])
```

##### 2. [python/ray/data/tests/datasource/test_zarrv2.py](https://github.com/ray-project/ray/blob/master/python/ray/data/tests/datasource/test_zarrv2.py#L837) (Line 837)
- **Protocol:** `zip`

```python
zip_fs = fsspec.filesystem("zip", fo=str(zarr_zip_store))
```

</details>

#### <a id="ray-project-ray-cached-classes"></a><a id="ray-project-ray-dirfs"></a><a id="ray-project-ray-zipfs"></a>🔹 Chained / Cached Class Implementations (4 occurrences)

<details open>
<summary><b>View 4 Class References in ray-project/ray</b></summary>

##### 1. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L309) (Line 309)
- **Class:** `ZipFileSystem` (ZipFileSystem (in-memory ZIP archive wrapper))

```python
#   2. ``.zip`` URL/path: auto-wrap with fsspec's ZipFileSystem.
```

##### 2. [python/ray/data/tests/datasource/test_zarrv2.py](https://github.com/ray-project/ray/blob/master/python/ray/data/tests/datasource/test_zarrv2.py#L552) (Line 552)
- **Class:** `ZipFileSystem` (ZipFileSystem (in-memory ZIP archive wrapper))

```python
"""A local ``.zarr.zip`` path auto-wires fsspec's ZipFileSystem."""
```

##### 3. [python/ray/train/tests/test_new_persistence.py](https://github.com/ray-project/ray/blob/master/python/ray/train/tests/test_new_persistence.py#L74) (Line 74)
- **Class:** `DirFileSystem` (DirFileSystem (subtree directory prefix wrapper))

```python
from fsspec.implementations.dirfs import DirFileSystem
```

##### 4. [python/ray/train/v2/tests/test_persistence.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/tests/test_persistence.py#L75) (Line 75)
- **Class:** `DirFileSystem` (DirFileSystem (subtree directory prefix wrapper))

```python
from fsspec.implementations.dirfs import DirFileSystem
```

</details>
