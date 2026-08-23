# Master FSSPEC & Filesystem Method Usage Report

- **Repositories Crawled:** `21`
- **Total Files Scanned:** `9440`
- **Files with Method Usages:** `187`
- **Total Method Usages Detected:** `922`
- **Distinct Methods Detected:** `68`
- **Skipping Test Files (test_*.py):** `True`

---

## 📊 Repository Summary Table

| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Top Methods |
| :--- | :--- | :--- | :--- | :--- |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | `2556` | `19` | `57` | `f.write` (13), `f.close` (11), `f.flush` (4) |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | `300` | `3` | `13` | `fs.open` (5), `f.close` (2), `f.readable` (1) |
| [ray-project/ray](https://github.com/ray-project/ray) | `2022` | `21` | `54` | `f.close` (11), `f.read` (7), `f.seek` (6) |
| [pola-rs/polars](https://github.com/pola-rs/polars) | `212` | `1` | `2` | `fs.open` (1), `fs.open_files` (1) |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | `457` | `22` | `99` | `fs.exists` (24), `fs.open` (14), `fs.makedirs` (9) |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | `15` | `0` | `0` | None |
| [huggingface/datasets](https://github.com/huggingface/datasets) | `141` | `17` | `102` | `url_to_fs` (22), `fs.open` (17), `fs.isfile` (11) |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | `1301` | `3` | `3` | `f.read` (2), `f.close` (1) |
| [apache/arrow](https://github.com/apache/arrow) | `80` | `1` | `21` | `fs.rm` (4), `fs.open` (4), `fs.isfile` (3) |
| [iterative/dvc](https://github.com/iterative/dvc) | `258` | `51` | `282` | `fs.join` (56), `fs.relparts` (25), `fs.relpath` (24) |
| [dask/dask](https://github.com/dask/dask) | `184` | `16` | `76` | `fs.open` (16), `f.read` (10), `stringify_path` (9) |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | `0` | `0` | `0` | None |
| [modin-project/modin](https://github.com/modin-project/modin) | `283` | `8` | `52` | `url_to_fs` (11), `f.read` (8), `f.seek` (7) |
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | `242` | `0` | `0` | None |
| [feast-dev/feast](https://github.com/feast-dev/feast) | `600` | `5` | `13` | `fs.get` (7), `url_to_fs` (2), `fs.exists` (2) |
| [pydata/xarray](https://github.com/pydata/xarray) | `123` | `1` | `4` | `get_fs_token_paths` (2), `fs.glob` (1), `fs.open` (1) |
| [kedro-org/kedro](https://github.com/kedro-org/kedro) | `106` | `1` | `12` | `fsspec.filesystem` (4), `fs.ls` (3), `fs.isdir` (1) |
| [pytorch/torchtitan](https://github.com/pytorch/torchtitan) | `317` | `5` | `18` | `fs.join` (8), `fs.isdir` (2), `fs.isfile` (2) |
| [delta-io/delta-rs](https://github.com/delta-io/delta-rs) | `18` | `0` | `0` | None |
| [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) | `173` | `2` | `8` | `f.tell` (3), `f.seek` (3), `url_to_fs` (1) |
| [intake/intake](https://github.com/intake/intake) | `52` | `11` | `106` | `fs.open` (45), `f.read` (22), `open_files` (6) |

---

## 📊 Repository × Target Call Usage Matrix (68 Methods)

| Repository | Total Calls | `fs.open` | `fs.join` | `f.read` | `fs.exists` | `url_to_fs` | `fs.isdir` | `f.close` | `f.write` | `fs.isfile` | `fs.info` | `fs.relparts` | `fs.relpath` | `fs.ls` | `fs.makedirs` | `f.seek` | `fs.abspath` | `fs.get` | `f.tell` | `fs.getcwd` | `fs.glob` | `fs.parts` | `fs.normpath` | `open_files` | `fs.rm` | `fs.find` | `f.flush` | `get_fs_token_paths` | `fs.isin` | `fsspec.filesystem` | `f.readline` | `stringify_path` | `fs.listdir` | `fs.walk` | `fs.split` | `fs.read_text` | `fs.get_file` | `fs.put` | `fs.open_local` | `fs.move` | `fs.open_files` | `fs.rename` | `fs.mkdir` | `fs.rm_file` | `f.readlines` | `fs.mv` | `fs.close` | `fs.chdir` | `fs.as_posix` | `fs.du` | `fs.ukey` | `fs.read_block` | `infer_compression` | `expand_paths_if_needed` | `fs.cat_file` | `fs.cat` | `fs.flush` | `f.readable` | `f.seekable` | `f.writable` | `f.writelines` | `fs.rmdir` | `fs.size` | `fs.copy` | `fs.commonpath` | `fs.expand_path` | `fs.checksum` | `fsspec.open_parquet_file` | `get_filesystem_class` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | **57** | [**1**](#pytorch-pytorch-fs-open) | [**1**](#pytorch-pytorch-fs-join) | [**4**](#pytorch-pytorch-f-read) | [**4**](#pytorch-pytorch-fs-exists) | [**2**](#pytorch-pytorch-url-to-fs) | [**1**](#pytorch-pytorch-fs-isdir) | [**11**](#pytorch-pytorch-f-close) | [**13**](#pytorch-pytorch-f-write) | - | - | - | - | [**2**](#pytorch-pytorch-fs-ls) | [**2**](#pytorch-pytorch-fs-makedirs) | - | - | [**1**](#pytorch-pytorch-fs-get) | [**2**](#pytorch-pytorch-f-tell) | - | - | - | - | - | [**1**](#pytorch-pytorch-fs-rm) | - | [**4**](#pytorch-pytorch-f-flush) | - | - | - | [**1**](#pytorch-pytorch-f-readline) | - | - | - | [**1**](#pytorch-pytorch-fs-split) | - | - | [**1**](#pytorch-pytorch-fs-put) | - | - | - | [**2**](#pytorch-pytorch-fs-rename) | [**1**](#pytorch-pytorch-fs-mkdir) | [**1**](#pytorch-pytorch-fs-rm-file) | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#pytorch-pytorch-fs-flush) | - | - | - | - | - | - | - | - | - | - | - | - |
| [pandas-dev/pandas](https://github.com/pandas-dev/pandas) | **13** | [**5**](#pandas-dev-pandas-fs-open) | - | [**1**](#pandas-dev-pandas-f-read) | - | [**1**](#pandas-dev-pandas-url-to-fs) | - | [**2**](#pandas-dev-pandas-f-close) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#pandas-dev-pandas-f-flush) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#pandas-dev-pandas-f-readable) | [**1**](#pandas-dev-pandas-f-seekable) | [**1**](#pandas-dev-pandas-f-writable) | - | - | - | - | - | - | - | - | - |
| [ray-project/ray](https://github.com/ray-project/ray) | **54** | [**5**](#ray-project-ray-fs-open) | - | [**7**](#ray-project-ray-f-read) | [**1**](#ray-project-ray-fs-exists) | [**1**](#ray-project-ray-url-to-fs) | - | [**11**](#ray-project-ray-f-close) | [**5**](#ray-project-ray-f-write) | - | - | - | - | - | - | [**6**](#ray-project-ray-f-seek) | - | [**1**](#ray-project-ray-fs-get) | [**3**](#ray-project-ray-f-tell) | - | - | - | - | - | - | - | [**5**](#ray-project-ray-f-flush) | - | - | [**1**](#ray-project-ray-fsspec-filesystem) | [**3**](#ray-project-ray-f-readline) | - | - | - | [**1**](#ray-project-ray-fs-split) | - | - | - | - | [**2**](#ray-project-ray-fs-move) | - | - | - | - | [**1**](#ray-project-ray-f-readlines) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#ray-project-ray-f-writelines) | - | - | - | - | - | - | - | - |
| [pola-rs/polars](https://github.com/pola-rs/polars) | **2** | [**1**](#pola-rs-polars-fs-open) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#pola-rs-polars-fs-open-files) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning) | **99** | [**14**](#lightning-ai-pytorch-lightning-fs-open) | - | - | [**24**](#lightning-ai-pytorch-lightning-fs-exists) | [**3**](#lightning-ai-pytorch-lightning-url-to-fs) | [**8**](#lightning-ai-pytorch-lightning-fs-isdir) | [**1**](#lightning-ai-pytorch-lightning-f-close) | [**2**](#lightning-ai-pytorch-lightning-f-write) | [**6**](#lightning-ai-pytorch-lightning-fs-isfile) | [**3**](#lightning-ai-pytorch-lightning-fs-info) | - | - | [**6**](#lightning-ai-pytorch-lightning-fs-ls) | [**9**](#lightning-ai-pytorch-lightning-fs-makedirs) | - | - | [**7**](#lightning-ai-pytorch-lightning-fs-get) | - | - | - | - | - | - | [**5**](#lightning-ai-pytorch-lightning-fs-rm) | - | [**1**](#lightning-ai-pytorch-lightning-f-flush) | - | - | - | - | - | [**5**](#lightning-ai-pytorch-lightning-fs-listdir) | - | - | - | - | [**3**](#lightning-ai-pytorch-lightning-fs-put) | - | - | - | - | - | [**1**](#lightning-ai-pytorch-lightning-fs-rm-file) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#lightning-ai-pytorch-lightning-fs-rmdir) | - | - | - | - | - | - | - |
| [duckdb/duckdb](https://github.com/duckdb/duckdb) | **0** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [huggingface/datasets](https://github.com/huggingface/datasets) | **102** | [**17**](#huggingface-datasets-fs-open) | - | [**6**](#huggingface-datasets-f-read) | [**4**](#huggingface-datasets-fs-exists) | [**22**](#huggingface-datasets-url-to-fs) | [**3**](#huggingface-datasets-fs-isdir) | [**4**](#huggingface-datasets-f-close) | [**8**](#huggingface-datasets-f-write) | [**11**](#huggingface-datasets-fs-isfile) | [**4**](#huggingface-datasets-fs-info) | - | - | - | [**3**](#huggingface-datasets-fs-makedirs) | - | - | - | - | - | [**8**](#huggingface-datasets-fs-glob) | - | - | - | - | - | - | [**1**](#huggingface-datasets-get-fs-token-paths) | - | [**1**](#huggingface-datasets-fsspec-filesystem) | - | - | [**1**](#huggingface-datasets-fs-listdir) | [**1**](#huggingface-datasets-fs-walk) | - | [**5**](#huggingface-datasets-fs-read-text) | [**1**](#huggingface-datasets-fs-get-file) | - | - | - | - | - | - | - | - | [**1**](#huggingface-datasets-fs-mv) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#huggingface-datasets-fs-size) | - | - | - | - | - | - |
| [mlflow/mlflow](https://github.com/mlflow/mlflow) | **3** | - | - | [**2**](#mlflow-mlflow-f-read) | - | - | - | [**1**](#mlflow-mlflow-f-close) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [apache/arrow](https://github.com/apache/arrow) | **21** | [**4**](#apache-arrow-fs-open) | - | - | [**2**](#apache-arrow-fs-exists) | - | [**2**](#apache-arrow-fs-isdir) | - | - | [**3**](#apache-arrow-fs-isfile) | [**1**](#apache-arrow-fs-info) | - | - | - | - | - | - | - | - | - | - | - | - | - | [**4**](#apache-arrow-fs-rm) | [**1**](#apache-arrow-fs-find) | - | - | - | - | - | - | [**1**](#apache-arrow-fs-listdir) | - | - | - | - | - | - | - | - | - | [**1**](#apache-arrow-fs-mkdir) | - | - | [**1**](#apache-arrow-fs-mv) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#apache-arrow-fs-copy) | - | - | - | - | - |
| [iterative/dvc](https://github.com/iterative/dvc) | **282** | [**11**](#iterative-dvc-fs-open) | [**56**](#iterative-dvc-fs-join) | [**3**](#iterative-dvc-f-read) | [**20**](#iterative-dvc-fs-exists) | - | [**16**](#iterative-dvc-fs-isdir) | [**2**](#iterative-dvc-f-close) | [**2**](#iterative-dvc-f-write) | [**5**](#iterative-dvc-fs-isfile) | [**12**](#iterative-dvc-fs-info) | [**25**](#iterative-dvc-fs-relparts) | [**24**](#iterative-dvc-fs-relpath) | [**6**](#iterative-dvc-fs-ls) | [**4**](#iterative-dvc-fs-makedirs) | - | [**17**](#iterative-dvc-fs-abspath) | - | - | [**14**](#iterative-dvc-fs-getcwd) | - | [**13**](#iterative-dvc-fs-parts) | [**13**](#iterative-dvc-fs-normpath) | - | - | [**7**](#iterative-dvc-fs-find) | - | - | [**11**](#iterative-dvc-fs-isin) | - | - | - | - | [**5**](#iterative-dvc-fs-walk) | [**3**](#iterative-dvc-fs-split) | - | [**3**](#iterative-dvc-fs-get-file) | - | - | [**1**](#iterative-dvc-fs-move) | - | - | - | - | [**1**](#iterative-dvc-f-readlines) | - | [**1**](#iterative-dvc-fs-close) | [**2**](#iterative-dvc-fs-chdir) | [**2**](#iterative-dvc-fs-as-posix) | [**2**](#iterative-dvc-fs-du) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#iterative-dvc-fs-commonpath) | - | - | - | - |
| [dask/dask](https://github.com/dask/dask) | **76** | [**16**](#dask-dask-fs-open) | - | [**10**](#dask-dask-f-read) | [**2**](#dask-dask-fs-exists) | - | [**2**](#dask-dask-fs-isdir) | [**2**](#dask-dask-f-close) | [**2**](#dask-dask-f-write) | [**1**](#dask-dask-fs-isfile) | [**2**](#dask-dask-fs-info) | - | - | - | - | [**1**](#dask-dask-f-seek) | - | - | [**1**](#dask-dask-f-tell) | - | - | - | - | [**7**](#dask-dask-open-files) | [**1**](#dask-dask-fs-rm) | [**2**](#dask-dask-fs-find) | - | [**7**](#dask-dask-get-fs-token-paths) | - | - | - | [**9**](#dask-dask-stringify-path) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**2**](#dask-dask-fs-ukey) | [**2**](#dask-dask-fs-read-block) | [**2**](#dask-dask-infer-compression) | [**2**](#dask-dask-expand-paths-if-needed) | - | - | - | - | - | - | - | - | - | - | - | [**1**](#dask-dask-fs-expand-path) | [**1**](#dask-dask-fs-checksum) | [**1**](#dask-dask-fsspec-open-parquet-file) | - |
| [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations) | **0** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [modin-project/modin](https://github.com/modin-project/modin) | **52** | [**5**](#modin-project-modin-fs-open) | - | [**8**](#modin-project-modin-f-read) | [**4**](#modin-project-modin-fs-exists) | [**11**](#modin-project-modin-url-to-fs) | - | [**1**](#modin-project-modin-f-close) | - | [**1**](#modin-project-modin-fs-isfile) | - | - | - | - | - | [**7**](#modin-project-modin-f-seek) | - | - | [**5**](#modin-project-modin-f-tell) | - | [**2**](#modin-project-modin-fs-glob) | - | - | - | - | [**2**](#modin-project-modin-fs-find) | - | - | - | - | [**5**](#modin-project-modin-f-readline) | - | - | [**1**](#modin-project-modin-fs-walk) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [flyteorg/flyte](https://github.com/flyteorg/flyte) | **0** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [feast-dev/feast](https://github.com/feast-dev/feast) | **13** | - | [**2**](#feast-dev-feast-fs-join) | - | [**2**](#feast-dev-feast-fs-exists) | [**2**](#feast-dev-feast-url-to-fs) | - | - | - | - | - | - | - | - | - | - | - | [**7**](#feast-dev-feast-fs-get) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [pydata/xarray](https://github.com/pydata/xarray) | **4** | [**1**](#pydata-xarray-fs-open) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#pydata-xarray-fs-glob) | - | - | - | - | - | - | [**2**](#pydata-xarray-get-fs-token-paths) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [kedro-org/kedro](https://github.com/kedro-org/kedro) | **12** | [**1**](#kedro-org-kedro-fs-open) | - | [**1**](#kedro-org-kedro-f-read) | - | - | [**1**](#kedro-org-kedro-fs-isdir) | - | - | [**1**](#kedro-org-kedro-fs-isfile) | - | - | - | [**3**](#kedro-org-kedro-fs-ls) | - | - | - | - | - | - | [**1**](#kedro-org-kedro-fs-glob) | - | - | - | - | - | - | - | - | [**4**](#kedro-org-kedro-fsspec-filesystem) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [pytorch/torchtitan](https://github.com/pytorch/torchtitan) | **18** | - | [**8**](#pytorch-torchtitan-fs-join) | - | [**1**](#pytorch-torchtitan-fs-exists) | [**1**](#pytorch-torchtitan-url-to-fs) | [**2**](#pytorch-torchtitan-fs-isdir) | - | - | [**2**](#pytorch-torchtitan-fs-isfile) | - | - | - | [**1**](#pytorch-torchtitan-fs-ls) | - | - | - | - | - | - | - | - | - | - | [**1**](#pytorch-torchtitan-fs-rm) | - | - | - | - | - | - | - | [**1**](#pytorch-torchtitan-fs-listdir) | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#pytorch-torchtitan-fs-close) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [delta-io/delta-rs](https://github.com/delta-io/delta-rs) | **0** | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python) | **8** | - | - | [**1**](#zarr-developers-zarr-python-f-read) | - | [**1**](#zarr-developers-zarr-python-url-to-fs) | - | - | - | - | - | - | - | - | - | [**3**](#zarr-developers-zarr-python-f-seek) | - | - | [**3**](#zarr-developers-zarr-python-f-tell) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| [intake/intake](https://github.com/intake/intake) | **106** | [**45**](#intake-intake-fs-open) | - | [**22**](#intake-intake-f-read) | - | [**6**](#intake-intake-url-to-fs) | [**1**](#intake-intake-fs-isdir) | - | [**1**](#intake-intake-f-write) | - | [**3**](#intake-intake-fs-info) | - | - | [**3**](#intake-intake-fs-ls) | - | [**1**](#intake-intake-f-seek) | - | - | - | - | [**1**](#intake-intake-fs-glob) | - | - | [**6**](#intake-intake-open-files) | - | - | - | [**1**](#intake-intake-get-fs-token-paths) | - | [**4**](#intake-intake-fsspec-filesystem) | - | - | - | - | - | - | [**1**](#intake-intake-fs-get-file) | - | [**4**](#intake-intake-fs-open-local) | - | [**2**](#intake-intake-fs-open-files) | - | - | - | - | - | - | - | - | - | - | - | - | - | [**2**](#intake-intake-fs-cat-file) | [**2**](#intake-intake-fs-cat) | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#intake-intake-get-filesystem-class) |

---

## 🔍 Detailed Usage Breakdown by Repository

### [pytorch/pytorch](https://github.com/pytorch/pytorch)
- **Files Scanned:** `2556` | **Files with Usages:** `19` | **Total Usages:** `57`

#### <a id="pytorch-pytorch-f-write"></a>🔹 `f.write` (13 occurrences)

<details open>
<summary><b>Click to expand/collapse 13 occurrences for <code>f.write</code> in pytorch/pytorch</b></summary>

##### 1. [torch/_inductor/runtime/caching/implementations.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/runtime/caching/implementations.py#L338) (Line 338)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/runtime/caching/implementations.py#L338
- **Target Call:** `f.write`
- **Context:** `_OnDiskCacheImpl.insert`
- **Arguments:** `value`
- **Keywords:** `{}`

```python
                    w_fp.write(value)
```

##### 2. [torch/_logging/_internal.py](https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1095) (Line 1095)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1095
- **Target Call:** `f.write`
- **Context:** `_StderrHandler.emit`
- **Arguments:** `msg + self.terminator`
- **Keywords:** `{}`

```python
            stream.write(msg + self.terminator)
```

##### 3. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L141) (Line 141)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L141
- **Target Call:** `f.write`
- **Context:** `_send`
- **Arguments:** `struct.pack('<I', len(data))`
- **Keywords:** `{}`

```python
    stream.write(struct.pack("<I", len(data)))
```

##### 4. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L142) (Line 142)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L142
- **Target Call:** `f.write`
- **Context:** `_send`
- **Arguments:** `data`
- **Keywords:** `{}`

```python
    stream.write(data)
```

##### 5. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L407) (Line 407)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L407
- **Target Call:** `f.write`
- **Context:** `Autotuner._send`
- **Arguments:** `struct.pack('<I', len(data))`
- **Keywords:** `{}`

```python
            stream.write(struct.pack("<I", len(data)))
```

##### 6. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L408) (Line 408)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L408
- **Target Call:** `f.write`
- **Context:** `Autotuner._send`
- **Arguments:** `data`
- **Keywords:** `{}`

```python
            stream.write(data)
```

##### 7. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L459) (Line 459)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L459
- **Target Call:** `f.write`
- **Context:** `_write_files_from_queue`
- **Arguments:** `save(tensor_dict, metadata={CUSTOM_METADATA_KEY: json.dumps(metadata_dict), DCP_VERSION_KEY: str(HF_DCP_VERSION), FORMAT_KEY: FORMAT_VALUE})`
- **Keywords:** `{}`

```python
                    stream.write(
                        save(
                            tensor_dict,
                            metadata={
                                CUSTOM_METADATA_KEY: json.dumps(metadata_dict),
                                DCP_VERSION_KEY: str(HF_DCP_VERSION),
                                FORMAT_KEY: FORMAT_VALUE,
                            },
                        )
                    )
```

##### 8. [torch/hub.py](https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L771) (Line 771)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L771
- **Target Call:** `f.write`
- **Context:** `download_url_to_file`
- **Arguments:** `buffer`
- **Keywords:** `{}`

```python
                    f.write(buffer)
```

##### 9. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L31) (Line 31)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L31
- **Target Call:** `f.write`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `repr(obj)`
- **Keywords:** `{}`

```python
            stream.write(repr(obj))
```

##### 10. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L34) (Line 34)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L34
- **Target Call:** `f.write`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `f'{obj.module}.{obj.name}'`
- **Keywords:** `{}`

```python
            stream.write(f"{obj.module}.{obj.name}")
```

##### 11. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L38) (Line 38)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L38
- **Target Call:** `f.write`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `f'{obj.module}.{obj.name}()(state=\n'`
- **Keywords:** `{}`

```python
            stream.write(f"{obj.module}.{obj.name}()(state=\n")
```

##### 12. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L40) (Line 40)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L40
- **Target Call:** `f.write`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `' ' * indent`
- **Keywords:** `{}`

```python
            stream.write(" " * indent)
```

##### 13. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L42) (Line 42)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L42
- **Target Call:** `f.write`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `')'`
- **Keywords:** `{}`

```python
            stream.write(")")
```

</details>

#### <a id="pytorch-pytorch-f-close"></a>🔹 `f.close` (11 occurrences)

<details open>
<summary><b>Click to expand/collapse 11 occurrences for <code>f.close</code> in pytorch/pytorch</b></summary>

##### 1. [torch/_inductor/compile_worker/subproc_pool.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/compile_worker/subproc_pool.py#L620) (Line 620)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/compile_worker/subproc_pool.py#L620
- **Target Call:** `f.close`
- **Context:** `SubprocPool.shutdown`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                self.log_file.close()
```

##### 2. [torch/_inductor/runtime/caching/implementations.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/runtime/caching/implementations.py#L341) (Line 341)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/runtime/caching/implementations.py#L341
- **Target Call:** `f.close`
- **Context:** `_OnDiskCacheImpl.insert`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    w_fp.close()
```

##### 3. [torch/_logging/_internal.py](https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1274) (Line 1274)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1274
- **Target Call:** `f.close`
- **Context:** `LazyTraceHandler._close_stream`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    stream.close()
```

##### 4. [torch/_logging/_internal.py](https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1281) (Line 1281)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1281
- **Target Call:** `f.close`
- **Context:** `LazyTraceHandler._close_stream`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                        stream.close()
```

##### 5. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L479) (Line 479)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L479
- **Target Call:** `f.close`
- **Context:** `_write_files_from_queue`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                stream.close()
```

##### 6. [torch/distributed/elastic/multiprocessing/api.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/multiprocessing/api.py#L665) (Line 665)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/multiprocessing/api.py#L665
- **Target Call:** `f.close`
- **Context:** `PContext.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.filtered_stdout.close()
```

##### 7. [torch/distributed/elastic/multiprocessing/api.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/multiprocessing/api.py#L667) (Line 667)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/multiprocessing/api.py#L667
- **Target Call:** `f.close`
- **Context:** `PContext.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.filtered_stderr.close()
```

##### 8. [torch/hub.py](https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L776) (Line 776)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L776
- **Target Call:** `f.close`
- **Context:** `download_url_to_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            f.close()
```

##### 9. [torch/hub.py](https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L785) (Line 785)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L785
- **Target Call:** `f.close`
- **Context:** `download_url_to_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        f.close()
```

##### 10. [torch/serialization.py](https://github.com/pytorch/pytorch/blob/main/torch/serialization.py#L836) (Line 836)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/serialization.py#L836
- **Target Call:** `f.close`
- **Context:** `_open_zipfile_writer_file.__exit__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.file_stream.close()
```

##### 11. [torch/utils/data/datapipes/utils/common.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/data/datapipes/utils/common.py#L378) (Line 378)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/data/datapipes/utils/common.py#L378
- **Target Call:** `f.close`
- **Context:** `StreamWrapper.close`
- **Arguments:** `*args`
- **Keywords:** `{}`

```python
            self.file_obj.close(*args, **kwargs)
```

</details>

#### <a id="pytorch-pytorch-f-flush"></a>🔹 `f.flush` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>f.flush</code> in pytorch/pytorch</b></summary>

##### 1. [torch/_logging/_internal.py](https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1087) (Line 1087)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1087
- **Target Call:** `f.flush`
- **Context:** `_StderrHandler.flush`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                stream.flush()
```

##### 2. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L143) (Line 143)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L143
- **Target Call:** `f.flush`
- **Context:** `_send`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    stream.flush()
```

##### 3. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L409) (Line 409)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L409
- **Target Call:** `f.flush`
- **Context:** `Autotuner._send`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            stream.flush()
```

##### 4. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L472) (Line 472)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L472
- **Target Call:** `f.flush`
- **Context:** `_write_files_from_queue`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    stream.flush()
```

</details>

#### <a id="pytorch-pytorch-f-read"></a>🔹 `f.read` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>f.read</code> in pytorch/pytorch</b></summary>

##### 1. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L128) (Line 128)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L128
- **Target Call:** `f.read`
- **Context:** `_recv`
- **Arguments:** `4`
- **Keywords:** `{}`

```python
    header = stream.read(4)
```

##### 2. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L134) (Line 134)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L134
- **Target Call:** `f.read`
- **Context:** `_recv`
- **Arguments:** `length`
- **Keywords:** `{}`

```python
    data = stream.read(length)
```

##### 3. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L266) (Line 266)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L266
- **Target Call:** `f.read`
- **Context:** `_recv_from_worker`
- **Arguments:** `4`
- **Keywords:** `{}`

```python
    header = stream.read(4)
```

##### 4. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L272) (Line 272)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L272
- **Target Call:** `f.read`
- **Context:** `_recv_from_worker`
- **Arguments:** `length`
- **Keywords:** `{}`

```python
    body = stream.read(length)
```

</details>

#### <a id="pytorch-pytorch-fs-exists"></a>🔹 `fs.exists` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fs.exists</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L84) (Line 84)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L84
- **Target Call:** `fs.exists`
- **Context:** `FileSystem.exists`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return self.fs.exists(path)
```

##### 2. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L653) (Line 653)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L653
- **Target Call:** `fs.exists`
- **Context:** `_FileSystemWriter._metadata_exists`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python
        return self.fs.exists(metadata_path)
```

##### 3. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L795) (Line 795)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L795
- **Target Call:** `fs.exists`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python
        if self.fs.exists(metadata_path):
```

##### 4. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L920) (Line 920)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L920
- **Target Call:** `fs.exists`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
        if fs.exists(save_path):
```

</details>

#### <a id="pytorch-pytorch-url-to-fs"></a>🔹 `url_to_fs` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>url_to_fs</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L62) (Line 62)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L62
- **Target Call:** `url_to_fs`
- **Context:** `FileSystem.init_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs, _ = url_to_fs(path, **kwargs)
```

##### 2. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L77) (Line 77)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L77
- **Target Call:** `url_to_fs`
- **Context:** `FileSystem.validate_checkpoint_id`
- **Arguments:** `checkpoint_id`
- **Keywords:** `{}`

```python
            url_to_fs(checkpoint_id)
```

</details>

#### <a id="pytorch-pytorch-fs-rename"></a>🔹 `fs.rename` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.rename</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L66) (Line 66)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L66
- **Target Call:** `fs.rename`
- **Context:** `FileSystem.rename`
- **Arguments:** `path, new_path`
- **Keywords:** `{}`

```python
        self.fs.rename(path, new_path)
```

##### 2. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L798) (Line 798)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L798
- **Target Call:** `fs.rename`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `tmp_path, metadata_path`
- **Keywords:** `{}`

```python
        self.fs.rename(tmp_path, metadata_path)
```

</details>

#### <a id="pytorch-pytorch-fs-makedirs"></a>🔹 `fs.makedirs` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.makedirs</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L69) (Line 69)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L69
- **Target Call:** `fs.makedirs`
- **Context:** `FileSystem.mkdir`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        self.fs.makedirs(path, exist_ok=True)
```

##### 2. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L930) (Line 930)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L930
- **Target Call:** `fs.makedirs`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
            fs.makedirs(save_path)
```

</details>

#### <a id="pytorch-pytorch-fs-ls"></a>🔹 `fs.ls` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.ls</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L92) (Line 92)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L92
- **Target Call:** `fs.ls`
- **Context:** `FileSystem.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'False'}`

```python
        return self.fs.ls(path, detail=False)
```

##### 2. [torch/distributed/checkpoint/hf_storage.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L321) (Line 321)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L321
- **Target Call:** `fs.ls`
- **Context:** `HuggingFaceStorageReader.read_metadata`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        for file in self.fs.ls(self.path):
```

</details>

#### <a id="pytorch-pytorch-f-tell"></a>🔹 `f.tell` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>f.tell</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L328) (Line 328)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L328
- **Target Call:** `f.tell`
- **Context:** `_write_item`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    offset = stream.tell()
```

##### 2. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L353) (Line 353)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L353
- **Target Call:** `f.tell`
- **Context:** `_write_item`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        length = stream.tell() - offset
```

</details>

#### <a id="pytorch-pytorch-fs-get"></a>🔹 `fs.get` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.get</code> in pytorch/pytorch</b></summary>

##### 1. [torch/_inductor/remote_cache.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/remote_cache.py#L247) (Line 247)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/remote_cache.py#L247
- **Target Call:** `fs.get`
- **Context:** `RemoteCache._backend_get`
- **Arguments:** `key`
- **Keywords:** `{}`

```python
        return self.backend.get(key)
```

</details>

#### <a id="pytorch-pytorch-fs-put"></a>🔹 `fs.put` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.put</code> in pytorch/pytorch</b></summary>

##### 1. [torch/_inductor/remote_cache.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/remote_cache.py#L259) (Line 259)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/remote_cache.py#L259
- **Target Call:** `fs.put`
- **Context:** `RemoteCache._backend_put`
- **Arguments:** `key, data`
- **Keywords:** `{}`

```python
        self.backend.put(key, data)
```

</details>

#### <a id="pytorch-pytorch-fs-flush"></a>🔹 `fs.flush` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.flush</code> in pytorch/pytorch</b></summary>

##### 1. [torch/_inductor/scheduler.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/scheduler.py#L9844) (Line 9844)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/scheduler.py#L9844
- **Target Call:** `fs.flush`
- **Context:** `Scheduler.flush`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            backend.flush()
```

</details>

#### <a id="pytorch-pytorch-fs-open"></a>🔹 `fs.open` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.open</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L47) (Line 47)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L47
- **Target Call:** `fs.open`
- **Context:** `FileSystem.create_stream`
- **Arguments:** `path, mode`
- **Keywords:** `{}`

```python
        with self.fs.open(path, mode) as stream:
```

</details>

#### <a id="pytorch-pytorch-fs-rm"></a>🔹 `fs.rm` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.rm</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L87) (Line 87)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L87
- **Target Call:** `fs.rm`
- **Context:** `FileSystem.rm_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs.rm(path)
```

</details>

#### <a id="pytorch-pytorch-fs-mkdir"></a>🔹 `fs.mkdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.mkdir</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L656) (Line 656)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L656
- **Target Call:** `fs.mkdir`
- **Context:** `_FileSystemWriter.prepare_local_plan`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        self.fs.mkdir(self.path)
```

</details>

#### <a id="pytorch-pytorch-fs-rm-file"></a>🔹 `fs.rm_file` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.rm_file</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L796) (Line 796)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L796
- **Target Call:** `fs.rm_file`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python
            self.fs.rm_file(metadata_path)
```

</details>

#### <a id="pytorch-pytorch-fs-split"></a>🔹 `fs.split` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.split</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/distributed_c10d.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/distributed_c10d.py#L1083) (Line 1083)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/distributed_c10d.py#L1083
- **Target Call:** `fs.split`
- **Context:** `_parse_backend_string`
- **Arguments:** `','`
- **Keywords:** `{}`

```python
        for part in backend.split(","):
```

</details>

#### <a id="pytorch-pytorch-f-readline"></a>🔹 `f.readline` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.readline</code> in pytorch/pytorch</b></summary>

##### 1. [torch/distributed/elastic/timer/file_based_local_timer.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/timer/file_based_local_timer.py#L379) (Line 379)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/timer/file_based_local_timer.py#L379
- **Target Call:** `f.readline`
- **Context:** `FileTimerServer._get_requests`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            json_request = fd.readline()
```

</details>

#### <a id="pytorch-pytorch-fs-join"></a>🔹 `fs.join` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.join</code> in pytorch/pytorch</b></summary>

##### 1. [torch/utils/tensorboard/_embedding.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/_embedding.py#L21) (Line 21)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/_embedding.py#L21
- **Target Call:** `fs.join`
- **Context:** `_gfile_join`
- **Arguments:** `a, b`
- **Keywords:** `{}`

```python
        return fs.join(a, b)
```

</details>

#### <a id="pytorch-pytorch-fs-isdir"></a>🔹 `fs.isdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.isdir</code> in pytorch/pytorch</b></summary>

##### 1. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L921) (Line 921)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L921
- **Target Call:** `fs.isdir`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
            if fs.isdir(save_path):
```

</details>

### [pandas-dev/pandas](https://github.com/pandas-dev/pandas)
- **Files Scanned:** `300` | **Files with Usages:** `3` | **Total Usages:** `13`

#### <a id="pandas-dev-pandas-fs-open"></a>🔹 `fs.open` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>fs.open</code> in pandas-dev/pandas</b></summary>

##### 1. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L453) (Line 453)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L453
- **Target Call:** `fs.open`
- **Context:** `_get_filepath_or_buffer`
- **Arguments:** `filepath_or_buffer`
- **Keywords:** `{'mode': 'fsspec_mode'}`

```python
            open_file = fsspec.open(
                filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
            )
```

##### 2. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L465) (Line 465)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L465
- **Target Call:** `fs.open`
- **Context:** `_get_filepath_or_buffer`
- **Arguments:** `filepath_or_buffer`
- **Keywords:** `{'mode': 'fsspec_mode'}`

```python
            open_file = fsspec.open(
                filepath_or_buffer, mode=fsspec_mode, **(storage_options or {})
            )
```

##### 3. [pandas/io/parquet.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L347) (Line 347)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L347
- **Target Call:** `fs.open`
- **Context:** `FastParquetImpl.write`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            kwargs["open_with"] = lambda path, _: fsspec.open(
                path, "wb", **(storage_options or {})
            ).open()
```

##### 4. [pandas/io/parquet.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L347) (Line 347)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L347
- **Target Call:** `fs.open`
- **Context:** `FastParquetImpl.write`
- **Arguments:** `path, 'wb'`
- **Keywords:** `{}`

```python
            kwargs["open_with"] = lambda path, _: fsspec.open(
                path, "wb", **(storage_options or {})
            ).open()
```

##### 5. [pandas/io/parquet.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L397) (Line 397)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L397
- **Target Call:** `fs.open`
- **Context:** `FastParquetImpl.read`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
            parquet_kwargs["fs"] = fsspec.open(path, "rb", **(storage_options or {})).fs
```

</details>

#### <a id="pandas-dev-pandas-f-close"></a>🔹 `f.close` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>f.close</code> in pandas-dev/pandas</b></summary>

##### 1. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1241) (Line 1241)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1241
- **Target Call:** `f.close`
- **Context:** `_maybe_memory_map`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            handle.close()  # type: ignore[attr-defined]
```

##### 2. [pandas/io/pytables.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/pytables.py#L841) (Line 841)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/pytables.py#L841
- **Target Call:** `f.close`
- **Context:** `HDFStore.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self._handle.close()
```

</details>

#### <a id="pandas-dev-pandas-f-readable"></a>🔹 `f.readable` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.readable</code> in pandas-dev/pandas</b></summary>

##### 1. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1159) (Line 1159)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1159
- **Target Call:** `f.readable`
- **Context:** `_IOWrapper.readable`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            return self.buffer.readable()
```

</details>

#### <a id="pandas-dev-pandas-f-seekable"></a>🔹 `f.seekable` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.seekable</code> in pandas-dev/pandas</b></summary>

##### 1. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1164) (Line 1164)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1164
- **Target Call:** `f.seekable`
- **Context:** `_IOWrapper.seekable`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            return self.buffer.seekable()
```

</details>

#### <a id="pandas-dev-pandas-f-writable"></a>🔹 `f.writable` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.writable</code> in pandas-dev/pandas</b></summary>

##### 1. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1169) (Line 1169)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1169
- **Target Call:** `f.writable`
- **Context:** `_IOWrapper.writable`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            return self.buffer.writable()
```

</details>

#### <a id="pandas-dev-pandas-f-read"></a>🔹 `f.read` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.read</code> in pandas-dev/pandas</b></summary>

##### 1. [pandas/io/common.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1190) (Line 1190)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/common.py#L1190
- **Target Call:** `f.read`
- **Context:** `_BytesIOWrapper.read`
- **Arguments:** `n`
- **Keywords:** `{}`

```python
        bytestring = self.buffer.read(n).encode(self.encoding)
```

</details>

#### <a id="pandas-dev-pandas-url-to-fs"></a>🔹 `url_to_fs` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>url_to_fs</code> in pandas-dev/pandas</b></summary>

##### 1. [pandas/io/parquet.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L131) (Line 131)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/parquet.py#L131
- **Target Call:** `url_to_fs`
- **Context:** `_get_path_or_handle`
- **Arguments:** `path_or_handle`
- **Keywords:** `{}`

```python
            fs, path_or_handle = fsspec.core.url_to_fs(
                path_or_handle, **(storage_options or {})
            )
```

</details>

#### <a id="pandas-dev-pandas-f-flush"></a>🔹 `f.flush` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.flush</code> in pandas-dev/pandas</b></summary>

##### 1. [pandas/io/pytables.py](https://github.com/pandas-dev/pandas/blob/main/pandas/io/pytables.py#L904) (Line 904)
- **Line Link:** https://github.com/pandas-dev/pandas/blob/main/pandas/io/pytables.py#L904
- **Target Call:** `f.flush`
- **Context:** `HDFStore.flush`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self._handle.flush()
```

</details>

### [ray-project/ray](https://github.com/ray-project/ray)
- **Files Scanned:** `2022` | **Files with Usages:** `21` | **Total Usages:** `54`

#### <a id="ray-project-ray-f-close"></a>🔹 `f.close` (11 occurrences)

<details open>
<summary><b>Click to expand/collapse 11 occurrences for <code>f.close</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L107) (Line 107)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L107
- **Target Call:** `f.close`
- **Context:** `LogFileInfo.reopen_if_necessary`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    self.file_handle.close()
```

##### 2. [python/ray/_private/runtime_env/packaging.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L199) (Line 199)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L199
- **Target Call:** `f.close`
- **Context:** `_hash_file_content_or_directory_name`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                f.close()
```

##### 3. [python/ray/autoscaler/_private/cluster_dump.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/cluster_dump.py#L97) (Line 97)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/cluster_dump.py#L97
- **Target Call:** `f.close`
- **Context:** `Archive.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self.tar.close()
```

##### 4. [python/ray/data/_internal/datasource/webdataset_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/webdataset_datasink.py#L53) (Line 53)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/webdataset_datasink.py#L53
- **Target Call:** `f.close`
- **Context:** `WebDatasetDatasink.write_block_to_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        stream.close()
```

##### 5. [python/ray/experimental/sandbox/backend/gvisor.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L166) (Line 166)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L166
- **Target Call:** `f.close`
- **Context:** `GVisorSandboxBackend.create_sandbox`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            stderr_file.close()
```

##### 6. [python/ray/experimental/sandbox/backend/gvisor.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L208) (Line 208)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L208
- **Target Call:** `f.close`
- **Context:** `GVisorSandboxBackend.delete_sandbox`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    stderr_file.close()
```

##### 7. [python/ray/serve/_private/tracing_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/tracing_utils.py#L87) (Line 87)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/tracing_utils.py#L87
- **Target Call:** `f.close`
- **Context:** `FileConsoleSpanExporter.shutdown`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                out_file.close()
```

##### 8. [python/ray/tune/logger/csv.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/csv.py#L78) (Line 78)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/csv.py#L78
- **Target Call:** `f.close`
- **Context:** `CSVLoggerCallback.log_trial_end`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self._trial_files[trial].close()
```

##### 9. [python/ray/tune/logger/json.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/json.py#L60) (Line 60)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/json.py#L60
- **Target Call:** `f.close`
- **Context:** `JsonLoggerCallback.log_trial_end`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self._trial_files[trial].close()
```

##### 10. [python/ray/tune/trainable/trainable.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/trainable/trainable.py#L713) (Line 713)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/trainable/trainable.py#L713
- **Target Call:** `f.close`
- **Context:** `Trainable._close_logfiles`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self._stdout_fp.close()
```

##### 11. [python/ray/tune/trainable/trainable.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/trainable/trainable.py#L718) (Line 718)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/trainable/trainable.py#L718
- **Target Call:** `f.close`
- **Context:** `Trainable._close_logfiles`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self._stderr_fp.close()
```

</details>

#### <a id="ray-project-ray-f-read"></a>🔹 `f.read` (7 occurrences)

<details open>
<summary><b>Click to expand/collapse 7 occurrences for <code>f.read</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/runtime_env/packaging.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L194) (Line 194)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L194
- **Target Call:** `f.read`
- **Context:** `_hash_file_content_or_directory_name`
- **Arguments:** `BUF_SIZE`
- **Keywords:** `{}`

```python
                data = f.read(BUF_SIZE)
```

##### 2. [python/ray/_private/runtime_env/packaging.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L197) (Line 197)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L197
- **Target Call:** `f.read`
- **Context:** `_hash_file_content_or_directory_name`
- **Arguments:** `BUF_SIZE`
- **Keywords:** `{}`

```python
                    data = f.read(BUF_SIZE)
```

##### 3. [python/ray/_private/runtime_env/protocol.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L290) (Line 290)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L290
- **Target Call:** `f.read`
- **Context:** `ProtocolsProvider.download_remote_uri`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                fout.write(fin.read())
```

##### 4. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1291) (Line 1291)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1291
- **Target Call:** `f.read`
- **Context:** `_decode_image_frames`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    data = fh.read()
```

##### 5. [python/ray/experimental/sandbox/backend/gvisor.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L130) (Line 130)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L130
- **Target Call:** `f.read`
- **Context:** `GVisorSandboxBackend.create_sandbox`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    stderr_str = stderr_file.read()
```

##### 6. [python/ray/tune/utils/file_transfer.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L357) (Line 357)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L357
- **Target Call:** `f.read`
- **Context:** `_PackActor._chunk_generator`
- **Arguments:** `self.chunk_size`
- **Keywords:** `{}`

```python
        data = self.stream.read(self.chunk_size)
```

##### 7. [python/ray/tune/utils/file_transfer.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L360) (Line 360)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L360
- **Target Call:** `f.read`
- **Context:** `_PackActor._chunk_generator`
- **Arguments:** `self.chunk_size`
- **Keywords:** `{}`

```python
            data = self.stream.read(self.chunk_size)
```

</details>

#### <a id="ray-project-ray-f-seek"></a>🔹 `f.seek` (6 occurrences)

<details open>
<summary><b>Click to expand/collapse 6 occurrences for <code>f.seek</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L95) (Line 95)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L95
- **Target Call:** `f.seek`
- **Context:** `LogFileInfo.reopen_if_necessary`
- **Arguments:** `self.file_position`
- **Keywords:** `{}`

```python
                self.file_handle.seek(self.file_position)
```

##### 2. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L353) (Line 353)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L353
- **Target Call:** `f.seek`
- **Context:** `LogMonitor.open_closed_files`
- **Arguments:** `file_info.file_position`
- **Keywords:** `{}`

```python
                f.seek(file_info.file_position)
```

##### 3. [python/ray/experimental/sandbox/backend/gvisor.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L129) (Line 129)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L129
- **Target Call:** `f.seek`
- **Context:** `GVisorSandboxBackend.create_sandbox`
- **Arguments:** `0`
- **Keywords:** `{}`

```python
                    stderr_file.seek(0)
```

##### 4. [python/ray/tune/utils/file_transfer.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L337) (Line 337)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L337
- **Target Call:** `f.seek`
- **Context:** `_PackActor.__init__`
- **Arguments:** `0, 2`
- **Keywords:** `{}`

```python
        self.stream.seek(0, 2)
```

##### 5. [python/ray/tune/utils/file_transfer.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L356) (Line 356)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L356
- **Target Call:** `f.seek`
- **Context:** `_PackActor._chunk_generator`
- **Arguments:** `0`
- **Keywords:** `{}`

```python
        self.stream.seek(0)
```

##### 6. [python/ray/tune/utils/file_transfer.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L382) (Line 382)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L382
- **Target Call:** `f.seek`
- **Context:** `_unpack_dir`
- **Arguments:** `0`
- **Keywords:** `{}`

```python
    stream.seek(0)
```

</details>

#### <a id="ray-project-ray-fs-open"></a>🔹 `fs.open` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>fs.open</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/runtime_env/protocol.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L203) (Line 203)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L203
- **Target Call:** `fs.open`
- **Context:** `ProtocolsProvider.open_file`
- **Arguments:** `uri, mode`
- **Keywords:** `{}`

```python
            return filesystem.open(uri, mode)
```

##### 2. [python/ray/data/_internal/datasource/_lerobot_compat.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40) (Line 40)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40
- **Target Call:** `fs.open`
- **Context:** `_CredsVideoDecoderCache.get_decoder`
- **Arguments:** `video_path`
- **Keywords:** `{}`

```python
                    file_handle = fsspec.open(video_path, **opts).__enter__()
```

##### 3. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L235) (Line 235)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L235
- **Target Call:** `fs.open`
- **Context:** `_build_schema`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    with fs.open(path, "rb") as f:
```

##### 4. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L813) (Line 813)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L813
- **Target Call:** `fs.open`
- **Context:** `_read_lerobot_segment`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
        with fs.open(path, "rb") as f:
```

##### 5. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1290) (Line 1290)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1290
- **Target Call:** `fs.open`
- **Context:** `_decode_image_frames`
- **Arguments:** `p, 'rb'`
- **Keywords:** `{}`

```python
                with root.fs.open(p, "rb") as fh:
```

</details>

#### <a id="ray-project-ray-f-write"></a>🔹 `f.write` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>f.write</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L335) (Line 335)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L335
- **Target Call:** `f.write`
- **Context:** `Unbuffered.write`
- **Arguments:** `data`
- **Keywords:** `{}`

```python
        self.stream.write(data)
```

##### 2. [python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py#L307) (Line 307)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py#L307
- **Target Call:** `f.write`
- **Context:** `_PartitionWriter._flush`
- **Arguments:** `memoryview(buf)`
- **Keywords:** `{}`

```python
        self._out_file.write(memoryview(buf))
```

##### 3. [python/ray/tune/logger/json.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/json.py#L53) (Line 53)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/json.py#L53
- **Target Call:** `f.write`
- **Context:** `JsonLoggerCallback.log_trial_result`
- **Arguments:** `'\n'`
- **Keywords:** `{}`

```python
        self._trial_files[trial].write("\n")
```

##### 4. [python/ray/tune/utils/file_transfer.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L414) (Line 414)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L414
- **Target Call:** `f.write`
- **Context:** `_unpack_from_actor`
- **Arguments:** `buffer`
- **Keywords:** `{}`

```python
        stream.write(buffer)
```

##### 5. [rllib/utils/tf_run_builder.py](https://github.com/ray-project/ray/blob/master/rllib/utils/tf_run_builder.py#L106) (Line 106)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/utils/tf_run_builder.py#L106
- **Target Call:** `f.write`
- **Context:** `_run_timeline`
- **Arguments:** `trace.generate_chrome_trace_format()`
- **Keywords:** `{}`

```python
        trace_file.write(trace.generate_chrome_trace_format())
```

</details>

#### <a id="ray-project-ray-f-flush"></a>🔹 `f.flush` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>f.flush</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L336) (Line 336)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L336
- **Target Call:** `f.flush`
- **Context:** `Unbuffered.write`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self.stream.flush()
```

##### 2. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L340) (Line 340)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L340
- **Target Call:** `f.flush`
- **Context:** `Unbuffered.writelines`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self.stream.flush()
```

##### 3. [python/ray/serve/_private/tracing_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/tracing_utils.py#L86) (Line 86)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/tracing_utils.py#L86
- **Target Call:** `f.flush`
- **Context:** `FileConsoleSpanExporter.shutdown`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                out_file.flush()
```

##### 4. [python/ray/tune/logger/csv.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/csv.py#L71) (Line 71)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/csv.py#L71
- **Target Call:** `f.flush`
- **Context:** `CSVLoggerCallback.log_trial_result`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self._trial_files[trial].flush()
```

##### 5. [python/ray/tune/logger/json.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/json.py#L54) (Line 54)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/json.py#L54
- **Target Call:** `f.flush`
- **Context:** `JsonLoggerCallback.log_trial_result`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self._trial_files[trial].flush()
```

</details>

#### <a id="ray-project-ray-f-readline"></a>🔹 `f.readline` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>f.readline</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L401) (Line 401)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L401
- **Target Call:** `f.readline`
- **Context:** `LogMonitor.check_log_files_and_publish_updates`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    next_line = file_info.file_handle.readline()
```

##### 2. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L438) (Line 438)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L438
- **Target Call:** `f.readline`
- **Context:** `LogMonitor.check_log_files_and_publish_updates`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                        file_info.file_handle.readline()
```

##### 3. [rllib/offline/json_reader.py](https://github.com/ray-project/ray/blob/master/rllib/offline/json_reader.py#L330) (Line 330)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/offline/json_reader.py#L330
- **Target Call:** `f.readline`
- **Context:** `JsonReader.read_all_files`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                line = file.readline()
```

</details>

#### <a id="ray-project-ray-f-tell"></a>🔹 `f.tell` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>f.tell</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L462) (Line 462)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L462
- **Target Call:** `f.tell`
- **Context:** `LogMonitor.check_log_files_and_publish_updates`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            file_info.file_position = file_info.file_handle.tell()
```

##### 2. [python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py#L306) (Line 306)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py#L306
- **Target Call:** `f.tell`
- **Context:** `_PartitionWriter._flush`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        off = self._out_file.tell()
```

##### 3. [python/ray/tune/utils/file_transfer.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L338) (Line 338)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/file_transfer.py#L338
- **Target Call:** `f.tell`
- **Context:** `_PackActor.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        file_size = self.stream.tell()
```

</details>

#### <a id="ray-project-ray-fs-move"></a>🔹 `fs.move` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.move</code> in ray-project/ray</b></summary>

##### 1. [python/ray/data/_internal/util.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/util.py#L1455) (Line 1455)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/util.py#L1455
- **Target Call:** `fs.move`
- **Context:** `RetryingPyFileSystemHandler.move`
- **Arguments:** `src, dest`
- **Keywords:** `{}`

```python
            lambda: self._fs.move(src, dest), f"move from {src} to {dest}"
```

##### 2. [python/ray/data/checkpoint/checkpoint_writer.py](https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/checkpoint_writer.py#L267) (Line 267)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/checkpoint/checkpoint_writer.py#L267
- **Target Call:** `fs.move`
- **Context:** `BatchBasedCheckpointWriter._rename`
- **Arguments:** `pending.pending_path, pending.committed_path`
- **Keywords:** `{}`

```python
            self.filesystem.move(pending.pending_path, pending.committed_path)
```

</details>

#### <a id="ray-project-ray-f-readlines"></a>🔹 `f.readlines` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.readlines</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/runtime_env/packaging.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L320) (Line 320)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L320
- **Target Call:** `f.readlines`
- **Context:** `_get_ignore_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            pathspec = PathSpec.from_lines("gitwildmatch", f.readlines())
```

</details>

#### <a id="ray-project-ray-f-writelines"></a>🔹 `f.writelines` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.writelines</code> in ray-project/ray</b></summary>

##### 1. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L339) (Line 339)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L339
- **Target Call:** `f.writelines`
- **Context:** `Unbuffered.writelines`
- **Arguments:** `datas`
- **Keywords:** `{}`

```python
        self.stream.writelines(datas)
```

</details>

#### <a id="ray-project-ray-url-to-fs"></a>🔹 `url_to_fs` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>url_to_fs</code> in ray-project/ray</b></summary>

##### 1. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L451) (Line 451)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L451
- **Target Call:** `url_to_fs`
- **Context:** `_resolve_filesystem`
- **Arguments:** `video_root_uri`
- **Keywords:** `{}`

```python
        fs, fs_root = fsspec.core.url_to_fs(video_root_uri, **video_storage_options)
```

</details>

#### <a id="ray-project-ray-fs-exists"></a>🔹 `fs.exists` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.exists</code> in ray-project/ray</b></summary>

##### 1. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L477) (Line 477)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L477
- **Target Call:** `fs.exists`
- **Context:** `_load_lerobot_metadata`
- **Arguments:** `f'{fs_root}/meta/info.json'`
- **Keywords:** `{}`

```python
    if not fs.exists(f"{fs_root}/meta/info.json"):
```

</details>

#### <a id="ray-project-ray-fs-get"></a>🔹 `fs.get` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.get</code> in ray-project/ray</b></summary>

##### 1. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L491) (Line 491)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L491
- **Target Call:** `fs.get`
- **Context:** `_load_lerobot_metadata`
- **Arguments:** `f'{fs_root}/meta', os.path.join(local_root, 'meta')`
- **Keywords:** `{'recursive': 'True'}`

```python
    fs.get(f"{fs_root}/meta", os.path.join(local_root, "meta"), recursive=True)
```

</details>

#### <a id="ray-project-ray-fsspec-filesystem"></a>🔹 `fsspec.filesystem` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fsspec.filesystem</code> in ray-project/ray</b></summary>

##### 1. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L317) (Line 317)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L317
- **Target Call:** `fsspec.filesystem`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `'zip'`
- **Keywords:** `{'fo': 'self.paths[0]'}`

```python
            self._fs = fsspec.filesystem("zip", fo=self.paths[0])
```

</details>

#### <a id="ray-project-ray-fs-split"></a>🔹 `fs.split` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.split</code> in ray-project/ray</b></summary>

##### 1. [python/ray/train/torch/config.py](https://github.com/ray-project/ray/blob/master/python/ray/train/torch/config.py#L91) (Line 91)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/torch/config.py#L91
- **Target Call:** `fs.split`
- **Context:** `_is_backend_nccl`
- **Arguments:** `','`
- **Keywords:** `{}`

```python
        for item in backend.split(",")
```

</details>

### [pola-rs/polars](https://github.com/pola-rs/polars)
- **Files Scanned:** `212` | **Files with Usages:** `1` | **Total Usages:** `2`

#### <a id="pola-rs-polars-fs-open"></a>🔹 `fs.open` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.open</code> in pola-rs/polars</b></summary>

##### 1. [py-polars/src/polars/io/_utils.py](https://github.com/pola-rs/polars/blob/main/py-polars/src/polars/io/_utils.py#L269) (Line 269)
- **Line Link:** https://github.com/pola-rs/polars/blob/main/py-polars/src/polars/io/_utils.py#L269
- **Target Call:** `fs.open`
- **Context:** `prepare_file_arg`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
            return fsspec.open(file, **storage_options)
```

</details>

#### <a id="pola-rs-polars-fs-open-files"></a>🔹 `fs.open_files` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.open_files</code> in pola-rs/polars</b></summary>

##### 1. [py-polars/src/polars/io/_utils.py](https://github.com/pola-rs/polars/blob/main/py-polars/src/polars/io/_utils.py#L285) (Line 285)
- **Line Link:** https://github.com/pola-rs/polars/blob/main/py-polars/src/polars/io/_utils.py#L285
- **Target Call:** `fs.open_files`
- **Context:** `prepare_file_arg`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
            return fsspec.open_files(file, **storage_options)
```

</details>

### [Lightning-AI/pytorch-lightning](https://github.com/Lightning-AI/pytorch-lightning)
- **Files Scanned:** `457` | **Files with Usages:** `22` | **Total Usages:** `99`

#### <a id="lightning-ai-pytorch-lightning-fs-exists"></a>🔹 `fs.exists` (24 occurrences)

<details open>
<summary><b>Click to expand/collapse 24 occurrences for <code>fs.exists</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L151) (Line 151)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L151
- **Target Call:** `fs.exists`
- **Context:** `Drive.list`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
            if self.fs.exists(p):
```

##### 2. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L183) (Line 183)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L183
- **Target Call:** `fs.exists`
- **Context:** `Drive.get`
- **Arguments:** `shared_path`
- **Keywords:** `{}`

```python
                while not self.fs.exists(shared_path):
```

##### 3. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L228) (Line 228)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L228
- **Target Call:** `fs.exists`
- **Context:** `Drive.delete`
- **Arguments:** `str(shared_path)`
- **Keywords:** `{}`

```python
        if self.fs.exists(str(shared_path)):
```

##### 4. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L264) (Line 264)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L264
- **Target Call:** `fs.exists`
- **Context:** `Drive._collect_component_names`
- **Arguments:** `self.drive_root`
- **Keywords:** `{}`

```python
        if self.fs.exists(self.drive_root):
```

##### 5. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L282) (Line 282)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L282
- **Target Call:** `fs.exists`
- **Context:** `Drive._get`
- **Arguments:** `dst`
- **Keywords:** `{}`

```python
                if fs.exists(dst):
```

##### 6. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L299) (Line 299)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L299
- **Target Call:** `fs.exists`
- **Context:** `Drive._find_match`
- **Arguments:** `possible_path`
- **Keywords:** `{}`

```python
            if self.fs.exists(possible_path):
```

##### 7. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L322) (Line 322)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L322
- **Target Call:** `fs.exists`
- **Context:** `Drive._check_for_allow_duplicates`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        matches = [self.fs.exists(p) for p in possible_paths]
```

##### 8. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L17) (Line 17)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L17
- **Target Call:** `fs.exists`
- **Context:** `_get_files`
- **Arguments:** `dst`
- **Keywords:** `{}`

```python
            if fs.exists(dst):
```

##### 9. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L92) (Line 92)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L92
- **Target Call:** `fs.exists`
- **Context:** `FileSystem.listdir`
- **Arguments:** `shared_path`
- **Keywords:** `{}`

```python
        if not self._fs.exists(shared_path):
```

##### 10. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L117) (Line 117)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L117
- **Target Call:** `fs.exists`
- **Context:** `FileSystem.walk`
- **Arguments:** `shared_path`
- **Keywords:** `{}`

```python
        if not self._fs.exists(shared_path):
```

##### 11. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L146) (Line 146)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L146
- **Target Call:** `fs.exists`
- **Context:** `FileSystem.rm`
- **Arguments:** `str(delete_path)`
- **Keywords:** `{}`

```python
        if self._fs.exists(str(delete_path)):
```

##### 12. [src/lightning/app/storage/orchestrator.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/orchestrator.py#L122) (Line 122)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/orchestrator.py#L122
- **Target Call:** `fs.exists`
- **Context:** `StorageOrchestrator.run_once`
- **Arguments:** `maybe_artifact_path`
- **Keywords:** `{}`

```python
                if self.fs.exists(maybe_artifact_path):
```

##### 13. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L223) (Line 223)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L223
- **Target Call:** `fs.exists`
- **Context:** `Path.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        while not fs.exists(response.path) or fs.info(response.path)["size"] != response.size:
```

##### 14. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L450) (Line 450)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L450
- **Target Call:** `fs.exists`
- **Context:** `_filesystem`
- **Arguments:** `_shared_storage_path()`
- **Keywords:** `{}`

```python
        if not fs.exists(_shared_storage_path()):
```

##### 15. [src/lightning/app/storage/payload.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L182) (Line 182)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L182
- **Target Call:** `fs.exists`
- **Context:** `_BasePayload.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        while not fs.exists(response.path) or fs.info(response.path)["size"] != response.size:
```

##### 16. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L268) (Line 268)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L268
- **Target Call:** `fs.exists`
- **Context:** `_ExperimentWriter._check_log_dir_exists`
- **Arguments:** `self.log_dir`
- **Keywords:** `{}`

```python
        if self._fs.exists(self.log_dir) and self._fs.listdir(self.log_dir):
```

##### 17. [src/lightning/fabric/plugins/io/torch_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L80) (Line 80)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L80
- **Target Call:** `fs.exists`
- **Context:** `TorchCheckpointIO.load_checkpoint`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if not fs.exists(path):
```

##### 18. [src/lightning/fabric/plugins/io/torch_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L94) (Line 94)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L94
- **Target Call:** `fs.exists`
- **Context:** `TorchCheckpointIO.remove_checkpoint`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if fs.exists(path):
```

##### 19. [src/lightning/pytorch/callbacks/model_checkpoint.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L646) (Line 646)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L646
- **Target Call:** `fs.exists`
- **Context:** `ModelCheckpoint._find_last_checkpoints`
- **Arguments:** `ckpt_path`
- **Keywords:** `{}`

```python
        if self._fs.exists(ckpt_path):
```

##### 20. [src/lightning/pytorch/callbacks/model_checkpoint.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L773) (Line 773)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L773
- **Target Call:** `fs.exists`
- **Context:** `ModelCheckpoint.file_exists`
- **Arguments:** `filepath`
- **Keywords:** `{}`

```python
        exists = self._fs.exists(filepath)
```

##### 21. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L259) (Line 259)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L259
- **Target Call:** `fs.exists`
- **Context:** `load_hparams_from_tags_csv`
- **Arguments:** `tags_csv`
- **Keywords:** `{}`

```python
    if not fs.exists(tags_csv):
```

##### 22. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L302) (Line 302)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L302
- **Target Call:** `fs.exists`
- **Context:** `load_hparams_from_yaml`
- **Arguments:** `config_yaml`
- **Keywords:** `{}`

```python
    if not fs.exists(config_yaml):
```

##### 23. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L183) (Line 183)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L183
- **Target Call:** `fs.exists`
- **Context:** `_CheckpointConnector._parse_ckpt_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            candidates_ts = {path: fs.modified(path) for path, fs in candidates_fs.items() if fs.exists(path)}
```

##### 24. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L520) (Line 520)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L520
- **Target Call:** `fs.exists`
- **Context:** `_CheckpointConnector.__max_ckpt_version_in_folder`
- **Arguments:** `dir_path`
- **Keywords:** `{}`

```python
        if not fs.exists(dir_path):
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-open"></a>🔹 `fs.open` (14 occurrences)

<details open>
<summary><b>Click to expand/collapse 14 occurrences for <code>fs.open</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L241) (Line 241)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L241
- **Target Call:** `fs.open`
- **Context:** `_ExperimentWriter.save`
- **Arguments:** `self.metrics_file_path`
- **Keywords:** `{'mode': "'a' if file_exists else 'w'", 'newline': "''"}`

```python
        with self._fs.open(self.metrics_file_path, mode=("a" if file_exists else "w"), newline="") as file:
```

##### 2. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L259) (Line 259)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L259
- **Target Call:** `fs.open`
- **Context:** `_ExperimentWriter._rewrite_with_new_header`
- **Arguments:** `self.metrics_file_path, 'r'`
- **Keywords:** `{'newline': "''"}`

```python
        with self._fs.open(self.metrics_file_path, "r", newline="") as file:
```

##### 3. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L262) (Line 262)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L262
- **Target Call:** `fs.open`
- **Context:** `_ExperimentWriter._rewrite_with_new_header`
- **Arguments:** `self.metrics_file_path, 'w'`
- **Keywords:** `{'newline': "''"}`

```python
        with self._fs.open(self.metrics_file_path, "w", newline="") as file:
```

##### 4. [src/lightning/fabric/plugins/environments/lsf.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/environments/lsf.py#L170) (Line 170)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/environments/lsf.py#L170
- **Target Call:** `fs.open`
- **Context:** `LSFEnvironment._read_hosts`
- **Arguments:** `rankfile, 'r'`
- **Keywords:** `{}`

```python
        with fs.open(rankfile, "r") as f:
```

##### 5. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L56) (Line 56)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L56
- **Target Call:** `fs.open`
- **Context:** `_load`
- **Arguments:** `path_or_url, 'rb'`
- **Keywords:** `{}`

```python
    with fs.open(path_or_url, "rb") as f:
```

##### 6. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L79) (Line 79)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L79
- **Target Call:** `fs.open`
- **Context:** `_atomic_save`
- **Arguments:** `filepath, 'wb'`
- **Keywords:** `{}`

```python
    with fsspec.open(filepath, "wb") as f:
```

##### 7. [src/lightning/pytorch/callbacks/model_checkpoint.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L767) (Line 767)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L767
- **Target Call:** `fs.open`
- **Context:** `ModelCheckpoint.to_yaml`
- **Arguments:** `filepath, 'w'`
- **Keywords:** `{}`

```python
        with self._fs.open(filepath, "w") as fp:
```

##### 8. [src/lightning/pytorch/core/module.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/module.py#L1480) (Line 1480)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/module.py#L1480
- **Target Call:** `fs.open`
- **Context:** `LightningModule.to_torchscript`
- **Arguments:** `file_path, 'wb'`
- **Keywords:** `{}`

```python
            with fs.open(file_path, "wb") as f:
```

##### 9. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L263) (Line 263)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L263
- **Target Call:** `fs.open`
- **Context:** `load_hparams_from_tags_csv`
- **Arguments:** `tags_csv, 'r'`
- **Keywords:** `{'newline': "''"}`

```python
    with fs.open(tags_csv, "r", newline="") as fp:
```

##### 10. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L276) (Line 276)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L276
- **Target Call:** `fs.open`
- **Context:** `save_hparams_to_tags_csv`
- **Arguments:** `tags_csv, 'w'`
- **Keywords:** `{'newline': "''"}`

```python
    with fs.open(tags_csv, "w", newline="") as fp:
```

##### 11. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L306) (Line 306)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L306
- **Target Call:** `fs.open`
- **Context:** `load_hparams_from_yaml`
- **Arguments:** `config_yaml, 'r'`
- **Keywords:** `{}`

```python
    with fs.open(config_yaml, "r") as fp:
```

##### 12. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L346) (Line 346)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L346
- **Target Call:** `fs.open`
- **Context:** `save_hparams_to_yaml`
- **Arguments:** `config_yaml, 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with fs.open(config_yaml, "w", encoding="utf-8") as fp:
```

##### 13. [src/lightning/pytorch/core/saving.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L369) (Line 369)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/core/saving.py#L369
- **Target Call:** `fs.open`
- **Context:** `save_hparams_to_yaml`
- **Arguments:** `config_yaml, 'w'`
- **Keywords:** `{'newline': "''"}`

```python
    with fs.open(config_yaml, "w", newline="") as fp:
```

##### 14. [src/lightning/pytorch/profilers/profiler.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/profilers/profiler.py#L99) (Line 99)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/profilers/profiler.py#L99
- **Target Call:** `fs.open`
- **Context:** `Profiler._prepare_streams`
- **Arguments:** `filepath, 'a'`
- **Keywords:** `{}`

```python
            file = fs.open(filepath, "a")
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-makedirs"></a>🔹 `fs.makedirs` (9 occurrences)

<details open>
<summary><b>Click to expand/collapse 9 occurrences for <code>fs.makedirs</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/copier.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L131) (Line 131)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L131
- **Target Call:** `fs.makedirs`
- **Context:** `_copy`
- **Arguments:** `str(to_path.parent)`
- **Keywords:** `{'exist_ok': 'True'}`

```python
                fs.makedirs(str(to_path.parent), exist_ok=True)
```

##### 2. [src/lightning/app/storage/copier.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L153) (Line 153)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L153
- **Target Call:** `fs.makedirs`
- **Context:** `_copy_files`
- **Arguments:** `str(destination_path.parent)`
- **Keywords:** `{'exist_ok': 'True'}`

```python
            fs.makedirs(str(destination_path.parent), exist_ok=True)
```

##### 3. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L88) (Line 88)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L88
- **Target Call:** `fs.makedirs`
- **Context:** `Drive.root`
- **Arguments:** `root_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
            self.fs.makedirs(root_path, exist_ok=True)
```

##### 4. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L212) (Line 212)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L212
- **Target Call:** `fs.makedirs`
- **Context:** `_ExperimentWriter.__init__`
- **Arguments:** `self.log_dir`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        self._fs.makedirs(self.log_dir, exist_ok=True)
```

##### 5. [src/lightning/fabric/loggers/tensorboard.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/tensorboard.py#L190) (Line 190)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/tensorboard.py#L190
- **Target Call:** `fs.makedirs`
- **Context:** `TensorBoardLogger.experiment`
- **Arguments:** `self.root_dir`
- **Keywords:** `{'exist_ok': 'True'}`

```python
            self._fs.makedirs(self.root_dir, exist_ok=True)
```

##### 6. [src/lightning/fabric/plugins/io/torch_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L57) (Line 57)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L57
- **Target Call:** `fs.makedirs`
- **Context:** `TorchCheckpointIO.save_checkpoint`
- **Arguments:** `os.path.dirname(path)`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        fs.makedirs(os.path.dirname(path), exist_ok=True)
```

##### 7. [src/lightning/fabric/plugins/io/xla.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/xla.py#L64) (Line 64)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/xla.py#L64
- **Target Call:** `fs.makedirs`
- **Context:** `XLACheckpointIO.save_checkpoint`
- **Arguments:** `os.path.dirname(path)`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        fs.makedirs(os.path.dirname(path), exist_ok=True)
```

##### 8. [src/lightning/pytorch/cli.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/cli.py#L273) (Line 273)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/cli.py#L273
- **Target Call:** `fs.makedirs`
- **Context:** `SaveConfigCallback.setup`
- **Arguments:** `log_dir`
- **Keywords:** `{'exist_ok': 'True'}`

```python
                fs.makedirs(log_dir, exist_ok=True)
```

##### 9. [src/lightning/pytorch/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/loggers/csv_logs.py#L169) (Line 169)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/loggers/csv_logs.py#L169
- **Target Call:** `fs.makedirs`
- **Context:** `CSVLogger.experiment`
- **Arguments:** `self.root_dir`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        self._fs.makedirs(self.root_dir, exist_ok=True)
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-isdir"></a>🔹 `fs.isdir` (8 occurrences)

<details open>
<summary><b>Click to expand/collapse 8 occurrences for <code>fs.isdir</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L279) (Line 279)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L279
- **Target Call:** `fs.isdir`
- **Context:** `Drive._get`
- **Arguments:** `src`
- **Keywords:** `{}`

```python
        if fs.isdir(src):
```

##### 2. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L14) (Line 14)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L14
- **Target Call:** `fs.isdir`
- **Context:** `_get_files`
- **Arguments:** `src`
- **Keywords:** `{}`

```python
    if fs.isdir(src):
```

##### 3. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L132) (Line 132)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L132
- **Target Call:** `fs.isdir`
- **Context:** `FileSystem.walk`
- **Arguments:** `shared_path`
- **Keywords:** `{}`

```python
            if self._fs.isdir(shared_path):
```

##### 4. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L147) (Line 147)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L147
- **Target Call:** `fs.isdir`
- **Context:** `FileSystem.rm`
- **Arguments:** `str(delete_path)`
- **Keywords:** `{}`

```python
            if self._fs.isdir(str(delete_path)):
```

##### 5. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L166) (Line 166)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L166
- **Target Call:** `fs.isdir`
- **Context:** `FileSystem.isdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return self._fs.isdir(path)
```

##### 6. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L231) (Line 231)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L231
- **Target Call:** `fs.isdir`
- **Context:** `Path.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        if fs.isdir(response.path):
```

##### 7. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L126) (Line 126)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L126
- **Target Call:** `fs.isdir`
- **Context:** `_is_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return fs.isdir(path)
```

##### 8. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L132) (Line 132)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L132
- **Target Call:** `fs.isdir`
- **Context:** `_is_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    return fs.isdir(path)
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-get"></a>🔹 `fs.get` (7 occurrences)

<details open>
<summary><b>Click to expand/collapse 7 occurrences for <code>fs.get</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L291) (Line 291)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L291
- **Target Call:** `fs.get`
- **Context:** `Drive._get`
- **Arguments:** `glob, str(dst.absolute())`
- **Keywords:** `{'recursive': 'False'}`

```python
                fs.get(glob, str(dst.absolute()), recursive=False)
```

##### 2. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L293) (Line 293)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L293
- **Target Call:** `fs.get`
- **Context:** `Drive._get`
- **Arguments:** `str(src), str(dst.absolute())`
- **Keywords:** `{'recursive': 'False'}`

```python
            fs.get(str(src), str(dst.absolute()), recursive=False)
```

##### 3. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L26) (Line 26)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L26
- **Target Call:** `fs.get`
- **Context:** `_get_files`
- **Arguments:** `glob, str(dst)`
- **Keywords:** `{'recursive': 'False'}`

```python
            fs.get(glob, str(dst), recursive=False)
```

##### 4. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L28) (Line 28)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L28
- **Target Call:** `fs.get`
- **Context:** `_get_files`
- **Arguments:** `str(src), str(dst)`
- **Keywords:** `{'recursive': 'False'}`

```python
        fs.get(str(src), str(dst), recursive=False)
```

##### 5. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L237) (Line 237)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L237
- **Target Call:** `fs.get`
- **Context:** `Path.get`
- **Arguments:** `glob, str(self.absolute())`
- **Keywords:** `{'recursive': 'False'}`

```python
                fs.get(glob, str(self.absolute()), recursive=False)
```

##### 6. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L240) (Line 240)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L240
- **Target Call:** `fs.get`
- **Context:** `Path.get`
- **Arguments:** `str(response.path), str(self.absolute())`
- **Keywords:** `{'recursive': 'False'}`

```python
            fs.get(str(response.path), str(self.absolute()), recursive=False)
```

##### 7. [src/lightning/app/storage/payload.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L188) (Line 188)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L188
- **Target Call:** `fs.get`
- **Context:** `_BasePayload.get`
- **Arguments:** `str(response.path), str(local_path)`
- **Keywords:** `{'recursive': 'False'}`

```python
        fs.get(str(response.path), str(local_path), recursive=False)
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-ls"></a>🔹 `fs.ls` (6 occurrences)

<details open>
<summary><b>Click to expand/collapse 6 occurrences for <code>fs.ls</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L152) (Line 152)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L152
- **Target Call:** `fs.ls`
- **Context:** `Drive.list`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
                for f in self.fs.ls(p):
```

##### 2. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L268) (Line 268)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L268
- **Target Call:** `fs.ls`
- **Context:** `Drive._collect_component_names`
- **Arguments:** `self.drive_root`
- **Keywords:** `{}`

```python
            return [str(p.split(sep)[-1]) for p in self.fs.ls(self.drive_root)]
```

##### 3. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L99) (Line 99)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L99
- **Target Call:** `fs.ls`
- **Context:** `FileSystem.listdir`
- **Arguments:** `shared_path`
- **Keywords:** `{}`

```python
        paths = self._fs.ls(shared_path)
```

##### 4. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L124) (Line 124)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L124
- **Target Call:** `fs.ls`
- **Context:** `FileSystem.walk`
- **Arguments:** `shared_path`
- **Keywords:** `{}`

```python
        paths = self._fs.ls(shared_path)
```

##### 5. [src/lightning/pytorch/callbacks/model_checkpoint.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L647) (Line 647)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L647
- **Target Call:** `fs.ls`
- **Context:** `ModelCheckpoint._find_last_checkpoints`
- **Arguments:** `ckpt_path`
- **Keywords:** `{'detail': 'False'}`

```python
            return {os.path.normpath(p) for p in self._fs.ls(ckpt_path, detail=False) if _is_last(Path(p))}
```

##### 6. [src/lightning/pytorch/callbacks/model_checkpoint.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L651) (Line 651)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/callbacks/model_checkpoint.py#L651
- **Target Call:** `fs.ls`
- **Context:** `ModelCheckpoint.__warn_if_dir_not_empty`
- **Arguments:** `dirpath`
- **Keywords:** `{}`

```python
        if self.save_top_k != 0 and _is_dir(self._fs, dirpath, strict=True) and len(self._fs.ls(dirpath)) > 0:
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-isfile"></a>🔹 `fs.isfile` (6 occurrences)

<details open>
<summary><b>Click to expand/collapse 6 occurrences for <code>fs.isfile</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L159) (Line 159)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L159
- **Target Call:** `fs.isfile`
- **Context:** `FileSystem.isfile`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return self._fs.isfile(path)
```

##### 2. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L235) (Line 235)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L235
- **Target Call:** `fs.isfile`
- **Context:** `_ExperimentWriter.save`
- **Arguments:** `self.metrics_file_path`
- **Keywords:** `{}`

```python
        file_exists = self._fs.isfile(self.metrics_file_path)
```

##### 3. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L273) (Line 273)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L273
- **Target Call:** `fs.isfile`
- **Context:** `_ExperimentWriter._check_log_dir_exists`
- **Arguments:** `self.metrics_file_path`
- **Keywords:** `{}`

```python
            if self._fs.isfile(self.metrics_file_path):
```

##### 4. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L130) (Line 130)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L130
- **Target Call:** `fs.isfile`
- **Context:** `_is_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return not fs.isfile(path)
```

##### 5. [src/lightning/pytorch/cli.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/cli.py#L258) (Line 258)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/cli.py#L258
- **Target Call:** `fs.isfile`
- **Context:** `SaveConfigCallback.setup`
- **Arguments:** `config_path`
- **Keywords:** `{}`

```python
                file_exists = fs.isfile(config_path) if trainer.is_global_zero else False
```

##### 6. [src/lightning/pytorch/loggers/tensorboard.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/loggers/tensorboard.py#L220) (Line 220)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/loggers/tensorboard.py#L220
- **Target Call:** `fs.isfile`
- **Context:** `TensorBoardLogger.save`
- **Arguments:** `hparams_file`
- **Keywords:** `{}`

```python
        if _is_dir(self._fs, dir_path) and not self._fs.isfile(hparams_file):
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-rm"></a>🔹 `fs.rm` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>fs.rm</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L229) (Line 229)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L229
- **Target Call:** `fs.rm`
- **Context:** `Drive.delete`
- **Arguments:** `str(shared_path)`
- **Keywords:** `{}`

```python
            self.fs.rm(str(shared_path))
```

##### 2. [src/lightning/app/storage/drive.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L284) (Line 284)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/drive.py#L284
- **Target Call:** `fs.rm`
- **Context:** `Drive._get`
- **Arguments:** `str(dst)`
- **Keywords:** `{'recursive': 'True'}`

```python
                        fs.rm(str(dst), recursive=True)
```

##### 3. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L19) (Line 19)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L19
- **Target Call:** `fs.rm`
- **Context:** `_get_files`
- **Arguments:** `str(dst)`
- **Keywords:** `{'recursive': 'True'}`

```python
                    fs.rm(str(dst), recursive=True)
```

##### 4. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L150) (Line 150)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L150
- **Target Call:** `fs.rm`
- **Context:** `FileSystem.rm`
- **Arguments:** `str(delete_path)`
- **Keywords:** `{}`

```python
                self._fs.rm(str(delete_path))
```

##### 5. [src/lightning/fabric/plugins/io/torch_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L95) (Line 95)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/plugins/io/torch_io.py#L95
- **Target Call:** `fs.rm`
- **Context:** `TorchCheckpointIO.remove_checkpoint`
- **Arguments:** `path`
- **Keywords:** `{'recursive': 'True'}`

```python
            fs.rm(path, recursive=True)
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-listdir"></a>🔹 `fs.listdir` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>fs.listdir</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L179) (Line 179)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L179
- **Target Call:** `fs.listdir`
- **Context:** `CSVLogger._get_next_version`
- **Arguments:** `versions_root`
- **Keywords:** `{}`

```python
        for d in self._fs.listdir(versions_root):
```

##### 2. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L268) (Line 268)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L268
- **Target Call:** `fs.listdir`
- **Context:** `_ExperimentWriter._check_log_dir_exists`
- **Arguments:** `self.log_dir`
- **Keywords:** `{}`

```python
        if self._fs.exists(self.log_dir) and self._fs.listdir(self.log_dir):
```

##### 3. [src/lightning/fabric/loggers/tensorboard.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/tensorboard.py#L306) (Line 306)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/tensorboard.py#L306
- **Target Call:** `fs.listdir`
- **Context:** `TensorBoardLogger._get_next_version`
- **Arguments:** `save_dir`
- **Keywords:** `{}`

```python
            listdir_info = self._fs.listdir(save_dir)
```

##### 4. [src/lightning/pytorch/loggers/tensorboard.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/loggers/tensorboard.py#L246) (Line 246)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/loggers/tensorboard.py#L246
- **Target Call:** `fs.listdir`
- **Context:** `TensorBoardLogger._get_next_version`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python
            listdir_info = self._fs.listdir(root_dir)
```

##### 5. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L524) (Line 524)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L524
- **Target Call:** `fs.listdir`
- **Context:** `_CheckpointConnector.__max_ckpt_version_in_folder`
- **Arguments:** `uri`
- **Keywords:** `{}`

```python
        files = [os.path.basename(f["name"]) for f in fs.listdir(uri)]
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-put"></a>🔹 `fs.put` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.put</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/copier.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L133) (Line 133)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L133
- **Target Call:** `fs.put`
- **Context:** `_copy`
- **Arguments:** `str(from_path), str(to_path)`
- **Keywords:** `{'recursive': 'False'}`

```python
            fs.put(str(from_path), str(to_path), recursive=False)
```

##### 2. [src/lightning/app/storage/copier.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L155) (Line 155)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/copier.py#L155
- **Target Call:** `fs.put`
- **Context:** `_copy_files`
- **Arguments:** `str(source_path), str(destination_path)`
- **Keywords:** `{}`

```python
        fs.put(str(source_path), str(destination_path))
```

##### 3. [src/lightning/app/utilities/commands/base.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/utilities/commands/base.py#L204) (Line 204)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/utilities/commands/base.py#L204
- **Target Call:** `fs.put`
- **Context:** `_upload`
- **Arguments:** `source_file, remote_url`
- **Keywords:** `{}`

```python
        fs.put(source_file, remote_url)
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-info"></a>🔹 `fs.info` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.info</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/orchestrator.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/orchestrator.py#L134) (Line 134)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/orchestrator.py#L134
- **Target Call:** `fs.info`
- **Context:** `StorageOrchestrator.run_once`
- **Arguments:** `maybe_artifact_path`
- **Keywords:** `{}`

```python
                            size=self.fs.info(maybe_artifact_path)["size"],
```

##### 2. [src/lightning/app/storage/path.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L223) (Line 223)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/path.py#L223
- **Target Call:** `fs.info`
- **Context:** `Path.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        while not fs.exists(response.path) or fs.info(response.path)["size"] != response.size:
```

##### 3. [src/lightning/app/storage/payload.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L182) (Line 182)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/payload.py#L182
- **Target Call:** `fs.info`
- **Context:** `_BasePayload.get`
- **Arguments:** `response.path`
- **Keywords:** `{}`

```python
        while not fs.exists(response.path) or fs.info(response.path)["size"] != response.size:
```

</details>

#### <a id="lightning-ai-pytorch-lightning-url-to-fs"></a>🔹 `url_to_fs` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>url_to_fs</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L61) (Line 61)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L61
- **Target Call:** `url_to_fs`
- **Context:** `get_filesystem`
- **Arguments:** `str(path)`
- **Keywords:** `{}`

```python
    fs, _ = url_to_fs(str(path), **kwargs)
```

##### 2. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L53) (Line 53)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L53
- **Target Call:** `url_to_fs`
- **Context:** `_CheckpointConnector._hpc_resume_path`
- **Arguments:** `dir_path_hpc`
- **Keywords:** `{}`

```python
        fs, path = url_to_fs(dir_path_hpc)
```

##### 3. [src/lightning/pytorch/trainer/connectors/checkpoint_connector.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L519) (Line 519)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/trainer/connectors/checkpoint_connector.py#L519
- **Target Call:** `url_to_fs`
- **Context:** `_CheckpointConnector.__max_ckpt_version_in_folder`
- **Arguments:** `str(dir_path)`
- **Keywords:** `{}`

```python
        fs, uri = url_to_fs(str(dir_path))
```

</details>

#### <a id="lightning-ai-pytorch-lightning-f-write"></a>🔹 `f.write` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>f.write</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/cli/cmd_pl_init.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/cli/cmd_pl_init.py#L133) (Line 133)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/cli/cmd_pl_init.py#L133
- **Target Call:** `f.write`
- **Context:** `project_file_from_template`
- **Arguments:** `rendered_template`
- **Keywords:** `{}`

```python
        file.write(rendered_template)
```

##### 2. [src/lightning/fabric/utilities/cloud_io.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L80) (Line 80)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/utilities/cloud_io.py#L80
- **Target Call:** `f.write`
- **Context:** `_atomic_save`
- **Arguments:** `bytesbuffer.getvalue()`
- **Keywords:** `{}`

```python
        f.write(bytesbuffer.getvalue())
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-rmdir"></a>🔹 `fs.rmdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.rmdir</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/app/storage/filesystem.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L148) (Line 148)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/app/storage/filesystem.py#L148
- **Target Call:** `fs.rmdir`
- **Context:** `FileSystem.rm`
- **Arguments:** `str(delete_path)`
- **Keywords:** `{}`

```python
                self._fs.rmdir(str(delete_path))
```

</details>

#### <a id="lightning-ai-pytorch-lightning-fs-rm-file"></a>🔹 `fs.rm_file` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.rm_file</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/fabric/loggers/csv_logs.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L274) (Line 274)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/fabric/loggers/csv_logs.py#L274
- **Target Call:** `fs.rm_file`
- **Context:** `_ExperimentWriter._check_log_dir_exists`
- **Arguments:** `self.metrics_file_path`
- **Keywords:** `{}`

```python
                self._fs.rm_file(self.metrics_file_path)
```

</details>

#### <a id="lightning-ai-pytorch-lightning-f-flush"></a>🔹 `f.flush` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.flush</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/pytorch/profilers/profiler.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/profilers/profiler.py#L115) (Line 115)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/profilers/profiler.py#L115
- **Target Call:** `f.flush`
- **Context:** `Profiler.describe`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self._output_file.flush()
```

</details>

#### <a id="lightning-ai-pytorch-lightning-f-close"></a>🔹 `f.close` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.close</code> in Lightning-AI/pytorch-lightning</b></summary>

##### 1. [src/lightning/pytorch/profilers/profiler.py](https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/profilers/profiler.py#L143) (Line 143)
- **Line Link:** https://github.com/Lightning-AI/pytorch-lightning/blob/main/src/lightning/pytorch/profilers/profiler.py#L143
- **Target Call:** `f.close`
- **Context:** `Profiler.teardown`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self._output_file.close()
```

</details>

### [duckdb/duckdb](https://github.com/duckdb/duckdb)
- **Files Scanned:** `15` | **Files with Usages:** `0` | **Total Usages:** `0`

No direct filesystem / fsspec usages detected in this target.

### [huggingface/datasets](https://github.com/huggingface/datasets)
- **Files Scanned:** `141` | **Files with Usages:** `17` | **Total Usages:** `102`

#### <a id="huggingface-datasets-url-to-fs"></a>🔹 `url_to_fs` (22 occurrences)

<details open>
<summary><b>Click to expand/collapse 22 occurrences for <code>url_to_fs</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1851) (Line 1851)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1851
- **Target Call:** `url_to_fs`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
        fs, _ = url_to_fs(dataset_path, **(storage_options or {}))
```

##### 2. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2022) (Line 2022)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2022
- **Target Call:** `url_to_fs`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
        fs, dataset_path = url_to_fs(dataset_path, **(storage_options or {}))
```

##### 3. [src/datasets/arrow_writer.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L521) (Line 521)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L521
- **Target Call:** `url_to_fs`
- **Context:** `ArrowWriter.__init__`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            fs, path = url_to_fs(path, **(storage_options or {}))
```

##### 4. [src/datasets/builder.py](https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L789) (Line 789)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L789
- **Target Call:** `url_to_fs`
- **Context:** `DatasetBuilder.download_and_prepare`
- **Arguments:** `output_dir`
- **Keywords:** `{}`

```python
        fs, output_dir = url_to_fs(output_dir, **(storage_options or {}))
```

##### 5. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L356) (Line 356)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L356
- **Target Call:** `url_to_fs`
- **Context:** `resolve_pattern`
- **Arguments:** `pattern`
- **Keywords:** `{}`

```python
    fs, fs_pattern = url_to_fs(pattern, **storage_options)
```

##### 6. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L509) (Line 509)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L509
- **Target Call:** `url_to_fs`
- **Context:** `_get_single_origin_metadata`
- **Arguments:** `data_file`
- **Keywords:** `{}`

```python
        fs, fs_path = url_to_fs(data_file, **storage_options)
```

##### 7. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1359) (Line 1359)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1359
- **Target Call:** `url_to_fs`
- **Context:** `DatasetDict.save_to_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{}`

```python
        fs, _ = url_to_fs(dataset_dict_path, **(storage_options or {}))
```

##### 8. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1418) (Line 1418)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1418
- **Target Call:** `url_to_fs`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{}`

```python
        fs, dataset_dict_path = url_to_fs(dataset_dict_path, **(storage_options or {}))
```

##### 9. [src/datasets/download/download_manager.py](https://github.com/huggingface/datasets/blob/main/src/datasets/download/download_manager.py#L196) (Line 196)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/download/download_manager.py#L196
- **Target Call:** `url_to_fs`
- **Context:** `DownloadManager._download_batched`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            fs, path = url_to_fs(path, **download_config.storage_options)
```

##### 10. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L208) (Line 208)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L208
- **Target Call:** `url_to_fs`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `dataset_info_dir`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(dataset_info_dir, **(storage_options or {}))
```

##### 11. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L273) (Line 273)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L273
- **Target Call:** `url_to_fs`
- **Context:** `DatasetInfo.from_directory`
- **Arguments:** `dataset_info_dir`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(dataset_info_dir, **(storage_options or {}))
```

##### 12. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1772) (Line 1772)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1772
- **Target Call:** `url_to_fs`
- **Context:** `load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
    fs, *_ = url_to_fs(dataset_path, **(storage_options or {}))
```

##### 13. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L295) (Line 295)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L295
- **Target Call:** `url_to_fs`
- **Context:** `fsspec_head`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
    fs, path = url_to_fs(url, **(storage_options or {}))
```

##### 14. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L317) (Line 317)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L317
- **Target Call:** `url_to_fs`
- **Context:** `fsspec_get`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
    fs, path = url_to_fs(url, **(storage_options or {}))
```

##### 15. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L645) (Line 645)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L645
- **Target Call:** `url_to_fs`
- **Context:** `xexists`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(urlpath, **storage_options)
```

##### 16. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L745) (Line 745)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L745
- **Target Call:** `url_to_fs`
- **Context:** `xisfile`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(path, **storage_options)
```

##### 17. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L765) (Line 765)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L765
- **Target Call:** `url_to_fs`
- **Context:** `xgetsize`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs, *_ = fs, *_ = url_to_fs(path, **storage_options)
```

##### 18. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L793) (Line 793)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L793
- **Target Call:** `url_to_fs`
- **Context:** `xisdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs, *_ = fs, *_ = url_to_fs(path, **storage_options)
```

##### 19. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1030) (Line 1030)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1030
- **Target Call:** `url_to_fs`
- **Context:** `xlistdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(path, **storage_options)
```

##### 20. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1057) (Line 1057)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1057
- **Target Call:** `url_to_fs`
- **Context:** `xglob`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(urlpath, **storage_options)
```

##### 21. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1083) (Line 1083)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1083
- **Target Call:** `url_to_fs`
- **Context:** `xwalk`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        fs, *_ = url_to_fs(urlpath, **storage_options)
```

##### 22. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1161) (Line 1161)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1161
- **Target Call:** `url_to_fs`
- **Context:** `xPath.glob`
- **Arguments:** `xjoin(posix_path, pattern)`
- **Keywords:** `{}`

```python
            fs, *_ = url_to_fs(xjoin(posix_path, pattern), **(storage_options or {}))
```

</details>

#### <a id="huggingface-datasets-fs-open"></a>🔹 `fs.open` (17 occurrences)

<details open>
<summary><b>Click to expand/collapse 17 occurrences for <code>fs.open</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1931) (Line 1931)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1931
- **Target Call:** `fs.open`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME), 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with fs.open(
            posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME), "w", encoding="utf-8"
        ) as state_file:
```

##### 2. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1935) (Line 1935)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1935
- **Target Call:** `fs.open`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_INFO_FILENAME), 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with fs.open(
            posixpath.join(dataset_path, config.DATASET_INFO_FILENAME), "w", encoding="utf-8"
        ) as dataset_info_file:
```

##### 3. [src/datasets/arrow_writer.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L524) (Line 524)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L524
- **Target Call:** `fs.open`
- **Context:** `ArrowWriter.__init__`
- **Arguments:** `path, 'wb'`
- **Keywords:** `{}`

```python
            self.stream = self._fs.open(path, "wb")
```

##### 4. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1370) (Line 1370)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1370
- **Target Call:** `fs.open`
- **Context:** `DatasetDict.save_to_disk`
- **Arguments:** `posixpath.join(dataset_dict_path, config.DATASETDICT_JSON_FILENAME), 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with fs.open(
            posixpath.join(dataset_dict_path, config.DATASETDICT_JSON_FILENAME),
            "w",
            encoding="utf-8",
        ) as f:
```

##### 5. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1432) (Line 1432)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1432
- **Target Call:** `fs.open`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_json_path, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with fs.open(dataset_dict_json_path, "r", encoding="utf-8") as f:
```

##### 6. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L209) (Line 209)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L209
- **Target Call:** `fs.open`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), 'wb'`
- **Keywords:** `{}`

```python
        with fs.open(posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), "wb") as f:
```

##### 7. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L212) (Line 212)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L212
- **Target Call:** `fs.open`
- **Context:** `DatasetInfo.write_to_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.LICENSE_FILENAME), 'wb'`
- **Keywords:** `{}`

```python
            with fs.open(posixpath.join(dataset_info_dir, config.LICENSE_FILENAME), "wb") as f:
```

##### 8. [src/datasets/info.py](https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L277) (Line 277)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/info.py#L277
- **Target Call:** `fs.open`
- **Context:** `DatasetInfo.from_directory`
- **Arguments:** `posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with fs.open(posixpath.join(dataset_info_dir, config.DATASET_INFO_FILENAME), "r", encoding="utf-8") as f:
```

##### 9. [src/datasets/io/csv.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/csv.py#L94) (Line 94)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/io/csv.py#L94
- **Target Call:** `fs.open`
- **Context:** `CsvDatasetWriter.write`
- **Arguments:** `self.path_or_buf, 'wb'`
- **Keywords:** `{}`

```python
            with fsspec.open(self.path_or_buf, "wb", **(self.storage_options or {})) as buffer:
```

##### 10. [src/datasets/io/json.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/json.py#L113) (Line 113)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/io/json.py#L113
- **Target Call:** `fs.open`
- **Context:** `JsonDatasetWriter.write`
- **Arguments:** `self.path_or_buf, 'wb'`
- **Keywords:** `{'compression': 'compression'}`

```python
            with fsspec.open(
                self.path_or_buf, "wb", compression=compression, **(self.storage_options or {})
            ) as buffer:
```

##### 11. [src/datasets/io/parquet.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/parquet.py#L100) (Line 100)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/io/parquet.py#L100
- **Target Call:** `fs.open`
- **Context:** `ParquetDatasetWriter.write`
- **Arguments:** `self.path_or_buf, 'wb'`
- **Keywords:** `{}`

```python
            with fsspec.open(self.path_or_buf, "wb", **(self.storage_options or {})) as buffer:
```

##### 12. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L881) (Line 881)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L881
- **Target Call:** `fs.open`
- **Context:** `HubBucketDatasetModuleFactory.get_module`
- **Arguments:** `standalone_yaml_path, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
            with hffs.open(standalone_yaml_path, "r", encoding="utf-8") as f:
```

##### 13. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L935) (Line 935)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L935
- **Target Call:** `fs.open`
- **Context:** `HubBucketDatasetModuleFactory.get_module`
- **Arguments:** `xjoin(self.path, config.DATASETDICT_INFOS_FILENAME), 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
            with hffs.open(xjoin(self.path, config.DATASETDICT_INFOS_FILENAME), "r", encoding="utf-8") as f:
```

##### 14. [src/datasets/search.py](https://github.com/huggingface/datasets/blob/main/src/datasets/search.py#L396) (Line 396)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/search.py#L396
- **Target Call:** `fs.open`
- **Context:** `FaissIndex.save`
- **Arguments:** `str(file), 'wb'`
- **Keywords:** `{}`

```python
        with fsspec.open(str(file), "wb", **(storage_options or {})) as f:
```

##### 15. [src/datasets/search.py](https://github.com/huggingface/datasets/blob/main/src/datasets/search.py#L411) (Line 411)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/search.py#L411
- **Target Call:** `fs.open`
- **Context:** `FaissIndex.load`
- **Arguments:** `str(file), 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(str(file), "rb", **(storage_options or {})) as f:
```

##### 16. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L559) (Line 559)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L559
- **Target Call:** `fs.open`
- **Context:** `_get_extraction_protocol`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
        with fsspec.open(urlpath, **(storage_options or {})) as f:
```

##### 17. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L982) (Line 982)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L982
- **Target Call:** `fs.open`
- **Context:** `xopen`
- **Arguments:** `paths[0], mode`
- **Keywords:** `{}`

```python
            file_obj = fs.open(paths[0], mode)
```

</details>

#### <a id="huggingface-datasets-fs-isfile"></a>🔹 `fs.isfile` (11 occurrences)

<details open>
<summary><b>Click to expand/collapse 11 occurrences for <code>fs.isfile</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2029) (Line 2029)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2029
- **Target Call:** `fs.isfile`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_dict_json_path`
- **Keywords:** `{}`

```python
        dataset_dict_is_file = fs.isfile(dataset_dict_json_path)
```

##### 2. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2030) (Line 2030)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2030
- **Target Call:** `fs.isfile`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_info_path`
- **Keywords:** `{}`

```python
        dataset_info_is_file = fs.isfile(dataset_info_path)
```

##### 3. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2031) (Line 2031)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L2031
- **Target Call:** `fs.isfile`
- **Context:** `Dataset.load_from_disk`
- **Arguments:** `dataset_state_json_path`
- **Keywords:** `{}`

```python
        dataset_state_is_file = fs.isfile(dataset_state_json_path)
```

##### 4. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1423) (Line 1423)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1423
- **Target Call:** `fs.isfile`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_dict_json_path`
- **Keywords:** `{}`

```python
        if not fs.isfile(dataset_dict_json_path):
```

##### 5. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1424) (Line 1424)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1424
- **Target Call:** `fs.isfile`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_info_path`
- **Keywords:** `{}`

```python
            if fs.isfile(dataset_info_path) and fs.isfile(dataset_state_json_path):
```

##### 6. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1424) (Line 1424)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1424
- **Target Call:** `fs.isfile`
- **Context:** `DatasetDict.load_from_disk`
- **Arguments:** `dataset_state_json_path`
- **Keywords:** `{}`

```python
            if fs.isfile(dataset_info_path) and fs.isfile(dataset_state_json_path):
```

##### 7. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L934) (Line 934)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L934
- **Target Call:** `fs.isfile`
- **Context:** `HubBucketDatasetModuleFactory.get_module`
- **Arguments:** `xjoin(self.path, config.DATASETDICT_INFOS_FILENAME)`
- **Keywords:** `{}`

```python
        if hffs.isfile(xjoin(self.path, config.DATASETDICT_INFOS_FILENAME)):
```

##### 8. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1775) (Line 1775)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1775
- **Target Call:** `fs.isfile`
- **Context:** `load_from_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_INFO_FILENAME)`
- **Keywords:** `{}`

```python
    if fs.isfile(posixpath.join(dataset_path, config.DATASET_INFO_FILENAME)) and fs.isfile(
```

##### 9. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1775) (Line 1775)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1775
- **Target Call:** `fs.isfile`
- **Context:** `load_from_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME)`
- **Keywords:** `{}`

```python
    if fs.isfile(posixpath.join(dataset_path, config.DATASET_INFO_FILENAME)) and fs.isfile(
        posixpath.join(dataset_path, config.DATASET_STATE_JSON_FILENAME)
    ):
```

##### 10. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1779) (Line 1779)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1779
- **Target Call:** `fs.isfile`
- **Context:** `load_from_disk`
- **Arguments:** `posixpath.join(dataset_path, config.DATASETDICT_JSON_FILENAME)`
- **Keywords:** `{}`

```python
    elif fs.isfile(posixpath.join(dataset_path, config.DATASETDICT_JSON_FILENAME)):
```

##### 11. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L746) (Line 746)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L746
- **Target Call:** `fs.isfile`
- **Context:** `xisfile`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
        return fs.isfile(main_hop)
```

</details>

#### <a id="huggingface-datasets-fs-glob"></a>🔹 `fs.glob` (8 occurrences)

<details open>
<summary><b>Click to expand/collapse 8 occurrences for <code>fs.glob</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6758) (Line 6758)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6758
- **Target Call:** `fs.glob`
- **Context:** `_push_to_repo`
- **Arguments:** `f'{data_dir}/{split}-*'`
- **Keywords:** `{'detail': 'True'}`

```python
            files_to_delete = dirfs.glob(f"{data_dir}/{split}-*", detail=True)
```

##### 2. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6848) (Line 6848)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6848
- **Target Call:** `fs.glob`
- **Context:** `_push_to_bucket`
- **Arguments:** `f'{data_dir}/{split}-*'`
- **Keywords:** `{'detail': 'True'}`

```python
        files_to_delete = dirfs.glob(f"{data_dir}/{split}-*", detail=True)
```

##### 3. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6966) (Line 6966)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6966
- **Target Call:** `fs.glob`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED.replace('{split}', '*')`
- **Keywords:** `{}`

```python
    for file_path in fs.glob(PUSH_TO_HUB_WITHOUT_METADATA_CONFIGS_SPLIT_PATTERN_SHARDED.replace("{split}", "*")):
```

##### 4. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L372) (Line 372)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L372
- **Target Call:** `fs.glob`
- **Context:** `resolve_pattern`
- **Arguments:** `fs_pattern`
- **Keywords:** `{'detail': 'True'}`

```python
    for filepath, info in fs.glob(fs_pattern, detail=True, **glob_kwargs).items():
```

##### 5. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L2630) (Line 2630)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L2630
- **Target Call:** `fs.glob`
- **Context:** `_push_to_repo`
- **Arguments:** `f'{data_dir}/*'`
- **Keywords:** `{}`

```python
            files_to_delete = list(dirfs.glob(f"{data_dir}/*"))
```

##### 6. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L2722) (Line 2722)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L2722
- **Target Call:** `fs.glob`
- **Context:** `_push_to_bucket`
- **Arguments:** `f'{data_dir}/*'`
- **Keywords:** `{}`

```python
        files_to_delete = list(dirfs.glob(f"{data_dir}/*"))
```

##### 7. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1059) (Line 1059)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1059
- **Target Call:** `fs.glob`
- **Context:** `xglob`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        globbed_paths = fs.glob(inner_path)
```

##### 8. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1162) (Line 1162)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1162
- **Target Call:** `fs.glob`
- **Context:** `xPath.glob`
- **Arguments:** `xjoin(main_hop, pattern)`
- **Keywords:** `{}`

```python
            globbed_paths = fs.glob(xjoin(main_hop, pattern))
```

</details>

#### <a id="huggingface-datasets-f-write"></a>🔹 `f.write` (8 occurrences)

<details open>
<summary><b>Click to expand/collapse 8 occurrences for <code>f.write</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/io/csv.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/csv.py#L127) (Line 127)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/io/csv.py#L127
- **Target Call:** `f.write`
- **Context:** `CsvDatasetWriter._write`
- **Arguments:** `csv_str`
- **Keywords:** `{}`

```python
                written += file_obj.write(csv_str)
```

##### 2. [src/datasets/io/csv.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/csv.py#L141) (Line 141)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/io/csv.py#L141
- **Target Call:** `f.write`
- **Context:** `CsvDatasetWriter._write`
- **Arguments:** `csv_str`
- **Keywords:** `{}`

```python
                    written += file_obj.write(csv_str)
```

##### 3. [src/datasets/io/json.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/json.py#L163) (Line 163)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/io/json.py#L163
- **Target Call:** `f.write`
- **Context:** `JsonDatasetWriter._write`
- **Arguments:** `json_str`
- **Keywords:** `{}`

```python
                written += file_obj.write(json_str)
```

##### 4. [src/datasets/io/json.py](https://github.com/huggingface/datasets/blob/main/src/datasets/io/json.py#L176) (Line 176)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/io/json.py#L176
- **Target Call:** `f.write`
- **Context:** `JsonDatasetWriter._write`
- **Arguments:** `json_str`
- **Keywords:** `{}`

```python
                    written += file_obj.write(json_str)
```

##### 5. [src/datasets/packaged_modules/webdataset/_tenbin.py](https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L226) (Line 226)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L226
- **Target Call:** `f.write`
- **Context:** `write_chunk`
- **Arguments:** `magic_bytes`
- **Keywords:** `{}`

```python
    stream.write(magic_bytes)
```

##### 6. [src/datasets/packaged_modules/webdataset/_tenbin.py](https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L227) (Line 227)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L227
- **Target Call:** `f.write`
- **Context:** `write_chunk`
- **Arguments:** `struct.pack('@q', nbytes)`
- **Keywords:** `{}`

```python
    stream.write(struct.pack("@q", nbytes))
```

##### 7. [src/datasets/packaged_modules/webdataset/_tenbin.py](https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L228) (Line 228)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L228
- **Target Call:** `f.write`
- **Context:** `write_chunk`
- **Arguments:** `bytedata(buf)`
- **Keywords:** `{}`

```python
    stream.write(bytedata(buf))
```

##### 8. [src/datasets/packaged_modules/webdataset/_tenbin.py](https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L231) (Line 231)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L231
- **Target Call:** `f.write`
- **Context:** `write_chunk`
- **Arguments:** `b'\x00' * padding`
- **Keywords:** `{}`

```python
        stream.write(b"\0" * padding)
```

</details>

#### <a id="huggingface-datasets-f-read"></a>🔹 `f.read` (6 occurrences)

<details open>
<summary><b>Click to expand/collapse 6 occurrences for <code>f.read</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L882) (Line 882)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L882
- **Target Call:** `f.read`
- **Context:** `HubBucketDatasetModuleFactory.get_module`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                standalone_yaml_data = yaml.safe_load(f.read())
```

##### 2. [src/datasets/packaged_modules/webdataset/_tenbin.py](https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L236) (Line 236)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L236
- **Target Call:** `f.read`
- **Context:** `read_chunk`
- **Arguments:** `8`
- **Keywords:** `{}`

```python
    magic = stream.read(8)
```

##### 3. [src/datasets/packaged_modules/webdataset/_tenbin.py](https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L241) (Line 241)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L241
- **Target Call:** `f.read`
- **Context:** `read_chunk`
- **Arguments:** `8`
- **Keywords:** `{}`

```python
    nbytes = stream.read(8)
```

##### 4. [src/datasets/packaged_modules/webdataset/_tenbin.py](https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L245) (Line 245)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L245
- **Target Call:** `f.read`
- **Context:** `read_chunk`
- **Arguments:** `nbytes`
- **Keywords:** `{}`

```python
    data = stream.read(nbytes)
```

##### 5. [src/datasets/packaged_modules/webdataset/_tenbin.py](https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L248) (Line 248)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/packaged_modules/webdataset/_tenbin.py#L248
- **Target Call:** `f.read`
- **Context:** `read_chunk`
- **Arguments:** `padding`
- **Keywords:** `{}`

```python
        stream.read(padding)
```

##### 6. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L773) (Line 773)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L773
- **Target Call:** `f.read`
- **Context:** `xgetsize`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                size = len(f.read())
```

</details>

#### <a id="huggingface-datasets-fs-read-text"></a>🔹 `fs.read_text` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>fs.read_text</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6911) (Line 6911)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6911
- **Target Call:** `fs.read_text`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.DATASETDICT_INFOS_FILENAME`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        legacy_dataset_info: dict = json.loads(fs.read_text(config.DATASETDICT_INFOS_FILENAME, encoding="utf-8")).get(
```

##### 2. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6920) (Line 6920)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L6920
- **Target Call:** `fs.read_text`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.REPOCARD_FILENAME`
- **Keywords:** `{'newline': "''", 'encoding': "'utf-8'"}`

```python
        dataset_card = DatasetCard(fs.read_text(config.REPOCARD_FILENAME, newline="", encoding="utf-8"))
```

##### 3. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L7019) (Line 7019)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L7019
- **Target Call:** `fs.read_text`
- **Context:** `_get_updated_dataset_card`
- **Arguments:** `config.DATASETDICT_INFOS_FILENAME`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        legacy_dataset_infos: dict = json.loads(fs.read_text(config.DATASETDICT_INFOS_FILENAME, encoding="utf-8"))
```

##### 4. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L873) (Line 873)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L873
- **Target Call:** `fs.read_text`
- **Context:** `HubBucketDatasetModuleFactory.get_module`
- **Arguments:** `readme_path`
- **Keywords:** `{'newline': "''", 'encoding': "'utf-8'"}`

```python
            dataset_card_data = DatasetCard(hffs.read_text(readme_path, newline="", encoding="utf-8")).data
```

##### 5. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L877) (Line 877)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L877
- **Target Call:** `fs.read_text`
- **Context:** `HubBucketDatasetModuleFactory.get_module`
- **Arguments:** `standalone_yaml_path`
- **Keywords:** `{'newline': "''", 'encoding': "'utf-8'"}`

```python
            standalone_yaml_data = yaml.safe_load(hffs.read_text(standalone_yaml_path, newline="", encoding="utf-8"))
```

</details>

#### <a id="huggingface-datasets-f-close"></a>🔹 `f.close` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>f.close</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/arrow_writer.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L570) (Line 570)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L570
- **Target Call:** `f.close`
- **Context:** `ArrowWriter.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.stream.close()  # This also closes self.pa_writer if it is opened
```

##### 2. [src/datasets/arrow_writer.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L791) (Line 791)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L791
- **Target Call:** `f.close`
- **Context:** `ArrowWriter.finalize`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                self.stream.close()
```

##### 3. [src/datasets/arrow_writer.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L794) (Line 794)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_writer.py#L794
- **Target Call:** `f.close`
- **Context:** `ArrowWriter.finalize`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                self.stream.close()
```

##### 4. [src/datasets/utils/extract.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/extract.py#L132) (Line 132)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/extract.py#L132
- **Target Call:** `f.close`
- **Context:** `TarExtractor.extract`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        tar_file.close()
```

</details>

#### <a id="huggingface-datasets-fs-exists"></a>🔹 `fs.exists` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fs.exists</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/builder.py](https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L842) (Line 842)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L842
- **Target Call:** `fs.exists`
- **Context:** `DatasetBuilder.download_and_prepare`
- **Arguments:** `posixpath.join(self._output_dir, config.DATASET_INFO_FILENAME)`
- **Keywords:** `{}`

```python
            data_exists = self._fs.exists(posixpath.join(self._output_dir, config.DATASET_INFO_FILENAME))
```

##### 2. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L880) (Line 880)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L880
- **Target Call:** `fs.exists`
- **Context:** `HubBucketDatasetModuleFactory.get_module`
- **Arguments:** `standalone_yaml_path`
- **Keywords:** `{}`

```python
        if hffs.exists(standalone_yaml_path):
```

##### 3. [src/datasets/load.py](https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1773) (Line 1773)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/load.py#L1773
- **Target Call:** `fs.exists`
- **Context:** `load_from_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{}`

```python
    if not fs.exists(dataset_path):
```

##### 4. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L646) (Line 646)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L646
- **Target Call:** `fs.exists`
- **Context:** `xexists`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
        return fs.exists(main_hop)
```

</details>

#### <a id="huggingface-datasets-fs-info"></a>🔹 `fs.info` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fs.info</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/data_files.py](https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L514) (Line 514)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/data_files.py#L514
- **Target Call:** `fs.info`
- **Context:** `_get_single_origin_metadata`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    info = fs.info(fs_path)
```

##### 2. [src/datasets/download/download_manager.py](https://github.com/huggingface/datasets/blob/main/src/datasets/download/download_manager.py#L199) (Line 199)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/download/download_manager.py#L199
- **Target Call:** `fs.info`
- **Context:** `DownloadManager._download_batched`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                size = fs.info(path).get("size", 0)
```

##### 3. [src/datasets/filesystems/compression.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/compression.py#L66) (Line 66)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/compression.py#L66
- **Target Call:** `fs.info`
- **Context:** `BaseCompressedFileFileSystem._get_dirs`
- **Arguments:** `self.fo`
- **Keywords:** `{}`

```python
            f = {**self._open_with_fsspec().fs.info(self.fo), "name": self.uncompressed_name}
```

##### 4. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L296) (Line 296)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L296
- **Target Call:** `fs.info`
- **Context:** `fsspec_head`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    return fs.info(path)
```

</details>

#### <a id="huggingface-datasets-fs-makedirs"></a>🔹 `fs.makedirs` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.makedirs</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/arrow_dataset.py](https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1863) (Line 1863)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/arrow_dataset.py#L1863
- **Target Call:** `fs.makedirs`
- **Context:** `Dataset.save_to_disk`
- **Arguments:** `dataset_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        fs.makedirs(dataset_path, exist_ok=True)
```

##### 2. [src/datasets/builder.py](https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L863) (Line 863)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L863
- **Target Call:** `fs.makedirs`
- **Context:** `DatasetBuilder.incomplete_dir`
- **Arguments:** `dirname`
- **Keywords:** `{'exist_ok': 'True'}`

```python
                    self._fs.makedirs(dirname, exist_ok=True)
```

##### 3. [src/datasets/dataset_dict.py](https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1368) (Line 1368)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/dataset_dict.py#L1368
- **Target Call:** `fs.makedirs`
- **Context:** `DatasetDict.save_to_disk`
- **Arguments:** `dataset_dict_path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        fs.makedirs(dataset_dict_path, exist_ok=True)
```

</details>

#### <a id="huggingface-datasets-fs-isdir"></a>🔹 `fs.isdir` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.isdir</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L797) (Line 797)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L797
- **Target Call:** `fs.isdir`
- **Context:** `xisdir`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        return fs.isdir(inner_path)
```

##### 2. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1032) (Line 1032)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1032
- **Target Call:** `fs.isdir`
- **Context:** `xlistdir`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        if inner_path.strip("/") and not fs.isdir(inner_path):
```

##### 3. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1085) (Line 1085)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1085
- **Target Call:** `fs.isdir`
- **Context:** `xwalk`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        if inner_path.strip("/") and not fs.isdir(inner_path):
```

</details>

#### <a id="huggingface-datasets-fsspec-filesystem"></a>🔹 `fsspec.filesystem` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fsspec.filesystem</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/builder.py](https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L422) (Line 422)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/builder.py#L422
- **Target Call:** `fsspec.filesystem`
- **Context:** `DatasetBuilder.__init__`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
        self._fs: fsspec.AbstractFileSystem = fsspec.filesystem("file")
```

</details>

#### <a id="huggingface-datasets-fs-mv"></a>🔹 `fs.mv` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.mv</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/filesystems/__init__.py](https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L52) (Line 52)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/filesystems/__init__.py#L52
- **Target Call:** `fs.mv`
- **Context:** `rename`
- **Arguments:** `src, dst`
- **Keywords:** `{'recursive': 'True'}`

```python
        fs.mv(src, dst, recursive=True)
```

</details>

#### <a id="huggingface-datasets-fs-get-file"></a>🔹 `fs.get_file` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.get_file</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L330) (Line 330)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L330
- **Target Call:** `fs.get_file`
- **Context:** `fsspec_get`
- **Arguments:** `path, temp_file.name`
- **Keywords:** `{'callback': 'callback'}`

```python
    fs.get_file(path, temp_file.name, callback=callback)
```

</details>

#### <a id="huggingface-datasets-fs-size"></a>🔹 `fs.size` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.size</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L767) (Line 767)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L767
- **Target Call:** `fs.size`
- **Context:** `xgetsize`
- **Arguments:** `main_hop`
- **Keywords:** `{}`

```python
            size = fs.size(main_hop)
```

</details>

#### <a id="huggingface-datasets-get-fs-token-paths"></a>🔹 `get_fs_token_paths` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>get_fs_token_paths</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L977) (Line 977)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L977
- **Target Call:** `get_fs_token_paths`
- **Context:** `xopen`
- **Arguments:** `file, mode`
- **Keywords:** `{'storage_options': 'kwargs'}`

```python
            fs, fs_token, paths = fsspec.get_fs_token_paths(
                file,
                mode,
                storage_options=kwargs,
            )
```

</details>

#### <a id="huggingface-datasets-fs-listdir"></a>🔹 `fs.listdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.listdir</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1034) (Line 1034)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1034
- **Target Call:** `fs.listdir`
- **Context:** `xlistdir`
- **Arguments:** `inner_path`
- **Keywords:** `{'detail': 'False'}`

```python
        paths = fs.listdir(inner_path, detail=False)
```

</details>

#### <a id="huggingface-datasets-fs-walk"></a>🔹 `fs.walk` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.walk</code> in huggingface/datasets</b></summary>

##### 1. [src/datasets/utils/file_utils.py](https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1088) (Line 1088)
- **Line Link:** https://github.com/huggingface/datasets/blob/main/src/datasets/utils/file_utils.py#L1088
- **Target Call:** `fs.walk`
- **Context:** `xwalk`
- **Arguments:** `inner_path`
- **Keywords:** `{}`

```python
        for dirpath, dirnames, filenames in fs.walk(inner_path, **kwargs):
```

</details>

### [mlflow/mlflow](https://github.com/mlflow/mlflow)
- **Files Scanned:** `1301` | **Files with Usages:** `3` | **Total Usages:** `3`

#### <a id="mlflow-mlflow-f-read"></a>🔹 `f.read` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>f.read</code> in mlflow/mlflow</b></summary>

##### 1. [mlflow/server/handlers.py](https://github.com/mlflow/mlflow/blob/master/mlflow/server/handlers.py#L3727) (Line 3727)
- **Line Link:** https://github.com/mlflow/mlflow/blob/master/mlflow/server/handlers.py#L3727
- **Target Call:** `f.read`
- **Context:** `_upload_artifact`
- **Arguments:** `ARTIFACT_STREAM_CHUNK_SIZE`
- **Keywords:** `{}`

```python
                while chunk := request.stream.read(ARTIFACT_STREAM_CHUNK_SIZE):
```

##### 2. [mlflow/tracking/client.py](https://github.com/mlflow/mlflow/blob/master/mlflow/tracking/client.py#L3014) (Line 3014)
- **Line Link:** https://github.com/mlflow/mlflow/blob/master/mlflow/tracking/client.py#L3014
- **Target Call:** `f.read`
- **Context:** `MlflowClient.log_stream`
- **Arguments:** `8192`
- **Keywords:** `{}`

```python
                while chunk := stream.read(8192):
```

</details>

#### <a id="mlflow-mlflow-f-close"></a>🔹 `f.close` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.close</code> in mlflow/mlflow</b></summary>

##### 1. [mlflow/utils/file_utils.py](https://github.com/mlflow/mlflow/blob/master/mlflow/utils/file_utils.py#L920) (Line 920)
- **Line Link:** https://github.com/mlflow/mlflow/blob/master/mlflow/utils/file_utils.py#L920
- **Target Call:** `f.close`
- **Context:** `ExclusiveFileLock.__exit__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self.fd.close()
```

</details>

### [apache/arrow](https://github.com/apache/arrow)
- **Files Scanned:** `80` | **Files with Usages:** `1` | **Total Usages:** `21`

#### <a id="apache-arrow-fs-rm"></a>🔹 `fs.rm` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fs.rm</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L363) (Line 363)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L363
- **Target Call:** `fs.rm`
- **Context:** `FSSpecHandler.delete_dir`
- **Arguments:** `path`
- **Keywords:** `{'recursive': 'True'}`

```python
        self.fs.rm(path, recursive=True)
```

##### 2. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L374) (Line 374)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L374
- **Target Call:** `fs.rm`
- **Context:** `FSSpecHandler._delete_dir_contents`
- **Arguments:** `subpath`
- **Keywords:** `{'recursive': 'True'}`

```python
                self.fs.rm(subpath, recursive=True)
```

##### 3. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L376) (Line 376)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L376
- **Target Call:** `fs.rm`
- **Context:** `FSSpecHandler._delete_dir_contents`
- **Arguments:** `subpath`
- **Keywords:** `{}`

```python
                self.fs.rm(subpath)
```

##### 4. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L392) (Line 392)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L392
- **Target Call:** `fs.rm`
- **Context:** `FSSpecHandler.delete_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs.rm(path)
```

</details>

#### <a id="apache-arrow-fs-open"></a>🔹 `fs.open` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fs.open</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L410) (Line 410)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L410
- **Target Call:** `fs.open`
- **Context:** `FSSpecHandler.open_input_stream`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'rb'"}`

```python
        return PythonFile(self.fs.open(path, mode="rb"), mode="r")
```

##### 2. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L418) (Line 418)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L418
- **Target Call:** `fs.open`
- **Context:** `FSSpecHandler.open_input_file`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'rb'"}`

```python
        return PythonFile(self.fs.open(path, mode="rb"), mode="r")
```

##### 3. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L423) (Line 423)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L423
- **Target Call:** `fs.open`
- **Context:** `FSSpecHandler.open_output_stream`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'wb'"}`

```python
        return PythonFile(self.fs.open(path, mode="wb"), mode="w")
```

##### 4. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L428) (Line 428)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L428
- **Target Call:** `fs.open`
- **Context:** `FSSpecHandler.open_append_stream`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'ab'"}`

```python
        return PythonFile(self.fs.open(path, mode="ab"), mode="w")
```

</details>

#### <a id="apache-arrow-fs-isfile"></a>🔹 `fs.isfile` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.isfile</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L375) (Line 375)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L375
- **Target Call:** `fs.isfile`
- **Context:** `FSSpecHandler._delete_dir_contents`
- **Arguments:** `subpath`
- **Keywords:** `{}`

```python
            elif self.fs.isfile(subpath):
```

##### 2. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L407) (Line 407)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L407
- **Target Call:** `fs.isfile`
- **Context:** `FSSpecHandler.open_input_stream`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if not self.fs.isfile(path):
```

##### 3. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L415) (Line 415)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L415
- **Target Call:** `fs.isfile`
- **Context:** `FSSpecHandler.open_input_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if not self.fs.isfile(path):
```

</details>

#### <a id="apache-arrow-fs-isdir"></a>🔹 `fs.isdir` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.isdir</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L327) (Line 327)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L327
- **Target Call:** `fs.isdir`
- **Context:** `FSSpecHandler.get_file_info_selector`
- **Arguments:** `selector.base_dir`
- **Keywords:** `{}`

```python
        if not self.fs.isdir(selector.base_dir):
```

##### 2. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L373) (Line 373)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L373
- **Target Call:** `fs.isdir`
- **Context:** `FSSpecHandler._delete_dir_contents`
- **Arguments:** `subpath`
- **Keywords:** `{}`

```python
            if self.fs.isdir(subpath):
```

</details>

#### <a id="apache-arrow-fs-exists"></a>🔹 `fs.exists` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.exists</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L328) (Line 328)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L328
- **Target Call:** `fs.exists`
- **Context:** `FSSpecHandler.get_file_info_selector`
- **Arguments:** `selector.base_dir`
- **Keywords:** `{}`

```python
            if self.fs.exists(selector.base_dir):
```

##### 2. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L390) (Line 390)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L390
- **Target Call:** `fs.exists`
- **Context:** `FSSpecHandler.delete_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if not self.fs.exists(path):
```

</details>

#### <a id="apache-arrow-fs-info"></a>🔹 `fs.info` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.info</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L319) (Line 319)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L319
- **Target Call:** `fs.info`
- **Context:** `FSSpecHandler.get_file_info`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                info = self.fs.info(path)
```

</details>

#### <a id="apache-arrow-fs-find"></a>🔹 `fs.find` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.find</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L342) (Line 342)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L342
- **Target Call:** `fs.find`
- **Context:** `FSSpecHandler.get_file_info_selector`
- **Arguments:** `selector.base_dir`
- **Keywords:** `{'maxdepth': 'maxdepth', 'withdirs': 'True', 'detail': 'True'}`

```python
        selected_files = self.fs.find(
            selector.base_dir, maxdepth=maxdepth, withdirs=True, detail=True
        )
```

</details>

#### <a id="apache-arrow-fs-mkdir"></a>🔹 `fs.mkdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.mkdir</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L358) (Line 358)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L358
- **Target Call:** `fs.mkdir`
- **Context:** `FSSpecHandler.create_dir`
- **Arguments:** `path`
- **Keywords:** `{'create_parents': 'recursive'}`

```python
            self.fs.mkdir(path, create_parents=recursive)
```

</details>

#### <a id="apache-arrow-fs-listdir"></a>🔹 `fs.listdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.listdir</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L367) (Line 367)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L367
- **Target Call:** `fs.listdir`
- **Context:** `FSSpecHandler._delete_dir_contents`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'False'}`

```python
            subpaths = self.fs.listdir(path, detail=False)
```

</details>

#### <a id="apache-arrow-fs-mv"></a>🔹 `fs.mv` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.mv</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L395) (Line 395)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L395
- **Target Call:** `fs.mv`
- **Context:** `FSSpecHandler.move`
- **Arguments:** `src, dest`
- **Keywords:** `{'recursive': 'True'}`

```python
        self.fs.mv(src, dest, recursive=True)
```

</details>

#### <a id="apache-arrow-fs-copy"></a>🔹 `fs.copy` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.copy</code> in apache/arrow</b></summary>

##### 1. [python/pyarrow/fs.py](https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L400) (Line 400)
- **Line Link:** https://github.com/apache/arrow/blob/main/python/pyarrow/fs.py#L400
- **Target Call:** `fs.copy`
- **Context:** `FSSpecHandler.copy_file`
- **Arguments:** `src, dest`
- **Keywords:** `{}`

```python
        self.fs.copy(src, dest)
```

</details>

### [iterative/dvc](https://github.com/iterative/dvc)
- **Files Scanned:** `258` | **Files with Usages:** `51` | **Total Usages:** `282`

#### <a id="iterative-dvc-fs-join"></a>🔹 `fs.join` (56 occurrences)

<details open>
<summary><b>Click to expand/collapse 56 occurrences for <code>fs.join</code> in iterative/dvc</b></summary>

##### 1. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L53) (Line 53)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L53
- **Target Call:** `fs.join`
- **Context:** `artifacts_show`
- **Arguments:** `root, dirname`
- **Keywords:** `{}`

```python
            _dirname = _repo.fs.join(root, dirname) if dirname else root
```

##### 2. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L56) (Line 56)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L56
- **Target Call:** `fs.join`
- **Context:** `artifacts_show`
- **Arguments:** `_repo.fs.root_marker, as_posix(path)`
- **Keywords:** `{}`

```python
                path = _repo.fs.join(_repo.fs.root_marker, as_posix(path))
```

##### 3. [dvc/cachemgr.py](https://github.com/iterative/dvc/blob/main/dvc/cachemgr.py#L30) (Line 30)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/cachemgr.py#L30
- **Target Call:** `fs.join`
- **Context:** `_get_odb`
- **Arguments:** `fs_path, *prefix`
- **Keywords:** `{}`

```python
        fs_path = fs.join(fs_path, *prefix)
```

##### 4. [dvc/cachemgr.py](https://github.com/iterative/dvc/blob/main/dvc/cachemgr.py#L89) (Line 89)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/cachemgr.py#L89
- **Target Call:** `fs.join`
- **Context:** `CacheManager.fs_cache`
- **Arguments:** `self.local_cache_dir, self.FS_DIR`
- **Keywords:** `{}`

```python
            path=self.local.fs.join(self.local_cache_dir, self.FS_DIR),
```

##### 5. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L140) (Line 140)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/config.py#L140
- **Target Call:** `fs.join`
- **Context:** `Config.files`
- **Arguments:** `self.dvc_dir, self.CONFIG`
- **Keywords:** `{}`

```python
            files["repo"] = self.fs.join(self.dvc_dir, self.CONFIG)
```

##### 6. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L143) (Line 143)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/config.py#L143
- **Target Call:** `fs.join`
- **Context:** `Config.files`
- **Arguments:** `self.local_dvc_dir, self.CONFIG_LOCAL`
- **Keywords:** `{}`

```python
            files["local"] = self.wfs.join(self.local_dvc_dir, self.CONFIG_LOCAL)
```

##### 7. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L39) (Line 39)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L39
- **Target Call:** `fs.join`
- **Context:** `Remote.odb`
- **Arguments:** `path, '.dvc', CacheManager.FILES_DIR, DEFAULT_ALGORITHM`
- **Keywords:** `{}`

```python
            path = self.fs.join(path, ".dvc", CacheManager.FILES_DIR, DEFAULT_ALGORITHM)
```

##### 8. [dvc/data_cloud.py](https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L41) (Line 41)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/data_cloud.py#L41
- **Target Call:** `fs.join`
- **Context:** `Remote.odb`
- **Arguments:** `path, CacheManager.FILES_DIR, DEFAULT_ALGORITHM`
- **Keywords:** `{}`

```python
            path = self.fs.join(path, CacheManager.FILES_DIR, DEFAULT_ALGORITHM)
```

##### 9. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L197) (Line 197)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L197
- **Target Call:** `fs.join`
- **Context:** `_DVCFileSystem.abspath`
- **Arguments:** `self.getcwd(), path`
- **Keywords:** `{}`

```python
            path = self.join(self.getcwd(), path)
```

##### 10. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L268) (Line 268)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L268
- **Target Call:** `fs.join`
- **Context:** `_DVCFileSystem._from_key`
- **Arguments:** `self.repo.root_dir, *parts`
- **Keywords:** `{}`

```python
        return self.repo.fs.join(self.repo.root_dir, *parts)
```

##### 11. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L334) (Line 334)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L334
- **Target Call:** `fs.join`
- **Context:** `_DVCFileSystem._is_dvc_repo`
- **Arguments:** `dir_path, Repo.DVC_DIR`
- **Keywords:** `{}`

```python
        repo_path = self.repo.fs.join(dir_path, Repo.DVC_DIR)
```

##### 12. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L429) (Line 429)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L429
- **Target Call:** `fs.join`
- **Context:** `_DVCFileSystem.ls`
- **Arguments:** `path, name`
- **Keywords:** `{}`

```python
            entry_path = self.join(path, name) if name else path
```

##### 13. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L540) (Line 540)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L540
- **Target Call:** `fs.join`
- **Context:** `_DVCFileSystem._get`
- **Arguments:** `lpath, os.path.basename(rpath)`
- **Keywords:** `{}`

```python
            lpath = self.join(lpath, os.path.basename(rpath))
```

##### 14. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L310) (Line 310)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L310
- **Target Call:** `fs.join`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `dirname, DvcIgnore.DVCIGNORE_FILE`
- **Keywords:** `{}`

```python
        path = self.fs.join(dirname, DvcIgnore.DVCIGNORE_FILE)
```

##### 15. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L345) (Line 345)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L345
- **Target Call:** `fs.join`
- **Context:** `DvcIgnoreFilter._update`
- **Arguments:** `dirname, dname`
- **Keywords:** `{}`

```python
                self._update_sub_repo(self.fs.join(dirname, dname), ignore_trie)
```

##### 16. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L353) (Line 353)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L353
- **Target Call:** `fs.join`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `path, Repo.DVC_DIR`
- **Keywords:** `{}`

```python
        dvc_dir = self.fs.join(path, Repo.DVC_DIR)
```

##### 17. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L481) (Line 481)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L481
- **Target Call:** `fs.join`
- **Context:** `DvcIgnoreFilter._get_trie_pattern`
- **Arguments:** `self.root_dir, *prefix_key`
- **Keywords:** `{}`

```python
        prefix = self.fs.join(self.root_dir, *prefix_key)
```

##### 18. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L456) (Line 456)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L456
- **Target Call:** `fs.join`
- **Context:** `Output._parse_path`
- **Arguments:** `self.stage.wdir, fs_path`
- **Keywords:** `{}`

```python
            fs_path = fs.join(self.stage.wdir, fs_path)
```

##### 19. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L147) (Line 147)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L147
- **Target Call:** `fs.join`
- **Context:** `DataResolver.__init__`
- **Arguments:** `self.wdir, 'dvc.yaml'`
- **Keywords:** `{}`

```python
        self.relpath = fs.normpath(fs.join(self.wdir, "dvc.yaml"))
```

##### 20. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L290) (Line 290)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L290
- **Target Call:** `fs.join`
- **Context:** `EntryDefinition._resolve_wdir`
- **Arguments:** `self.wdir, wdir`
- **Keywords:** `{}`

```python
        return self.resolver.fs.join(self.wdir, wdir)
```

##### 21. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L388) (Line 388)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L388
- **Target Call:** `fs.join`
- **Context:** `Context.merge_from`
- **Arguments:** `wdir, path`
- **Keywords:** `{}`

```python
        path = fs.normpath(fs.join(wdir, path))
```

##### 22. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L433) (Line 433)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L433
- **Target Call:** `fs.join`
- **Context:** `Context.load_from_vars`
- **Arguments:** `wdir, default`
- **Keywords:** `{}`

```python
            to_import = fs.join(wdir, default)
```

##### 23. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L116) (Line 116)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L116
- **Target Call:** `fs.join`
- **Context:** `Repo._get_repo_dirs`
- **Arguments:** `root_dir, self.DVC_DIR`
- **Keywords:** `{}`

```python
            dvc_dir = fs.join(root_dir, self.DVC_DIR)
```

##### 24. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L206) (Line 206)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L206
- **Target Call:** `fs.join`
- **Context:** `Repo.__init__`
- **Arguments:** `self.tmp_dir, 'lock'`
- **Keywords:** `{}`

```python
                    self.fs.join(self.tmp_dir, "lock"),
```

##### 25. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L420) (Line 420)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L420
- **Target Call:** `fs.join`
- **Context:** `Repo.find_root`
- **Arguments:** `root_dir, cls.DVC_DIR`
- **Keywords:** `{}`

```python
            dvc_dir = fs.join(root_dir, cls.DVC_DIR)
```

##### 26. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L443) (Line 443)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L443
- **Target Call:** `fs.join`
- **Context:** `Repo.find_dvc_dir`
- **Arguments:** `root_dir, cls.DVC_DIR`
- **Keywords:** `{}`

```python
        return fs.join(root_dir, cls.DVC_DIR)
```

##### 27. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L180) (Line 180)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L180
- **Target Call:** `fs.join`
- **Context:** `Artifacts.get_path`
- **Arguments:** `scm_root, *dirparts, PROJECT_FILE`
- **Keywords:** `{}`

```python
        abspath = fs.join(scm_root, *dirparts, PROJECT_FILE)
```

##### 28. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L210) (Line 210)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L210
- **Target Call:** `fs.join`
- **Context:** `Artifacts.download`
- **Arguments:** `root, dirname`
- **Keywords:** `{}`

```python
            _dirname = self.repo.fs.join(root, dirname) if dirname else root
```

##### 29. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L213) (Line 213)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L213
- **Target Call:** `fs.join`
- **Context:** `Artifacts.download`
- **Arguments:** `root, as_posix(path)`
- **Keywords:** `{}`

```python
                path = self.repo.fs.join(root, as_posix(path))
```

##### 30. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L218) (Line 218)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L218
- **Target Call:** `fs.join`
- **Context:** `Artifacts.download`
- **Arguments:** `root, path`
- **Keywords:** `{}`

```python
                path = self.repo.fs.join(root, path)
```

##### 31. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L129) (Line 129)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L129
- **Target Call:** `fs.join`
- **Context:** `_switch_fs`
- **Arguments:** `'/', *repo_root_parts`
- **Keywords:** `{}`

```python
    root_dir = repo.fs.join("/", *repo_root_parts)
```

##### 32. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L135) (Line 135)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L135
- **Target Call:** `fs.join`
- **Context:** `_switch_fs`
- **Arguments:** `root_dir, repo.DVC_DIR`
- **Keywords:** `{}`

```python
    repo.dvc_dir = fs.join(root_dir, repo.DVC_DIR)
```

##### 33. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L139) (Line 139)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L139
- **Target Call:** `fs.join`
- **Context:** `_switch_fs`
- **Arguments:** `'/', *cwd_parts`
- **Keywords:** `{}`

```python
        cwd = repo.fs.join("/", *cwd_parts)
```

##### 34. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L98) (Line 98)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L98
- **Target Call:** `fs.join`
- **Context:** `_check_can_delete`
- **Arguments:** `path, *(entry.key or ())`
- **Keywords:** `{}`

```python
        entry_paths.append(fs.join(path, *(entry.key or ())))
```

##### 35. [dvc/repo/checkout.py](https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L193) (Line 193)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/checkout.py#L193
- **Target Call:** `fs.join`
- **Context:** `checkout`
- **Arguments:** `self.root_dir, *key`
- **Keywords:** `{}`

```python
        out_path = self.fs.join(self.root_dir, *key)
```

##### 36. [dvc/repo/fetch.py](https://github.com/iterative/dvc/blob/main/dvc/repo/fetch.py#L224) (Line 224)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/fetch.py#L224
- **Target Call:** `fs.join`
- **Context:** `_log_unversioned`
- **Arguments:** `remote.path, *key`
- **Keywords:** `{}`

```python
                unversioned.append(fs.unstrip_protocol(fs.join(remote.path, *key)))
```

##### 37. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L91) (Line 91)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L91
- **Target Call:** `fs.join`
- **Context:** `collect_files`
- **Arguments:** `root, file`
- **Keywords:** `{}`

```python
            file_path = fs.join(root, file)
```

##### 38. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L210) (Line 210)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L210
- **Target Call:** `fs.join`
- **Context:** `_load_storage_from_import`
- **Arguments:** `fs_cache.path, dep.fs.protocol, tokenize(dep.fs_path, meta_token)`
- **Keywords:** `{}`

```python
                fs_cache.fs.join(
                    fs_cache.path,
                    dep.fs.protocol,
                    tokenize(dep.fs_path, meta_token),
                ),
```

##### 39. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L856) (Line 856)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L856
- **Target Call:** `fs.join`
- **Context:** `build_data_index`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
        out_path = fs.join(path, *key)
```

##### 40. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L901) (Line 901)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L901
- **Target Call:** `fs.join`
- **Context:** `build_data_index`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
        parent_path = fs.join(path, *key)
```

##### 41. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L30) (Line 30)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L30
- **Target Call:** `fs.join`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `wdir, as_posix(file)`
- **Keywords:** `{}`

```python
            path = repo.fs.join(wdir, as_posix(file))
```

##### 42. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L26) (Line 26)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L26
- **Target Call:** `fs.join`
- **Context:** `_collect_top_level_params`
- **Arguments:** `wdir, as_posix(file)`
- **Keywords:** `{}`

```python
            path = repo.fs.join(wdir, as_posix(file))
```

##### 43. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391
- **Target Call:** `fs.join`
- **Context:** `_relpath`
- **Arguments:** `'/', fs.from_os_path(path)`
- **Keywords:** `{}`

```python
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())
```

##### 44. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L405) (Line 405)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L405
- **Target Call:** `fs.join`
- **Context:** `_collect_output_plots`
- **Arguments:** `wdir_relpath, plot.def_path`
- **Keywords:** `{}`

```python
                _normpath(fs.join(wdir_relpath, plot.def_path)),
```

##### 45. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L433) (Line 433)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L433
- **Target Call:** `fs.join`
- **Context:** `_adjust_sources`
- **Arguments:** `config_dir, filepath`
- **Keywords:** `{}`

```python
            new[_normpath(fs.join(config_dir, filepath))] = val
```

##### 46. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L451) (Line 451)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L451
- **Target Call:** `fs.join`
- **Context:** `_resolve_definitions`
- **Arguments:** `config_dir, plot_id`
- **Keywords:** `{}`

```python
        _normpath(fs.join(config_dir, plot_id)) for plot_id in definitions
```

##### 47. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L457) (Line 457)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L457
- **Target Call:** `fs.join`
- **Context:** `_resolve_definitions`
- **Arguments:** `config_dir, plot_id`
- **Keywords:** `{}`

```python
            data_path = _normpath(fs.join(config_dir, plot_id))
```

##### 48. [dvc/repo/push.py](https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L25) (Line 25)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L25
- **Target Call:** `fs.join`
- **Context:** `_rebuild`
- **Arguments:** `path, *key`
- **Keywords:** `{}`

```python
                meta = Meta.from_info(fs.info(fs.join(path, *key)), fs.protocol)
```

##### 49. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L131) (Line 131)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L131
- **Target Call:** `fs.join`
- **Context:** `_merge_push_meta`
- **Arguments:** `repo.root_dir, *subkey`
- **Keywords:** `{}`

```python
            fs_path = repo.fs.join(repo.root_dir, *subkey)
```

##### 50. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L331) (Line 331)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L331
- **Target Call:** `fs.join`
- **Context:** `_get_update_diff_index`
- **Arguments:** `repo.root_dir, *entry.key`
- **Keywords:** `{}`

```python
                    fs_path = repo.fs.join(repo.root_dir, *entry.key)
```

##### 51. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L46) (Line 46)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L46
- **Target Call:** `fs.join`
- **Context:** `_edit_rwlock`
- **Arguments:** `lock_dir, RWLOCK_FILE`
- **Keywords:** `{}`

```python
    path = fs.join(lock_dir, RWLOCK_FILE)
```

##### 52. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L49) (Line 49)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L49
- **Target Call:** `fs.join`
- **Context:** `_edit_rwlock`
- **Arguments:** `lock_dir, RWLOCK_LOCK`
- **Keywords:** `{}`

```python
        fs.join(lock_dir, RWLOCK_LOCK),
```

##### 53. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L186) (Line 186)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L186
- **Target Call:** `fs.join`
- **Context:** `StageCache.save`
- **Arguments:** `parent, fs.utils.tmp_fname()`
- **Keywords:** `{}`

```python
        tmp = local_fs.join(parent, fs.utils.tmp_fname())
```

##### 54. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L239) (Line 239)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L239
- **Target Call:** `fs.join`
- **Context:** `StageCache.transfer`
- **Arguments:** `from_odb.path, 'runs'`
- **Keywords:** `{}`

```python
        runs = from_fs.join(from_odb.path, "runs")
```

##### 55. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L259) (Line 259)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L259
- **Target Call:** `fs.join`
- **Context:** `StageCache.transfer`
- **Arguments:** `to_odb.path, rel`
- **Keywords:** `{}`

```python
            dst = to_fs.join(to_odb.path, rel)
```

##### 56. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187) (Line 187)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187
- **Target Call:** `fs.join`
- **Context:** `resolve_paths`
- **Arguments:** `fs.dirname(path), wdir`
- **Keywords:** `{}`

```python
    wdir = fs.abspath(fs.join(fs.dirname(path), wdir))
```

</details>

#### <a id="iterative-dvc-fs-relparts"></a>🔹 `fs.relparts` (25 occurrences)

<details open>
<summary><b>Click to expand/collapse 25 occurrences for <code>fs.relparts</code> in iterative/dvc</b></summary>

##### 1. [dvc/api/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L57) (Line 57)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/api/artifacts.py#L57
- **Target Call:** `fs.relparts`
- **Context:** `artifacts_show`
- **Arguments:** `path, _repo.root_dir`
- **Keywords:** `{}`

```python
                parts = _repo.fs.relparts(path, _repo.root_dir)
```

##### 2. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L79) (Line 79)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L79
- **Target Call:** `fs.relparts`
- **Context:** `download`
- **Arguments:** `info, fs_path`
- **Keywords:** `{}`

```python
                localfs.join(to, *fs.relparts(info, fs_path)) for info in from_infos
```

##### 3. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L166) (Line 166)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L166
- **Target Call:** `fs.relparts`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** `self.repo.fs.getcwd(), self.repo.root_dir`
- **Keywords:** `{}`

```python
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
```

##### 4. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L244) (Line 244)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L244
- **Target Call:** `fs.relparts`
- **Context:** `_DVCFileSystem._get_key`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        parts = self.repo.fs.relparts(path, self.repo.root_dir)
```

##### 5. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L262) (Line 262)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L262
- **Target Call:** `fs.relparts`
- **Context:** `_DVCFileSystem._get_key_from_relative`
- **Arguments:** `path, self.root_marker`
- **Keywords:** `{}`

```python
        parts = self.relparts(path, self.root_marker)
```

##### 6. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L556) (Line 556)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L556
- **Target Call:** `fs.relparts`
- **Context:** `_DVCFileSystem._get`
- **Arguments:** `root, rpath`
- **Keywords:** `{}`

```python
            parts = self.relparts(root, rpath)
```

##### 7. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L300) (Line 300)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L300
- **Target Call:** `fs.relparts`
- **Context:** `DvcIgnoreFilter._get_key`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
        parts = self.fs.relparts(path, self.root_dir)
```

##### 8. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L592) (Line 592)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L592
- **Target Call:** `fs.relparts`
- **Context:** `Output.index_key`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python
            key = self.repo.fs.relparts(self.fs_path, self.repo.root_dir)
```

##### 9. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L933) (Line 933)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L933
- **Target Call:** `fs.relparts`
- **Context:** `Output.get_obj`
- **Arguments:** `filter_info, self.fs_path`
- **Keywords:** `{}`

```python
            prefix = fs_path.relparts(filter_info, self.fs_path)
```

##### 10. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L272) (Line 272)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L272
- **Target Call:** `fs.relparts`
- **Context:** `Repo.local_dvc_dir`
- **Arguments:** `self.root_dir, '/'`
- **Keywords:** `{}`

```python
            relparts = self.fs.relparts(self.root_dir, "/")
```

##### 11. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L398) (Line 398)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L398
- **Target Call:** `fs.relparts`
- **Context:** `Repo.get_data_index_entry`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
            key = self.fs.relparts(path, self.root_dir)
```

##### 12. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L65) (Line 65)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L65
- **Target Call:** `fs.relparts`
- **Context:** `brancher`
- **Arguments:** `self.root_dir, self.scm.root_dir`
- **Keywords:** `{}`

```python
        repo_root_parts = self.fs.relparts(self.root_dir, self.scm.root_dir)
```

##### 13. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L69) (Line 69)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L69
- **Target Call:** `fs.relparts`
- **Context:** `brancher`
- **Arguments:** `self.fs.getcwd(), self.scm.root_dir`
- **Keywords:** `{}`

```python
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)
```

##### 14. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L153) (Line 153)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L153
- **Target Call:** `fs.relparts`
- **Context:** `switch`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
        repo_root_parts = repo.fs.relparts(repo.root_dir, repo.scm.root_dir)
```

##### 15. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L157) (Line 157)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L157
- **Target Call:** `fs.relparts`
- **Context:** `switch`
- **Arguments:** `repo.fs.getcwd(), repo.scm.root_dir`
- **Keywords:** `{}`

```python
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)
```

##### 16. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L513) (Line 513)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L513
- **Target Call:** `fs.relparts`
- **Context:** `status`
- **Arguments:** `os.fspath(t)`
- **Keywords:** `{}`

```python
    filter_keys: list[DataIndexKey] = [repo.fs.relparts(os.fspath(t)) for t in targets]
```

##### 17. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L513) (Line 513)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L513
- **Target Call:** `fs.relparts`
- **Context:** `Index.metric_keys`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
            key = self.repo.fs.relparts(path, self.repo.root_dir)
```

##### 18. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L531) (Line 531)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L531
- **Target Call:** `fs.relparts`
- **Context:** `Index.param_keys`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
            key = self.repo.fs.relparts(path, self.repo.root_dir)
```

##### 19. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L789) (Line 789)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L789
- **Target Call:** `fs.relparts`
- **Context:** `IndexView._data_prefixes`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
                key = key + out.fs.relparts(filter_info, out.fs_path)
```

##### 20. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L806) (Line 806)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L806
- **Target Call:** `fs.relparts`
- **Context:** `IndexView.data_keys`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
                key = key + out.fs.relparts(filter_info, out.fs_path)
```

##### 21. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L130) (Line 130)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L130
- **Target Call:** `fs.relparts`
- **Context:** `_ls`
- **Arguments:** `root, fs_path`
- **Keywords:** `{}`

```python
            parts = fs.relparts(root, fs_path)
```

##### 22. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L24) (Line 24)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L24
- **Target Call:** `fs.relparts`
- **Context:** `ls_url`
- **Arguments:** `root, fs_path`
- **Keywords:** `{}`

```python
        parts = fs.relparts(root, fs_path)
```

##### 23. [dvc/repo/open_repo.py](https://github.com/iterative/dvc/blob/main/dvc/repo/open_repo.py#L70) (Line 70)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/open_repo.py#L70
- **Target Call:** `fs.relparts`
- **Context:** `make_repo`
- **Arguments:** `path, root_dir`
- **Keywords:** `{}`

```python
            repo_path = os.path.join(url, *fs.relparts(path, root_dir))
```

##### 24. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L132) (Line 132)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L132
- **Target Call:** `fs.relparts`
- **Context:** `_merge_push_meta`
- **Arguments:** `fs_path, out.fs_path`
- **Keywords:** `{}`

```python
            meta, hash_info = old_tree.get(repo.fs.relparts(fs_path, out.fs_path)) or (
```

##### 25. [dvc/repo/worktree.py](https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L335) (Line 335)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/worktree.py#L335
- **Target Call:** `fs.relparts`
- **Context:** `_get_update_diff_index`
- **Arguments:** `fs_path, out.fs_path`
- **Keywords:** `{}`

```python
                        repo.fs.relparts(fs_path, out.fs_path)
```

</details>

#### <a id="iterative-dvc-fs-relpath"></a>🔹 `fs.relpath` (24 occurrences)

<details open>
<summary><b>Click to expand/collapse 24 occurrences for <code>fs.relpath</code> in iterative/dvc</b></summary>

##### 1. [dvc/commands/dataset.py](https://github.com/iterative/dvc/blob/main/dvc/commands/dataset.py#L66) (Line 66)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/commands/dataset.py#L66
- **Target Call:** `fs.relpath`
- **Context:** `CmdDatasetAdd.run`
- **Arguments:** `existing.manifest_path`
- **Keywords:** `{}`

```python
                path = self.repo.fs.relpath(existing.manifest_path)
```

##### 2. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L206) (Line 206)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L206
- **Target Call:** `fs.relpath`
- **Context:** `_DVCFileSystem.relparts`
- **Arguments:** `path`
- **Keywords:** `{'start': 'start'}`

```python
        return self.parts(self.relpath(path, start=start))
```

##### 3. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L312) (Line 312)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L312
- **Target Call:** `fs.relpath`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `path, self.root_dir`
- **Keywords:** `{}`

```python
            name = self.fs.relpath(path, self.root_dir)
```

##### 4. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L479) (Line 479)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L479
- **Target Call:** `fs.relpath`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, cur_dir`
- **Keywords:** `{}`

```python
            return self.fs.relpath(self.fs_path, cur_dir)
```

##### 5. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L481) (Line 481)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L481
- **Target Call:** `fs.relpath`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        return self.fs.relpath(self.fs_path, self.repo.root_dir)
```

##### 6. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L787) (Line 787)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L787
- **Target Call:** `fs.relpath`
- **Context:** `Output.commit`
- **Arguments:** `filter_info or self.fs_path`
- **Keywords:** `{}`

```python
                rel = self.fs.relpath(filter_info or self.fs_path)
```

##### 7. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L803) (Line 803)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L803
- **Target Call:** `fs.relpath`
- **Context:** `Output._commit_granular_dir`
- **Arguments:** `filter_info, self.fs_path`
- **Keywords:** `{}`

```python
        prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
```

##### 8. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1144) (Line 1144)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L1144
- **Target Call:** `fs.relpath`
- **Context:** `Output._collect_used_dir_cache`
- **Arguments:** `filter_info, self.fs_path`
- **Keywords:** `{}`

```python
            prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
```

##### 9. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1286) (Line 1286)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L1286
- **Target Call:** `fs.relpath`
- **Context:** `Output.unstage`
- **Arguments:** `path, self.fs_path`
- **Keywords:** `{}`

```python
        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))
```

##### 10. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1320) (Line 1320)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L1320
- **Target Call:** `fs.relpath`
- **Context:** `Output.apply`
- **Arguments:** `path, self.fs_path`
- **Keywords:** `{}`

```python
        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))
```

##### 11. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L143) (Line 143)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L143
- **Target Call:** `fs.relpath`
- **Context:** `DataResolver.__init__`
- **Arguments:** `wdir`
- **Keywords:** `{}`

```python
            wdir = fs.relpath(wdir)
```

##### 12. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L102) (Line 102)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L102
- **Target Call:** `fs.relpath`
- **Context:** `Artifacts.read`
- **Arguments:** `dvcfile, self.repo.root_dir`
- **Keywords:** `{}`

```python
            dvcyaml = self.repo.fs.relpath(dvcfile, self.repo.root_dir)
```

##### 13. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L181) (Line 181)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L181
- **Target Call:** `fs.relpath`
- **Context:** `Artifacts.get_path`
- **Arguments:** `abspath, self.repo.root_dir`
- **Keywords:** `{}`

```python
        rela = fs.relpath(abspath, self.repo.root_dir)
```

##### 14. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L214) (Line 214)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L214
- **Target Call:** `fs.relpath`
- **Context:** `Artifacts.download`
- **Arguments:** `path, self.repo.root_dir`
- **Keywords:** `{}`

```python
                path = self.repo.fs.relpath(path, self.repo.root_dir)
```

##### 15. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L371) (Line 371)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L371
- **Target Call:** `fs.relpath`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
    rel = repo.fs.relpath(repo.root_dir, repo.scm.root_dir).rstrip("/")
```

##### 16. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L381) (Line 381)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L381
- **Target Call:** `fs.relpath`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `repo.fs.getcwd(), repo.root_dir`
- **Keywords:** `{}`

```python
    start = repo.fs.relpath(repo.fs.getcwd(), repo.root_dir)
```

##### 17. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L385) (Line 385)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L385
- **Target Call:** `fs.relpath`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** `file, start`
- **Keywords:** `{}`

```python
    return [repo.fs.relpath(file, start) for file in files]
```

##### 18. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L32) (Line 32)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L32
- **Target Call:** `fs.relpath`
- **Context:** `ls_url`
- **Arguments:** `info['name'], fs_path`
- **Keywords:** `{}`

```python
                "path": fs.relpath(info["name"], fs_path),
```

##### 19. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L28) (Line 28)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L28
- **Target Call:** `fs.relpath`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `repo.fs.parent(dvcfile), repo.root_dir`
- **Keywords:** `{}`

```python
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
```

##### 20. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L24) (Line 24)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L24
- **Target Call:** `fs.relpath`
- **Context:** `_collect_top_level_params`
- **Arguments:** `repo.fs.parent(dvcfile), repo.root_dir`
- **Keywords:** `{}`

```python
        wdir = repo.fs.relpath(repo.fs.parent(dvcfile), repo.root_dir)
```

##### 21. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391
- **Target Call:** `fs.relpath`
- **Context:** `_relpath`
- **Arguments:** `fs.join('/', fs.from_os_path(path)), fs.getcwd()`
- **Keywords:** `{}`

```python
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())
```

##### 22. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L255) (Line 255)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L255
- **Target Call:** `fs.relpath`
- **Context:** `StageCache.transfer`
- **Arguments:** `src, from_odb.path`
- **Keywords:** `{}`

```python
            rel = from_fs.relpath(src, from_odb.path)
```

##### 23. [dvc/utils/strictyaml.py](https://github.com/iterative/dvc/blob/main/dvc/utils/strictyaml.py#L47) (Line 47)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/utils/strictyaml.py#L47
- **Target Call:** `fs.relpath`
- **Context:** `make_relpath`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        rel = fs.relpath(fs_path).replace(fs.sep, sep)
```

##### 24. [dvc/utils/studio.py](https://github.com/iterative/dvc/blob/main/dvc/utils/studio.py#L126) (Line 126)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/utils/studio.py#L126
- **Target Call:** `fs.relpath`
- **Context:** `get_subrepo_relpath`
- **Arguments:** `repo.root_dir, scm_root_dir`
- **Keywords:** `{}`

```python
    relpath = as_posix(repo.fs.relpath(repo.root_dir, scm_root_dir))
```

</details>

#### <a id="iterative-dvc-fs-exists"></a>🔹 `fs.exists` (20 occurrences)

<details open>
<summary><b>Click to expand/collapse 20 occurrences for <code>fs.exists</code> in iterative/dvc</b></summary>

##### 1. [dvc/dvcfile.py](https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L108) (Line 108)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L108
- **Target Call:** `fs.exists`
- **Context:** `FileMixin.exists`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        return self.repo.fs.exists(self.path) and not is_ignored
```

##### 2. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L526) (Line 526)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L526
- **Target Call:** `fs.exists`
- **Context:** `_DVCFileSystem._get`
- **Arguments:** `rpath`
- **Keywords:** `{}`

```python
            or not self.exists(rpath)
```

##### 3. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L311) (Line 311)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L311
- **Target Call:** `fs.exists`
- **Context:** `DvcIgnoreFilter._update_trie`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if not matches and self.fs.exists(path):
```

##### 4. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L354) (Line 354)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L354
- **Target Call:** `fs.exists`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
        if not self.fs.exists(dvc_dir):
```

##### 5. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L585) (Line 585)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L585
- **Target Call:** `fs.exists`
- **Context:** `Output.exists`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
        return self.fs.exists(self.fs_path)
```

##### 6. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L356) (Line 356)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L356
- **Target Call:** `fs.exists`
- **Context:** `Context.load_from`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if not fs.exists(path):
```

##### 7. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L434) (Line 434)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L434
- **Target Call:** `fs.exists`
- **Context:** `Context.load_from_vars`
- **Arguments:** `to_import`
- **Keywords:** `{}`

```python
            if fs.exists(to_import):
```

##### 8. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L130) (Line 130)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L130
- **Target Call:** `fs.exists`
- **Context:** `_switch_fs`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python
    if not fs.exists(root_dir):
```

##### 9. [dvc/repo/cache.py](https://github.com/iterative/dvc/blob/main/dvc/repo/cache.py#L24) (Line 24)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/cache.py#L24
- **Target Call:** `fs.exists`
- **Context:** `check_missing`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if not fs.exists(path):
```

##### 10. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L61) (Line 61)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L61
- **Target Call:** `fs.exists`
- **Context:** `_get_missing_paths`
- **Arguments:** `list(paths_map)`
- **Keywords:** `{'batch_size': 'batch_size', 'callback': 'callback'}`

```python
            results = fs.exists(
                list(paths_map), batch_size=batch_size, callback=callback
            )
```

##### 11. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L527) (Line 527)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L527
- **Target Call:** `fs.exists`
- **Context:** `Index.param_keys`
- **Arguments:** `f'{self.repo.fs.root_marker}{default_file}'`
- **Keywords:** `{}`

```python
        if self.repo.fs.exists(f"{self.repo.fs.root_marker}{default_file}"):
```

##### 12. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L861) (Line 861)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L861
- **Target Call:** `fs.exists`
- **Context:** `build_data_index`
- **Arguments:** `out_path`
- **Keywords:** `{}`

```python
        if not fs.exists(out_path):
```

##### 13. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L902) (Line 902)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L902
- **Target Call:** `fs.exists`
- **Context:** `build_data_index`
- **Arguments:** `parent_path`
- **Keywords:** `{}`

```python
        if not fs.exists(parent_path):
```

##### 14. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L68) (Line 68)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L68
- **Target Call:** `fs.exists`
- **Context:** `_collect_params`
- **Arguments:** `f'{fs.root_marker}{default_file}'`
- **Keywords:** `{}`

```python
        if default_file and fs.exists(f"{fs.root_marker}{default_file}"):
```

##### 15. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L524) (Line 524)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L524
- **Target Call:** `fs.exists`
- **Context:** `_collect_definitions`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        if not result or fs.exists(target):
```

##### 16. [dvc/repo/remove.py](https://github.com/iterative/dvc/blob/main/dvc/repo/remove.py#L27) (Line 27)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/remove.py#L27
- **Target Call:** `fs.exists`
- **Context:** `remove`
- **Arguments:** `target + DVC_FILE_SUFFIX`
- **Keywords:** `{}`

```python
        if self.fs.exists(target + DVC_FILE_SUFFIX):
```

##### 17. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L63) (Line 63)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L63
- **Target Call:** `fs.exists`
- **Context:** `_maybe_collect_from_dvc_yaml`
- **Arguments:** `PROJECT_FILE`
- **Keywords:** `{}`

```python
    if loader.fs.exists(PROJECT_FILE):
```

##### 18. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L251) (Line 251)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L251
- **Target Call:** `fs.exists`
- **Context:** `StageCache.transfer`
- **Arguments:** `runs`
- **Keywords:** `{}`

```python
        if not from_fs.exists(runs):
```

##### 19. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L265) (Line 265)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L265
- **Target Call:** `fs.exists`
- **Context:** `StageCache.transfer`
- **Arguments:** `key`
- **Keywords:** `{}`

```python
            if not force and to_fs.exists(key) and first(to_fs.find(key)):
```

##### 20. [dvc/utils/serialize/_common.py](https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/_common.py#L88) (Line 88)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/_common.py#L88
- **Target Call:** `fs.exists`
- **Context:** `_modify_data`
- **Arguments:** `os.fspath(path)`
- **Keywords:** `{}`

```python
    file_exists = fs.exists(os.fspath(path)) if fs else os.path.exists(path)
```

</details>

#### <a id="iterative-dvc-fs-abspath"></a>🔹 `fs.abspath` (17 occurrences)

<details open>
<summary><b>Click to expand/collapse 17 occurrences for <code>fs.abspath</code> in iterative/dvc</b></summary>

##### 1. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L99) (Line 99)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/config.py#L99
- **Target Call:** `fs.abspath`
- **Context:** `Config.__init__`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
            self.dvc_dir = self.fs.abspath(dvc_dir)
```

##### 2. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L203) (Line 203)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L203
- **Target Call:** `fs.abspath`
- **Context:** `_DVCFileSystem.relpath`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return posixpath.relpath(self.abspath(path), start=self.abspath(start))
```

##### 3. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L203) (Line 203)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L203
- **Target Call:** `fs.abspath`
- **Context:** `_DVCFileSystem.relpath`
- **Arguments:** `start`
- **Keywords:** `{}`

```python
        return posixpath.relpath(self.abspath(path), start=self.abspath(start))
```

##### 4. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L377) (Line 377)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L377
- **Target Call:** `fs.abspath`
- **Context:** `DvcIgnoreFilter.__call__`
- **Arguments:** `root`
- **Keywords:** `{}`

```python
        abs_root = self.fs.abspath(root)
```

##### 5. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L510) (Line 510)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L510
- **Target Call:** `fs.abspath`
- **Context:** `DvcIgnoreFilter.is_ignored_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = self.fs.abspath(path)
```

##### 6. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L518) (Line 518)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L518
- **Target Call:** `fs.abspath`
- **Context:** `DvcIgnoreFilter.is_ignored_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = self.fs.abspath(path)
```

##### 7. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L527) (Line 527)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L527
- **Target Call:** `fs.abspath`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        full_target = self.fs.abspath(target)
```

##### 8. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L458) (Line 458)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L458
- **Target Call:** `fs.abspath`
- **Context:** `Output._parse_path`
- **Arguments:** `fs.normpath(fs_path)`
- **Keywords:** `{}`

```python
        return fs.abspath(fs.normpath(fs_path))
```

##### 9. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L414) (Line 414)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L414
- **Target Call:** `fs.abspath`
- **Context:** `Repo.find_root`
- **Arguments:** `root`
- **Keywords:** `{}`

```python
        root_dir = fs.abspath(root)
```

##### 10. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L554) (Line 554)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L554
- **Target Call:** `fs.abspath`
- **Context:** `Repo.find_outs_by_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        abs_path = self.fs.abspath(path)
```

##### 11. [dvc/repo/add.py](https://github.com/iterative/dvc/blob/main/dvc/repo/add.py#L181) (Line 181)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/add.py#L181
- **Target Call:** `fs.abspath`
- **Context:** `_add`
- **Arguments:** `source`
- **Keywords:** `{}`

```python
    path = out.fs.abspath(source) if source else None
```

##### 12. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L96) (Line 96)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L96
- **Target Call:** `fs.abspath`
- **Context:** `_collect_vars`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
                abspath = repo.fs.abspath(file)
```

##### 13. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L223) (Line 223)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L223
- **Target Call:** `fs.abspath`
- **Context:** `StageLoad._get_filepath`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return self.repo.fs.abspath(path)
```

##### 14. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L352) (Line 352)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L352
- **Target Call:** `fs.abspath`
- **Context:** `StageLoad.collect`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
            path = self.fs.abspath(target)
```

##### 15. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L397) (Line 397)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L397
- **Target Call:** `fs.abspath`
- **Context:** `StageLoad.collect_granular`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
                    return [StageInfo(out.stage, self.fs.abspath(target))]
```

##### 16. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L185) (Line 185)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L185
- **Target Call:** `fs.abspath`
- **Context:** `resolve_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    path = fs.abspath(path)
```

##### 17. [dvc/stage/utils.py](https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187) (Line 187)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/utils.py#L187
- **Target Call:** `fs.abspath`
- **Context:** `resolve_paths`
- **Arguments:** `fs.join(fs.dirname(path), wdir)`
- **Keywords:** `{}`

```python
    wdir = fs.abspath(fs.join(fs.dirname(path), wdir))
```

</details>

#### <a id="iterative-dvc-fs-isdir"></a>🔹 `fs.isdir` (16 occurrences)

<details open>
<summary><b>Click to expand/collapse 16 occurrences for <code>fs.isdir</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L62) (Line 62)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L62
- **Target Call:** `fs.isdir`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
                    if fs.isdir(fs_path)
```

##### 2. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L71) (Line 71)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L71
- **Target Call:** `fs.isdir`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        if fs.isdir(fs_path):
```

##### 3. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L335) (Line 335)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L335
- **Target Call:** `fs.isdir`
- **Context:** `_DVCFileSystem._is_dvc_repo`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        return self.repo.fs.isdir(repo_path)
```

##### 4. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L535) (Line 535)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L535
- **Target Call:** `fs.isdir`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `full_target`
- **Keywords:** `{}`

```python
                    dirname, basename, self.fs.isdir(full_target), details=True
```

##### 5. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L548) (Line 548)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L548
- **Target Call:** `fs.isdir`
- **Context:** `DvcIgnoreFilter.is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if fs.isdir(path):
```

##### 6. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L658) (Line 658)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L658
- **Target Call:** `fs.isdir`
- **Context:** `Output.isdir`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
        return self.fs.isdir(self.fs_path)
```

##### 7. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L358) (Line 358)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L358
- **Target Call:** `fs.isdir`
- **Context:** `Context.load_from`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if fs.isdir(path):
```

##### 8. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L416) (Line 416)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L416
- **Target Call:** `fs.isdir`
- **Context:** `Repo.find_root`
- **Arguments:** `root_dir`
- **Keywords:** `{}`

```python
        if not fs.isdir(root_dir):
```

##### 9. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L421) (Line 421)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L421
- **Target Call:** `fs.isdir`
- **Context:** `Repo.find_root`
- **Arguments:** `dvc_dir`
- **Keywords:** `{}`

```python
            if fs.isdir(dvc_dir):
```

##### 10. [dvc/repo/collect.py](https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L38) (Line 38)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L38
- **Target Call:** `fs.isdir`
- **Context:** `_collect_paths`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        if recursive and fs.isdir(fs_path):
```

##### 11. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L35) (Line 35)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L35
- **Target Call:** `fs.isdir`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if summarize or not fs.isdir(path):
```

##### 12. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L123) (Line 123)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L123
- **Target Call:** `fs.isdir`
- **Context:** `try_expand_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            if fs.isdir(path):
```

##### 13. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L533) (Line 533)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L533
- **Target Call:** `fs.isdir`
- **Context:** `unpack_if_dir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    if fs.isdir(path):
```

##### 14. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L90) (Line 90)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L90
- **Target Call:** `fs.isdir`
- **Context:** `_collect_specific_target`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        if not (recursive and loader.fs.isdir(target)):
```

##### 15. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L349) (Line 349)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L349
- **Target Call:** `fs.isdir`
- **Context:** `StageLoad.collect`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
        if recursive and self.fs.isdir(target):
```

##### 16. [dvc/repo/stage.py](https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L394) (Line 394)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/stage.py#L394
- **Target Call:** `fs.isdir`
- **Context:** `StageLoad.collect_granular`
- **Arguments:** `target`
- **Keywords:** `{}`

```python
            if not (recursive and self.fs.isdir(target)):
```

</details>

#### <a id="iterative-dvc-fs-getcwd"></a>🔹 `fs.getcwd` (14 occurrences)

<details open>
<summary><b>Click to expand/collapse 14 occurrences for <code>fs.getcwd</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/data.py](https://github.com/iterative/dvc/blob/main/dvc/fs/data.py#L31) (Line 31)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/data.py#L31
- **Target Call:** `fs.getcwd`
- **Context:** `DataFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return self.fs.getcwd()
```

##### 2. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L165) (Line 165)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L165
- **Target Call:** `fs.getcwd`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
```

##### 3. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L166) (Line 166)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L166
- **Target Call:** `fs.getcwd`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            relparts = self.repo.fs.relparts(self.repo.fs.getcwd(), self.repo.root_dir)
```

##### 4. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L197) (Line 197)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L197
- **Target Call:** `fs.getcwd`
- **Context:** `_DVCFileSystem.abspath`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            path = self.join(self.getcwd(), path)
```

##### 5. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L688) (Line 688)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L688
- **Target Call:** `fs.getcwd`
- **Context:** `DVCFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return self.fs.getcwd()
```

##### 6. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L48) (Line 48)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L48
- **Target Call:** `fs.getcwd`
- **Context:** `GitFileSystem.getcwd`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return self.fs.getcwd()
```

##### 7. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L477) (Line 477)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L477
- **Target Call:** `fs.getcwd`
- **Context:** `Output.__str__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        cur_dir = self.fs.getcwd()
```

##### 8. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L68) (Line 68)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L68
- **Target Call:** `fs.getcwd`
- **Context:** `brancher`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
```

##### 9. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L69) (Line 69)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L69
- **Target Call:** `fs.getcwd`
- **Context:** `brancher`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        cwd_parts = self.fs.relparts(self.fs.getcwd(), self.scm.root_dir)
```

##### 10. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L156) (Line 156)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L156
- **Target Call:** `fs.getcwd`
- **Context:** `switch`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
```

##### 11. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L157) (Line 157)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L157
- **Target Call:** `fs.getcwd`
- **Context:** `switch`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        cwd_parts = repo.fs.relparts(repo.fs.getcwd(), repo.scm.root_dir)
```

##### 12. [dvc/repo/data.py](https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L381) (Line 381)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/data.py#L381
- **Target Call:** `fs.getcwd`
- **Context:** `_transform_git_paths_to_dvc`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    start = repo.fs.relpath(repo.fs.getcwd(), repo.root_dir)
```

##### 13. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L138) (Line 138)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L138
- **Target Call:** `fs.getcwd`
- **Context:** `to_relpath`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    cwd = fs.getcwd()
```

##### 14. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391) (Line 391)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L391
- **Target Call:** `fs.getcwd`
- **Context:** `_relpath`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    return fs.relpath(fs.join("/", fs.from_os_path(path)), fs.getcwd())
```

</details>

#### <a id="iterative-dvc-fs-parts"></a>🔹 `fs.parts` (13 occurrences)

<details open>
<summary><b>Click to expand/collapse 13 occurrences for <code>fs.parts</code> in iterative/dvc</b></summary>

##### 1. [dvc/commands/dag.py](https://github.com/iterative/dvc/blob/main/dvc/commands/dag.py#L89) (Line 89)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/commands/dag.py#L89
- **Target Call:** `fs.parts`
- **Context:** `_collect_targets`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        for out in outs_trie.itervalues(prefix=repo.fs.parts(path)):
```

##### 2. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L206) (Line 206)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L206
- **Target Call:** `fs.parts`
- **Context:** `_DVCFileSystem.relparts`
- **Arguments:** `self.relpath(path, start=start)`
- **Keywords:** `{}`

```python
        return self.parts(self.relpath(path, start=start))
```

##### 3. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L596) (Line 596)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L596
- **Target Call:** `fs.parts`
- **Context:** `Output.index_key`
- **Arguments:** `no_drive`
- **Keywords:** `{}`

```python
            key = self.fs.parts(no_drive)[1:]
```

##### 4. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L803) (Line 803)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L803
- **Target Call:** `fs.parts`
- **Context:** `Output._commit_granular_dir`
- **Arguments:** `self.fs.relpath(filter_info, self.fs_path)`
- **Keywords:** `{}`

```python
        prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
```

##### 5. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1144) (Line 1144)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L1144
- **Target Call:** `fs.parts`
- **Context:** `Output._collect_used_dir_cache`
- **Arguments:** `self.fs.relpath(filter_info, self.fs_path)`
- **Keywords:** `{}`

```python
            prefix = self.fs.parts(self.fs.relpath(filter_info, self.fs_path))
```

##### 6. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1286) (Line 1286)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L1286
- **Target Call:** `fs.parts`
- **Context:** `Output.unstage`
- **Arguments:** `self.fs.relpath(path, self.fs_path)`
- **Keywords:** `{}`

```python
        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))
```

##### 7. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1320) (Line 1320)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L1320
- **Target Call:** `fs.parts`
- **Context:** `Output.apply`
- **Arguments:** `self.fs.relpath(path, self.fs_path)`
- **Keywords:** `{}`

```python
        rel_key = tuple(self.fs.parts(self.fs.relpath(path, self.fs_path)))
```

##### 8. [dvc/repo/graph.py](https://github.com/iterative/dvc/blob/main/dvc/repo/graph.py#L146) (Line 146)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/graph.py#L146
- **Target Call:** `fs.parts`
- **Context:** `build_graph`
- **Arguments:** `dep.fs_path`
- **Keywords:** `{}`

```python
            dep_key = dep.fs.parts(dep.fs_path)
```

##### 9. [dvc/repo/graph.py](https://github.com/iterative/dvc/blob/main/dvc/repo/graph.py#L176) (Line 176)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/graph.py#L176
- **Target Call:** `fs.parts`
- **Context:** `build_outs_graph`
- **Arguments:** `dep.fs_path`
- **Keywords:** `{}`

```python
            dep_key = dep.fs.parts(dep.fs_path)
```

##### 10. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L550) (Line 550)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L550
- **Target Call:** `fs.parts`
- **Context:** `Index.plot_keys`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            key = self.repo.fs.parts(path)
```

##### 11. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L165) (Line 165)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L165
- **Target Call:** `fs.parts`
- **Context:** `_gather_metrics`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        repo_os_path = os.sep.join(fs.parts(repo_path))
```

##### 12. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L141) (Line 141)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L141
- **Target Call:** `fs.parts`
- **Context:** `_gather_params`
- **Arguments:** `repo_path`
- **Keywords:** `{}`

```python
        repo_os_path = os.sep.join(fs.parts(repo_path))
```

##### 13. [dvc/repo/trie.py](https://github.com/iterative/dvc/blob/main/dvc/repo/trie.py#L12) (Line 12)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/trie.py#L12
- **Target Call:** `fs.parts`
- **Context:** `build_outs_trie`
- **Arguments:** `out.fs_path`
- **Keywords:** `{}`

```python
            out_key = out.fs.parts(out.fs_path)
```

</details>

#### <a id="iterative-dvc-fs-normpath"></a>🔹 `fs.normpath` (13 occurrences)

<details open>
<summary><b>Click to expand/collapse 13 occurrences for <code>fs.normpath</code> in iterative/dvc</b></summary>

##### 1. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L40) (Line 40)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L40
- **Target Call:** `fs.normpath`
- **Context:** `RepoDependency.__init__`
- **Arguments:** `self.def_path`
- **Keywords:** `{}`

```python
        self.fs_path = as_posix(self.fs.normpath(self.def_path))
```

##### 2. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L61) (Line 61)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L61
- **Target Call:** `fs.normpath`
- **Context:** `download`
- **Arguments:** `glob.escape(fs_path)`
- **Keywords:** `{}`

```python
                    f"{fs.normpath(glob.escape(fs_path))}/**"
```

##### 3. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L198) (Line 198)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L198
- **Target Call:** `fs.normpath`
- **Context:** `_DVCFileSystem.abspath`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return self.normpath(path)
```

##### 4. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L116) (Line 116)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L116
- **Target Call:** `fs.normpath`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `fs.dirname(path)`
- **Keywords:** `{}`

```python
        dirname = fs.normpath(fs.dirname(path))
```

##### 5. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L502) (Line 502)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L502
- **Target Call:** `fs.normpath`
- **Context:** `DvcIgnoreFilter._is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        dirname, basename = self.fs.split(self.fs.normpath(path))
```

##### 6. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L531) (Line 531)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L531
- **Target Call:** `fs.normpath`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `full_target`
- **Keywords:** `{}`

```python
            dirname, basename = self.fs.split(self.fs.normpath(full_target))
```

##### 7. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L458) (Line 458)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L458
- **Target Call:** `fs.normpath`
- **Context:** `Output._parse_path`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        return fs.abspath(fs.normpath(fs_path))
```

##### 8. [dvc/parsing/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L147) (Line 147)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/__init__.py#L147
- **Target Call:** `fs.normpath`
- **Context:** `DataResolver.__init__`
- **Arguments:** `fs.join(self.wdir, 'dvc.yaml')`
- **Keywords:** `{}`

```python
        self.relpath = fs.normpath(fs.join(self.wdir, "dvc.yaml"))
```

##### 9. [dvc/parsing/context.py](https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L388) (Line 388)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/parsing/context.py#L388
- **Target Call:** `fs.normpath`
- **Context:** `Context.merge_from`
- **Arguments:** `fs.join(wdir, path)`
- **Keywords:** `{}`

```python
        path = fs.normpath(fs.join(wdir, path))
```

##### 10. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L574) (Line 574)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L574
- **Target Call:** `fs.normpath`
- **Context:** `Repo.is_dvc_internal`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path_parts = self.fs.normpath(path).split(self.fs.sep)
```

##### 11. [dvc/repo/artifacts.py](https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L219) (Line 219)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/artifacts.py#L219
- **Target Call:** `fs.normpath`
- **Context:** `Artifacts.download`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                path = self.repo.fs.normpath(path)
```

##### 12. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L31) (Line 31)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L31
- **Target Call:** `fs.normpath`
- **Context:** `_collect_top_level_metrics`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            yield repo.fs.normpath(path)
```

##### 13. [dvc/repo/params/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L27) (Line 27)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/params/show.py#L27
- **Target Call:** `fs.normpath`
- **Context:** `_collect_top_level_params`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            yield repo.fs.normpath(path)
```

</details>

#### <a id="iterative-dvc-fs-info"></a>🔹 `fs.info` (12 occurrences)

<details open>
<summary><b>Click to expand/collapse 12 occurrences for <code>fs.info</code> in iterative/dvc</b></summary>

##### 1. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L106) (Line 106)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L106
- **Target Call:** `fs.info`
- **Context:** `RepoDependency.download`
- **Arguments:** `src_path`
- **Keywords:** `{}`

```python
                info = maybe_info or self.fs.info(src_path)
```

##### 2. [dvc/dependency/repo.py](https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L108) (Line 108)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/dependency/repo.py#L108
- **Target Call:** `fs.info`
- **Context:** `RepoDependency.download`
- **Arguments:** `dest_path`
- **Keywords:** `{}`

```python
                dest_info = to.fs.info(dest_path)
```

##### 3. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L374) (Line 374)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L374
- **Target Call:** `fs.info`
- **Context:** `_DVCFileSystem.isdvc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            return self.info(path).get("dvc_info", {}).get("isout", False)
```

##### 4. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L401) (Line 401)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L401
- **Target Call:** `fs.info`
- **Context:** `_DVCFileSystem.ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
                fs_info = fs.info(fs_path)
```

##### 5. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L465) (Line 465)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L465
- **Target Call:** `fs.info`
- **Context:** `_DVCFileSystem._info`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            fs_info = fs.info(fs_path)
```

##### 6. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L479) (Line 479)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L479
- **Target Call:** `fs.info`
- **Context:** `_DVCFileSystem._info`
- **Arguments:** `parent`
- **Keywords:** `{}`

```python
                    if fs.info(parent)["type"] != "directory":
```

##### 7. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L630) (Line 630)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L630
- **Target Call:** `fs.info`
- **Context:** `_DVCFileSystem.du`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        todo = deque([self.info(path)])
```

##### 8. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L114) (Line 114)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L114
- **Target Call:** `fs.info`
- **Context:** `_ls`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    fs_path = fs.info(path)["name"]
```

##### 9. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L121) (Line 121)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L121
- **Target Call:** `fs.info`
- **Context:** `_ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        infos[os.path.basename(path) or os.curdir] = fs.info(fs_path)
```

##### 10. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L151) (Line 151)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L151
- **Target Call:** `fs.info`
- **Context:** `_ls_tree`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    info = _info or fs.info(path)
```

##### 11. [dvc/repo/ls_url.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L10) (Line 10)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls_url.py#L10
- **Target Call:** `fs.info`
- **Context:** `ls_url`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
        info = fs.info(fs_path)
```

##### 12. [dvc/repo/push.py](https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L25) (Line 25)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/push.py#L25
- **Target Call:** `fs.info`
- **Context:** `_rebuild`
- **Arguments:** `fs.join(path, *key)`
- **Keywords:** `{}`

```python
                meta = Meta.from_info(fs.info(fs.join(path, *key)), fs.protocol)
```

</details>

#### <a id="iterative-dvc-fs-open"></a>🔹 `fs.open` (11 occurrences)

<details open>
<summary><b>Click to expand/collapse 11 occurrences for <code>fs.open</code> in iterative/dvc</b></summary>

##### 1. [dvc/api/data.py](https://github.com/iterative/dvc/blob/main/dvc/api/data.py#L297) (Line 297)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/api/data.py#L297
- **Target Call:** `fs.open`
- **Context:** `_open`
- **Arguments:** `fs_path`
- **Keywords:** `{'mode': 'mode', 'encoding': 'encoding'}`

```python
                with fs.open(fs_path, mode=mode, encoding=encoding) as fobj:
```

##### 2. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L211) (Line 211)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/config.py#L211
- **Target Call:** `fs.open`
- **Context:** `Config.load_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        with fs.open(path) as fobj:
```

##### 3. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L241) (Line 241)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/config.py#L241
- **Target Call:** `fs.open`
- **Context:** `Config._save_config`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{}`

```python
        with fs.open(filename, "wb") as fobj:
```

##### 4. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L362) (Line 362)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L362
- **Target Call:** `fs.open`
- **Context:** `_DVCFileSystem._open`
- **Arguments:** `fs_path`
- **Keywords:** `{'mode': 'mode'}`

```python
            return self.repo.fs.open(fs_path, mode=mode)
```

##### 5. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L117) (Line 117)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L117
- **Target Call:** `fs.open`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** `path`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with fs.open(path, encoding="utf-8") as fobj:
```

##### 6. [dvc/repo/experiments/cache.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/cache.py#L53) (Line 53)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/cache.py#L53
- **Target Call:** `fs.open`
- **Context:** `ExpCache.get`
- **Arguments:** `obj.path, 'rb'`
- **Keywords:** `{}`

```python
            with obj.fs.open(obj.path, "rb") as fobj:
```

##### 7. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L552) (Line 552)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L552
- **Target Call:** `fs.open`
- **Context:** `parse`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'rb'"}`

```python
        with fs.open(path, mode="rb", **fs_kwargs) as fd:
```

##### 8. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L559) (Line 559)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L559
- **Target Call:** `fs.open`
- **Context:** `parse`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'r'", 'encoding': "'utf8'"}`

```python
        with fs.open(path, mode="r", encoding="utf8", **fs_kwargs) as fd:
```

##### 9. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L55) (Line 55)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L55
- **Target Call:** `fs.open`
- **Context:** `_edit_rwlock`
- **Arguments:** `path`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
            with fs.open(path, encoding="utf-8") as fobj:
```

##### 10. [dvc/rwlock.py](https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L66) (Line 66)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/rwlock.py#L66
- **Target Call:** `fs.open`
- **Context:** `_edit_rwlock`
- **Arguments:** `path, 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with fs.open(path, "w", encoding="utf-8") as fobj:
```

##### 11. [dvc/scm.py](https://github.com/iterative/dvc/blob/main/dvc/scm.py#L281) (Line 281)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/scm.py#L281
- **Target Call:** `fs.open`
- **Context:** `lfs_prefetch`
- **Arguments:** `'.gitattributes'`
- **Keywords:** `{}`

```python
        if "filter=lfs" not in git_fs.open(".gitattributes").read():
```

</details>

#### <a id="iterative-dvc-fs-isin"></a>🔹 `fs.isin` (11 occurrences)

<details open>
<summary><b>Click to expand/collapse 11 occurrences for <code>fs.isin</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L165) (Line 165)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L165
- **Target Call:** `fs.isin`
- **Context:** `_DVCFileSystem.getcwd`
- **Arguments:** `self.repo.fs.getcwd(), self.repo.root_dir`
- **Keywords:** `{}`

```python
        if self.repo.fs.isin(self.repo.fs.getcwd(), self.repo.root_dir):
```

##### 2. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L474) (Line 474)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L474
- **Target Call:** `fs.isin`
- **Context:** `Output.__str__`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        if not self.fs.isin(self.fs_path, self.repo.root_dir):
```

##### 3. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L478) (Line 478)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L478
- **Target Call:** `fs.isin`
- **Context:** `Output.__str__`
- **Arguments:** `cur_dir, self.repo.root_dir`
- **Keywords:** `{}`

```python
        if self.fs.isin(cur_dir, self.repo.root_dir):
```

##### 4. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L501) (Line 501)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L501
- **Target Call:** `fs.isin`
- **Context:** `Output.is_in_repo`
- **Arguments:** `self.fs_path, self.repo.root_dir`
- **Keywords:** `{}`

```python
        return self.repo and self.fs.isin(self.fs_path, self.repo.root_dir)
```

##### 5. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L565) (Line 565)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L565
- **Target Call:** `fs.isin`
- **Context:** `Repo.func`
- **Arguments:** `out.fs_path, fs_path`
- **Keywords:** `{}`

```python
            return recursive and out.fs.isin(out.fs_path, fs_path)
```

##### 6. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L64) (Line 64)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L64
- **Target Call:** `fs.isin`
- **Context:** `brancher`
- **Arguments:** `self.root_dir, self.scm.root_dir`
- **Keywords:** `{}`

```python
    if self.fs.isin(self.root_dir, self.scm.root_dir):
```

##### 7. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L68) (Line 68)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L68
- **Target Call:** `fs.isin`
- **Context:** `brancher`
- **Arguments:** `self.fs.getcwd(), self.scm.root_dir`
- **Keywords:** `{}`

```python
    if self.fs.isin(self.fs.getcwd(), self.scm.root_dir):
```

##### 8. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L152) (Line 152)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L152
- **Target Call:** `fs.isin`
- **Context:** `switch`
- **Arguments:** `repo.root_dir, repo.scm.root_dir`
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.root_dir, repo.scm.root_dir):
```

##### 9. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L156) (Line 156)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L156
- **Target Call:** `fs.isin`
- **Context:** `switch`
- **Arguments:** `repo.fs.getcwd(), repo.scm.root_dir`
- **Keywords:** `{}`

```python
    if repo.fs.isin(repo.fs.getcwd(), repo.scm.root_dir):
```

##### 10. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L788) (Line 788)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L788
- **Target Call:** `fs.isin`
- **Context:** `IndexView._data_prefixes`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            if filter_info and out.fs.isin(filter_info, out.fs_path):
```

##### 11. [dvc/repo/index.py](https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L805) (Line 805)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/index.py#L805
- **Target Call:** `fs.isin`
- **Context:** `IndexView.data_keys`
- **Arguments:** `filter_info, out.fs_path`
- **Keywords:** `{}`

```python
            if filter_info and out.fs.isin(filter_info, out.fs_path):
```

</details>

#### <a id="iterative-dvc-fs-find"></a>🔹 `fs.find` (7 occurrences)

<details open>
<summary><b>Click to expand/collapse 7 occurrences for <code>fs.find</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L73) (Line 73)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/__init__.py#L73
- **Target Call:** `fs.find`
- **Context:** `download`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
                path for path in fs.find(fs_path) if not path.endswith(fs.flavour.sep)
```

##### 2. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L460) (Line 460)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L460
- **Target Call:** `fs.find`
- **Context:** `DvcIgnoreFilter.find`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            yield from fs.find(path)
```

##### 3. [dvc/repo/collect.py](https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L39) (Line 39)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/collect.py#L39
- **Target Call:** `fs.find`
- **Context:** `_collect_paths`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
            target_paths.extend(fs.find(fs_path))
```

##### 4. [dvc/repo/metrics/show.py](https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L124) (Line 124)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/metrics/show.py#L124
- **Target Call:** `fs.find`
- **Context:** `try_expand_paths`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                yield from fs.find(path)
```

##### 5. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L63) (Line 63)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L63
- **Target Call:** `fs.find`
- **Context:** `_unpack_dir_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    ret = list(fs.find(path))
```

##### 6. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L254) (Line 254)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L254
- **Target Call:** `fs.find`
- **Context:** `StageCache.transfer`
- **Arguments:** `runs`
- **Keywords:** `{}`

```python
        for src in from_fs.find(runs):
```

##### 7. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L265) (Line 265)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L265
- **Target Call:** `fs.find`
- **Context:** `StageCache.transfer`
- **Arguments:** `key`
- **Keywords:** `{}`

```python
            if not force and to_fs.exists(key) and first(to_fs.find(key)):
```

</details>

#### <a id="iterative-dvc-fs-ls"></a>🔹 `fs.ls` (6 occurrences)

<details open>
<summary><b>Click to expand/collapse 6 occurrences for <code>fs.ls</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L656) (Line 656)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L656
- **Target Call:** `fs.ls`
- **Context:** `_DVCFileSystem.du`
- **Arguments:** `info['name']`
- **Keywords:** `{'detail': 'True'}`

