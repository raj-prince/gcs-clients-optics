# 📦 Downstream Dependency Versions Analysis Report

Evaluated package manifests across **24** repository targets in **269.53s**.

## 📊 Executive Summary

- **Total Storage Package Constraints Found**: `91`

## 📋 Repository Storage Package Version Matrix

| Repository | `fsspec` Version | `gcsfs` Version | `s3fs` Version | `adlfs` Version | `pyarrow` Version |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`GitHub:pytorch/pytorch (main)`** | `>=0.8.5, >=0.8.5` | `—` | `—` | `—` | `—` |
| **`GitHub:pandas-dev/pandas (main)`** | `>=2025.7.0, >=2025.7.0, >=2025.7.0` | `>=2025.7.0, >=2025.7.0, >=2025.7.0` | `>=2025.7.0, >=2025.7.0, >=2025.7.0` | `—` | `= ['pyarrow>=16.0.0'], >=13.0.0, >=13.0.0, >=16.0.0, >=16.0.0,!=24.*` |
| **`GitHub:ray-project/ray (master)`** | `*, ==2023.12.1, ==2023.12.1, *, *` | `—` | `==2023.12.1, ==2023.12.1` | `==2026.4.0, ==2026.4.0` | `>= 17.0.0, ==23.0.1, ==23.0.1, >= 17.0.0` |
| **`GitHub:pola-rs/polars (main)`** | `= ["fsspec"], *` | `—` | `>=2026.2.0` | `—` | `= ["pyarrow >= 7.0.0"], *` |
| **`GitHub:Lightning-AI/pytorch-lightning (main)`** | `—` | `—` | `—` | `—` | `—` |
| **`GitHub:duckdb/duckdb (main)`** | `—` | `—` | `—` | `—` | `—` |
| **`GitHub:huggingface/datasets (main)`** | `>=2023.1.0,<=2026.6.0` | `—` | `—` | `—` | `>=21.0.0, *` |
| **`GitHub:mlflow/mlflow (master)`** | `—` | `—` | `—` | `—` | `*, <26,>=4.0.0, *` |
| **`GitHub:apache/arrow (main)`** | `—` | `—` | `—` | `—` | `*, *, *, *, *` |
| **`GitHub:iterative/dvc (main)`** | `>=2024.2.0` | `—` | `—` | `—` | `—` |
| **`GitHub:dask/dask (main)`** | `>= 2021.09.0` | `—` | `—` | `—` | `>= 16.0` |
| **`great-expectations/great_expectations`** | `—` | `—` | `—` | `—` | `—` |
| **`GitHub:modin-project/modin (main)`** | `>=2022.11.0, >=2022.11.0` | `—` | `>=2022.11.0` | `—` | `>=10.0.1, >=10.0.1` |
| **`GitHub:flyteorg/flyte (main)`** | `—` | `—` | `—` | `—` | `—` |
| **`GitHub:feast-dev/feast (master)`** | `>=2024.1.0, >=2024.1.0` | `—` | `—` | `—` | `>=16.1.0, <21.0.0` |
| **`GitHub:pydata/xarray (main)`** | `*` | `—` | `—` | `—` | `—` |
| **`GitHub:kedro-org/kedro (main)`** | `>=2021.4` | `—` | `>=2021.4,<2026.8` | `—` | `—` |
| **`GitHub:pytorch/torchtitan (main)`** | `—` | `—` | `—` | `—` | `—` |
| **`GitHub:delta-io/delta-rs (main)`** | `—` | `—` | `—` | `—` | `= ["pyarrow>=21"]` |
| **`GitHub:zarr-developers/zarr-python (main)`** | `*, >=2023.10.0, >=2023.10.0, ==2023.10.0, *` | `*` | `>=2023.10.0, >=2023.10.0, ==2023.10.0, *` | `—` | `—` |
| **`GitHub:intake/intake (master)`** | `>=2023.0.0` | `—` | `—` | `—` | `—` |
| **`GitHub:fsspec/s3fs (main)`** | `>=2026.7.0,<2026.7.1` | `—` | `*, *` | `—` | `—` |
| **`GitHub:fsspec/gcsfs (main)`** | `>=2026.7.0, *` | `*, *` | `—` | `—` | `—` |
| **`GitHub:fsspec/adlfs (main)`** | `>=2023.12.0` | `—` | `—` | `*` | `—` |

## 🔍 Detailed Manifest Entries

### `GitHub:pytorch/pytorch (main)`
- **fsspec** `>=0.8.5` (minimum) in `pyproject.toml:332`
  `"fsspec>=0.8.5",`
