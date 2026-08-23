# Master FSSPEC & Filesystem Method Usage Report

- **Repositories Crawled:** `1`
- **Total Files Scanned:** `2556`
- **Files with Method Usages:** `19`
- **Total Method Usages Detected:** `57`
- **Distinct Methods Detected:** `21`
- **Skipping Test Files (test_*.py):** `True`

---

## 📊 Repository Summary Table

| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Top Methods |
| :--- | :--- | :--- | :--- | :--- |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | `2556` | `19` | `57` | `f.write` (13), `f.close` (11), `f.flush` (4) |

---

## 📋 Complete 4-Column Summary Table of All 21 FSSPEC & Filesystem Methods

| Target Call | Occurrences | Major Repositories | Category | Primary Usage Pattern |
| :--- | :---: | :--- | :--- | :--- |
| **`f.write`** | **13** | `pytorch/pytorch` | Stream Reading & Writing | Write data bytes or string to file buffer |
| **`f.close`** | **11** | `pytorch/pytorch` | Stream Reading & Writing | Close file stream handle and release buffer resources |
| **`f.flush`** | **4** | `pytorch/pytorch` | Stream Reading & Writing | Write buffered data to backend store |
| **`f.read`** | **4** | `pytorch/pytorch` | Stream Reading & Writing | Read bytes from cache/stream, fetching chunks as necessary |
| **`fs.exists`** | **4** | `pytorch/pytorch` | Metadata & Existence Checks | Checking existence of a file or directory node on local or remote filesystem |
| **`url_to_fs`** | **2** | `pytorch/pytorch` | Protocol Resolution & Driver Lifecycle | Decomposing protocol URI string (`s3://...`, `gs://...`) into abstract `(filesystem, path)` tuple |
| **`fs.rename`** | **2** | `pytorch/pytorch` | File & Directory Mutation | Alias of `mv`; rename or move an object path within filesystem storage |
| **`fs.makedirs`** | **2** | `pytorch/pytorch` | File & Directory Mutation | Recursively create directory tree hierarchy (`exist_ok=True`) |
| **`fs.ls`** | **2** | `pytorch/pytorch` | Directory Listing & Traversal | List direct children of a directory (`detail=False` for paths, `detail=True` for info dicts) |
| **`f.tell`** | **2** | `pytorch/pytorch` | Stream Reading & Writing | Return current file location offset in stream |
| **`fs.get`** | **1** | `pytorch/pytorch` | Bulk Data Transfer | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fs.put`** | **1** | `pytorch/pytorch` | Bulk Data Transfer | Bulk batch uploading of local file(s) or directories up to remote filesystem target |
| **`fs.flush`** | **1** | `pytorch/pytorch` | Stream Reading & Writing | Write buffered data to backend store |
| **`fs.open`** | **1** | `pytorch/pytorch` | Stream Reading & Writing | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`fs.rm`** | **1** | `pytorch/pytorch` | File & Directory Mutation | Delete files or directory trees (`recursive=True/False`) |
| **`fs.mkdir`** | **1** | `pytorch/pytorch` | File & Directory Mutation | Create single directory container node at path (`create_parents=False`) |
| **`fs.rm_file`** | **1** | `pytorch/pytorch` | File & Directory Mutation | Delete a single leaf file node from storage driver |
| **`fs.split`** | **1** | `pytorch/pytorch` | Path Arithmetic & Topologies | Splitting abstract path into `(head, tail)` tuple pair |
| **`f.readline`** | **1** | `pytorch/pytorch` | Stream Reading & Writing | Read until and including the first occurrence of newline character |
| **`fs.join`** | **1** | `pytorch/pytorch` | Path Arithmetic & Topologies | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`fs.isdir`** | **1** | `pytorch/pytorch` | Metadata & Existence Checks | Verify whether a path points to an abstract directory container node |

---

## 🔍 Detailed Usage Breakdown by Repository

### [pytorch/pytorch](https://github.com/pytorch/pytorch)
- **Usages Found:** `57` in `19` files.

#### 1. [torch/_inductor/compile_worker/subproc_pool.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/compile_worker/subproc_pool.py#L620) (Line 620)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/compile_worker/subproc_pool.py#L620
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `SubprocPool.shutdown`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                self.log_file.close()
```

#### 2. [torch/_inductor/remote_cache.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/remote_cache.py#L247) (Line 247)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/remote_cache.py#L247
- **Target Call:** `fs.get` | **Category:** `Bulk Data Transfer`
- **Context:** `RemoteCache._backend_get`
- **Arguments:** `key`
- **Keywords:** `{}`

```python
        return self.backend.get(key)
```