```python
            todo.extend(self.ls(info["name"], detail=True))
```

##### 2. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L58) (Line 58)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L58
- **Target Call:** `fs.ls`
- **Context:** `GitFileSystem.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'detail'}`

```python
        return self.fs.ls(path, detail=detail, **kwargs) or []
```

##### 3. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L407) (Line 407)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L407
- **Target Call:** `fs.ls`
- **Context:** `DvcIgnoreFilter.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'True'}`

```python
        for entry in fs.ls(path, detail=True, **kwargs):
```

##### 4. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L39) (Line 39)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L39
- **Target Call:** `fs.ls`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            (entry_path, fs.du(entry_path, total=True)) for entry_path in fs.ls(path)
```

##### 5. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L168) (Line 168)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L168
- **Target Call:** `fs.ls`
- **Context:** `_ls_tree`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'True'}`

```python
            infos = fs.ls(path, detail=True, **fs_kwargs)
```

##### 6. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L66) (Line 66)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L66
- **Target Call:** `fs.ls`
- **Context:** `_unpack_dir_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        next(iter(fs.ls(path)), None)
```

</details>

#### <a id="iterative-dvc-fs-isfile"></a>🔹 `fs.isfile` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>fs.isfile</code> in iterative/dvc</b></summary>

##### 1. [dvc/dvcfile.py](https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L136) (Line 136)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/dvcfile.py#L136
- **Target Call:** `fs.isfile`
- **Context:** `FileMixin._load`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        if not self.repo.fs.isfile(self.path):
```

##### 2. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L542) (Line 542)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L542
- **Target Call:** `fs.isfile`
- **Context:** `_DVCFileSystem._get`
- **Arguments:** `rpath`
- **Keywords:** `{}`

```python
        if self.isfile(rpath):
