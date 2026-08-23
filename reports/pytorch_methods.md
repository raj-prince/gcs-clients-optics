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

## 📊 Repository × Target Call Usage Matrix (21 Methods)

| Repository | Total Calls | `f.write` | `f.close` | `f.flush` | `f.read` | `fs.exists` | `url_to_fs` | `fs.rename` | `fs.makedirs` | `fs.ls` | `f.tell` | `fs.get` | `fs.put` | `fs.flush` | `fs.open` | `fs.rm` | `fs.mkdir` | `fs.rm_file` | `fs.split` | `f.readline` | `fs.join` | `fs.isdir` |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| [pytorch/pytorch](https://github.com/pytorch/pytorch) | **57** | [**13**](#pytorch-pytorch-f-write) | [**11**](#pytorch-pytorch-f-close) | [**4**](#pytorch-pytorch-f-flush) | [**4**](#pytorch-pytorch-f-read) | [**4**](#pytorch-pytorch-fs-exists) | [**2**](#pytorch-pytorch-url-to-fs) | [**2**](#pytorch-pytorch-fs-rename) | [**2**](#pytorch-pytorch-fs-makedirs) | [**2**](#pytorch-pytorch-fs-ls) | [**2**](#pytorch-pytorch-f-tell) | [**1**](#pytorch-pytorch-fs-get) | [**1**](#pytorch-pytorch-fs-put) | [**1**](#pytorch-pytorch-fs-flush) | [**1**](#pytorch-pytorch-fs-open) | [**1**](#pytorch-pytorch-fs-rm) | [**1**](#pytorch-pytorch-fs-mkdir) | [**1**](#pytorch-pytorch-fs-rm-file) | [**1**](#pytorch-pytorch-fs-split) | [**1**](#pytorch-pytorch-f-readline) | [**1**](#pytorch-pytorch-fs-join) | [**1**](#pytorch-pytorch-fs-isdir) |

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