- **fsspec** `>=0.8.5` (minimum) in `requirements.txt:10`
  `fsspec>=0.8.5`

### `GitHub:pandas-dev/pandas (main)`
- **pyarrow** `= ['pyarrow>=16.0.0']` (minimum) in `pyproject.toml:90`
  `pyarrow = ['pyarrow>=16.0.0']`
- **fsspec** `>=2025.7.0` (minimum) in `pyproject.toml:93`
  `fss = ['fsspec>=2025.7.0']`
- **s3fs** `>=2025.7.0` (minimum) in `pyproject.toml:94`
  `aws = ['s3fs>=2025.7.0']`
- **gcsfs** `>=2025.7.0` (minimum) in `pyproject.toml:95`
  `gcp = ['gcsfs>=2025.7.0']`
- **pyarrow** `>=13.0.0` (minimum) in `pyproject.toml:97`
  `parquet = ['pyarrow>=13.0.0']`
- **pyarrow** `>=13.0.0` (minimum) in `pyproject.toml:98`
  `feather = ['pyarrow>=13.0.0']`
- **fsspec** `>=2025.7.0` (minimum) in `pyproject.toml:117`
  `'fsspec>=2025.7.0',`
- **gcsfs** `>=2025.7.0` (minimum) in `pyproject.toml:118`
  `'gcsfs>=2025.7.0',`
- **pyarrow** `>=16.0.0` (minimum) in `pyproject.toml:129`
  `'pyarrow>=16.0.0',`
- **s3fs** `>=2025.7.0` (minimum) in `pyproject.toml:141`
  `'s3fs>=2025.7.0',`
- **fsspec** `>=2025.7.0` (minimum) in `requirements-dev.txt:23`
  `fsspec>=2025.7.0`
- **gcsfs** `>=2025.7.0` (minimum) in `requirements-dev.txt:26`
  `gcsfs>=2025.7.0`
- **pyarrow** `>=16.0.0,!=24.*` (minimum) in `requirements-dev.txt:35`
  `pyarrow>=16.0.0,!=24.*`
- **s3fs** `>=2025.7.0` (minimum) in `requirements-dev.txt:43`
  `s3fs>=2025.7.0`

### `GitHub:ray-project/ray (master)`
- **pyarrow** `>= 17.0.0` (minimum) in `python/requirements.txt:24`
  `pyarrow >= 17.0.0`
- **fsspec** `*` (unconstrained) in `python/requirements.txt:52`
  `fsspec`
- **adlfs** `==2026.4.0` (pinned) in `python/requirements_compiled.txt:31`
  `adlfs==2026.4.0`
- **fsspec** `==2023.12.1` (pinned) in `python/requirements_compiled.txt:594`
  `fsspec==2023.12.1`
- **google-cloud-storage** `==2.14.0` (pinned) in `python/requirements_compiled.txt:677`
  `google-cloud-storage==2.14.0`
- **pyarrow** `==23.0.1` (pinned) in `python/requirements_compiled.txt:1691`
  `pyarrow==23.0.1`
- **s3fs** `==2023.12.1` (pinned) in `python/requirements_compiled.txt:2089`
  `s3fs==2023.12.1`
- **adlfs** `==2026.4.0` (pinned) in `python/requirements_compiled_py3.14.txt:31`
  `adlfs==2026.4.0`
- **fsspec** `==2023.12.1` (pinned) in `python/requirements_compiled_py3.14.txt:601`
  `fsspec==2023.12.1`
- **google-cloud-storage** `==2.14.0` (pinned) in `python/requirements_compiled_py3.14.txt:684`
  `google-cloud-storage==2.14.0`
- **pyarrow** `==23.0.1` (pinned) in `python/requirements_compiled_py3.14.txt:1690`
  `pyarrow==23.0.1`
- **s3fs** `==2023.12.1` (pinned) in `python/requirements_compiled_py3.14.txt:2085`
  `s3fs==2023.12.1`
- **pyarrow** `>= 17.0.0` (minimum) in `python/setup.py:228`
  `"pyarrow >= 17.0.0",`
- **fsspec** `*` (unconstrained) in `python/setup.py:239`
  `"fsspec",`
- **fsspec** `*` (unconstrained) in `python/setup.py:256`
  `"fsspec",`

### `GitHub:pola-rs/polars (main)`
- **pyarrow** `= ["pyarrow >= 7.0.0"]` (minimum) in `py-polars/pyproject.toml:55`
  `pyarrow = ["pyarrow >= 7.0.0"]`