```

##### 3. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L546) (Line 546)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L546
- **Target Call:** `fs.isfile`
- **Context:** `DvcIgnoreFilter.is_ignored`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if fs.isfile(path):
```

##### 4. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L663) (Line 663)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L663
- **Target Call:** `fs.isfile`
- **Context:** `Output.isfile`
- **Arguments:** `self.fs_path`
- **Keywords:** `{}`

```python
        return self.fs.isfile(self.fs_path)
```

##### 5. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L120) (Line 120)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L120
- **Target Call:** `fs.isfile`
- **Context:** `_ls`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
    if maxdepth == 0 or fs.isfile(fs_path):
```

</details>

#### <a id="iterative-dvc-fs-walk"></a>🔹 `fs.walk` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>fs.walk</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L552) (Line 552)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L552
- **Target Call:** `fs.walk`
- **Context:** `_DVCFileSystem._get`
- **Arguments:** `rpath`
- **Keywords:** `{'maxdepth': 'maxdepth', 'detail': 'True'}`

```python
        for root, dirs, files in self.walk(rpath, maxdepth=maxdepth, detail=True):
```

##### 2. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L340) (Line 340)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L340
- **Target Call:** `fs.walk`
- **Context:** `DvcIgnoreFilter._update`
- **Arguments:** `dirname`
- **Keywords:** `{}`

```python
                    _, dnames, _ = next(self.fs.walk(dirname))
