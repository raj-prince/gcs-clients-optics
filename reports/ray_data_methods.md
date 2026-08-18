# Master FSSPEC Usage Report Across GitHub Repositories

- **Repositories Crawled:** `1`
- **Total Files Scanned:** `377`
- **Files with FSSPEC Usages:** `11`
- **Total FSSPEC Usages Detected:** `27`
- **Skipping Test Files (test_*.py):** `True`

---

## 📊 Repository Summary Table

| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Cache_Types |
| :--- | :--- | :--- | :--- | :--- |
| [ray-project/ray](https://github.com/ray-project/ray) | `377` | `11` | `27` | `NOT_EXPLICIT:27` |

---

## 📈 Global Cache_Type Breakdown

| Cache_Type Option | Total Occurrences | Is Specified Keyword | Description |
| :--- | :--- | :--- | :--- |
| `NOT_EXPLICIT` | `27` | `False` | cache_type keyword omitted (uses fsspec default) |

---

## 🔍 Detailed Usage Breakdown by Repository

### [ray-project/ray](https://github.com/ray-project/ray)
- **Usages Found:** `27` in `11` files.

#### 1. [python/ray/data/_internal/datasource/_lerobot_compat.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40) (Line 40)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40
- **Target Call:** `fsspec.open(video_path, **opts).__enter__` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CredsVideoDecoderCache.get_decoder`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    file_handle = fsspec.open(video_path, **opts).__enter__()
```

#### 2. [python/ray/data/_internal/datasource/_lerobot_compat.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40) (Line 40)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CredsVideoDecoderCache.get_decoder`
- **Arguments:** `video_path`
- **Keywords:** `{}`

```python
                    file_handle = fsspec.open(video_path, **opts).__enter__()
```

#### 3. [python/ray/data/_internal/datasource/bigquery_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/bigquery_datasink.py#L94) (Line 94)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/bigquery_datasink.py#L94
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BigQueryDatasink._write_single_block`
- **Arguments:** `fp, 'rb'`
- **Keywords:** `{}`

```python
                    with open(fp, "rb") as source_file:
```

#### 4. [python/ray/data/_internal/datasource/databricks_uc_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/databricks_uc_datasource.py#L193) (Line 193)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/databricks_uc_datasource.py#L193
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatabricksUCDatasource.read_fn`
- **Arguments:** `mock_setup_fn_path, 'rb'`
- **Keywords:** `{}`

```python
                    with open(mock_setup_fn_path, "rb") as f:
```

#### 5. [python/ray/data/_internal/datasource/kafka_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L792) (Line 792)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L792
- **Target Call:** `start_offset.get(topic_name, {}).get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `KafkaDatasource.get_read_tasks`
- **Arguments:** `partition_id, 'earliest'`
- **Keywords:** `{}`

```python
                start_offset.get(topic_name, {}).get(partition_id, "earliest")
```

#### 6. [python/ray/data/_internal/datasource/kafka_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L792) (Line 792)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L792
- **Target Call:** `start_offset.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `KafkaDatasource.get_read_tasks`
- **Arguments:** `topic_name, {}`
- **Keywords:** `{}`

```python
                start_offset.get(topic_name, {}).get(partition_id, "earliest")
```

#### 7. [python/ray/data/_internal/datasource/kafka_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L797) (Line 797)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L797
- **Target Call:** `end_offset.get(topic_name, {}).get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `KafkaDatasource.get_read_tasks`
- **Arguments:** `partition_id, 'latest'`
- **Keywords:** `{}`

```python
                end_offset.get(topic_name, {}).get(partition_id, "latest")
```

#### 8. [python/ray/data/_internal/datasource/kafka_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L797) (Line 797)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L797
- **Target Call:** `end_offset.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `KafkaDatasource.get_read_tasks`
- **Arguments:** `topic_name, {}`
- **Keywords:** `{}`

```python
                end_offset.get(topic_name, {}).get(partition_id, "latest")
```

#### 9. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L235) (Line 235)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L235
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_build_schema`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    with fs.open(path, "rb") as f:
```

#### 10. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L412) (Line 412)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L412
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `root_uri`
- **Keywords:** `{}`

```python
    protocol, rest = split_protocol(root_uri)
```

#### 11. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L433) (Line 433)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L433
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `filesystem`
- **Keywords:** `{}`

```python
            fs = ArrowFSWrapper(filesystem)
```

#### 12. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L446) (Line 446)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L446
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `video_root_uri`
- **Keywords:** `{}`

```python
        _, fs_root = split_protocol(video_root_uri)
```

#### 13. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L451) (Line 451)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L451
- **Target Call:** `fsspec.core.url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `video_root_uri`
- **Keywords:** `{}`

```python
        fs, fs_root = fsspec.core.url_to_fs(video_root_uri, **video_storage_options)
```

#### 14. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L461) (Line 461)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L461
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `pa_fs`
- **Keywords:** `{}`

```python
        fs = ArrowFSWrapper(pa_fs)
```

#### 15. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L477) (Line 477)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L477
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_lerobot_metadata`
- **Arguments:** `f'{fs_root}/meta/info.json'`
- **Keywords:** `{}`

```python
    if not fs.exists(f"{fs_root}/meta/info.json"):
```

#### 16. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L491) (Line 491)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L491
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_lerobot_metadata`
- **Arguments:** `f'{fs_root}/meta', os.path.join(local_root, 'meta')`
- **Keywords:** `{'recursive': 'True'}`

```python
    fs.get(f"{fs_root}/meta", os.path.join(local_root, "meta"), recursive=True)
```

#### 17. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L813) (Line 813)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L813
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_read_lerobot_segment`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
        with fs.open(path, "rb") as f:
```

#### 18. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1290) (Line 1290)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1290
- **Target Call:** `root.fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_decode_image_frames`
- **Arguments:** `p, 'rb'`
- **Keywords:** `{}`

```python
                with root.fs.open(p, "rb") as fh:
```

#### 19. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L317) (Line 317)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L317
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `'zip'`
- **Keywords:** `{'fo': 'self.paths[0]'}`

```python
            self._fs = fsspec.filesystem("zip", fo=self.paths[0])
```

#### 20. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L327) (Line 327)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L327
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `pa_fs`
- **Keywords:** `{}`

```python
            self._fs = ArrowFSWrapper(pa_fs)
```

#### 21. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L337) (Line 337)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L337
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `filesystem`
- **Keywords:** `{}`

```python
                self._fs = ArrowFSWrapper(filesystem)
```

#### 22. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L353) (Line 353)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L353
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `self.paths[0]`
- **Keywords:** `{}`

```python
                _, store_path = split_protocol(self.paths[0])
```

#### 23. [python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py#L334) (Line 334)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py#L334
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ShuffleFlightServer.do_action`
- **Arguments:** `fpath, 'rb'`
- **Keywords:** `{}`

```python
                with open(fpath, "rb") as f:
```

#### 24. [python/ray/data/_internal/logging.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/logging.py#L182) (Line 182)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/logging.py#L182
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_logging_config`
- **Arguments:** `config_path`
- **Keywords:** `{}`

```python
        with open(config_path) as file:
```

#### 25. [python/ray/data/_internal/util.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/util.py#L1455) (Line 1455)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/util.py#L1455
- **Target Call:** `self._fs.move` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RetryingPyFileSystemHandler.move`
- **Arguments:** `src, dest`
- **Keywords:** `{}`

```python
            lambda: self._fs.move(src, dest), f"move from {src} to {dest}"
```

#### 26. [python/ray/data/datasource/path_util.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/path_util.py#L39) (Line 39)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/path_util.py#L39
- **Target Call:** `HTTPFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_fsspec_http_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    return PyFileSystem(FSSpecHandler(HTTPFileSystem()))
```

#### 27. [python/ray/data/read_api.py](https://github.com/ray-project/ray/blob/master/python/ray/data/read_api.py#L4582) (Line 4582)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/read_api.py#L4582
- **Target Call:** `fsspec.implementations.http.HTTPFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `from_huggingface`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                http = fsspec.implementations.http.HTTPFileSystem()
```