- **fsspec** `= ["fsspec"]` (custom) in `py-polars/pyproject.toml:72`
  `fsspec = ["fsspec"]`
- **pyarrow** `*` (unconstrained) in `py-polars/requirements-dev.txt:23`
  `pyarrow`
- **fsspec** `*` (unconstrained) in `py-polars/requirements-dev.txt:38`
  `fsspec`
- **s3fs** `>=2026.2.0` (minimum) in `py-polars/requirements-dev.txt:41`
  `s3fs>=2026.2.0`

### `GitHub:huggingface/datasets (main)`
- **pyarrow** `>=21.0.0` (minimum) in `setup.py:114`
  `"pyarrow>=21.0.0",`
- **fsspec** `>=2023.1.0,<=2026.6.0` (range) in `setup.py:130`
  `"fsspec[http]>=2023.1.0,<=2026.6.0",`
- **pyarrow** `*` (unconstrained) in `src/datasets/formatting/__init__.py:77`
  `_register_formatter(ArrowFormatter, "arrow", aliases=["pa", "pyarrow"])`

### `GitHub:mlflow/mlflow (master)`
- **pyarrow** `*` (unconstrained) in `libs/skinny/pyproject.toml:62`
  `"pyarrow",`
- **google-cloud-storage** `>=1.30.0` (minimum) in `libs/skinny/pyproject.toml:66`
  `"google-cloud-storage>=1.30.0",`
- **google-cloud-storage** `>=1.30.0` (minimum) in `libs/skinny/pyproject.toml:75`
  `"google-cloud-storage>=1.30.0",`
- **pyarrow** `<26,>=4.0.0` (range) in `pyproject.toml:58`
  `"pyarrow<26,>=4.0.0",`
- **pyarrow** `*` (unconstrained) in `pyproject.toml:82`
  `"pyarrow",`
- **google-cloud-storage** `>=1.30.0` (minimum) in `pyproject.toml:86`
  `"google-cloud-storage>=1.30.0",`
- **google-cloud-storage** `>=1.30.0` (minimum) in `pyproject.toml:95`
  `"google-cloud-storage>=1.30.0",`

### `GitHub:apache/arrow (main)`
- **pyarrow** `*` (unconstrained) in `python/pyproject.toml:30`
  `name = "pyarrow"`
- **pyarrow** `*` (unconstrained) in `python/pyproject.toml:85`
  `wheel.packages = ["pyarrow"]`
- **pyarrow** `*` (unconstrained) in `python/pyproject.toml:86`
  `wheel.install-dir = "pyarrow"`
- **pyarrow** `*` (unconstrained) in `python/pyproject.toml:129`
  `"pyarrow",`
- **pyarrow** `*` (unconstrained) in `python/pyproject.toml:145`
  `"pyarrow",`

### `GitHub:iterative/dvc (main)`
- **fsspec** `>=2024.2.0` (minimum) in `pyproject.toml:52`
  `"fsspec>=2024.2.0",`

### `GitHub:dask/dask (main)`
- **fsspec** `>= 2021.09.0` (minimum) in `pyproject.toml:40`
  `"fsspec >= 2021.09.0",`
- **pyarrow** `>= 16.0` (minimum) in `pyproject.toml:61`
  `"pyarrow >= 16.0",`

### `GitHub:modin-project/modin (main)`
- **fsspec** `>=2022.11.0` (minimum) in `requirements-dev.txt:4`
  `fsspec>=2022.11.0`
- **pyarrow** `>=10.0.1` (minimum) in `requirements-dev.txt:10`
  `pyarrow>=10.0.1`
- **s3fs** `>=2022.11.0` (minimum) in `requirements-dev.txt:16`
  `s3fs>=2022.11.0`
- **pyarrow** `>=10.0.1` (minimum) in `setup.py:9`
  `ray_deps = ["ray>=2.10.0,<3", "pyarrow>=10.0.1"]`
- **fsspec** `>=2022.11.0` (minimum) in `setup.py:57`
  `"fsspec>=2022.11.0",`

### `GitHub:feast-dev/feast (master)`
- **pyarrow** `>=16.1.0` (minimum) in `pyproject.toml:26`
  `"pyarrow>=16.1.0",`
- **fsspec** `>=2024.1.0` (minimum) in `pyproject.toml:55`
  `aws = ["boto3>=1.38.27", "fsspec>=2024.1.0", "aiobotocore>=2"]`
- **pyarrow** `<21.0.0` (maximum) in `pyproject.toml:71`
  `flink = ["apache-flink>=2.2.1,<3", "pyarrow<21.0.0"]`