```

##### 3. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L433) (Line 433)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L433
- **Target Call:** `fs.walk`
- **Context:** `DvcIgnoreFilter.walk`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            for root, dirs, files in fs.walk(path, **kwargs):
```

##### 4. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L451) (Line 451)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L451
- **Target Call:** `fs.walk`
- **Context:** `DvcIgnoreFilter.walk`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            yield from fs.walk(path, **kwargs)
```

##### 5. [dvc/repo/ls.py](https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L123) (Line 123)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/ls.py#L123
- **Target Call:** `fs.walk`
- **Context:** `_ls`
- **Arguments:** `fs_path`
- **Keywords:** `{'dvcfiles': 'True', 'dvc_only': 'dvc_only', 'detail': 'True', 'maxdepth': 'maxdepth'}`

```python
        for root, dirs, files in fs.walk(
            fs_path,
            dvcfiles=True,
            dvc_only=dvc_only,
            detail=True,
            maxdepth=maxdepth,
        ):
```

</details>

#### <a id="iterative-dvc-fs-makedirs"></a>🔹 `fs.makedirs` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fs.makedirs</code> in iterative/dvc</b></summary>

##### 1. [dvc/config.py](https://github.com/iterative/dvc/blob/main/dvc/config.py#L238) (Line 238)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/config.py#L238
- **Target Call:** `fs.makedirs`
- **Context:** `Config._save_config`
- **Arguments:** `os.path.dirname(filename)`
- **Keywords:** `{}`

```python
        fs.makedirs(os.path.dirname(filename))
