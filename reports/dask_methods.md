# Master FSSPEC & Filesystem Method Usage Report

- **Repositories Crawled:** `1`
- **Total Files Scanned:** `184`
- **Files with Method Usages:** `16`
- **Total Method Usages Detected:** `76`
- **Distinct Methods Detected:** `22`
- **Skipping Test Files (test_*.py):** `True`

---

## 📊 Repository Summary Table

| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Top Methods |
| :--- | :--- | :--- | :--- | :--- |
| [dask/dask](https://github.com/dask/dask) | `184` | `16` | `76` | `fs.open` (16), `f.read` (10), `stringify_path` (9) |

---

## 📊 Repository × Target Call Usage Matrix (22 Methods)

| Repository | Total Calls | `fs.open` | `f.read` | `stringify_path` | `get_fs_token_paths` | `open_files` | `fs.info` | `fs.ukey` | `fs.read_block` | `infer_compression` | `fs.exists` | `fs.isdir` | `fs.find` | `expand_paths_if_needed` | `f.write` | `f.close` | `f.tell` | `f.seek` | `fs.expand_path` | `fs.rm` | `fs.checksum` | `fs.isfile` | `fsspec.open_parquet_file` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [dask/dask](https://github.com/dask/dask) | **76** | [**16**](#dask-dask-fs-open) | [**10**](#dask-dask-f-read) | [**9**](#dask-dask-stringify-path) | [**7**](#dask-dask-get-fs-token-paths) | [**7**](#dask-dask-open-files) | [**2**](#dask-dask-fs-info) | [**2**](#dask-dask-fs-ukey) | [**2**](#dask-dask-fs-read-block) | [**2**](#dask-dask-infer-compression) | [**2**](#dask-dask-fs-exists) | [**2**](#dask-dask-fs-isdir) | [**2**](#dask-dask-fs-find) | [**2**](#dask-dask-expand-paths-if-needed) | [**2**](#dask-dask-f-write) | [**2**](#dask-dask-f-close) | [**1**](#dask-dask-f-tell) | [**1**](#dask-dask-f-seek) | [**1**](#dask-dask-fs-expand-path) | [**1**](#dask-dask-fs-rm) | [**1**](#dask-dask-fs-checksum) | [**1**](#dask-dask-fs-isfile) | [**1**](#dask-dask-fsspec-open-parquet-file) |

---

## 🔍 Detailed Usage Breakdown by Repository

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