- **google-cloud-storage** `>=1.34.0,<3` (range) in `pyproject.toml:78`
  `"google-cloud-storage>=1.34.0,<3",`
- **fsspec** `>=2024.1.0` (minimum) in `pyproject.toml:80`
  `"fsspec>=2024.1.0",`

### `GitHub:pydata/xarray (main)`
- **fsspec** `*` (unconstrained) in `pyproject.toml:46`
  `"fsspec",`

### `GitHub:kedro-org/kedro (main)`
- **fsspec** `>=2021.4` (minimum) in `pyproject.toml:20`
  `"fsspec>=2021.4",`
- **s3fs** `>=2021.4,<2026.8` (range) in `pyproject.toml:74`
  `"s3fs>=2021.4,<2026.8",`

### `GitHub:delta-io/delta-rs (main)`
- **pyarrow** `= ["pyarrow>=21"]` (minimum) in `python/pyproject.toml:25`
  `pyarrow = ["pyarrow>=21"]`

### `GitHub:zarr-developers/zarr-python (main)`
- **fsspec** `*` (unconstrained) in `packages/zarr-http-server/pyproject.toml:62`
  `"fsspec[http]",`
- **fsspec** `>=2023.10.0` (minimum) in `pyproject.toml:78`
  `"fsspec>=2023.10.0",`
- **fsspec** `>=2023.10.0` (minimum) in `pyproject.toml:125`
  `"fsspec>=2023.10.0",`
- **s3fs** `>=2023.10.0` (minimum) in `pyproject.toml:128`
  `"s3fs>=2023.10.0",`
- **s3fs** `>=2023.10.0` (minimum) in `pyproject.toml:150`
  `"s3fs>=2023.10.0",`
- **fsspec** `==2023.10.0` (pinned) in `pyproject.toml:279`
  `'fsspec==2023.10.0',`
- **s3fs** `==2023.10.0` (pinned) in `pyproject.toml:280`
  `'s3fs==2023.10.0',`
- **fsspec** `*` (unconstrained) in `src/zarr/__init__.py:76`
  `"fsspec",`
- **s3fs** `*` (unconstrained) in `src/zarr/__init__.py:78`
  `"s3fs",`
- **gcsfs** `*` (unconstrained) in `src/zarr/__init__.py:79`
  `"gcsfs",`

### `GitHub:intake/intake (master)`
- **fsspec** `>=2023.0.0` (minimum) in `pyproject.toml:37`
  `"fsspec >=2023.0.0",`

### `GitHub:fsspec/s3fs (main)`
- **fsspec** `>=2026.7.0,<2026.7.1` (range) in `requirements.txt:2`
  `fsspec>=2026.7.0,<2026.7.1`
- **s3fs** `*` (unconstrained) in `setup.py:7`
  `name="s3fs",`
- **s3fs** `*` (unconstrained) in `setup.py:27`
  `packages=["s3fs"],`

### `GitHub:fsspec/gcsfs (main)`
- **google-cloud-storage** `*` (unconstrained) in `cloudbuild/macrobenchmarks/metrics/requirements.txt:4`
  `google-cloud-storage`
- **gcsfs** `*` (unconstrained) in `gcsfs/__init__.py:10`
  `__version__ = version("gcsfs")`
- **gcsfs** `*` (unconstrained) in `pyproject.toml:6`
  `name = "gcsfs"`
- **google-cloud-storage** `*` (unconstrained) in `pyproject.toml:14`
  `keywords = ["google-cloud-storage", "gcloud", "file-system"]`
- **fsspec** `>=2026.7.0` (minimum) in `pyproject.toml:29`
  `"fsspec>=2026.7.0",`
- **google-cloud-storage** `>=3.11.0` (minimum) in `pyproject.toml:32`
  `"google-cloud-storage>=3.11.0",`
- **fsspec** `*` (unconstrained) in `pyproject.toml:82`
  `known_third_party = ["aiohttp", "click", "datasets", "decorator", "fsspec", "fuse", "google", "google_auth_oauthlib", "lightning", "metrics", "numpy", "prettytable", "psutil", "pytest", "pytest_asyncio", "requests", "torch", "torchdata", "transformers", "yaml"]`

### `GitHub:fsspec/adlfs (main)`
- **adlfs** `*` (unconstrained) in `pyproject.toml:9`
  `name = "adlfs"`
- **fsspec** `>=2023.12.0` (minimum) in `pyproject.toml:31`
  `"fsspec>=2023.12.0",`