```

##### 2. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L203) (Line 203)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L203
- **Target Call:** `fs.makedirs`
- **Context:** `Repo.__init__`
- **Arguments:** `self.tmp_dir`
- **Keywords:** `{'exist_ok': 'True'}`

```python
                self.fs.makedirs(self.tmp_dir, exist_ok=True)
```

##### 3. [dvc/repo/experiments/executor/base.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/executor/base.py#L362) (Line 362)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/executor/base.py#L362
- **Target Call:** `fs.makedirs`
- **Context:** `BaseExecutor.pack_repro_args`
- **Arguments:** `dpath`
- **Keywords:** `{}`

```python
            fs.makedirs(dpath)
```

##### 4. [dvc/repo/experiments/utils.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/utils.py#L44) (Line 44)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/utils.py#L44
- **Target Call:** `fs.makedirs`
- **Context:** `get_exp_rwlock`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
    repo.fs.makedirs(path, exist_ok=True)
```

</details>

#### <a id="iterative-dvc-fs-get-file"></a>🔹 `fs.get_file` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.get_file</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L544) (Line 544)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L544
- **Target Call:** `fs.get_file`
- **Context:** `_DVCFileSystem._get`
- **Arguments:** `rpath, lpath`
- **Keywords:** `{'callback': 'child'}`