#### 3. [torch/_inductor/remote_cache.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/remote_cache.py#L259) (Line 259)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/remote_cache.py#L259
- **Target Call:** `fs.put` | **Category:** `Bulk Data Transfer`
- **Context:** `RemoteCache._backend_put`
- **Arguments:** `key, data`
- **Keywords:** `{}`

```python
        self.backend.put(key, data)
```

#### 4. [torch/_inductor/runtime/caching/implementations.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/runtime/caching/implementations.py#L338) (Line 338)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/runtime/caching/implementations.py#L338
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `_OnDiskCacheImpl.insert`
- **Arguments:** `value`
- **Keywords:** `{}`

```python
                    w_fp.write(value)
```

#### 5. [torch/_inductor/runtime/caching/implementations.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/runtime/caching/implementations.py#L341) (Line 341)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/runtime/caching/implementations.py#L341
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `_OnDiskCacheImpl.insert`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    w_fp.close()
```

#### 6. [torch/_inductor/scheduler.py](https://github.com/pytorch/pytorch/blob/main/torch/_inductor/scheduler.py#L9844) (Line 9844)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_inductor/scheduler.py#L9844
- **Target Call:** `fs.flush` | **Category:** `Stream Reading & Writing`
- **Context:** `Scheduler.flush`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            backend.flush()
```

#### 7. [torch/_logging/_internal.py](https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1087) (Line 1087)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1087
- **Target Call:** `f.flush` | **Category:** `Stream Reading & Writing`
- **Context:** `_StderrHandler.flush`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                stream.flush()
```

#### 8. [torch/_logging/_internal.py](https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1095) (Line 1095)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1095
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `_StderrHandler.emit`
- **Arguments:** `msg + self.terminator`
- **Keywords:** `{}`

```python
            stream.write(msg + self.terminator)
```

#### 9. [torch/_logging/_internal.py](https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1274) (Line 1274)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1274
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `LazyTraceHandler._close_stream`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    stream.close()
```

#### 10. [torch/_logging/_internal.py](https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1281) (Line 1281)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_logging/_internal.py#L1281
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `LazyTraceHandler._close_stream`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                        stream.close()
```

#### 11. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L128) (Line 128)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L128
- **Target Call:** `f.read` | **Category:** `Stream Reading & Writing`
- **Context:** `_recv`
- **Arguments:** `4`
- **Keywords:** `{}`

```python
    header = stream.read(4)
```

#### 12. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L134) (Line 134)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L134
- **Target Call:** `f.read` | **Category:** `Stream Reading & Writing`
- **Context:** `_recv`
- **Arguments:** `length`
- **Keywords:** `{}`

```python
    data = stream.read(length)
```

#### 13. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L141) (Line 141)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L141
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `_send`
- **Arguments:** `struct.pack('<I', len(data))`
- **Keywords:** `{}`

```python
    stream.write(struct.pack("<I", len(data)))
```

#### 14. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L142) (Line 142)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L142
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `_send`
- **Arguments:** `data`
- **Keywords:** `{}`

```python
    stream.write(data)
```

#### 15. [torch/_vendor/quack/_compile_worker.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L143) (Line 143)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/_compile_worker.py#L143
- **Target Call:** `f.flush` | **Category:** `Stream Reading & Writing`
- **Context:** `_send`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    stream.flush()
```

#### 16. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L266) (Line 266)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L266
- **Target Call:** `f.read` | **Category:** `Stream Reading & Writing`
- **Context:** `_recv_from_worker`
- **Arguments:** `4`
- **Keywords:** `{}`

```python
    header = stream.read(4)
```

#### 17. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L272) (Line 272)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L272
- **Target Call:** `f.read` | **Category:** `Stream Reading & Writing`
- **Context:** `_recv_from_worker`
- **Arguments:** `length`
- **Keywords:** `{}`

```python
    body = stream.read(length)
```

#### 18. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L407) (Line 407)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L407
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `Autotuner._send`
- **Arguments:** `struct.pack('<I', len(data))`
- **Keywords:** `{}`

```python
            stream.write(struct.pack("<I", len(data)))
```

#### 19. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L408) (Line 408)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L408
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `Autotuner._send`
- **Arguments:** `data`
- **Keywords:** `{}`

```python
            stream.write(data)
```

#### 20. [torch/_vendor/quack/autotuner.py](https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L409) (Line 409)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/_vendor/quack/autotuner.py#L409
- **Target Call:** `f.flush` | **Category:** `Stream Reading & Writing`
- **Context:** `Autotuner._send`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            stream.flush()
```

#### 21. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L47) (Line 47)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L47
- **Target Call:** `fs.open` | **Category:** `Stream Reading & Writing`
- **Context:** `FileSystem.create_stream`
- **Arguments:** `path, mode`
- **Keywords:** `{}`

```python
        with self.fs.open(path, mode) as stream:
