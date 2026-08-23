# Master FSSPEC & Filesystem Method Usage Report

- **Repositories Crawled:** `1`
- **Total Files Scanned:** `141`
- **Files with Method Usages:** `17`
- **Total Method Usages Detected:** `102`
- **Distinct Methods Detected:** `19`
- **Skipping Test Files (test_*.py):** `True`

---

## 📊 Repository Summary Table

| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Top Methods |
| :--- | :--- | :--- | :--- | :--- |
| [huggingface/datasets](https://github.com/huggingface/datasets) | `141` | `17` | `102` | `url_to_fs` (22), `fs.open` (17), `fs.isfile` (11) |

---

## 📊 Repository × Target Call Usage Matrix (19 Methods)

| Repository | Total Calls | `url_to_fs` | `fs.open` | `fs.isfile` | `fs.glob` | `f.write` | `f.read` | `fs.read_text` | `f.close` | `fs.exists` | `fs.info` | `fs.makedirs` | `fs.isdir` | `fsspec.filesystem` | `fs.mv` | `fs.get_file` | `fs.size` | `get_fs_token_paths` | `fs.listdir` | `fs.walk` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [huggingface/datasets](https://github.com/huggingface/datasets) | **102** | [**22**](#huggingface-datasets-url-to-fs) | [**17**](#huggingface-datasets-fs-open) | [**11**](#huggingface-datasets-fs-isfile) | [**8**](#huggingface-datasets-fs-glob) | [**8**](#huggingface-datasets-f-write) | [**6**](#huggingface-datasets-f-read) | [**5**](#huggingface-datasets-fs-read-text) | [**4**](#huggingface-datasets-f-close) | [**4**](#huggingface-datasets-fs-exists) | [**4**](#huggingface-datasets-fs-info) | [**3**](#huggingface-datasets-fs-makedirs) | [**3**](#huggingface-datasets-fs-isdir) | [**1**](#huggingface-datasets-fsspec-filesystem) | [**1**](#huggingface-datasets-fs-mv) | [**1**](#huggingface-datasets-fs-get-file) | [**1**](#huggingface-datasets-fs-size) | [**1**](#huggingface-datasets-get-fs-token-paths) | [**1**](#huggingface-datasets-fs-listdir) | [**1**](#huggingface-datasets-fs-walk) |

---

## 🔍 Detailed Usage Breakdown by Repository

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