```python
                self.get_file(rpath, lpath, callback=child, **kwargs)
```

##### 2. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L591) (Line 591)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L591
- **Target Call:** `fs.get_file`
- **Context:** `_DVCFileSystem.get_file`
- **Arguments:** `src, dest`
- **Keywords:** `{'callback': 'child'}`

```python
                fs.get_file(src, dest, callback=child, **kw)
```

##### 3. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L615) (Line 615)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L615
- **Target Call:** `fs.get_file`
- **Context:** `_DVCFileSystem.get_file`
- **Arguments:** `fs_path, lpath`
- **Keywords:** `{}`

```python
            return self.repo.fs.get_file(fs_path, lpath, **kwargs)
```

</details>

#### <a id="iterative-dvc-fs-split"></a>🔹 `fs.split` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.split</code> in iterative/dvc</b></summary>

##### 1. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L357) (Line 357)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L357
- **Target Call:** `fs.split`
- **Context:** `DvcIgnoreFilter._update_sub_repo`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        root, dname = self.fs.split(path)
```

##### 2. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L502) (Line 502)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L502
- **Target Call:** `fs.split`
- **Context:** `DvcIgnoreFilter._is_ignored`
- **Arguments:** `self.fs.normpath(path)`
- **Keywords:** `{}`

```python
        dirname, basename = self.fs.split(self.fs.normpath(path))
```

##### 3. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L531) (Line 531)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L531
- **Target Call:** `fs.split`
- **Context:** `DvcIgnoreFilter.check_ignore`
- **Arguments:** `self.fs.normpath(full_target)`
- **Keywords:** `{}`

```python
            dirname, basename = self.fs.split(self.fs.normpath(full_target))
```

</details>

#### <a id="iterative-dvc-f-read"></a>🔹 `f.read` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>f.read</code> in iterative/dvc</b></summary>

##### 1. [dvc/repo/experiments/cache.py](https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/cache.py#L54) (Line 54)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/experiments/cache.py#L54
- **Target Call:** `f.read`
- **Context:** `ExpCache.get`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                data = fobj.read()
```

##### 2. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L553) (Line 553)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L553
- **Target Call:** `f.read`
- **Context:** `parse`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            return fd.read()
```

##### 3. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L560) (Line 560)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L560
- **Target Call:** `f.read`
- **Context:** `parse`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            contents = fd.read()
```

</details>

#### <a id="iterative-dvc-fs-chdir"></a>🔹 `fs.chdir` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.chdir</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/git.py](https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L51) (Line 51)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/git.py#L51
- **Target Call:** `fs.chdir`
- **Context:** `GitFileSystem.chdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs.chdir(path)
```

##### 2. [dvc/repo/brancher.py](https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L140) (Line 140)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/brancher.py#L140
- **Target Call:** `fs.chdir`
- **Context:** `_switch_fs`
- **Arguments:** `cwd`
- **Keywords:** `{}`

```python
        repo.fs.chdir(cwd)
```

</details>

#### <a id="iterative-dvc-f-write"></a>🔹 `f.write` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>f.write</code> in iterative/dvc</b></summary>

##### 1. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L561) (Line 561)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L561
- **Target Call:** `f.write`
- **Context:** `init`
- **Arguments:** `'# Add patterns of files dvc should ignore, which could improve\n# the performance. Learn more at\n# https://dvc.org/doc/user-guide/dvcignore\n'`
- **Keywords:** `{}`

```python
        fobj.write(
            "# Add patterns of files dvc should ignore, which could improve\n"
            "# the performance. Learn more at\n"
            "# https://dvc.org/doc/user-guide/dvcignore\n"
        )
```

##### 2. [dvc/utils/serialize/_py.py](https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/_py.py#L74) (Line 74)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/_py.py#L74
- **Target Call:** `f.write`
- **Context:** `_dump`
- **Arguments:** `new_text`
- **Keywords:** `{}`

```python
    stream.write(new_text)
```

</details>

#### <a id="iterative-dvc-fs-as-posix"></a>🔹 `fs.as_posix` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.as_posix</code> in iterative/dvc</b></summary>

##### 1. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L844) (Line 844)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L844
- **Target Call:** `fs.as_posix`
- **Context:** `Output.dumpd`
- **Arguments:** `relpath(self.fs_path, self.stage.wdir)`
- **Keywords:** `{}`

```python
            path = self.fs.as_posix(relpath(self.fs_path, self.stage.wdir))
```

##### 2. [dvc/stage/cache.py](https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L257) (Line 257)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/stage/cache.py#L257
- **Target Call:** `fs.as_posix`
- **Context:** `StageCache.transfer`
- **Arguments:** `rel`
- **Keywords:** `{}`

```python
                rel = from_fs.as_posix(rel)
```

</details>

#### <a id="iterative-dvc-f-close"></a>🔹 `f.close` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>f.close</code> in iterative/dvc</b></summary>

##### 1. [dvc/repo/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L662) (Line 662)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/__init__.py#L662
- **Target Call:** `f.close`
- **Context:** `Repo.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self._data_index.close()
```

##### 2. [dvc/utils/serialize/_py.py](https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/_py.py#L75) (Line 75)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/utils/serialize/_py.py#L75
- **Target Call:** `f.close`
- **Context:** `_dump`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    stream.close()
```

</details>

#### <a id="iterative-dvc-fs-du"></a>🔹 `fs.du` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.du</code> in iterative/dvc</b></summary>

##### 1. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L36) (Line 36)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L36
- **Target Call:** `fs.du`
- **Context:** `du`
- **Arguments:** `path`
- **Keywords:** `{'total': 'True'}`

```python
            return [(path, fs.du(path, total=True))]
```

##### 2. [dvc/repo/du.py](https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L39) (Line 39)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/du.py#L39
- **Target Call:** `fs.du`
- **Context:** `du`
- **Arguments:** `entry_path`
- **Keywords:** `{'total': 'True'}`

```python
            (entry_path, fs.du(entry_path, total=True)) for entry_path in fs.ls(path)
```

</details>

#### <a id="iterative-dvc-fs-close"></a>🔹 `fs.close` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.close</code> in iterative/dvc</b></summary>

##### 1. [dvc/fs/dvc.py](https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L753) (Line 753)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/fs/dvc.py#L753
- **Target Call:** `fs.close`
- **Context:** `DVCFileSystem.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.fs.close()
```

</details>

#### <a id="iterative-dvc-f-readlines"></a>🔹 `f.readlines` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.readlines</code> in iterative/dvc</b></summary>

##### 1. [dvc/ignore.py](https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L120) (Line 120)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/ignore.py#L120
- **Target Call:** `f.readlines`
- **Context:** `DvcIgnorePatterns.from_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                for line_no, line in enumerate(map(str.strip, fobj.readlines()))
```

</details>

#### <a id="iterative-dvc-fs-move"></a>🔹 `fs.move` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.move</code> in iterative/dvc</b></summary>

##### 1. [dvc/output.py](https://github.com/iterative/dvc/blob/main/dvc/output.py#L1002) (Line 1002)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/output.py#L1002
- **Target Call:** `fs.move`
- **Context:** `Output.move`
- **Arguments:** `self.fs_path, out.fs_path`
- **Keywords:** `{}`

```python
            self.fs.move(self.fs_path, out.fs_path)
```

</details>

#### <a id="iterative-dvc-fs-commonpath"></a>🔹 `fs.commonpath` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.commonpath</code> in iterative/dvc</b></summary>

##### 1. [dvc/repo/plots/__init__.py](https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L480) (Line 480)
- **Line Link:** https://github.com/iterative/dvc/blob/main/dvc/repo/plots/__init__.py#L480
- **Target Call:** `fs.commonpath`
- **Context:** `_closest_parent`
- **Arguments:** `[path, parent]`
- **Keywords:** `{}`

```python
        common_path = fs.commonpath([path, parent])
```

</details>

### [dask/dask](https://github.com/dask/dask)
- **Files Scanned:** `184` | **Files with Usages:** `16` | **Total Usages:** `76`

#### <a id="dask-dask-fs-open"></a>🔹 `fs.open` (16 occurrences)

<details open>
<summary><b>Click to expand/collapse 16 occurrences for <code>fs.open</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1781) (Line 1781)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1781
- **Target Call:** `fs.open`
- **Context:** `_read_partition_stats`
- **Arguments:** `path`
- **Keywords:** `{'default_cache': "'none'"}`

```python
            with fs.open(path, default_cache="none") as f:
```

##### 2. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L911) (Line 911)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L911
- **Target Call:** `fs.open`
- **Context:** `to_csv`
- **Arguments:** `filename`
- **Keywords:** `{'mode': 'mode'}`

```python
        first_file = open_file(filename, mode=mode, **file_options)
```

##### 3. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L915) (Line 915)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L915
- **Target Call:** `fs.open`
- **Context:** `to_csv`
- **Arguments:** `filename`
- **Keywords:** `{'mode': 'append_mode'}`

```python
        append_file = open_file(filename, mode=append_mode, **file_options)
```

##### 4. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L39) (Line 39)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L39
- **Target Call:** `fs.open`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
                with fs.open(path, "rb") as f:
```

##### 5. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L60) (Line 60)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L60
- **Target Call:** `fs.open`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0], 'rb'`
- **Keywords:** `{}`

```python
                    with fs.open(paths[0], "rb") as f:
```

##### 6. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L111) (Line 111)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L111
- **Target Call:** `fs.open`
- **Context:** `ArrowORCEngine.write_partition`
- **Arguments:** `fs.sep.join([path, filename]), 'wb'`
- **Keywords:** `{}`

```python
        with fs.open(fs.sep.join([path, filename]), "wb") as f:
```

##### 7. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L122) (Line 122)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L122
- **Target Call:** `fs.open`
- **Context:** `_read_orc_stripes`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    with fs.open(path, "rb") as f:
```

##### 8. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L150) (Line 150)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L150
- **Target Call:** `fs.open`
- **Context:** `_write_partitioned`
- **Arguments:** `full_path, 'wb'`
- **Keywords:** `{}`

```python
        with fs.open(full_path, "wb") as f:
```

##### 9. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L684) (Line 684)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L684
- **Target Call:** `fs.open`
- **Context:** `ArrowDatasetEngine.initialize_write`
- **Arguments:** `fs.sep.join([path, '_metadata'])`
- **Keywords:** `{'mode': "'rb'"}`

```python
                    with fs.open(fs.sep.join([path, "_metadata"]), mode="rb") as fil:
```

##### 10. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L690) (Line 690)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L690
- **Target Call:** `fs.open`
- **Context:** `ArrowDatasetEngine.initialize_write`
- **Arguments:** `sorted(ds.files, key=natural_sort_key)[-1]`
- **Keywords:** `{'mode': "'rb'"}`

```python
                        with fs.open(
                            sorted(ds.files, key=natural_sort_key)[-1], mode="rb"
                        ) as fil:
```

##### 11. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L851) (Line 851)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L851
- **Target Call:** `fs.open`
- **Context:** `ArrowDatasetEngine.write_partition`
- **Arguments:** `fs.sep.join([path, filename]), 'wb'`
- **Keywords:** `{}`

```python
            with fs.open(fs.sep.join([path, filename]), "wb") as fil:
```

##### 12. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L882) (Line 882)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L882
- **Target Call:** `fs.open`
- **Context:** `ArrowDatasetEngine.write_metadata`
- **Arguments:** `common_metadata_path, 'wb'`
- **Keywords:** `{}`

```python
                with fs.open(common_metadata_path, "wb") as fil:
```

##### 13. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L895) (Line 895)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L895
- **Target Call:** `fs.open`
- **Context:** `ArrowDatasetEngine.write_metadata`
- **Arguments:** `metadata_path, 'wb'`
- **Keywords:** `{}`

```python
            with fs.open(metadata_path, "wb") as fil:
```

##### 14. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L1820) (Line 1820)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L1820
- **Target Call:** `fs.open`
- **Context:** `ArrowDatasetEngine.collect_file_metadata`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
        with fs.open(path, "rb") as f:
```

##### 15. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L1836) (Line 1836)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L1836
- **Target Call:** `fs.open`
- **Context:** `ArrowDatasetEngine.aggregate_metadata`
- **Arguments:** `metadata_path, 'wb'`
- **Keywords:** `{}`

```python
            with fs.open(metadata_path, "wb") as fil:
```

##### 16. [dask/dataframe/io/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/utils.py#L221) (Line 221)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/utils.py#L221
- **Target Call:** `fs.open` | **Cache Strategy:** `parts`
- **Context:** `_open_input_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return [_set_context(fs.open(path, **kwargs), context_stack) for path in paths]
```

</details>

#### <a id="dask-dask-f-read"></a>🔹 `f.read` (10 occurrences)

<details open>
<summary><b>Click to expand/collapse 10 occurrences for <code>f.read</code> in dask/dask</b></summary>

##### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L18) (Line 18)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L18
- **Target Call:** `f.read`
- **Context:** `read_long`
- **Arguments:** `1`
- **Keywords:** `{}`

```python
    c = fo.read(1)
```

##### 2. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L23) (Line 23)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L23
- **Target Call:** `f.read`
- **Context:** `read_long`
- **Arguments:** `1`
- **Keywords:** `{}`

```python
        b = ord(fo.read(1))
```

##### 3. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L32) (Line 32)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L32
- **Target Call:** `f.read`
- **Context:** `read_bytes`
- **Arguments:** `size`
- **Keywords:** `{}`

```python
    return fo.read(size)
```

##### 4. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L47) (Line 47)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L47
- **Target Call:** `f.read`
- **Context:** `read_header`
- **Arguments:** `len(MAGIC)`
- **Keywords:** `{}`

```python
    assert fo.read(len(MAGIC)) == MAGIC, "Magic avro bytes missing"
```

##### 5. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L58) (Line 58)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L58
- **Target Call:** `f.read`
- **Context:** `read_header`
- **Arguments:** `SYNC_SIZE`
- **Keywords:** `{}`

```python
    out["sync"] = fo.read(SYNC_SIZE)
```

##### 6. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L61) (Line 61)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L61
- **Target Call:** `f.read`
- **Context:** `read_header`
- **Arguments:** `out['header_size']`
- **Keywords:** `{}`

```python
    out["head_bytes"] = fo.read(out["header_size"])
```

##### 7. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L171) (Line 171)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L171
- **Target Call:** `f.read`
- **Context:** `read_bytes`
- **Arguments:** `sample`
- **Keywords:** `{}`

```python
                sample = f.read(sample)
```

##### 8. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L173) (Line 173)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L173
- **Target Call:** `f.read`
- **Context:** `read_bytes`
- **Arguments:** `sample`
- **Keywords:** `{}`

```python
                sample_buff = f.read(sample)
```

##### 9. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L175) (Line 175)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L175
- **Target Call:** `f.read`
- **Context:** `read_bytes`
- **Arguments:** `sample`
- **Keywords:** `{}`

```python
                    new = f.read(sample)
```

##### 10. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L193) (Line 193)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L193
- **Target Call:** `f.read`
- **Context:** `read_block_from_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            return f.read()
```

</details>

#### <a id="dask-dask-stringify-path"></a>🔹 `stringify_path` (9 occurrences)

<details open>
<summary><b>Click to expand/collapse 9 occurrences for <code>stringify_path</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/dask_expr/_collection.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/_collection.py#L5359) (Line 5359)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/_collection.py#L5359
- **Target Call:** `stringify_path`
- **Context:** `read_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = stringify_path(path)
```

##### 2. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L489) (Line 489)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L489
- **Target Call:** `stringify_path`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = stringify_path(path)
```

##### 3. [dask/dataframe/io/hdf.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L147) (Line 147)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L147
- **Target Call:** `stringify_path`
- **Context:** `to_hdf`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    path = stringify_path(path)
```

##### 4. [dask/dataframe/io/hdf.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L381) (Line 381)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/hdf.py#L381
- **Target Call:** `stringify_path`
- **Context:** `read_hdf`
- **Arguments:** `pattern`
- **Keywords:** `{}`

```python
    pattern = stringify_path(pattern)
```

##### 5. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L174) (Line 174)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L174
- **Target Call:** `stringify_path`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        path = stringify_path(path)
```

##### 6. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L470) (Line 470)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L470
- **Target Call:** `stringify_path`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                urlpath = [stringify_path(u) for u in urlpath]
```

##### 7. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L472) (Line 472)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L472
- **Target Call:** `stringify_path`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
                urlpath = [stringify_path(urlpath)]
```

##### 8. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L95) (Line 95)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L95
- **Target Call:** `stringify_path`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                urlpath = [stringify_path(u) for u in urlpath]
```

##### 9. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L97) (Line 97)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L97
- **Target Call:** `stringify_path`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `urlpath`
- **Keywords:** `{}`

```python
                urlpath = [stringify_path(urlpath)]
```

</details>

#### <a id="dask-dask-get-fs-token-paths"></a>🔹 `get_fs_token_paths` (7 occurrences)

<details open>
<summary><b>Click to expand/collapse 7 occurrences for <code>get_fs_token_paths</code> in dask/dask</b></summary>

##### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L104) (Line 104)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L104
- **Target Call:** `get_fs_token_paths`
- **Context:** `read_avro`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
        fs, fs_token, paths = get_fs_token_paths(
            urlpath, mode="rb", storage_options=storage_options
        )
```

##### 2. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L83) (Line 83)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L83
- **Target Call:** `get_fs_token_paths`
- **Context:** `read_bytes`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'kwargs'}`

```python
    fs, fs_token, paths = get_fs_token_paths(urlpath, mode="rb", storage_options=kwargs)
```

##### 3. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L488) (Line 488)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L488
- **Target Call:** `get_fs_token_paths`
- **Context:** `read_pandas`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
        paths = get_fs_token_paths(urlpath, mode="rb", storage_options=storage_options)[
```

##### 4. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L81) (Line 81)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L81
- **Target Call:** `get_fs_token_paths`
- **Context:** `read_orc`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
    fs, fs_token, paths = get_fs_token_paths(
        path, mode="rb", storage_options=storage_options
    )
```

##### 5. [dask/dataframe/io/orc/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L175) (Line 175)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/core.py#L175
- **Target Call:** `get_fs_token_paths`
- **Context:** `to_orc`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'wb'", 'storage_options': 'storage_options'}`

```python
    fs, _, _ = get_fs_token_paths(path, mode="wb", storage_options=storage_options)
```

##### 6. [dask/dataframe/io/parquet/core.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/core.py#L289) (Line 289)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/core.py#L289
- **Target Call:** `get_fs_token_paths`
- **Context:** `create_metadata_file`
- **Arguments:** `paths`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
        fs, _, paths = get_fs_token_paths(
            paths, mode="rb", storage_options=storage_options
        )
```

##### 7. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L72) (Line 72)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L72
- **Target Call:** `get_fs_token_paths`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rb'", 'storage_options': 'storage_options'}`

```python
            fs, _, paths = get_fs_token_paths(
                urlpath, mode="rb", storage_options=storage_options
            )
```

</details>

#### <a id="dask-dask-open-files"></a>🔹 `open_files` (7 occurrences)

<details open>
<summary><b>Click to expand/collapse 7 occurrences for <code>open_files</code> in dask/dask</b></summary>

##### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L136) (Line 136)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L136
- **Target Call:** `open_files`
- **Context:** `read_avro`
- **Arguments:** `urlpath`
- **Keywords:** `{'compression': 'compression'}`

```python
        files = open_files(urlpath, compression=compression, **storage_options)
```

##### 2. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L256) (Line 256)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L256
- **Target Call:** `open_files`
- **Context:** `to_avro`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{'name_function': 'name_function', 'num': 'b.npartitions'}`

```python
    files = open_files(
        filename,
        "wb",
        name_function=name_function,
        num=b.npartitions,
        **storage_options,
    )
```

##### 3. [dask/bag/core.py](https://github.com/dask/dask/blob/main/dask/bag/core.py#L259) (Line 259)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/core.py#L259
- **Target Call:** `open_files`
- **Context:** `to_textfiles`
- **Arguments:** `path`
- **Keywords:** `{'compression': 'compression', 'mode': 'mode', 'encoding': 'encoding', 'name_function': 'name_function', 'num': 'b.npartitions'}`

```python
    files = open_files(
        path,
        compression=compression,
        mode=mode,
        encoding=encoding,
        name_function=name_function,
        num=b.npartitions,
        **(storage_options or {}),
    )
```

##### 4. [dask/bag/text.py](https://github.com/dask/dask/blob/main/dask/bag/text.py#L100) (Line 100)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/text.py#L100
- **Target Call:** `open_files`
- **Context:** `read_text`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': "'rt'", 'encoding': 'encoding', 'errors': 'errors', 'compression': 'compression', 'newline': 'newline'}`

```python
        files = open_files(
            urlpath,
            mode="rt",
            encoding=encoding,
            errors=errors,
            compression=compression,
            newline=newline,
            **(storage_options or {}),
        )
```

##### 5. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L922) (Line 922)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L922
- **Target Call:** `open_files`
- **Context:** `to_csv`
- **Arguments:** `filename`
- **Keywords:** `{'mode': 'mode', 'name_function': 'name_function', 'num': 'df.npartitions'}`

```python
        files = open_files(
            filename,
            mode=mode,
            name_function=name_function,
            num=df.npartitions,
            **file_options,
        )
```

##### 6. [dask/dataframe/io/json.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/json.py#L78) (Line 78)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/json.py#L78
- **Target Call:** `open_files`
- **Context:** `to_json`
- **Arguments:** `url_path, 'wt'`
- **Keywords:** `{'encoding': 'encoding', 'errors': 'errors', 'name_function': 'name_function', 'num': 'df.npartitions', 'compression': 'compression'}`

```python
    outfiles = open_files(
        url_path,
        "wt",
        encoding=encoding,
        errors=errors,
        name_function=name_function,
        num=df.npartitions,
        compression=compression,
        **(storage_options or {}),
    )
```

##### 7. [dask/dataframe/io/json.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/json.py#L268) (Line 268)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/json.py#L268
- **Target Call:** `open_files`
- **Context:** `read_json`
- **Arguments:** `url_path, 'rt'`
- **Keywords:** `{'encoding': 'encoding', 'errors': 'errors', 'compression': 'compression'}`

```python
        files = open_files(
            url_path,
            "rt",
            encoding=encoding,
            errors=errors,
            compression=compression,
            **storage_options,
        )
```

</details>

