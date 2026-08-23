# Master FSSPEC & Filesystem Method Usage Report

- **Repositories Crawled:** `3`
- **Total Files Scanned:** `2881`
- **Files with Method Usages:** `52`
- **Total Method Usages Detected:** `235`
- **Distinct Methods Detected:** `43`
- **Skipping Test Files (test_*.py):** `True`

---

## 📊 Repository Summary Table

| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Top Methods |
| :--- | :--- | :--- | :--- | :--- |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | `2556` | `19` | `57` | `f.write` (13), `f.close` (11), `f.flush` (4) |
| [huggingface/datasets](https://github.com/huggingface/datasets) | `141` | `17` | `102` | `url_to_fs` (22), `fs.open` (17), `fs.isfile` (11) |
| [dask/dask](https://github.com/dask/dask) | `184` | `16` | `76` | `fs.open` (16), `f.read` (10), `stringify_path` (9) |

---

## 📊 Repository × Target Call Usage Matrix (43 Methods)

| Repository | Total Calls | `fs.open` | `url_to_fs` | `f.write` | `f.read` | `f.close` | `fs.isfile` | `fs.exists` | `stringify_path` | `fs.glob` | `get_fs_token_paths` | `open_files` | `fs.isdir` | `fs.info` | `fs.makedirs` | `fs.read_text` | `f.flush` | `f.tell` | `fs.rename` | `fs.rm` | `fs.ls` | `fs.ukey` | `fs.read_block` | `infer_compression` | `fs.find` | `expand_paths_if_needed` | `fs.get` | `fs.put` | `fs.flush` | `fs.mkdir` | `fs.rm_file` | `fs.split` | `f.readline` | `fs.join` | `fsspec.filesystem` | `fs.mv` | `fs.get_file` | `fs.size` | `fs.listdir` | `fs.walk` | `f.seek` | `fs.expand_path` | `fs.checksum` | `fsspec.open_parquet_file` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | **57** | [**1**](#pytorch-pytorch-fs-open) | [**2**](#pytorch-pytorch-url-to-fs) | [**13**](#pytorch-pytorch-f-write) | [**4**](#pytorch-pytorch-f-read) | [**11**](#pytorch-pytorch-f-close) | - | [**4**](#pytorch-pytorch-fs-exists) | - | - | - | - | [**1**](#pytorch-pytorch-fs-isdir) | - | [**2**](#pytorch-pytorch-fs-makedirs) | - | [**4**](#pytorch-pytorch-f-flush) | [**2**](#pytorch-pytorch-f-tell) | [**2**](#pytorch-pytorch-fs-rename) | [**1**](#pytorch-pytorch-fs-rm) | [**2**](#pytorch-pytorch-fs-ls) | - | - | - | - | - | [**1**](#pytorch-pytorch-fs-get) | [**1**](#pytorch-pytorch-fs-put) | [**1**](#pytorch-pytorch-fs-flush) | [**1**](#pytorch-pytorch-fs-mkdir) | [**1**](#pytorch-pytorch-fs-rm-file) | [**1**](#pytorch-pytorch-fs-split) | [**1**](#pytorch-pytorch-f-readline) | [**1**](#pytorch-pytorch-fs-join) | - | - | - | - | - | - | - | - | - | - |
| [huggingface/datasets](https://github.com/huggingface/datasets) | **102** | [**17**](#huggingface-datasets-fs-open) | [**22**](#huggingface-datasets-url-to-fs) | [**8**](#huggingface-datasets-f-write) | [**6**](#huggingface-datasets-f-read) | [**4**](#huggingface-datasets-f-close) | [**11**](#huggingface-datasets-fs-isfile) | [**4**](#huggingface-datasets-fs-exists) | - | [**8**](#huggingface-datasets-fs-glob) | [**1**](#huggingface-datasets-get-fs-token-paths) | - | [**3**](#huggingface-datasets-fs-isdir) | [**4**](#huggingface-datasets-fs-info) | [**3**](#huggingface-datasets-fs-makedirs) | [**5**](#huggingface-datasets-fs-read-text) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#huggingface-datasets-fsspec-filesystem) | [**1**](#huggingface-datasets-fs-mv) | [**1**](#huggingface-datasets-fs-get-file) | [**1**](#huggingface-datasets-fs-size) | [**1**](#huggingface-datasets-fs-listdir) | [**1**](#huggingface-datasets-fs-walk) | - | - | - | - |
| [dask/dask](https://github.com/dask/dask) | **76** | [**16**](#dask-dask-fs-open) | - | [**2**](#dask-dask-f-write) | [**10**](#dask-dask-f-read) | [**2**](#dask-dask-f-close) | [**1**](#dask-dask-fs-isfile) | [**2**](#dask-dask-fs-exists) | [**9**](#dask-dask-stringify-path) | - | [**7**](#dask-dask-get-fs-token-paths) | [**7**](#dask-dask-open-files) | [**2**](#dask-dask-fs-isdir) | [**2**](#dask-dask-fs-info) | - | - | - | [**1**](#dask-dask-f-tell) | - | [**1**](#dask-dask-fs-rm) | - | [**2**](#dask-dask-fs-ukey) | [**2**](#dask-dask-fs-read-block) | [**2**](#dask-dask-infer-compression) | [**2**](#dask-dask-fs-find) | [**2**](#dask-dask-expand-paths-if-needed) | - | - | - | - | - | - | - | - | - | - | - | - | - | - | [**1**](#dask-dask-f-seek) | [**1**](#dask-dask-fs-expand-path) | [**1**](#dask-dask-fs-checksum) | [**1**](#dask-dask-fsspec-open-parquet-file) |

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