```

#### 22. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L62) (Line 62)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L62
- **Target Call:** `url_to_fs` | **Category:** `Protocol Resolution & Driver Lifecycle`
- **Context:** `FileSystem.init_path`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs, _ = url_to_fs(path, **kwargs)
```

#### 23. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L66) (Line 66)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L66
- **Target Call:** `fs.rename` | **Category:** `File & Directory Mutation`
- **Context:** `FileSystem.rename`
- **Arguments:** `path, new_path`
- **Keywords:** `{}`

```python
        self.fs.rename(path, new_path)
```

#### 24. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L69) (Line 69)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L69
- **Target Call:** `fs.makedirs` | **Category:** `File & Directory Mutation`
- **Context:** `FileSystem.mkdir`
- **Arguments:** `path`
- **Keywords:** `{'exist_ok': 'True'}`

```python
        self.fs.makedirs(path, exist_ok=True)
```

#### 25. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L77) (Line 77)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L77
- **Target Call:** `url_to_fs` | **Category:** `Protocol Resolution & Driver Lifecycle`
- **Context:** `FileSystem.validate_checkpoint_id`
- **Arguments:** `checkpoint_id`
- **Keywords:** `{}`

```python
            url_to_fs(checkpoint_id)
```

#### 26. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L84) (Line 84)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L84
- **Target Call:** `fs.exists` | **Category:** `Metadata & Existence Checks`
- **Context:** `FileSystem.exists`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        return self.fs.exists(path)
```

#### 27. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L87) (Line 87)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L87
- **Target Call:** `fs.rm` | **Category:** `File & Directory Mutation`
- **Context:** `FileSystem.rm_file`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        self.fs.rm(path)
```

#### 28. [torch/distributed/checkpoint/_fsspec_filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L92) (Line 92)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/_fsspec_filesystem.py#L92
- **Target Call:** `fs.ls` | **Category:** `Directory Listing & Traversal`
- **Context:** `FileSystem.ls`
- **Arguments:** `path`
- **Keywords:** `{'detail': 'False'}`

```python
        return self.fs.ls(path, detail=False)
```

#### 29. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L328) (Line 328)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L328
- **Target Call:** `f.tell` | **Category:** `Stream Reading & Writing`
- **Context:** `_write_item`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    offset = stream.tell()
```

#### 30. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L353) (Line 353)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L353
- **Target Call:** `f.tell` | **Category:** `Stream Reading & Writing`
- **Context:** `_write_item`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        length = stream.tell() - offset
```

#### 31. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L459) (Line 459)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L459
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
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

#### 32. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L472) (Line 472)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L472
- **Target Call:** `f.flush` | **Category:** `Stream Reading & Writing`
- **Context:** `_write_files_from_queue`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    stream.flush()
```

#### 33. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L479) (Line 479)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L479
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `_write_files_from_queue`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                stream.close()
```

#### 34. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L653) (Line 653)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L653
- **Target Call:** `fs.exists` | **Category:** `Metadata & Existence Checks`
- **Context:** `_FileSystemWriter._metadata_exists`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python
        return self.fs.exists(metadata_path)
```

#### 35. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L656) (Line 656)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L656
- **Target Call:** `fs.mkdir` | **Category:** `File & Directory Mutation`
- **Context:** `_FileSystemWriter.prepare_local_plan`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        self.fs.mkdir(self.path)
```

#### 36. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L795) (Line 795)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L795
- **Target Call:** `fs.exists` | **Category:** `Metadata & Existence Checks`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python
        if self.fs.exists(metadata_path):
```

#### 37. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L796) (Line 796)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L796
- **Target Call:** `fs.rm_file` | **Category:** `File & Directory Mutation`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `metadata_path`
- **Keywords:** `{}`

```python
            self.fs.rm_file(metadata_path)
```

#### 38. [torch/distributed/checkpoint/filesystem.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L798) (Line 798)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/filesystem.py#L798
- **Target Call:** `fs.rename` | **Category:** `File & Directory Mutation`
- **Context:** `_FileSystemWriter.finish`
- **Arguments:** `tmp_path, metadata_path`
- **Keywords:** `{}`

```python
        self.fs.rename(tmp_path, metadata_path)
```

#### 39. [torch/distributed/checkpoint/hf_storage.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L321) (Line 321)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/checkpoint/hf_storage.py#L321
- **Target Call:** `fs.ls` | **Category:** `Directory Listing & Traversal`
- **Context:** `HuggingFaceStorageReader.read_metadata`
- **Arguments:** `self.path`
- **Keywords:** `{}`

```python
        for file in self.fs.ls(self.path):