#### <a id="dask-dask-fs-info"></a>🔹 `fs.info` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.info</code> in dask/dask</b></summary>

##### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L69) (Line 69)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L69
- **Target Call:** `fs.info`
- **Context:** `open_head`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    size = fs.info(path)["size"]
```

##### 2. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L111) (Line 111)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L111
- **Target Call:** `fs.info`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            size = fs.info(path)["size"]
```

</details>

#### <a id="dask-dask-fs-ukey"></a>🔹 `fs.ukey` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.ukey</code> in dask/dask</b></summary>

##### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L125) (Line 125)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L125
- **Target Call:** `fs.ukey`
- **Context:** `read_avro`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                fs_token, delimiter, path, fs.ukey(path), compression, offset
```

##### 2. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L149) (Line 149)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L149
- **Target Call:** `fs.ukey`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        token = tokenize(fs_token, delimiter, path, fs.ukey(path), compression, offset)
```

</details>

#### <a id="dask-dask-fs-read-block"></a>🔹 `fs.read_block` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.read_block</code> in dask/dask</b></summary>

##### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L152) (Line 152)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L152
- **Target Call:** `fs.read_block`
- **Context:** `read_chunk`
- **Arguments:** `f, off, l, head['sync']`
- **Keywords:** `{}`

```python
        chunk = read_block(f, off, l, head["sync"])
```

##### 2. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L194) (Line 194)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L194
- **Target Call:** `fs.read_block`
- **Context:** `read_block_from_file`
- **Arguments:** `f, off, bs, delimiter`
- **Keywords:** `{}`

```python
        return read_block(f, off, bs, delimiter)
```

</details>

#### <a id="dask-dask-infer-compression"></a>🔹 `infer_compression` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>infer_compression</code> in dask/dask</b></summary>

##### 1. [dask/bytes/core.py](https://github.com/dask/dask/blob/main/dask/bytes/core.py#L103) (Line 103)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bytes/core.py#L103
- **Target Call:** `infer_compression`
- **Context:** `read_bytes`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                comp = infer_compression(path)
```

##### 2. [dask/dataframe/io/csv.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L497) (Line 497)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/csv.py#L497
- **Target Call:** `infer_compression`
- **Context:** `read_pandas`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        compression = infer_compression(paths[0])
```

</details>

#### <a id="dask-dask-fs-exists"></a>🔹 `fs.exists` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.exists</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L505) (Line 505)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L505
- **Target Call:** `fs.exists`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if fs.exists(path) and fs.isdir(path):
```

##### 2. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L947) (Line 947)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L947
- **Target Call:** `fs.exists`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `meta_path`
- **Keywords:** `{}`

```python
            if not ignore_metadata_file and fs.exists(meta_path):
```

</details>

#### <a id="dask-dask-fs-isdir"></a>🔹 `fs.isdir` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.isdir</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L505) (Line 505)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L505
- **Target Call:** `fs.isdir`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        if fs.exists(path) and fs.isdir(path):
```

##### 2. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L940) (Line 940)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L940
- **Target Call:** `fs.isdir`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        if len(paths) == 1 and fs.isdir(paths[0]):
```

</details>

#### <a id="dask-dask-fs-find"></a>🔹 `fs.find` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.find</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L24) (Line 24)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L24
- **Target Call:** `fs.find`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
            paths = fs.find(paths[0])
```

##### 2. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L961) (Line 961)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L961
- **Target Call:** `fs.find`
- **Context:** `ArrowDatasetEngine._collect_dataset_info`
- **Arguments:** `paths`
- **Keywords:** `{}`

```python
                    for path in fs.find(paths)
```

</details>

#### <a id="dask-dask-expand-paths-if-needed"></a>🔹 `expand_paths_if_needed` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>expand_paths_if_needed</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/io/parquet/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L492) (Line 492)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/arrow.py#L492
- **Target Call:** `expand_paths_if_needed`
- **Context:** `ArrowDatasetEngine.extract_filesystem`
- **Arguments:** `urlpath, 'rb', 1, fsspec_fs, None`
- **Keywords:** `{}`

```python
            paths = expand_paths_if_needed(urlpath, "rb", 1, fsspec_fs, None)
```

##### 2. [dask/dataframe/io/parquet/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L99) (Line 99)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/parquet/utils.py#L99
- **Target Call:** `expand_paths_if_needed`
- **Context:** `Engine.extract_filesystem`
- **Arguments:** `urlpath, 'rb', 1, fs, None`
- **Keywords:** `{}`

```python
            paths = expand_paths_if_needed(urlpath, "rb", 1, fs, None)
```

</details>

#### <a id="dask-dask-f-write"></a>🔹 `f.write` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>f.write</code> in dask/dask</b></summary>

##### 1. [dask/utils.py](https://github.com/dask/dask/blob/main/dask/utils.py#L417) (Line 417)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/utils.py#L417
- **Target Call:** `f.write`
- **Context:** `filetext`
- **Arguments:** `text`
- **Keywords:** `{}`

```python
            f.write(text)
```

##### 2. [dask/utils.py](https://github.com/dask/dask/blob/main/dask/utils.py#L485) (Line 485)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/utils.py#L485
- **Target Call:** `f.write`
- **Context:** `filetexts`
- **Arguments:** `text`
- **Keywords:** `{}`

```python
                f.write(text)
```

</details>

#### <a id="dask-dask-f-close"></a>🔹 `f.close` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>f.close</code> in dask/dask</b></summary>

##### 1. [dask/utils.py](https://github.com/dask/dask/blob/main/dask/utils.py#L420) (Line 420)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/utils.py#L420
- **Target Call:** `f.close`
- **Context:** `filetext`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                f.close()
```

##### 2. [dask/utils.py](https://github.com/dask/dask/blob/main/dask/utils.py#L488) (Line 488)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/utils.py#L488
- **Target Call:** `f.close`
- **Context:** `filetexts`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    f.close()
```

</details>

#### <a id="dask-dask-f-tell"></a>🔹 `f.tell` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.tell</code> in dask/dask</b></summary>

##### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L59) (Line 59)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L59
- **Target Call:** `f.tell`
- **Context:** `read_header`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    out["header_size"] = fo.tell()
```

</details>

#### <a id="dask-dask-f-seek"></a>🔹 `f.seek` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.seek</code> in dask/dask</b></summary>

##### 1. [dask/bag/avro.py](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L60) (Line 60)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/bag/avro.py#L60
- **Target Call:** `f.seek`
- **Context:** `read_header`
- **Arguments:** `0`
- **Keywords:** `{}`

```python
    fo.seek(0)
```

</details>

#### <a id="dask-dask-fs-expand-path"></a>🔹 `fs.expand_path` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.expand_path</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L520) (Line 520)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L520
- **Target Call:** `fs.expand_path`
- **Context:** `to_parquet`
- **Arguments:** `'.'`
- **Keywords:** `{}`

```python
                working_dir = fs.expand_path(".")[0]
```

</details>

#### <a id="dask-dask-fs-rm"></a>🔹 `fs.rm` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.rm</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L527) (Line 527)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L527
- **Target Call:** `fs.rm`
- **Context:** `to_parquet`
- **Arguments:** `path`
- **Keywords:** `{'recursive': 'True'}`

```python
            fs.rm(path, recursive=True)
```

</details>

#### <a id="dask-dask-fs-checksum"></a>🔹 `fs.checksum` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.checksum</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/dask_expr/io/parquet.py](https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1394) (Line 1394)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/dask_expr/io/parquet.py#L1394
- **Target Call:** `fs.checksum`
- **Context:** `ReadParquetFSSpec._dataset_info`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
            checksum.append(fs.checksum(file))
```

</details>

#### <a id="dask-dask-fs-isfile"></a>🔹 `fs.isfile` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.isfile</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/io/orc/arrow.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L23) (Line 23)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/orc/arrow.py#L23
- **Target Call:** `fs.isfile`
- **Context:** `ArrowORCEngine.read_metadata`
- **Arguments:** `paths[0]`
- **Keywords:** `{}`

```python
        if len(paths) == 1 and not fs.isfile(paths[0]):
```

</details>

#### <a id="dask-dask-fsspec-open-parquet-file"></a>🔹 `fsspec.open_parquet_file` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fsspec.open_parquet_file</code> in dask/dask</b></summary>

##### 1. [dask/dataframe/io/utils.py](https://github.com/dask/dask/blob/main/dask/dataframe/io/utils.py#L210) (Line 210)
- **Line Link:** https://github.com/dask/dask/blob/main/dask/dataframe/io/utils.py#L210
- **Target Call:** `fsspec.open_parquet_file` | **Cache Strategy:** `parts`
- **Context:** `_open_input_files`
- **Arguments:** `path`
- **Keywords:** `{'fs': 'fs', 'row_groups': 'rgs'}`

```python
                fsspec_parquet.open_parquet_file(
                    path,
                    fs=fs,
                    row_groups=rgs,
                    **kwargs,
                ),
```

</details>

### [great-expectations/great_expectations](https://github.com/great-expectations/great_expectations)
- **Files Scanned:** `0` | **Files with Usages:** `0` | **Total Usages:** `0`

No direct filesystem / fsspec usages detected in this target.

### [modin-project/modin](https://github.com/modin-project/modin)
- **Files Scanned:** `283` | **Files with Usages:** `8` | **Total Usages:** `52`

#### <a id="modin-project-modin-url-to-fs"></a>🔹 `url_to_fs` (11 occurrences)

<details open>
<summary><b>Click to expand/collapse 11 occurrences for <code>url_to_fs</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L112) (Line 112)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L112
- **Target Call:** `url_to_fs`
- **Context:** `ColumnStoreDataset.fs`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
                self._fs, self._fs_path = url_to_fs(self.path, **self.storage_options)
```

##### 2. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L129) (Line 129)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L129
- **Target Call:** `url_to_fs`
- **Context:** `ColumnStoreDataset.fs_path`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
                self._fs, self._fs_path = url_to_fs(self.path, **self.storage_options)
```

##### 3. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L863) (Line 863)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L863
- **Target Call:** `url_to_fs`
- **Context:** `ParquetDispatcher._read`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                    fs, fs_path = url_to_fs(path, **storage_options)
```

##### 4. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L865) (Line 865)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L865
- **Target Call:** `url_to_fs`
- **Context:** `ParquetDispatcher._read`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                    fs, fs_path = url_to_fs(path)
```

##### 5. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L928) (Line 928)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L928
- **Target Call:** `url_to_fs`
- **Context:** `ParquetDispatcher.write`
- **Arguments:** `output_path`
- **Keywords:** `{'client_kwargs': 'client_kwargs'}`

```python
        fs, url = fsspec.core.url_to_fs(output_path, client_kwargs=client_kwargs)
```

##### 6. [modin/core/io/file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L282) (Line 282)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L282
- **Target Call:** `url_to_fs`
- **Context:** `FileDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
        fs, _ = fsspec.core.url_to_fs(file_path, **new_storage_options)
```

##### 7. [modin/core/io/file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L287) (Line 287)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L287
- **Target Call:** `url_to_fs`
- **Context:** `FileDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{'anon': 'True'}`

```python
            fs, _ = fsspec.core.url_to_fs(file_path, anon=True, **new_storage_options)
```

##### 8. [modin/experimental/core/io/text/csv_glob_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L309) (Line 309)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L309
- **Target Call:** `url_to_fs`
- **Context:** `ExperimentalCSVGlobDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
        fs, _ = fsspec.core.url_to_fs(file_path, **new_storage_options)
```

##### 9. [modin/experimental/core/io/text/csv_glob_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L314) (Line 314)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L314
- **Target Call:** `url_to_fs`
- **Context:** `ExperimentalCSVGlobDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{'anon': 'True'}`

```python
            fs, _ = fsspec.core.url_to_fs(file_path, anon=True, **new_storage_options)
```

##### 10. [modin/experimental/core/io/text/csv_glob_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L376) (Line 376)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L376
- **Target Call:** `url_to_fs`
- **Context:** `ExperimentalCSVGlobDispatcher.get_path`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
        fs, _ = fsspec.core.url_to_fs(file_path, **new_storage_options)
```

##### 11. [modin/experimental/core/io/text/csv_glob_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L380) (Line 380)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L380
- **Target Call:** `url_to_fs`
- **Context:** `ExperimentalCSVGlobDispatcher.get_path`
- **Arguments:** `file_path`
- **Keywords:** `{'anon': 'True'}`

```python
            fs, _ = fsspec.core.url_to_fs(file_path, anon=True, **new_storage_options)
```

</details>

#### <a id="modin-project-modin-f-read"></a>🔹 `f.read` (8 occurrences)

<details open>
<summary><b>Click to expand/collapse 8 occurrences for <code>f.read</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L145) (Line 145)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L145
- **Target Call:** `f.read`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            f = BytesIO(f.read())
```

##### 2. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L152) (Line 152)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L152
- **Target Call:** `f.read`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** `EXCEL_READ_BLOCK_SIZE`
- **Keywords:** `{}`

```python
            sheet_block = f.read(EXCEL_READ_BLOCK_SIZE)
```

##### 3. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L155) (Line 155)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L155
- **Target Call:** `f.read`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** `EXCEL_READ_BLOCK_SIZE`
- **Keywords:** `{}`

```python
                sheet_block += f.read(EXCEL_READ_BLOCK_SIZE)
```

##### 4. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L223) (Line 223)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L223
- **Target Call:** `f.read`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** `chunk_size`
- **Keywords:** `{}`

```python
                chunk = f.read(chunk_size)
```

##### 5. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L233) (Line 233)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L233
- **Target Call:** `f.read`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** `chunk_size`
- **Keywords:** `{}`

```python
                    chunk += f.read(chunk_size)
```

##### 6. [modin/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L216) (Line 216)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L216
- **Target Call:** `f.read`
- **Context:** `PandasParser.generic_parse`
- **Arguments:** `end - start`
- **Keywords:** `{}`

```python
            to_read = header + bio.read(end - start)
```

##### 7. [modin/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L664) (Line 664)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L664
- **Target Call:** `f.read`
- **Context:** `PandasJSONParser.parse`
- **Arguments:** `end - start`
- **Keywords:** `{}`

```python
                to_read = b"" + bio.read(end - start)
```

##### 8. [modin/experimental/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/storage_formats/pandas/parsers.py#L65) (Line 65)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/storage_formats/pandas/parsers.py#L65
- **Target Call:** `f.read`
- **Context:** `ExperimentalPandasCSVGlobParser.parse`
- **Arguments:** `end - start`
- **Keywords:** `{}`

```python
                    to_read = header + bio.read(end - start)
```

</details>

#### <a id="modin-project-modin-f-seek"></a>🔹 `f.seek` (7 occurrences)

<details open>
<summary><b>Click to expand/collapse 7 occurrences for <code>f.seek</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L161) (Line 161)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L161
- **Target Call:** `f.seek`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** `idx_of_header_end`
- **Keywords:** `{}`

```python
                f.seek(idx_of_header_end)
```

##### 2. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L168) (Line 168)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L168
- **Target Call:** `f.seek`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** `idx_of_header_start`
- **Keywords:** `{}`

```python
                f.seek(idx_of_header_start)
```

##### 3. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L237) (Line 237)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L237
- **Target Call:** `f.seek`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** `-(len(chunk) - last_index) + len(row_close_tag), 1`
- **Keywords:** `{}`

```python
                f.seek(-(len(chunk) - last_index) + len(row_close_tag), 1)
```

##### 4. [modin/core/io/text/text_file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/text_file_dispatcher.py#L1104) (Line 1104)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/text_file_dispatcher.py#L1104
- **Target Call:** `f.seek`
- **Context:** `TextFileDispatcher._read`
- **Arguments:** `old_pos`
- **Keywords:** `{}`

```python
            f.seek(old_pos)
```

##### 5. [modin/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L215) (Line 215)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L215
- **Target Call:** `f.seek`
- **Context:** `PandasParser.generic_parse`
- **Arguments:** `start`
- **Keywords:** `{}`

```python
            bio.seek(start)
```

##### 6. [modin/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L663) (Line 663)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L663
- **Target Call:** `f.seek`
- **Context:** `PandasJSONParser.parse`
- **Arguments:** `start`
- **Keywords:** `{}`

```python
                bio.seek(start)
```

##### 7. [modin/experimental/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/storage_formats/pandas/parsers.py#L64) (Line 64)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/storage_formats/pandas/parsers.py#L64
- **Target Call:** `f.seek`
- **Context:** `ExperimentalPandasCSVGlobParser.parse`
- **Arguments:** `start`
- **Keywords:** `{}`

```python
                    bio.seek(start)
```

</details>

#### <a id="modin-project-modin-fs-open"></a>🔹 `fs.open` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>fs.open</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L206) (Line 206)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L206
- **Target Call:** `fs.open`
- **Context:** `PyArrowDataset.row_groups_per_file`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
            with self.fs.open(file) as f:
```

##### 2. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L256) (Line 256)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L256
- **Target Call:** `fs.open`
- **Context:** `FastParquetDataset.row_groups_per_file`
- **Arguments:** `file`
- **Keywords:** `{}`

```python
            with self.fs.open(file) as f:
```

##### 3. [modin/core/io/file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L96) (Line 96)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L96
- **Target Call:** `fs.open`
- **Context:** `OpenFile.__enter__`
- **Arguments:** `*args`
- **Keywords:** `{}`

```python
        self.file = fsspec.open(*args, **self.kwargs)
```

##### 4. [modin/core/io/file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L101) (Line 101)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L101
- **Target Call:** `fs.open`
- **Context:** `OpenFile.__enter__`
- **Arguments:** `*args`
- **Keywords:** `{}`

```python
            self.file = fsspec.open(*args, **self.kwargs)
```

##### 5. [modin/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L809) (Line 809)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L809
- **Target Call:** `fs.open`
- **Context:** `PandasParquetParser.parse`
- **Arguments:** `file_for_parser.path`
- **Keywords:** `{}`

```python
                context = fsspec.open(file_for_parser.path, **storage_options)
```

</details>

#### <a id="modin-project-modin-f-tell"></a>🔹 `f.tell` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>f.tell</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L205) (Line 205)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L205
- **Target Call:** `f.tell`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            chunk_size = max(1, (total_bytes - f.tell()) // NPartitions.get())
```

##### 2. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L219) (Line 219)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L219
- **Target Call:** `f.tell`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            while f.tell() < total_bytes:
```

##### 3. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L222) (Line 222)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L222
- **Target Call:** `f.tell`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                args["start"] = f.tell()
```

##### 4. [modin/core/io/text/excel_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L238) (Line 238)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L238
- **Target Call:** `f.tell`
- **Context:** `ExcelDispatcher._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                args["end"] = f.tell()
```

##### 5. [modin/core/io/text/text_file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/text_file_dispatcher.py#L1099) (Line 1099)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/text_file_dispatcher.py#L1099
- **Target Call:** `f.tell`
- **Context:** `TextFileDispatcher._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            old_pos = f.tell()
```

</details>

#### <a id="modin-project-modin-f-readline"></a>🔹 `f.readline` (5 occurrences)

<details open>
<summary><b>Click to expand/collapse 5 occurrences for <code>f.readline</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/text/json_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/text/json_dispatcher.py#L70) (Line 70)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/text/json_dispatcher.py#L70
- **Target Call:** `f.readline`
- **Context:** `JSONDispatcher._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            columns = pandas.read_json(BytesIO(b"" + f.readline()), lines=True).columns
```

##### 2. [modin/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L205) (Line 205)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L205
- **Target Call:** `f.readline`
- **Context:** `PandasParser.generic_parse`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    header = bio.readline()
```

##### 3. [modin/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L210) (Line 210)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L210
- **Target Call:** `f.readline`
- **Context:** `PandasParser.generic_parse`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    header += bio.readline()
```

##### 4. [modin/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L213) (Line 213)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/storage_formats/pandas/parsers.py#L213
- **Target Call:** `f.readline`
- **Context:** `PandasParser.generic_parse`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    header += bio.readline()
```

##### 5. [modin/experimental/core/storage_formats/pandas/parsers.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/storage_formats/pandas/parsers.py#L61) (Line 61)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/storage_formats/pandas/parsers.py#L61
- **Target Call:** `f.readline`
- **Context:** `ExperimentalPandasCSVGlobParser.parse`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                        header = b"" + bio.readline()
```

</details>

#### <a id="modin-project-modin-fs-exists"></a>🔹 `fs.exists` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fs.exists</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L285) (Line 285)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L285
- **Target Call:** `fs.exists`
- **Context:** `FileDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
            exists = fs.exists(file_path)
```

##### 2. [modin/core/io/file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L288) (Line 288)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L288
- **Target Call:** `fs.exists`
- **Context:** `FileDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
            exists = fs.exists(file_path)
```

##### 3. [modin/experimental/core/io/text/csv_glob_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L312) (Line 312)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L312
- **Target Call:** `fs.exists`
- **Context:** `ExperimentalCSVGlobDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
            exists = fs.exists(file_path)
```

##### 4. [modin/experimental/core/io/text/csv_glob_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L315) (Line 315)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L315
- **Target Call:** `fs.exists`
- **Context:** `ExperimentalCSVGlobDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
            exists = fs.exists(file_path)
```

</details>

#### <a id="modin-project-modin-fs-glob"></a>🔹 `fs.glob` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.glob</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L276) (Line 276)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L276
- **Target Call:** `fs.glob`
- **Context:** `FastParquetDataset._get_fastparquet_files`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
            files = self.fs.glob(self.path)
```

##### 2. [modin/experimental/core/io/text/csv_glob_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L316) (Line 316)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/experimental/core/io/text/csv_glob_dispatcher.py#L316
- **Target Call:** `fs.glob`
- **Context:** `ExperimentalCSVGlobDispatcher.file_exists`
- **Arguments:** `file_path`
- **Keywords:** `{}`

```python
        return exists or len(fs.glob(file_path)) > 0
```

</details>

#### <a id="modin-project-modin-fs-find"></a>🔹 `fs.find` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.find</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L288) (Line 288)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L288
- **Target Call:** `fs.find`
- **Context:** `FastParquetDataset._get_fastparquet_files`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
                files = self.fs.find(self.path)
```

##### 2. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L292) (Line 292)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L292
- **Target Call:** `fs.find`
- **Context:** `FastParquetDataset._get_fastparquet_files`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
                    for f in self.fs.find(self.path)
```

</details>

#### <a id="modin-project-modin-fs-isfile"></a>🔹 `fs.isfile` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.isfile</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L287) (Line 287)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L287
- **Target Call:** `fs.isfile`
- **Context:** `FastParquetDataset._get_fastparquet_files`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
            if self.fs.isfile(self.path):
```

</details>

#### <a id="modin-project-modin-fs-walk"></a>🔹 `fs.walk` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.walk</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/column_stores/parquet_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L866) (Line 866)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/column_stores/parquet_dispatcher.py#L866
- **Target Call:** `fs.walk`
- **Context:** `ParquetDispatcher._read`
- **Arguments:** `fs_path`
- **Keywords:** `{}`

```python
                path_generator = fs.walk(fs_path)
```

</details>

#### <a id="modin-project-modin-f-close"></a>🔹 `f.close` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.close</code> in modin-project/modin</b></summary>

##### 1. [modin/core/io/file_dispatcher.py](https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L113) (Line 113)
- **Line Link:** https://github.com/modin-project/modin/blob/main/modin/core/io/file_dispatcher.py#L113
- **Target Call:** `f.close`
- **Context:** `OpenFile.__exit__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self.file.close()
```

</details>

### [flyteorg/flyte](https://github.com/flyteorg/flyte)
- **Files Scanned:** `242` | **Files with Usages:** `0` | **Total Usages:** `0`

No direct filesystem / fsspec usages detected in this target.

### [feast-dev/feast](https://github.com/feast-dev/feast)
- **Files Scanned:** `600` | **Files with Usages:** `5` | **Total Usages:** `13`

#### <a id="feast-dev-feast-fs-get"></a>🔹 `fs.get` (7 occurrences)

<details open>
<summary><b>Click to expand/collapse 7 occurrences for <code>fs.get</code> in feast-dev/feast</b></summary>

##### 1. [sdk/python/feast/api/registry/rest/metrics.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/metrics.py#L187) (Line 187)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/metrics.py#L187
- **Target Call:** `fs.get`
- **Context:** `collect_resources_for_project`
- **Arguments:** `'spec', {}`
- **Keywords:** `{}`

```python
                    spec = fs.get("spec", {})
```

##### 2. [sdk/python/feast/api/registry/rest/search.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L208) (Line 208)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L208
- **Target Call:** `fs.get`
- **Context:** `search_resources`
- **Arguments:** `'featureService', {}`
- **Keywords:** `{}`

```python
                            "name": fs.get("featureService", {})
```

##### 3. [sdk/python/feast/api/registry/rest/search.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L211) (Line 211)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L211
- **Target Call:** `fs.get`
- **Context:** `search_resources`
- **Arguments:** `'spec', {}`
- **Keywords:** `{}`

```python
                            or fs.get("spec", {}).get("name", ""),
```

##### 4. [sdk/python/feast/api/registry/rest/search.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L212) (Line 212)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L212
- **Target Call:** `fs.get`
- **Context:** `search_resources`
- **Arguments:** `'featureService', {}`
- **Keywords:** `{}`

```python
                            "description": fs.get("featureService", {})
```

##### 5. [sdk/python/feast/api/registry/rest/search.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L215) (Line 215)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L215
- **Target Call:** `fs.get`
- **Context:** `search_resources`
- **Arguments:** `'spec', {}`
- **Keywords:** `{}`

```python
                            or fs.get("spec", {}).get("description", ""),
```

##### 6. [sdk/python/feast/api/registry/rest/search.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L217) (Line 217)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L217
- **Target Call:** `fs.get`
- **Context:** `search_resources`
- **Arguments:** `'featureService', {}`
- **Keywords:** `{}`

```python
                            "tags": fs.get("featureService", {})
```

##### 7. [sdk/python/feast/api/registry/rest/search.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L220) (Line 220)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/api/registry/rest/search.py#L220
- **Target Call:** `fs.get`
- **Context:** `search_resources`
- **Arguments:** `'spec', {}`
- **Keywords:** `{}`

```python
                            or fs.get("spec", {}).get("tags", {}),
```

</details>

#### <a id="feast-dev-feast-url-to-fs"></a>🔹 `url_to_fs` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>url_to_fs</code> in feast-dev/feast</b></summary>

##### 1. [sdk/python/feast/feature_view_utils.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/feature_view_utils.py#L99) (Line 99)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/feature_view_utils.py#L99
- **Target Call:** `url_to_fs`
- **Context:** `check_sink_source_exists`
- **Arguments:** `source_path`
- **Keywords:** `{}`

```python
        fs, path_in_fs = fsspec.core.url_to_fs(source_path)
```

##### 2. [sdk/python/feast/infra/offline_stores/contrib/ray_offline_store/ray.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/infra/offline_stores/contrib/ray_offline_store/ray.py#L2127) (Line 2127)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/infra/offline_stores/contrib/ray_offline_store/ray.py#L2127
- **Target Call:** `url_to_fs`
- **Context:** `RayOfflineStore.pull_all_from_table_or_query`
- **Arguments:** `source_path`
- **Keywords:** `{}`

```python
        fs, path_in_fs = fsspec.core.url_to_fs(source_path)
```

</details>

#### <a id="feast-dev-feast-fs-exists"></a>🔹 `fs.exists` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.exists</code> in feast-dev/feast</b></summary>

##### 1. [sdk/python/feast/feature_view_utils.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/feature_view_utils.py#L100) (Line 100)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/feature_view_utils.py#L100
- **Target Call:** `fs.exists`
- **Context:** `check_sink_source_exists`
- **Arguments:** `path_in_fs`
- **Keywords:** `{}`

```python
        return fs.exists(path_in_fs)
```

##### 2. [sdk/python/feast/infra/offline_stores/contrib/ray_offline_store/ray.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/infra/offline_stores/contrib/ray_offline_store/ray.py#L2128) (Line 2128)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/infra/offline_stores/contrib/ray_offline_store/ray.py#L2128
- **Target Call:** `fs.exists`
- **Context:** `RayOfflineStore.pull_all_from_table_or_query`
- **Arguments:** `path_in_fs`
- **Keywords:** `{}`

```python
        if not fs.exists(path_in_fs):
```

</details>

#### <a id="feast-dev-feast-fs-join"></a>🔹 `fs.join` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.join</code> in feast-dev/feast</b></summary>

##### 1. [sdk/python/feast/infra/compute_engines/local/nodes.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/infra/compute_engines/local/nodes.py#L87) (Line 87)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/infra/compute_engines/local/nodes.py#L87
- **Target Call:** `fs.join`
- **Context:** `LocalJoinNode.execute`
- **Arguments:** `joined_df, next_df`
- **Keywords:** `{'on': 'join_keys', 'how': 'self.how'}`

```python
            joined_df = self.backend.join(
                joined_df,
                next_df,
                on=join_keys,
                how=self.how,
            )
```

##### 2. [sdk/python/feast/infra/compute_engines/local/nodes.py](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/infra/compute_engines/local/nodes.py#L106) (Line 106)
- **Line Link:** https://github.com/feast-dev/feast/blob/master/sdk/python/feast/infra/compute_engines/local/nodes.py#L106
- **Target Call:** `fs.join`
- **Context:** `LocalJoinNode.execute`
- **Arguments:** `entity_df, joined_df`
- **Keywords:** `{'on': 'join_keys', 'how': "'left'"}`

```python
            joined_df = self.backend.join(
                entity_df,
                joined_df,
                on=join_keys,
                how="left",
            )
```

</details>

### [pydata/xarray](https://github.com/pydata/xarray)
- **Files Scanned:** `123` | **Files with Usages:** `1` | **Total Usages:** `4`

#### <a id="pydata-xarray-get-fs-token-paths"></a>🔹 `get_fs_token_paths` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>get_fs_token_paths</code> in pydata/xarray</b></summary>

##### 1. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L166) (Line 166)
- **Line Link:** https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L166
- **Target Call:** `get_fs_token_paths`
- **Context:** `_find_absolute_paths`
- **Arguments:** `paths`
- **Keywords:** `{'mode': "'rb'", 'storage_options': "kwargs.get('backend_kwargs', {}).get('storage_options', {})", 'expand': 'False'}`

```python
            fs, _, _ = fsspec.core.get_fs_token_paths(
                paths,
                mode="rb",
                storage_options=kwargs.get("backend_kwargs", {}).get(
                    "storage_options", {}
                ),
                expand=False,
            )
```

##### 2. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L221) (Line 221)
- **Line Link:** https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L221
- **Target Call:** `get_fs_token_paths`
- **Context:** `_open_remote_file`
- **Arguments:** `file`
- **Keywords:** `{'mode': 'mode', 'storage_options': 'storage_options'}`

```python
    fs, _, paths = fsspec.get_fs_token_paths(
        file, mode=mode, storage_options=storage_options
    )
```

</details>

#### <a id="pydata-xarray-fs-glob"></a>🔹 `fs.glob` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.glob</code> in pydata/xarray</b></summary>

##### 1. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L174) (Line 174)
- **Line Link:** https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L174
- **Target Call:** `fs.glob`
- **Context:** `_find_absolute_paths`
- **Arguments:** `fs._strip_protocol(paths)`
- **Keywords:** `{}`

```python
            tmp_paths = fs.glob(fs._strip_protocol(paths))  # finds directories
```

</details>

#### <a id="pydata-xarray-fs-open"></a>🔹 `fs.open` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.open</code> in pydata/xarray</b></summary>

##### 1. [xarray/backends/common.py](https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L227) (Line 227)
- **Line Link:** https://github.com/pydata/xarray/blob/main/xarray/backends/common.py#L227
- **Target Call:** `fs.open`
- **Context:** `_open_remote_file`
- **Arguments:** `paths[0]`
- **Keywords:** `{'mode': 'mode'}`

```python
    return fs.open(paths[0], mode=mode, **open_kwargs)
```

</details>

### [kedro-org/kedro](https://github.com/kedro-org/kedro)
- **Files Scanned:** `106` | **Files with Usages:** `1` | **Total Usages:** `12`

#### <a id="kedro-org-kedro-fsspec-filesystem"></a>🔹 `fsspec.filesystem` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fsspec.filesystem</code> in kedro-org/kedro</b></summary>

##### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L397) (Line 397)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L397
- **Target Call:** `fsspec.filesystem`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'tar'", 'fo': 'conf_source'}`

```python
            return fsspec.filesystem(protocol="tar", fo=conf_source), "tar"
```

##### 2. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L403) (Line 403)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L403
- **Target Call:** `fsspec.filesystem`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'zip'", 'fo': 'conf_source'}`

```python
            return fsspec.filesystem(protocol="zip", fo=conf_source), "zip"
```

##### 3. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L412) (Line 412)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L412
- **Target Call:** `fsspec.filesystem`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': 'protocol'}`

```python
            return fsspec.filesystem(protocol=protocol), protocol
```

##### 4. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L415) (Line 415)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L415
- **Target Call:** `fsspec.filesystem`
- **Context:** `OmegaConfigLoader._initialise_filesystem_and_protocol`
- **Arguments:** ``
- **Keywords:** `{'protocol': "'file'", 'fo': 'conf_source'}`

```python
            return fsspec.filesystem(protocol="file", fo=conf_source), "file"
```

</details>

#### <a id="kedro-org-kedro-fs-ls"></a>🔹 `fs.ls` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.ls</code> in kedro-org/kedro</b></summary>

##### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L226) (Line 226)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L226
- **Target Call:** `fs.ls`
- **Context:** `OmegaConfigLoader.__getitem__`
- **Arguments:** `''`
- **Keywords:** `{'detail': 'False'}`

```python
            base_path = str(Path(self._fs.ls("", detail=False)[-1]) / self.base_env)
```

##### 2. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L254) (Line 254)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L254
- **Target Call:** `fs.ls`
- **Context:** `OmegaConfigLoader.__getitem__`
- **Arguments:** `''`
- **Keywords:** `{'detail': 'False'}`

```python
            env_path = str(Path(self._fs.ls("", detail=False)[-1]) / run_env)
```

##### 3. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L323) (Line 323)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L323
- **Target Call:** `fs.ls`
- **Context:** `OmegaConfigLoader.load_and_merge_dir_config`
- **Arguments:** `conf_path`
- **Keywords:** `{}`

```python
                self._fs.ls(conf_path)
```

</details>

#### <a id="kedro-org-kedro-fs-isdir"></a>🔹 `fs.isdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.isdir</code> in kedro-org/kedro</b></summary>

##### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L330) (Line 330)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L330
- **Target Call:** `fs.isdir`
- **Context:** `OmegaConfigLoader.load_and_merge_dir_config`
- **Arguments:** `Path(conf_path).as_posix()`
- **Keywords:** `{}`

```python
        elif not self._fs.isdir(Path(conf_path).as_posix()):
```

</details>

#### <a id="kedro-org-kedro-fs-glob"></a>🔹 `fs.glob` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.glob</code> in kedro-org/kedro</b></summary>

##### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L338) (Line 338)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L338
- **Target Call:** `fs.glob`
- **Context:** `OmegaConfigLoader.load_and_merge_dir_config`
- **Arguments:** `Path(f'{conf_path!s}/{pattern}').as_posix()`
- **Keywords:** `{}`

```python
            for each in self._fs.glob(Path(f"{conf_path!s}/{pattern}").as_posix()):
```

</details>

#### <a id="kedro-org-kedro-fs-open"></a>🔹 `fs.open` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.open</code> in kedro-org/kedro</b></summary>

##### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L350) (Line 350)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L350
- **Target Call:** `fs.open`
- **Context:** `OmegaConfigLoader.load_and_merge_dir_config`
- **Arguments:** `str(config_filepath.as_posix())`
- **Keywords:** `{}`

```python
                with self._fs.open(str(config_filepath.as_posix())) as open_config:
```

</details>

#### <a id="kedro-org-kedro-f-read"></a>🔹 `f.read` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.read</code> in kedro-org/kedro</b></summary>

##### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L353) (Line 353)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L353
- **Target Call:** `f.read`
- **Context:** `OmegaConfigLoader.load_and_merge_dir_config`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    tmp_fo = io.StringIO(open_config.read().decode("utf8"))
```

</details>

#### <a id="kedro-org-kedro-fs-isfile"></a>🔹 `fs.isfile` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.isfile</code> in kedro-org/kedro</b></summary>

##### 1. [kedro/config/omegaconf_config.py](https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L453) (Line 453)
- **Line Link:** https://github.com/kedro-org/kedro/blob/main/kedro/config/omegaconf_config.py#L453
- **Target Call:** `fs.isfile`
- **Context:** `OmegaConfigLoader._is_valid_config_path`
- **Arguments:** `str(posix_path)`
- **Keywords:** `{}`

```python
        return self._fs.isfile(str(posix_path)) and path.suffix in [
```

</details>

### [pytorch/torchtitan](https://github.com/pytorch/torchtitan)
- **Files Scanned:** `317` | **Files with Usages:** `5` | **Total Usages:** `18`

#### <a id="pytorch-torchtitan-fs-join"></a>🔹 `fs.join` (8 occurrences)

<details open>
<summary><b>Click to expand/collapse 8 occurrences for <code>fs.join</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L168) (Line 168)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L168
- **Target Call:** `fs.join`
- **Context:** `CheckpointManager.__init__`
- **Arguments:** `base_folder, config.folder`
- **Keywords:** `{}`

```python
        self.folder = filesystem.join(base_folder, config.folder)
```

##### 2. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L700) (Line 700)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L700
- **Target Call:** `fs.join`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `folder, filename`
- **Keywords:** `{}`

```python
            checkpoint_path = filesystem.join(folder, filename)
```

##### 3. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L701) (Line 701)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L701
- **Target Call:** `fs.join`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `checkpoint_path, '.metadata'`
- **Keywords:** `{}`

```python
            is_dcp = self._storage.isfile(filesystem.join(checkpoint_path, ".metadata"))
```

##### 4. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L703) (Line 703)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L703
- **Target Call:** `fs.join`
- **Context:** `CheckpointManager._find_load_step`
- **Arguments:** `checkpoint_path, 'model.safetensors.index.json'`
- **Keywords:** `{}`

```python
                filesystem.join(checkpoint_path, "model.safetensors.index.json")
```

##### 5. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L715) (Line 715)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L715
- **Target Call:** `fs.join`
- **Context:** `CheckpointManager._create_checkpoint_id`
- **Arguments:** `folder, f'step-{step}'`
- **Keywords:** `{}`

```python
        return filesystem.join(folder, f"step-{step}")
```

##### 6. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L845) (Line 845)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L845
- **Target Call:** `fs.join`
- **Context:** `CheckpointManager._purge_stale_checkpoints`
- **Arguments:** `self.folder, filename`
- **Keywords:** `{}`

```python
                    path = filesystem.join(self.folder, filename)
```

##### 7. [torchtitan/components/checkpointer/torch_checkpointing.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/torch_checkpointing.py#L143) (Line 143)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/torch_checkpointing.py#L143
- **Target Call:** `fs.join`
- **Context:** `TorchCheckpointingManager.__init__`
- **Arguments:** `base_folder, config.folder`
- **Keywords:** `{}`

```python
        self.folder = filesystem.join(base_folder, config.folder)
```

##### 8. [torchtitan/experiments/torchft/checkpoint.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/experiments/torchft/checkpoint.py#L202) (Line 202)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/experiments/torchft/checkpoint.py#L202
- **Target Call:** `fs.join`
- **Context:** `TorchFTCheckpointManager._ft_folder`
- **Arguments:** `self.folder, f'ft-replicat-{self.ft_replica_id}'`
- **Keywords:** `{}`

```python
        return filesystem.join(self.folder, f"ft-replicat-{self.ft_replica_id}")
```

</details>

#### <a id="pytorch-torchtitan-fs-isdir"></a>🔹 `fs.isdir` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.isdir</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L77) (Line 77)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L77
- **Target Call:** `fs.isdir`
- **Context:** `_FilesystemCheckpointStorage.isdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return filesystem.isdir(path)
```

##### 2. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L53) (Line 53)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L53
- **Target Call:** `fs.isdir`
- **Context:** `isdir`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        return fs.isdir(p)
```

</details>

#### <a id="pytorch-torchtitan-fs-isfile"></a>🔹 `fs.isfile` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.isfile</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L80) (Line 80)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L80
- **Target Call:** `fs.isfile`
- **Context:** `_FilesystemCheckpointStorage.isfile`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return filesystem.isfile(path)
```

##### 2. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L60) (Line 60)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L60
- **Target Call:** `fs.isfile`
- **Context:** `isfile`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        return fs.isfile(p)
```

</details>

#### <a id="pytorch-torchtitan-fs-listdir"></a>🔹 `fs.listdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.listdir</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/components/checkpointer/dcp.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L83) (Line 83)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/checkpointer/dcp.py#L83
- **Target Call:** `fs.listdir`
- **Context:** `_FilesystemCheckpointStorage.listdir`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return filesystem.listdir(path)
```

</details>

#### <a id="pytorch-torchtitan-fs-close"></a>🔹 `fs.close` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.close</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/experiments/rl/observability/metrics/processor.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/experiments/rl/observability/metrics/processor.py#L222) (Line 222)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/experiments/rl/observability/metrics/processor.py#L222
- **Target Call:** `fs.close`
- **Context:** `MetricsProcessor.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                backend.close()
```

</details>

#### <a id="pytorch-torchtitan-url-to-fs"></a>🔹 `url_to_fs` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>url_to_fs</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L40) (Line 40)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L40
- **Target Call:** `url_to_fs`
- **Context:** `_resolve`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    return url_to_fs(path)
```

</details>

#### <a id="pytorch-torchtitan-fs-exists"></a>🔹 `fs.exists` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.exists</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L46) (Line 46)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L46
- **Target Call:** `fs.exists`
- **Context:** `exists`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
        return fs.exists(p)
```

</details>

#### <a id="pytorch-torchtitan-fs-ls"></a>🔹 `fs.ls` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.ls</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L81) (Line 81)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L81
- **Target Call:** `fs.ls`
- **Context:** `listdir`
- **Arguments:** `p`
- **Keywords:** `{'detail': 'False'}`

```python
            for entry in fs.ls(p, detail=False)
```

</details>

#### <a id="pytorch-torchtitan-fs-rm"></a>🔹 `fs.rm` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.rm</code> in pytorch/torchtitan</b></summary>

##### 1. [torchtitan/tools/filesystem.py](https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L94) (Line 94)
- **Line Link:** https://github.com/pytorch/torchtitan/blob/main/torchtitan/tools/filesystem.py#L94
- **Target Call:** `fs.rm`
- **Context:** `rmtree`
- **Arguments:** `p`
- **Keywords:** `{'recursive': 'True'}`

```python
            fs.rm(p, recursive=True)
```

</details>

### [delta-io/delta-rs](https://github.com/delta-io/delta-rs)
- **Files Scanned:** `18` | **Files with Usages:** `0` | **Total Usages:** `0`

No direct filesystem / fsspec usages detected in this target.

### [zarr-developers/zarr-python](https://github.com/zarr-developers/zarr-python)
- **Files Scanned:** `173` | **Files with Usages:** `2` | **Total Usages:** `8`

#### <a id="zarr-developers-zarr-python-f-tell"></a>🔹 `f.tell` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>f.tell</code> in zarr-developers/zarr-python</b></summary>

##### 1. [src/zarr/storage/_zip.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L48) (Line 48)
- **Line Link:** https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L48
- **Target Call:** `f.tell`
- **Context:** `_RawReaderAdapter._get_size`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            pos = self._fileobj.tell()
```

##### 2. [src/zarr/storage/_zip.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L63) (Line 63)
- **Line Link:** https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L63
- **Target Call:** `f.tell`
- **Context:** `_RawReaderAdapter.tell`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return self._fileobj.tell()
```

##### 3. [src/zarr/storage/_zip.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L66) (Line 66)
- **Line Link:** https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L66
- **Target Call:** `f.tell`
- **Context:** `_RawReaderAdapter.readinto`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        n_requested = min(len(b), self._get_size() - self._fileobj.tell())
```

</details>

#### <a id="zarr-developers-zarr-python-f-seek"></a>🔹 `f.seek` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>f.seek</code> in zarr-developers/zarr-python</b></summary>

##### 1. [src/zarr/storage/_zip.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L49) (Line 49)
- **Line Link:** https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L49
- **Target Call:** `f.seek`
- **Context:** `_RawReaderAdapter._get_size`
- **Arguments:** `0, os.SEEK_END`
- **Keywords:** `{}`

```python
            self._size = self._fileobj.seek(0, os.SEEK_END)
```

##### 2. [src/zarr/storage/_zip.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L50) (Line 50)
- **Line Link:** https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L50
- **Target Call:** `f.seek`
- **Context:** `_RawReaderAdapter._get_size`
- **Arguments:** `pos`
- **Keywords:** `{}`

```python
            self._fileobj.seek(pos)
```

##### 3. [src/zarr/storage/_zip.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L60) (Line 60)
- **Line Link:** https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L60
- **Target Call:** `f.seek`
- **Context:** `_RawReaderAdapter.seek`
- **Arguments:** `pos, whence`
- **Keywords:** `{}`

```python
        return self._fileobj.seek(pos, whence)
```

</details>

#### <a id="zarr-developers-zarr-python-url-to-fs"></a>🔹 `url_to_fs` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>url_to_fs</code> in zarr-developers/zarr-python</b></summary>

##### 1. [src/zarr/storage/_fsspec.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L253) (Line 253)
- **Line Link:** https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_fsspec.py#L253
- **Target Call:** `url_to_fs`
- **Context:** `FsspecStore.from_url`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
        fs, path = url_to_fs(url, **opts)
```

</details>

#### <a id="zarr-developers-zarr-python-f-read"></a>🔹 `f.read` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.read</code> in zarr-developers/zarr-python</b></summary>

##### 1. [src/zarr/storage/_zip.py](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L69) (Line 69)
- **Line Link:** https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/storage/_zip.py#L69
- **Target Call:** `f.read`
- **Context:** `_RawReaderAdapter.readinto`
- **Arguments:** `n_requested`
- **Keywords:** `{}`

```python
        data = self._fileobj.read(n_requested)
```

</details>

### [intake/intake](https://github.com/intake/intake)
- **Files Scanned:** `52` | **Files with Usages:** `11` | **Total Usages:** `106`

#### <a id="intake-intake-fs-open"></a>🔹 `fs.open` (45 occurrences)

<details open>
<summary><b>Click to expand/collapse 45 occurrences for <code>fs.open</code> in intake/intake</b></summary>

##### 1. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L644) (Line 644)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/catalog/local.py#L644
- **Target Call:** `fs.open`
- **Context:** `YAMLFileCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
                file_open = self.filesystem.open(self.path, mode="rb")
```

##### 2. [intake/readers/catalogs.py](https://github.com/intake/intake/blob/master/intake/readers/catalogs.py#L376) (Line 376)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/catalogs.py#L376
- **Target Call:** `fs.open`
- **Context:** `STACIndex._read`
- **Arguments:** `'https://stacindex.org/api/catalogs'`
- **Keywords:** `{}`

```python
        with fsspec.open("https://stacindex.org/api/catalogs") as f:
```

##### 3. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L420) (Line 420)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/entry.py#L420
- **Target Call:** `fs.open`
- **Context:** `Catalog.to_yaml_file`
- **Arguments:** `path`
- **Keywords:** `{'mode': "'wt'"}`

```python
        with fsspec.open(path, mode="wt", **storage_options) as stream:
```

##### 4. [intake/readers/entry.py](https://github.com/intake/intake/blob/master/intake/readers/entry.py#L432) (Line 432)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/entry.py#L432
- **Target Call:** `fs.open`
- **Context:** `Catalog.from_yaml_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        of = fsspec.open(path, **storage_options)
```

##### 5. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L125) (Line 125)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/output.py#L125
- **Target Call:** `fs.open`
- **Context:** `NumpyToNumpyFile.run`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
            with fsspec.open(path, **storage_options) as f:
```

##### 6. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L158) (Line 158)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/output.py#L158
- **Target Call:** `fs.open`
- **Context:** `MatplotlibToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
```

##### 7. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L293) (Line 293)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/output.py#L293
- **Target Call:** `fs.open`
- **Context:** `NumpyToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
```

##### 8. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L320) (Line 320)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/output.py#L320
- **Target Call:** `fs.open`
- **Context:** `NumpyToTIFF.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
            with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
```

##### 9. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L337) (Line 337)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/output.py#L337
- **Target Call:** `fs.open`
- **Context:** `PILImageToPNG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
```

##### 10. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L353) (Line 353)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/output.py#L353
- **Target Call:** `fs.open`
- **Context:** `PILImageToJPEG.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
```

##### 11. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L368) (Line 368)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/output.py#L368
- **Target Call:** `fs.open`
- **Context:** `PILImageToTIFF.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
        with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
```

##### 12. [intake/readers/output.py](https://github.com/intake/intake/blob/master/intake/readers/output.py#L402) (Line 402)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/output.py#L402
- **Target Call:** `fs.open`
- **Context:** `NumpyToWAV.run`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'"}`

```python
            with fsspec.open(url, mode="wb", **(storage_options or {})) as f:
```

##### 13. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L923) (Line 923)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L923
- **Target Call:** `fs.open`
- **Context:** `SKLearnModelReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
```

##### 14. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1044) (Line 1044)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1044
- **Target Call:** `fs.open`
- **Context:** `PandasHDF5._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
            with fsspec.open(data.url, "rb", **data.storage_options) as f:
```

##### 15. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1286) (Line 1286)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1286
- **Target Call:** `fs.open`
- **Context:** `PythonModule._read`
- **Arguments:** `data.url, 'rt'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rt", **(data.storage_options or {})) as f:
```

##### 16. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1318) (Line 1318)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1318
- **Target Call:** `fs.open`
- **Context:** `NumpyText._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            with fsspec.open(data.url, **(data.storage_options or {})) as f:
```

##### 17. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1436) (Line 1436)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1436
- **Target Call:** `fs.open`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    f = fsspec.open(data.url, **(data.storage_options or {})).open()
```

##### 18. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1436) (Line 1436)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1436
- **Target Call:** `fs.open`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
                    f = fsspec.open(data.url, **(data.storage_options or {})).open()
```

##### 19. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1578) (Line 1578)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1578
- **Target Call:** `fs.open`
- **Context:** `GeoPandasReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            with fsspec.open(data.url, **(data.storage_options or {})) as f:
```

##### 20. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1600) (Line 1600)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1600
- **Target Call:** `fs.open`
- **Context:** `ScipyMatrixMarketReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, **data.storage_options) as f:
```

##### 21. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1612) (Line 1612)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1612
- **Target Call:** `fs.open`
- **Context:** `NibabelNiftiReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
```

##### 22. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1639) (Line 1639)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1639
- **Target Call:** `fs.open`
- **Context:** `ASDFReader._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
```

##### 23. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1639) (Line 1639)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1639
- **Target Call:** `fs.open`
- **Context:** `ASDFReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
```

##### 24. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1653) (Line 1653)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1653
- **Target Call:** `fs.open`
- **Context:** `DicomReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, **(data.storage_options or {})) as f:
```

##### 25. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1683) (Line 1683)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1683
- **Target Call:** `fs.open`
- **Context:** `PMTileReader._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
```

##### 26. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1683) (Line 1683)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1683
- **Target Call:** `fs.open`
- **Context:** `PMTileReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
```

##### 27. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1889) (Line 1889)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1889
- **Target Call:** `fs.open`
- **Context:** `GeoPandasTabular._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
```

##### 28. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1889) (Line 1889)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1889
- **Target Call:** `fs.open`
- **Context:** `GeoPandasTabular._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
            f = fsspec.open(data.url, **(data.storage_options or {})).open()
```

##### 29. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1971) (Line 1971)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1971
- **Target Call:** `fs.open`
- **Context:** `MessagePackReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 30. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1998) (Line 1998)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1998
- **Target Call:** `fs.open`
- **Context:** `MarkdownReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
```

##### 31. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2005) (Line 2005)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2005
- **Target Call:** `fs.open`
- **Context:** `MarkdownReader.discover`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 32. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2036) (Line 2036)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2036
- **Target Call:** `fs.open`
- **Context:** `TOMLReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 33. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2081) (Line 2081)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2081
- **Target Call:** `fs.open`
- **Context:** `INIReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
```

##### 34. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2113) (Line 2113)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2113
- **Target Call:** `fs.open`
- **Context:** `PDFTextReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 35. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2251) (Line 2251)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2251
- **Target Call:** `fs.open`
- **Context:** `PILImageReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 36. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2468) (Line 2468)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2468
- **Target Call:** `fs.open`
- **Context:** `BioPythonFASTAReader._read`
- **Arguments:** `data.url, 'r'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "r", **(data.storage_options or {})) as f:
```

##### 37. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2664) (Line 2664)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2664
- **Target Call:** `fs.open`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 38. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2751) (Line 2751)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2751
- **Target Call:** `fs.open`
- **Context:** `PMTilesMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 39. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2847) (Line 2847)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2847
- **Target Call:** `fs.open`
- **Context:** `OSMPBFMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 40. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2980) (Line 2980)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2980
- **Target Call:** `fs.open`
- **Context:** `SKLearnModelMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 41. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3073) (Line 3073)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3073
- **Target Call:** `fs.open`
- **Context:** `TorchModelMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as raw_f:
```

##### 42. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3135) (Line 3135)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3135
- **Target Call:** `fs.open`
- **Context:** `JoblibMetadataReader._read`
- **Arguments:** `data.url, 'rb'`
- **Keywords:** `{}`

```python
        with fsspec.open(data.url, "rb", **(data.storage_options or {})) as f:
```

##### 43. [intake/readers/search.py](https://github.com/intake/intake/blob/master/intake/readers/search.py#L126) (Line 126)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/search.py#L126
- **Target Call:** `fs.open`
- **Context:** `EnvironmentSatisfied._is_consistent`
- **Arguments:** `env, 'rt'`
- **Keywords:** `{}`

```python
                with fsspec.open(env, "rt") as f:
```

##### 44. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L74) (Line 74)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L74
- **Target Call:** `fs.open`
- **Context:** `JSONFileSource.read`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': 'self.mode', 'encoding': 'self.encoding', 'compression': 'self.compression'}`

```python
        with fsspec.open(
            urlpath,
            mode=self.mode,
            encoding=self.encoding,
            compression=self.compression,
            **self._storage_options,
        ) as f:
```

##### 45. [intake/source/jsonfiles.py](https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L157) (Line 157)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/source/jsonfiles.py#L157
- **Target Call:** `fs.open`
- **Context:** `JSONLinesFileSource._open`
- **Arguments:** `urlpath`
- **Keywords:** `{'mode': 'self.mode', 'encoding': 'self.encoding', 'compression': 'self.compression'}`

```python
        with fsspec.open(
            urlpath,
            mode=self.mode,
            encoding=self.encoding,
            compression=self.compression,
            **self._storage_options,
        ) as f:
```

</details>

#### <a id="intake-intake-f-read"></a>🔹 `f.read` (22 occurrences)

<details open>
<summary><b>Click to expand/collapse 22 occurrences for <code>f.read</code> in intake/intake</b></summary>

##### 1. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1288) (Line 1288)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1288
- **Target Call:** `f.read`
- **Context:** `PythonModule._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            exec(f.read(), mod.__dict__)
```

##### 2. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1687) (Line 1687)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1687
- **Target Call:** `f.read`
- **Context:** `PMTileReader.get_bytes`
- **Arguments:** `length`
- **Keywords:** `{}`

```python
                return f.read(length)
```

##### 3. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1999) (Line 1999)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1999
- **Target Call:** `f.read`
- **Context:** `MarkdownReader._read`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            return f.read()
```

##### 4. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2006) (Line 2006)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2006
- **Target Call:** `f.read`
- **Context:** `MarkdownReader.discover`
- **Arguments:** `head_bytes`
- **Keywords:** `{}`

```python
            raw = f.read(head_bytes)
```

##### 5. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2665) (Line 2665)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2665
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `24`
- **Keywords:** `{}`

```python
            header = f.read(24)
```

##### 6. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2677) (Line 2677)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2677
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `8`
- **Keywords:** `{}`

```python
                    key_len = struct.unpack("<Q", f.read(8))[0]
```

##### 7. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2678) (Line 2678)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2678
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `key_len`
- **Keywords:** `{}`

```python
                    key = f.read(key_len).decode("utf-8", errors="replace")
```

##### 8. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2680) (Line 2680)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2680
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `4`
- **Keywords:** `{}`

```python
                    val_type = struct.unpack("<I", f.read(4))[0]
```

##### 9. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2696) (Line 2696)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2696
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `8`
- **Keywords:** `{}`

```python
                        slen = struct.unpack("<Q", f.read(8))[0]
```

##### 10. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2697) (Line 2697)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2697
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `slen`
- **Keywords:** `{}`

```python
                        val = f.read(slen).decode("utf-8", errors="replace")
```

##### 11. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2699) (Line 2699)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2699
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `4`
- **Keywords:** `{}`

```python
                        arr_type = struct.unpack("<I", f.read(4))[0]
```

##### 12. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2700) (Line 2700)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2700
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `8`
- **Keywords:** `{}`

```python
                        arr_len = struct.unpack("<Q", f.read(8))[0]
```

##### 13. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2704) (Line 2704)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2704
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `8`
- **Keywords:** `{}`

```python
                                slen = struct.unpack("<Q", f.read(8))[0]
```

##### 14. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2705) (Line 2705)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2705
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `slen`
- **Keywords:** `{}`

```python
                                f.read(slen)
```

##### 15. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2707) (Line 2707)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2707
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `scalar[1] * arr_len`
- **Keywords:** `{}`

```python
                            f.read(scalar[1] * arr_len)
```

##### 16. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2713) (Line 2713)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2713
- **Target Call:** `f.read`
- **Context:** `GGUFMetadataReader._read`
- **Arguments:** `sz`
- **Keywords:** `{}`

```python
                        val = struct.unpack(fmt, f.read(sz))[0]
```

##### 17. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2752) (Line 2752)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2752
- **Target Call:** `f.read`
- **Context:** `PMTilesMetadataReader._read`
- **Arguments:** `127`
- **Keywords:** `{}`

```python
            raw = f.read(127)
```

##### 18. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2849) (Line 2849)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2849
- **Target Call:** `f.read`
- **Context:** `OSMPBFMetadataReader._read`
- **Arguments:** `4`
- **Keywords:** `{}`

```python
            header_size_raw = f.read(4)
```

##### 19. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2853) (Line 2853)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2853
- **Target Call:** `f.read`
- **Context:** `OSMPBFMetadataReader._read`
- **Arguments:** `header_size`
- **Keywords:** `{}`

```python
            blob_header_bytes = f.read(header_size)
```

##### 20. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2855) (Line 2855)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2855
- **Target Call:** `f.read`
- **Context:** `OSMPBFMetadataReader._read`
- **Arguments:** `4`
- **Keywords:** `{}`

```python
            blob_size_raw = f.read(4)
```

##### 21. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2859) (Line 2859)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L2859
- **Target Call:** `f.read`
- **Context:** `OSMPBFMetadataReader._read`
- **Arguments:** `min(blob_size, 32768)`
- **Keywords:** `{}`

```python
            blob_bytes = f.read(min(blob_size, 32768))  # cap at 32 KB
```

##### 22. [intake/readers/search.py](https://github.com/intake/intake/blob/master/intake/readers/search.py#L127) (Line 127)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/search.py#L127
- **Target Call:** `f.read`
- **Context:** `EnvironmentSatisfied._is_consistent`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    env = f.read()
```

</details>

#### <a id="intake-intake-open-files"></a>🔹 `open_files` (6 occurrences)

<details open>
<summary><b>Click to expand/collapse 6 occurrences for <code>open_files</code> in intake/intake</b></summary>

##### 1. [intake/catalog/base.py](https://github.com/intake/intake/blob/master/intake/catalog/base.py#L341) (Line 341)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/catalog/base.py#L341
- **Target Call:** `open_files`
- **Context:** `Catalog.save`
- **Arguments:** `[url]`
- **Keywords:** `{'mode': "'wt'"}`

```python
        with open_files([url], **(storage_options or {}), mode="wt")[0] as f:
```

##### 2. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L639) (Line 639)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/catalog/local.py#L639
- **Target Call:** `open_files`
- **Context:** `YAMLFileCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
                file_open = open_files(self.path, mode="rb", **options)
```

##### 3. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L690) (Line 690)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/catalog/local.py#L690
- **Target Call:** `open_files`
- **Context:** `YAMLFileCatalog.add`
- **Arguments:** `[self.path]`
- **Keywords:** `{'mode': "'wt'"}`

```python
            file_open = open_files([self.path], mode="wt", **options)
```

##### 4. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L693) (Line 693)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/catalog/local.py#L693
- **Target Call:** `open_files`
- **Context:** `YAMLFileCatalog.add`
- **Arguments:** `[path]`
- **Keywords:** `{'mode': "'wt'"}`

```python
            file_open = open_files([path], mode="wt", **options)
```

##### 5. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L805) (Line 805)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/catalog/local.py#L805
- **Target Call:** `open_files`
- **Context:** `YAMLFilesCatalog._load`
- **Arguments:** `p`
- **Keywords:** `{'mode': "'rb'"}`

```python
            files = sum([open_files(p, mode="rb", **options) for p in self.path], [])
```

##### 6. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L812) (Line 812)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/catalog/local.py#L812
- **Target Call:** `open_files`
- **Context:** `YAMLFilesCatalog._load`
- **Arguments:** `self.path`
- **Keywords:** `{'mode': "'rb'"}`

```python
            files = open_files(self.path, mode="rb", **options)
```

</details>

#### <a id="intake-intake-url-to-fs"></a>🔹 `url_to_fs` (6 occurrences)

<details open>
<summary><b>Click to expand/collapse 6 occurrences for <code>url_to_fs</code> in intake/intake</b></summary>

##### 1. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1926) (Line 1926)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1926
- **Target Call:** `url_to_fs`
- **Context:** `recommend`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
            fs, url2 = fsspec.core.url_to_fs(url, **(storage_options or {}))
```

##### 2. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1931) (Line 1931)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1931
- **Target Call:** `url_to_fs`
- **Context:** `recommend`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
            fs, url2 = fsspec.core.url_to_fs(url, **(storage_options or {}))
```

##### 3. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L711) (Line 711)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L711
- **Target Call:** `url_to_fs`
- **Context:** `_file_storage_info`
- **Arguments:** `u`
- **Keywords:** `{}`

```python
                fs, path = fsspec.core.url_to_fs(u, **(storage_options or {}))
```

##### 4. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L714) (Line 714)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L714
- **Target Call:** `url_to_fs`
- **Context:** `_file_storage_info`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
            fs, path = fsspec.core.url_to_fs(url, **(storage_options or {}))
```

##### 5. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L263) (Line 263)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L263
- **Target Call:** `url_to_fs`
- **Context:** `FileReader._sniff_head`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
            _fs, url2 = fsspec.core.url_to_fs(url, **storage_options)
```

##### 6. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L693) (Line 693)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L693
- **Target Call:** `url_to_fs`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `f'simplecache::{data.url}'`
- **Keywords:** `{}`

```python
        fs, path = fsspec.core.url_to_fs(f"simplecache::{data.url}", **options)
```

</details>

#### <a id="intake-intake-fsspec-filesystem"></a>🔹 `fsspec.filesystem` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fsspec.filesystem</code> in intake/intake</b></summary>

##### 1. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L55) (Line 55)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L55
- **Target Call:** `fsspec.filesystem`
- **Context:** `FileSelector.__init__`
- **Arguments:** `'file'`
- **Keywords:** `{}`

```python
        self.fs = fsspec.filesystem("file")
```

##### 2. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L94) (Line 94)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L94
- **Target Call:** `fsspec.filesystem`
- **Context:** `FileSelector.go_clicked`
- **Arguments:** `self.protocol.value`
- **Keywords:** `{}`

```python
        self.fs = fsspec.filesystem(
            self.protocol.value, **ast.literal_eval(self.storage_options.value)
        )
```

##### 3. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L993) (Line 993)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L993
- **Target Call:** `fsspec.filesystem`
- **Context:** `HandleToUrlReader._extract`
- **Arguments:** `'http'`
- **Keywords:** `{}`

```python
        h = fsspec.filesystem("http")
```

##### 4. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1006) (Line 1006)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1006
- **Target Call:** `fsspec.filesystem`
- **Context:** `HandleToUrlReader._read`
- **Arguments:** `'http'`
- **Keywords:** `{}`

```python
        h = fsspec.filesystem("http")
```

</details>

#### <a id="intake-intake-fs-open-local"></a>🔹 `fs.open_local` (4 occurrences)

<details open>
<summary><b>Click to expand/collapse 4 occurrences for <code>fs.open_local</code> in intake/intake</b></summary>

##### 1. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L736) (Line 736)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L736
- **Target Call:** `fs.open_local`
- **Context:** `LlamaServerReader._read`
- **Arguments:** `f'simplecache::{v}'`
- **Keywords:** `{}`

```python
                path = fsspec.open_local(f"simplecache::{v}")
```

##### 2. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1415) (Line 1415)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1415
- **Target Call:** `fs.open_local`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
                ofs = fsspec.open_local(data.url, **(data.storage_options or {}))
```

##### 3. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1433) (Line 1433)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1433
- **Target Call:** `fs.open_local`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
                    f = fsspec.open_local(data.url, **(data.storage_options or {}))
```

##### 4. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3513) (Line 3513)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L3513
- **Target Call:** `fs.open_local`
- **Context:** `_as_local`
- **Arguments:** `f'simplecache::{url}'`
- **Keywords:** `{}`

```python
        return fsspec.open_local(
            f"simplecache::{url}", **{"simplecache": {}, **(data.storage_options or {})}
        )
```

</details>

#### <a id="intake-intake-fs-ls"></a>🔹 `fs.ls` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.ls</code> in intake/intake</b></summary>

##### 1. [intake/interface/catalog/add.py](https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L121) (Line 121)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/interface/catalog/add.py#L121
- **Target Call:** `fs.ls`
- **Context:** `FileSelector.make_options`
- **Arguments:** `self.path, True`
- **Keywords:** `{}`

```python
            for f in self.fs.ls(self.path, True):
```

##### 2. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1991) (Line 1991)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1991
- **Target Call:** `fs.ls`
- **Context:** `recommend`
- **Arguments:** `url`
- **Keywords:** `{'detail': 'False'}`

```python
                allfiles = fs.ls(url, detail=False)
```

##### 3. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L699) (Line 699)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L699
- **Target Call:** `fs.ls`
- **Context:** `_resolve_to_files`
- **Arguments:** `path.rstrip('/')`
- **Keywords:** `{'detail': 'True'}`

```python
                children = fs.ls(path.rstrip("/"), detail=True)
```

</details>

#### <a id="intake-intake-fs-info"></a>🔹 `fs.info` (3 occurrences)

<details open>
<summary><b>Click to expand/collapse 3 occurrences for <code>fs.info</code> in intake/intake</b></summary>

##### 1. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1927) (Line 1927)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1927
- **Target Call:** `fs.info`
- **Context:** `recommend`
- **Arguments:** `url2`
- **Keywords:** `{'refresh': 'True'}`

```python
            mime = mime or fs.info(url2, refresh=True).get("ContentType", None)
```

##### 2. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L684) (Line 684)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L684
- **Target Call:** `fs.info`
- **Context:** `_resolve_to_files`
- **Arguments:** `p`
- **Keywords:** `{}`

```python
                return [fs.info(p) for p in expanded]
```

##### 3. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L688) (Line 688)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L688
- **Target Call:** `fs.info`
- **Context:** `_resolve_to_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                entry = fs.info(path)
```

</details>

#### <a id="intake-intake-fs-cat-file"></a>🔹 `fs.cat_file` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.cat_file</code> in intake/intake</b></summary>

##### 1. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1932) (Line 1932)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1932
- **Target Call:** `fs.cat_file`
- **Context:** `recommend`
- **Arguments:** `url2[0] if isinstance(url2, list) else url2`
- **Keywords:** `{'end': '2 ** 20'}`

```python
            head = fs.cat_file(url2[0] if isinstance(url2, list) else url2, end=2**20)
```

##### 2. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L264) (Line 264)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L264
- **Target Call:** `fs.cat_file`
- **Context:** `FileReader._sniff_head`
- **Arguments:** `url2`
- **Keywords:** `{'start': '0', 'end': 'nbytes'}`

```python
            head = _fs.cat_file(url2, start=0, end=nbytes)
```

</details>

#### <a id="intake-intake-fs-cat"></a>🔹 `fs.cat` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.cat</code> in intake/intake</b></summary>

##### 1. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1000) (Line 1000)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1000
- **Target Call:** `fs.cat`
- **Context:** `HandleToUrlReader._extract`
- **Arguments:** `[f"{base}/{u.lstrip('hdl:/')}" for u in ids]`
- **Keywords:** `{}`

```python
            rr = h.cat([f"{base}/{u.lstrip('hdl:/')}" for u in ids])
```

##### 2. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1007) (Line 1007)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1007
- **Target Call:** `fs.cat`
- **Context:** `HandleToUrlReader._read`
- **Arguments:** `f"{base}/{data.url.lstrip('hdl:/')}"`
- **Keywords:** `{}`

```python
        r = h.cat(f"{base}/{data.url.lstrip('hdl:/')}")
```

</details>

#### <a id="intake-intake-fs-open-files"></a>🔹 `fs.open_files` (2 occurrences)

<details open>
<summary><b>Click to expand/collapse 2 occurrences for <code>fs.open_files</code> in intake/intake</b></summary>

##### 1. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1419) (Line 1419)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1419
- **Target Call:** `fs.open_files`
- **Context:** `XArrayDatasetReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
                ofs0 = fsspec.open_files(data.url, **(data.storage_options or {}))
```

##### 2. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1513) (Line 1513)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1513
- **Target Call:** `fs.open_files`
- **Context:** `RasterIOXarrayReader._read`
- **Arguments:** `data.url`
- **Keywords:** `{}`

```python
        ofs = fsspec.open_files(data.url, **(data.storage_options or {}))
```

</details>

#### <a id="intake-intake-get-filesystem-class"></a>🔹 `get_filesystem_class` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>get_filesystem_class</code> in intake/intake</b></summary>

##### 1. [intake/catalog/local.py](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L576) (Line 576)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/catalog/local.py#L576
- **Target Call:** `get_filesystem_class`
- **Context:** `get_dir`
- **Arguments:** `protocol`
- **Keywords:** `{}`

```python
        out = get_filesystem_class(protocol)._parent(path)
```

</details>

#### <a id="intake-intake-fs-isdir"></a>🔹 `fs.isdir` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.isdir</code> in intake/intake</b></summary>

##### 1. [intake/readers/datatypes.py](https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1989) (Line 1989)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/datatypes.py#L1989
- **Target Call:** `fs.isdir`
- **Context:** `recommend`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
        if fs is not None and fs.isdir(url):
```

</details>

#### <a id="intake-intake-fs-glob"></a>🔹 `fs.glob` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.glob</code> in intake/intake</b></summary>

##### 1. [intake/readers/inspect.py](https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L681) (Line 681)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/inspect.py#L681
- **Target Call:** `fs.glob`
- **Context:** `_resolve_to_files`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
                expanded = fs.glob(path)
```

</details>

#### <a id="intake-intake-fs-get-file"></a>🔹 `fs.get_file` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>fs.get_file</code> in intake/intake</b></summary>

##### 1. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L702) (Line 702)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L702
- **Target Call:** `fs.get_file`
- **Context:** `LlamaServerReader._local_model_path`
- **Arguments:** `path, cached_fn`
- **Keywords:** `{'callback': 'callback'}`

```python
        fs.fs.get_file(path, cached_fn, callback=callback)
```

</details>

#### <a id="intake-intake-get-fs-token-paths"></a>🔹 `get_fs_token_paths` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>get_fs_token_paths</code> in intake/intake</b></summary>

##### 1. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1480) (Line 1480)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1480
- **Target Call:** `get_fs_token_paths`
- **Context:** `XArrayPatternReader._read`
- **Arguments:** `url`
- **Keywords:** `{}`

```python
            fs, _, paths = fsspec.get_fs_token_paths(url, **(data.storage_options or {}))
```

</details>

#### <a id="intake-intake-f-seek"></a>🔹 `f.seek` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.seek</code> in intake/intake</b></summary>

##### 1. [intake/readers/readers.py](https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1686) (Line 1686)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/readers.py#L1686
- **Target Call:** `f.seek`
- **Context:** `PMTileReader.get_bytes`
- **Arguments:** `offset`
- **Keywords:** `{}`

```python
                f.seek(offset)
```

</details>

#### <a id="intake-intake-f-write"></a>🔹 `f.write` (1 occurrence)

<details open>
<summary><b>Click to expand/collapse 1 occurrence for <code>f.write</code> in intake/intake</b></summary>

##### 1. [intake/readers/search.py](https://github.com/intake/intake/blob/master/intake/readers/search.py#L129) (Line 129)
- **Line Link:** https://github.com/intake/intake/blob/master/intake/readers/search.py#L129
- **Target Call:** `f.write`
- **Context:** `EnvironmentSatisfied._is_consistent`
- **Arguments:** `env`
- **Keywords:** `{}`

```python
                f.write(env)
```

</details>