```

#### 40. [torch/distributed/distributed_c10d.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/distributed_c10d.py#L1083) (Line 1083)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/distributed_c10d.py#L1083
- **Target Call:** `fs.split` | **Category:** `Path Arithmetic & Topologies`
- **Context:** `_parse_backend_string`
- **Arguments:** `','`
- **Keywords:** `{}`

```python
        for part in backend.split(","):
```

#### 41. [torch/distributed/elastic/multiprocessing/api.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/multiprocessing/api.py#L665) (Line 665)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/multiprocessing/api.py#L665
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `PContext.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.filtered_stdout.close()
```

#### 42. [torch/distributed/elastic/multiprocessing/api.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/multiprocessing/api.py#L667) (Line 667)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/multiprocessing/api.py#L667
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `PContext.close`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.filtered_stderr.close()
```

#### 43. [torch/distributed/elastic/timer/file_based_local_timer.py](https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/timer/file_based_local_timer.py#L379) (Line 379)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/distributed/elastic/timer/file_based_local_timer.py#L379
- **Target Call:** `f.readline` | **Category:** `Stream Reading & Writing`
- **Context:** `FileTimerServer._get_requests`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            json_request = fd.readline()
```

#### 44. [torch/hub.py](https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L771) (Line 771)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L771
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `download_url_to_file`
- **Arguments:** `buffer`
- **Keywords:** `{}`

```python
                    f.write(buffer)
```

#### 45. [torch/hub.py](https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L776) (Line 776)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L776
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `download_url_to_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            f.close()
```

#### 46. [torch/hub.py](https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L785) (Line 785)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/hub.py#L785
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `download_url_to_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        f.close()
```

#### 47. [torch/serialization.py](https://github.com/pytorch/pytorch/blob/main/torch/serialization.py#L836) (Line 836)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/serialization.py#L836
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `_open_zipfile_writer_file.__exit__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.file_stream.close()
```

#### 48. [torch/utils/data/datapipes/utils/common.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/data/datapipes/utils/common.py#L378) (Line 378)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/data/datapipes/utils/common.py#L378
- **Target Call:** `f.close` | **Category:** `Stream Reading & Writing`
- **Context:** `StreamWrapper.close`
- **Arguments:** `*args`
- **Keywords:** `{}`

```python
            self.file_obj.close(*args, **kwargs)
```

#### 49. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L31) (Line 31)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L31
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `repr(obj)`
- **Keywords:** `{}`

```python
            stream.write(repr(obj))
```

#### 50. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L34) (Line 34)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L34
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `f'{obj.module}.{obj.name}'`
- **Keywords:** `{}`

```python
            stream.write(f"{obj.module}.{obj.name}")
```

#### 51. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L38) (Line 38)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L38
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `f'{obj.module}.{obj.name}()(state=\n'`
- **Keywords:** `{}`

```python
            stream.write(f"{obj.module}.{obj.name}()(state=\n")
```

#### 52. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L40) (Line 40)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L40
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `' ' * indent`
- **Keywords:** `{}`

```python
            stream.write(" " * indent)
```

#### 53. [torch/utils/show_pickle.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L42) (Line 42)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/show_pickle.py#L42
- **Target Call:** `f.write` | **Category:** `Stream Reading & Writing`
- **Context:** `FakeObject.pp_format`
- **Arguments:** `')'`
- **Keywords:** `{}`

```python
            stream.write(")")
```

#### 54. [torch/utils/tensorboard/_embedding.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/_embedding.py#L21) (Line 21)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/_embedding.py#L21
- **Target Call:** `fs.join` | **Category:** `Path Arithmetic & Topologies`
- **Context:** `_gfile_join`
- **Arguments:** `a, b`
- **Keywords:** `{}`

```python
        return fs.join(a, b)
```

#### 55. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L920) (Line 920)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L920
- **Target Call:** `fs.exists` | **Category:** `Metadata & Existence Checks`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
        if fs.exists(save_path):
```

#### 56. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L921) (Line 921)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L921
- **Target Call:** `fs.isdir` | **Category:** `Metadata & Existence Checks`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
            if fs.isdir(save_path):
```

#### 57. [torch/utils/tensorboard/writer.py](https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L930) (Line 930)
- **Line Link:** https://github.com/pytorch/pytorch/blob/main/torch/utils/tensorboard/writer.py#L930
- **Target Call:** `fs.makedirs` | **Category:** `File & Directory Mutation`
- **Context:** `SummaryWriter.add_embedding`
- **Arguments:** `save_path`
- **Keywords:** `{}`

```python
            fs.makedirs(save_path)
```
