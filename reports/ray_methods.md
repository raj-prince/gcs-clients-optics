# Master FSSPEC Usage Report Across GitHub Repositories

- **Repositories Crawled:** `1`
- **Total Files Scanned:** `2003`
- **Files with FSSPEC Usages:** `129`
- **Total FSSPEC Usages Detected:** `316`
- **Skipping Test Files (test_*.py):** `True`

---

## 📊 Repository Summary Table

| Project / Repository | Files Scanned | Files w/ Usages | Total Usages | Cache_Types |
| :--- | :--- | :--- | :--- | :--- |
| [ray-project/ray](https://github.com/ray-project/ray) | `2003` | `129` | `316` | `NOT_EXPLICIT:316` |

---

## 📈 Global Cache_Type Breakdown

| Cache_Type Option | Total Occurrences | Is Specified Keyword | Description |
| :--- | :--- | :--- | :--- |
| `NOT_EXPLICIT` | `316` | `False` | cache_type keyword omitted (uses fsspec default) |

---

## 🔍 Detailed Usage Breakdown by Repository

### [ray-project/ray](https://github.com/ray-project/ray)
- **Usages Found:** `316` in `129` files.

#### 1. [.buildkite/copy_files.py](https://github.com/ray-project/ray/blob/master/.buildkite/copy_files.py#L92) (Line 92)
- **Line Link:** https://github.com/ray-project/ray/blob/master/.buildkite/copy_files.py#L92
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `upload_paths`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
        of["file"] = open(path, "rb")
```

#### 2. [bazel/pyzip.py](https://github.com/ray-project/ray/blob/master/bazel/pyzip.py#L39) (Line 39)
- **Line Link:** https://github.com/ray-project/ray/blob/master/bazel/pyzip.py#L39
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `zip_dir`
- **Arguments:** `file_path, 'rb'`
- **Keywords:** `{}`

```python
                with open(file_path, "rb") as f:
```

#### 3. [python/ray/_common/tls_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/tls_utils.py#L94) (Line 94)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/tls_utils.py#L94
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_certs_from_env`
- **Arguments:** `os.environ['RAY_TLS_SERVER_CERT'], 'rb'`
- **Keywords:** `{}`

```python
    with open(os.environ["RAY_TLS_SERVER_CERT"], "rb") as f:
```

#### 4. [python/ray/_common/tls_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/tls_utils.py#L96) (Line 96)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/tls_utils.py#L96
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_certs_from_env`
- **Arguments:** `os.environ['RAY_TLS_SERVER_KEY'], 'rb'`
- **Keywords:** `{}`

```python
    with open(os.environ["RAY_TLS_SERVER_KEY"], "rb") as f:
```

#### 5. [python/ray/_common/tls_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/tls_utils.py#L98) (Line 98)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/tls_utils.py#L98
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_certs_from_env`
- **Arguments:** `os.environ['RAY_TLS_CA_CERT'], 'rb'`
- **Keywords:** `{}`

```python
    with open(os.environ["RAY_TLS_CA_CERT"], "rb") as f:
```

#### 6. [python/ray/_common/usage/usage_lib.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/usage/usage_lib.py#L368) (Line 368)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/usage/usage_lib.py#L368
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_usage_stats_enabledness`
- **Arguments:** `_usage_stats_config_path()`
- **Keywords:** `{}`

```python
        with open(_usage_stats_config_path()) as f:
```

#### 7. [python/ray/_common/usage/usage_lib.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/usage/usage_lib.py#L489) (Line 489)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/usage/usage_lib.py#L489
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `set_usage_stats_enabled_via_config`
- **Arguments:** `_usage_stats_config_path()`
- **Keywords:** `{}`

```python
        with open(_usage_stats_config_path()) as f:
```

#### 8. [python/ray/_common/usage/usage_lib.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/usage/usage_lib.py#L505) (Line 505)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/usage/usage_lib.py#L505
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `set_usage_stats_enabled_via_config`
- **Arguments:** `_usage_stats_config_path(), 'w'`
- **Keywords:** `{}`

```python
        with open(_usage_stats_config_path(), "w") as f:
```

#### 9. [python/ray/_common/usage/usage_lib.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/usage/usage_lib.py#L780) (Line 780)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/usage/usage_lib.py#L780
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_cluster_config_to_report`
- **Arguments:** `cluster_config_file_path`
- **Keywords:** `{}`

```python
        with open(cluster_config_file_path) as f:
```

#### 10. [python/ray/_common/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/utils.py#L399) (Line 399)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/utils.py#L399
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_system_memory`
- **Arguments:** `memory_limit_filename, 'r'`
- **Keywords:** `{}`

```python
        with open(memory_limit_filename, "r") as f:
```

#### 11. [python/ray/_common/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_common/utils.py#L402) (Line 402)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_common/utils.py#L402
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_system_memory`
- **Arguments:** `memory_limit_filename_v2, 'r'`
- **Keywords:** `{}`

```python
        with open(memory_limit_filename_v2, "r") as f:
```

#### 12. [python/ray/_private/accelerators/tpu.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/accelerators/tpu.py#L601) (Line 601)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/accelerators/tpu.py#L601
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_is_vfio_group_a_tpu`
- **Arguments:** `vendor_path`
- **Keywords:** `{'encoding': "'ascii'"}`

```python
            with open(vendor_path, encoding="ascii") as f:
```

#### 13. [python/ray/_private/authentication/authentication_token_setup.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/authentication/authentication_token_setup.py#L43) (Line 43)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/authentication/authentication_token_setup.py#L43
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `generate_and_save_token`
- **Arguments:** `token_path, 'w'`
- **Keywords:** `{}`

```python
        with open(token_path, "w") as f:
```

#### 14. [python/ray/_private/external_storage.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/external_storage.py#L346) (Line 346)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/external_storage.py#L346
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystemStorage.spill_objects`
- **Arguments:** `url, 'wb'`
- **Keywords:** `{'buffering': 'self._buffer_size'}`

```python
        with open(url, "wb", buffering=self._buffer_size) as f:
```

#### 15. [python/ray/_private/external_storage.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/external_storage.py#L361) (Line 361)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/external_storage.py#L361
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileSystemStorage.restore_spilled_objects`
- **Arguments:** `base_url, 'rb'`
- **Keywords:** `{}`

```python
            with open(base_url, "rb") as f:
```

#### 16. [python/ray/_private/external_storage.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/external_storage.py#L506) (Line 506)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/external_storage.py#L506
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ExternalStorageSmartOpenImpl.spill_objects`
- **Arguments:** `url`
- **Keywords:** `{'mode': "'wb'", 'transport_params': 'self.transport_params'}`

```python
        with open(
            url,
            mode="wb",
            transport_params=self.transport_params,
        ) as file_like:
```

#### 17. [python/ray/_private/external_storage.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/external_storage.py#L530) (Line 530)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/external_storage.py#L530
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ExternalStorageSmartOpenImpl.restore_spilled_objects`
- **Arguments:** `base_url, 'rb'`
- **Keywords:** `{'transport_params': 'self.transport_params'}`

```python
            with open(base_url, "rb", transport_params=self.transport_params) as f:
```

#### 18. [python/ray/_private/label_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/label_utils.py#L90) (Line 90)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/label_utils.py#L90
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `parse_node_labels_from_yaml_file`
- **Arguments:** `path, 'r'`
- **Keywords:** `{}`

```python
    with open(path, "r") as file:
```

#### 19. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L87) (Line 87)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L87
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LogFileInfo.reopen_if_necessary`
- **Arguments:** `self.filename, 'rb'`
- **Keywords:** `{}`

```python
                self.file_handle = open(self.filename, "rb")
```

#### 20. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L106) (Line 106)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L106
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LogFileInfo.reopen_if_necessary`
- **Arguments:** `self.filename, 'rb'`
- **Keywords:** `{}`

```python
                    reopened_file = open(self.filename, "rb")
```

#### 21. [python/ray/_private/log_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L342) (Line 342)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/log_monitor.py#L342
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LogMonitor.open_closed_files`
- **Arguments:** `file_info.filename, 'rb'`
- **Keywords:** `{}`

```python
                    f = open(file_info.filename, "rb")
```

#### 22. [python/ray/_private/memory_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/memory_monitor.py#L126) (Line 126)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/memory_monitor.py#L126
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MemoryMonitor.__init__`
- **Arguments:** `'/sys/fs/cgroup/memory/memory.limit_in_bytes', 'rb'`
- **Keywords:** `{}`

```python
            with open("/sys/fs/cgroup/memory/memory.limit_in_bytes", "rb") as f:
```

#### 23. [python/ray/_private/metrics_agent.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/metrics_agent.py#L835) (Line 835)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/metrics_agent.py#L835
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PrometheusServiceDiscoveryWriter.write`
- **Arguments:** `temp_file_name, 'w'`
- **Keywords:** `{}`

```python
        with open(temp_file_name, "w") as json_file:
```

#### 24. [python/ray/_private/node.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/node.py#L512) (Line 512)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/node.py#L512
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Node._check_persisted_rocksdb_session_name`
- **Arguments:** `session_name_file, 'rb'`
- **Keywords:** `{}`

```python
            with open(session_name_file, "rb") as f:
```

#### 25. [python/ray/_private/node.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/node.py#L1017) (Line 1017)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/node.py#L1017
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Node._init_gcs_client`
- **Arguments:** `os.path.join(self._logs_dir, 'gcs_server.err')`
- **Keywords:** `{}`

```python
                with open(os.path.join(self._logs_dir, "gcs_server.err")) as err:
```

#### 26. [python/ray/_private/node.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/node.py#L1867) (Line 1867)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/node.py#L1867
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Node._kill_process_impl`
- **Arguments:** `process_info.stdout_file, 'r'`
- **Keywords:** `{}`

```python
                        with open(process_info.stdout_file, "r") as f:
```

#### 27. [python/ray/_private/node.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/node.py#L1870) (Line 1870)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/node.py#L1870
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Node._kill_process_impl`
- **Arguments:** `process_info.stderr_file, 'r'`
- **Keywords:** `{}`

```python
                        with open(process_info.stderr_file, "r") as f:
```

#### 28. [python/ray/_private/process_watcher.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/process_watcher.py#L83) (Line 83)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/process_watcher.py#L83
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `report_raylet_error_logs`
- **Arguments:** `log_path, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with open(log_path, "r", encoding="utf-8") as f:
```

#### 29. [python/ray/_private/runtime_env/_clonevirtualenv.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L160) (Line 160)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L160
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fixup_script_`
- **Arguments:** `filename, 'rb'`
- **Keywords:** `{}`

```python
    with open(filename, "rb") as f:
```

#### 30. [python/ray/_private/runtime_env/_clonevirtualenv.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L177) (Line 177)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L177
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `rewrite_shebang`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{}`

```python
        with open(filename, "wb") as f:
```

#### 31. [python/ray/_private/runtime_env/_clonevirtualenv.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L216) (Line 216)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L216
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fixup_activate`
- **Arguments:** `filename, 'rb'`
- **Keywords:** `{}`

```python
    with open(filename, "rb") as f:
```

#### 32. [python/ray/_private/runtime_env/_clonevirtualenv.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L220) (Line 220)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L220
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fixup_activate`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{}`

```python
    with open(filename, "wb") as f:
```

#### 33. [python/ray/_private/runtime_env/_clonevirtualenv.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L278) (Line 278)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L278
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fixup_pth_file`
- **Arguments:** `filename, 'r'`
- **Keywords:** `{}`

```python
    with open(filename, "r") as f:
```

#### 34. [python/ray/_private/runtime_env/_clonevirtualenv.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L293) (Line 293)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L293
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fixup_pth_file`
- **Arguments:** `filename, 'w'`
- **Keywords:** `{}`

```python
        with open(filename, "w") as f:
```

#### 35. [python/ray/_private/runtime_env/_clonevirtualenv.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L300) (Line 300)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L300
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fixup_egglink_file`
- **Arguments:** `filename, 'rb'`
- **Keywords:** `{}`

```python
    with open(filename, "rb") as f:
```

#### 36. [python/ray/_private/runtime_env/_clonevirtualenv.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L304) (Line 304)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/_clonevirtualenv.py#L304
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fixup_egglink_file`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{}`

```python
        with open(filename, "wb") as f:
```

#### 37. [python/ray/_private/runtime_env/conda.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/conda.py#L106) (Line 106)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/conda.py#L106
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_inject_ray_to_conda_site`
- **Arguments:** `os.path.join(site_packages_path, 'ray_shared.pth'), 'w'`
- **Keywords:** `{}`

```python
    with open(os.path.join(site_packages_path, "ray_shared.pth"), "w") as f:
```

#### 38. [python/ray/_private/runtime_env/conda.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/conda.py#L369) (Line 369)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/conda.py#L369
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CondaPlugin._create`
- **Arguments:** `conda_yaml_file, 'w'`
- **Keywords:** `{}`

```python
                    with open(conda_yaml_file, "w") as file:
```

#### 39. [python/ray/_private/runtime_env/conda_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/conda_utils.py#L85) (Line 85)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/conda_utils.py#L85
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_conda_env_name`
- **Arguments:** `conda_env_path`
- **Keywords:** `{}`

```python
    conda_env_contents = open(conda_env_path).read()
```

#### 40. [python/ray/_private/runtime_env/dependency_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/dependency_utils.py#L18) (Line 18)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/dependency_utils.py#L18
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `gen_requirements_txt`
- **Arguments:** `requirements_file, 'w'`
- **Keywords:** `{}`

```python
    with open(requirements_file, "w") as file:
```

#### 41. [python/ray/_private/runtime_env/dependency_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/dependency_utils.py#L59) (Line 59)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/dependency_utils.py#L59
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_ray_version_and_path`
- **Arguments:** `ray_version_path, 'rt'`
- **Keywords:** `{}`

```python
            with open(ray_version_path, "rt") as f:
```

#### 42. [python/ray/_private/runtime_env/image_uri.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/image_uri.py#L54) (Line 54)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/image_uri.py#L54
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_create_impl`
- **Arguments:** `result_file, 'r'`
- **Keywords:** `{}`

```python
        with open(result_file, "r") as f:
```

#### 43. [python/ray/_private/runtime_env/packaging.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L1163) (Line 1163)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L1163
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `unzip_package`
- **Arguments:** `member_path, 'wb'`
- **Keywords:** `{}`

```python
                with zip_ref.open(member) as source, open(member_path, "wb") as target:
```

#### 44. [python/ray/_private/runtime_env/packaging.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L1271) (Line 1271)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/packaging.py#L1271
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `untar_package`
- **Arguments:** `member_path, 'wb'`
- **Keywords:** `{}`

```python
                    open(member_path, "wb") as target,
```

#### 45. [python/ray/_private/runtime_env/pip.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/pip.py#L32) (Line 32)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/pip.py#L32
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_parse_requirements_file`
- **Arguments:** `file_path, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
    with open(file_path, "r", encoding="utf-8") as f:
```

#### 46. [python/ray/_private/runtime_env/plugin_schema_manager.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/plugin_schema_manager.py#L29) (Line 29)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/plugin_schema_manager.py#L29
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RuntimeEnvPluginSchemaManager._load_schemas`
- **Arguments:** `schema_path`
- **Keywords:** `{}`

```python
                with open(schema_path) as f:
```

#### 47. [python/ray/_private/runtime_env/protocol.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L266) (Line 266)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L266
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ProtocolsProvider.open_file`
- **Arguments:** `uri, mode`
- **Keywords:** `{}`

```python
                return open(uri, mode)
```

#### 48. [python/ray/_private/runtime_env/protocol.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L289) (Line 289)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/protocol.py#L289
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ProtocolsProvider.download_remote_uri`
- **Arguments:** `dest_file, 'wb'`
- **Keywords:** `{}`

```python
            with open(dest_file, "wb") as fout:
```

#### 49. [python/ray/_private/runtime_env/rocprof_sys.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/rocprof_sys.py#L91) (Line 91)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/runtime_env/rocprof_sys.py#L91
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RocProfSysPlugin._check_rocprof_sys_script`
- **Arguments:** `f'{test_folder}/test.py', 'w'`
- **Keywords:** `{}`

```python
        with open(f"{test_folder}/test.py", "w") as f:
```

#### 50. [python/ray/_private/services.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/services.py#L1011) (Line 1011)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/services.py#L1011
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `start_ray_process`
- **Arguments:** `gdb_init_path, 'w'`
- **Keywords:** `{}`

```python
        with open(gdb_init_path, "w") as gdb_init_file:
```

#### 51. [python/ray/_private/services.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/services.py#L1439) (Line 1439)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/services.py#L1439
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_log`
- **Arguments:** `dashboard_log, 'rb'`
- **Keywords:** `{}`

```python
                with open(dashboard_log, "rb") as f:
```

#### 52. [python/ray/_private/state.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/state.py#L669) (Line 669)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/state.py#L669
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GlobalState.chrome_tracing_dump`
- **Arguments:** `filename, 'w'`
- **Keywords:** `{}`

```python
            with open(filename, "w") as outfile:
```

#### 53. [python/ray/_private/state.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/state.py#L764) (Line 764)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/state.py#L764
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GlobalState.chrome_tracing_object_transfer_dump`
- **Arguments:** `filename, 'w'`
- **Keywords:** `{}`

```python
            with open(filename, "w") as outfile:
```

#### 54. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L83) (Line 83)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L83
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `write_ray_address`
- **Arguments:** `address_file, 'r'`
- **Keywords:** `{}`

```python
        with open(address_file, "r") as f:
```

#### 55. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L95) (Line 95)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L95
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `write_ray_address`
- **Arguments:** `address_file, 'w+'`
- **Keywords:** `{}`

```python
    with open(address_file, "w+") as f:
```

#### 56. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L103) (Line 103)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L103
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `read_ray_address`
- **Arguments:** `address_file, 'r'`
- **Keywords:** `{}`

```python
    with open(address_file, "r") as f:
```

#### 57. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L358) (Line 358)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L358
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `open_log`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    stream = open(path, **kwargs)
```

#### 58. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L384) (Line 384)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L384
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_docker_cpus`
- **Arguments:** `cpu_quota_file_name, 'r'`
- **Keywords:** `{}`

```python
                open(cpu_quota_file_name, "r") as quota_file,
```

#### 59. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L385) (Line 385)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L385
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_docker_cpus`
- **Arguments:** `cpu_period_file_name, 'r'`
- **Keywords:** `{}`

```python
                open(cpu_period_file_name, "r") as period_file,
```

#### 60. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L393) (Line 393)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L393
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_docker_cpus`
- **Arguments:** `cpu_max_file_name`
- **Keywords:** `{}`

```python
            max_file = open(cpu_max_file_name).read()
```

#### 61. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L411) (Line 411)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L411
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_docker_cpus`
- **Arguments:** `cpuset_file_name`
- **Keywords:** `{}`

```python
            with open(cpuset_file_name) as cpuset_file:
```

#### 62. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L516) (Line 516)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L516
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_cgroup_used_memory`
- **Arguments:** `memory_stat_filename, 'r'`
- **Keywords:** `{}`

```python
    with open(memory_stat_filename, "r") as f:
```

#### 63. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L524) (Line 524)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L524
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_cgroup_used_memory`
- **Arguments:** `memory_usage_filename, 'r'`
- **Keywords:** `{}`

```python
    with open(memory_usage_filename, "r") as f:
```

#### 64. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L564) (Line 564)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L564
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_cgroup_mem_stats`
- **Arguments:** `mem_limit_v1_file, 'r'`
- **Keywords:** `{}`

```python
            with open(mem_limit_v1_file, "r") as f:
```

#### 65. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L577) (Line 577)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L577
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_cgroup_mem_stats`
- **Arguments:** `mem_limit_v2_file, 'r'`
- **Keywords:** `{}`

```python
            with open(mem_limit_v2_file, "r") as f:
```

#### 66. [python/ray/_private/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L1740) (Line 1740)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/utils.py#L1740
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_current_node_cpu_model_name`
- **Arguments:** `'/proc/cpuinfo', 'r'`
- **Keywords:** `{}`

```python
        with open("/proc/cpuinfo", "r") as f:
```

#### 67. [python/ray/_private/worker.py](https://github.com/ray-project/ray/blob/master/python/ray/_private/worker.py#L2959) (Line 2959)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/_private/worker.py#L2959
- **Target Call:** `object_refs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get`
- **Arguments:** ``
- **Keywords:** `{'timeout': 'timeout'}`

```python
            return object_refs.get(timeout=timeout)
```

#### 68. [python/ray/air/integrations/wandb.py](https://github.com/ray-project/ray/blob/master/python/ray/air/integrations/wandb.py#L346) (Line 346)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/air/integrations/wandb.py#L346
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_set_api_key`
- **Arguments:** `api_key_file, 'rt'`
- **Keywords:** `{}`

```python
        with open(api_key_file, "rt") as fp:
```

#### 69. [python/ray/air/result.py](https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L173) (Line 173)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L173
- **Target Call:** `Path(fs_path, EXPR_RESULT_FILE).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Result.from_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        result_json_file = Path(fs_path, EXPR_RESULT_FILE).as_posix()
```

#### 70. [python/ray/air/result.py](https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L174) (Line 174)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L174
- **Target Call:** `Path(fs_path, EXPR_PROGRESS_FILE).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Result.from_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        progress_csv_file = Path(fs_path, EXPR_PROGRESS_FILE).as_posix()
```

#### 71. [python/ray/air/result.py](https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L176) (Line 176)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L176
- **Target Call:** `cls._read_file_as_str(fs, result_json_file).split` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Result.from_path`
- **Arguments:** `'\n'`
- **Keywords:** `{}`

```python
            lines = cls._read_file_as_str(fs, result_json_file).split("\n")
```

#### 72. [python/ray/air/result.py](https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L208) (Line 208)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L208
- **Target Call:** `Path(fs_path, checkpoint_dir_name).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Result.from_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    path=Path(fs_path, checkpoint_dir_name).as_posix(), filesystem=fs
```

#### 73. [python/ray/air/result.py](https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L238) (Line 238)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/air/result.py#L238
- **Target Call:** `Path(fs_path, EXPR_ERROR_PICKLE_FILE).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Result.from_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        error_file_path = Path(fs_path, EXPR_ERROR_PICKLE_FILE).as_posix()
```

#### 74. [python/ray/autoscaler/_private/_azure/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L89) (Line 89)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L89
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_configure_resource_group`
- **Arguments:** `template_path, 'r'`
- **Keywords:** `{}`

```python
    with open(template_path, "r") as template_fp:
```

#### 75. [python/ray/autoscaler/_private/_azure/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L392) (Line 392)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L392
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_configure_key_pair`
- **Arguments:** `public_key_path, 'r'`
- **Keywords:** `{}`

```python
        with open(public_key_path, "r") as f:
```

#### 76. [python/ray/autoscaler/_private/_azure/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L412) (Line 412)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L412
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_configure_key_pair`
- **Arguments:** `public_key_path, 'r'`
- **Keywords:** `{}`

```python
            with open(public_key_path, "r") as f:
```

#### 77. [python/ray/autoscaler/_private/_azure/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L423) (Line 423)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L423
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_configure_key_pair`
- **Arguments:** `private_key_path, 'w'`
- **Keywords:** `{'opener': 'lambda path, flags: os.open(path, flags, 384)'}`

```python
            with open(
                private_key_path,
                "w",
                opener=lambda path, flags: os.open(path, flags, 0o600),
            ) as f:
```

#### 78. [python/ray/autoscaler/_private/_azure/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L429) (Line 429)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/config.py#L429
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_configure_key_pair`
- **Arguments:** `public_key_path, 'w'`
- **Keywords:** `{}`

```python
            with open(public_key_path, "w") as f:
```

#### 79. [python/ray/autoscaler/_private/_azure/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/node_provider.py#L432) (Line 432)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/_azure/node_provider.py#L432
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AzureNodeProvider._create_node`
- **Arguments:** `template_path, 'r'`
- **Keywords:** `{}`

```python
        with open(template_path, "r") as template_fp:
```

#### 80. [python/ray/autoscaler/_private/aliyun/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/aliyun/config.py#L106) (Line 106)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/aliyun/config.py#L106
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_or_import_key_pair`
- **Arguments:** `key_path, 'w+'`
- **Keywords:** `{}`

```python
                with open(key_path, "w+") as f:
```

#### 81. [python/ray/autoscaler/_private/aliyun/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/aliyun/config.py#L113) (Line 113)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/aliyun/config.py#L113
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_or_import_key_pair`
- **Arguments:** `public_key_file`
- **Keywords:** `{}`

```python
            with open(public_key_file) as f:
```

#### 82. [python/ray/autoscaler/_private/autoscaler.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/autoscaler.py#L230) (Line 230)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/autoscaler.py#L230
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StandardAutoscaler.read_fn`
- **Arguments:** `config_reader`
- **Keywords:** `{}`

```python
                with open(config_reader) as f:
```

#### 83. [python/ray/autoscaler/_private/aws/cloudwatch/cloudwatch_helper.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/aws/cloudwatch/cloudwatch_helper.py#L350) (Line 350)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/aws/cloudwatch/cloudwatch_helper.py#L350
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CloudwatchHelper._load_config_file`
- **Arguments:** `json_config_path`
- **Keywords:** `{}`

```python
        with open(json_config_path) as f:
```

#### 84. [python/ray/autoscaler/_private/aws/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/aws/config.py#L413) (Line 413)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/aws/config.py#L413
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_configure_key_pair`
- **Arguments:** `key_path, 'w'`
- **Keywords:** `{'opener': 'partial(os.open, mode=384)'}`

```python
            with open(key_path, "w", opener=partial(os.open, mode=0o600)) as f:
```

#### 85. [python/ray/autoscaler/_private/cluster_dump.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/cluster_dump.py#L417) (Line 417)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/cluster_dump.py#L417
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `create_and_get_archive_from_remote_node`
- **Arguments:** `tmp, 'wb'`
- **Keywords:** `{}`

```python
    with open(tmp, "wb") as fp:
```

#### 86. [python/ray/autoscaler/_private/cluster_dump.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/cluster_dump.py#L569) (Line 569)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/cluster_dump.py#L569
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_info_from_ray_cluster_config`
- **Arguments:** `cluster_config`
- **Keywords:** `{}`

```python
    config = yaml.safe_load(open(cluster_config).read())
```

#### 87. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L288) (Line 288)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L288
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `create_or_update_cluster`
- **Arguments:** `config_file`
- **Keywords:** `{}`

```python
        config = yaml.safe_load(open(config_file).read())
```

#### 88. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L376) (Line 376)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L376
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_bootstrap_config`
- **Arguments:** `cache_key`
- **Keywords:** `{}`

```python
        config_cache = json.loads(open(cache_key).read())
```

#### 89. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L454) (Line 454)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L454
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_bootstrap_config`
- **Arguments:** `cache_key, 'w'`
- **Keywords:** `{}`

```python
        with open(cache_key, "w") as f:
```

#### 90. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L472) (Line 472)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L472
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `teardown_cluster`
- **Arguments:** `config_file`
- **Keywords:** `{}`

```python
    config = yaml.safe_load(open(config_file).read())
```

#### 91. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L619) (Line 619)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L619
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `kill_node`
- **Arguments:** `config_file`
- **Keywords:** `{}`

```python
    config = yaml.safe_load(open(config_file).read())
```

#### 92. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1223) (Line 1223)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1223
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `exec_cluster`
- **Arguments:** `config_file`
- **Keywords:** `{}`

```python
    config = yaml.safe_load(open(config_file).read())
```

#### 93. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1414) (Line 1414)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1414
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `rsync`
- **Arguments:** `config_file`
- **Keywords:** `{}`

```python
    config = yaml.safe_load(open(config_file).read())
```

#### 94. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1485) (Line 1485)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1485
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_head_node_ip`
- **Arguments:** `config_file`
- **Keywords:** `{}`

```python
    config = yaml.safe_load(open(config_file).read())
```

#### 95. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1509) (Line 1509)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1509
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_worker_node_ips`
- **Arguments:** `config_file`
- **Keywords:** `{}`

```python
    config = yaml.safe_load(open(config_file).read())
```

#### 96. [python/ray/autoscaler/_private/commands.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1641) (Line 1641)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/commands.py#L1641
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_local_dump_archive`
- **Arguments:** `tmp, 'rb'`
- **Keywords:** `{}`

```python
        with open(tmp, "rb") as fp:
```

#### 97. [python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py#L36) (Line 36)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py#L36
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_read_yaml`
- **Arguments:** `path, 'rt'`
- **Keywords:** `{}`

```python
    with open(path, "rt") as f:
```

#### 98. [python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py#L143) (Line 143)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py#L143
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_update_docker_status`
- **Arguments:** `docker_status_path, 'wt'`
- **Keywords:** `{}`

```python
    with open(docker_status_path, "wt") as f:
```

#### 99. [python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py#L227) (Line 227)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/docker_monitor.py#L227
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `start_monitor`
- **Arguments:** `docker_status_path, 'wt'`
- **Keywords:** `{}`

```python
        with open(docker_status_path, "wt") as f:
```

#### 100. [python/ray/autoscaler/_private/fake_multi_node/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L213) (Line 213)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L213
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `create_node_spec`
- **Arguments:** `filename, 'wt'`
- **Keywords:** `{}`

```python
                with open(filename, "wt") as f:
```

#### 101. [python/ray/autoscaler/_private/fake_multi_node/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L563) (Line 563)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L563
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FakeMultiNodeDockerProvider._load_node_state`
- **Arguments:** `self._node_state_path, 'rt'`
- **Keywords:** `{}`

```python
            with open(self._node_state_path, "rt") as f:
```

#### 102. [python/ray/autoscaler/_private/fake_multi_node/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L573) (Line 573)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L573
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FakeMultiNodeDockerProvider._save_node_state`
- **Arguments:** `self._node_state_path, 'wt'`
- **Keywords:** `{}`

```python
        with open(self._node_state_path, "wt") as f:
```

#### 103. [python/ray/autoscaler/_private/fake_multi_node/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L587) (Line 587)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L587
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FakeMultiNodeDockerProvider._update_docker_compose_config`
- **Arguments:** `self._docker_compose_config_path, 'wt'`
- **Keywords:** `{}`

```python
        with open(self._docker_compose_config_path, "wt") as f:
```

#### 104. [python/ray/autoscaler/_private/fake_multi_node/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L593) (Line 593)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/fake_multi_node/node_provider.py#L593
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FakeMultiNodeDockerProvider._update_docker_status`
- **Arguments:** `self._docker_status_path, 'rt'`
- **Keywords:** `{}`

```python
        with open(self._docker_status_path, "rt") as f:
```

#### 105. [python/ray/autoscaler/_private/gcp/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/gcp/config.py#L578) (Line 578)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/gcp/config.py#L578
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_configure_key_pair`
- **Arguments:** `private_key_path, 'w'`
- **Keywords:** `{'opener': 'partial(os.open, mode=384)'}`

```python
            with open(
                private_key_path,
                "w",
                opener=partial(os.open, mode=0o600),
            ) as f:
```

#### 106. [python/ray/autoscaler/_private/gcp/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/gcp/config.py#L585) (Line 585)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/gcp/config.py#L585
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_configure_key_pair`
- **Arguments:** `public_key_path, 'w'`
- **Keywords:** `{}`

```python
            with open(public_key_path, "w") as f:
```

#### 107. [python/ray/autoscaler/_private/kuberay/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/kuberay/node_provider.py#L176) (Line 176)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/kuberay/node_provider.py#L176
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `load_k8s_secrets`
- **Arguments:** `'/var/run/secrets/kubernetes.io/serviceaccount/token'`
- **Keywords:** `{}`

```python
    with open("/var/run/secrets/kubernetes.io/serviceaccount/token") as secret:
```

#### 108. [python/ray/autoscaler/_private/local/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L42) (Line 42)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L42
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ClusterState.__init__`
- **Arguments:** `self.save_path`
- **Keywords:** `{}`

```python
                    workers = json.loads(open(self.save_path).read())
```

#### 109. [python/ray/autoscaler/_private/local/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L94) (Line 94)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L94
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ClusterState.__init__`
- **Arguments:** `self.save_path, 'w'`
- **Keywords:** `{}`

```python
                with open(self.save_path, "w") as f:
```

#### 110. [python/ray/autoscaler/_private/local/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L103) (Line 103)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L103
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ClusterState.get`
- **Arguments:** `self.save_path`
- **Keywords:** `{}`

```python
                workers = json.loads(open(self.save_path).read())
```

#### 111. [python/ray/autoscaler/_private/local/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L113) (Line 113)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L113
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ClusterState.put`
- **Arguments:** `self.save_path, 'w'`
- **Keywords:** `{}`

```python
                with open(self.save_path, "w") as f:
```

#### 112. [python/ray/autoscaler/_private/local/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L138) (Line 138)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L138
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OnPremCoordinatorState.__init__`
- **Arguments:** `self.save_path`
- **Keywords:** `{}`

```python
                    nodes = json.loads(open(self.save_path).read())
```

#### 113. [python/ray/autoscaler/_private/local/node_provider.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L158) (Line 158)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/local/node_provider.py#L158
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OnPremCoordinatorState.__init__`
- **Arguments:** `self.save_path, 'w'`
- **Keywords:** `{}`

```python
                with open(self.save_path, "w") as f:
```

#### 114. [python/ray/autoscaler/_private/providers.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/providers.py#L296) (Line 296)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/providers.py#L296
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_default_config`
- **Arguments:** `path_to_default`
- **Keywords:** `{}`

```python
    with open(path_to_default) as f:
```

#### 115. [python/ray/autoscaler/_private/subprocess_output_util.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/subprocess_output_util.py#L371) (Line 371)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/subprocess_output_util.py#L371
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `run_cmd_redirected`
- **Arguments:** `tmpfile_path`
- **Keywords:** `{'mode': "'w'", 'buffering': '1'}`

```python
        with open(
            tmpfile_path,
            mode="w",
            # line buffering
            buffering=1,
        ) as tmp:
```

#### 116. [python/ray/autoscaler/_private/util.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/util.py#L161) (Line 161)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/util.py#L161
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `validate_config`
- **Arguments:** `schema_path`
- **Keywords:** `{}`

```python
    with open(schema_path) as f:
```

#### 117. [python/ray/autoscaler/_private/util.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/util.py#L455) (Line 455)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/util.py#L455
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `hash_launch_conf`
- **Arguments:** `os.path.expanduser(auth[key_type])`
- **Keywords:** `{}`

```python
            with open(os.path.expanduser(auth[key_type])) as key:
```

#### 118. [python/ray/autoscaler/_private/util.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/util.py#L488) (Line 488)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/util.py#L488
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `add_hash_of_file`
- **Arguments:** `fpath, 'rb'`
- **Keywords:** `{}`

```python
            with open(fpath, "rb") as f:
```

#### 119. [python/ray/autoscaler/_private/vsphere/cluster_operator_client.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/cluster_operator_client.py#L153) (Line 153)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/cluster_operator_client.py#L153
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ClusterOperatorClient._create_tls_secrets`
- **Arguments:** `cert_path`
- **Keywords:** `{}`

```python
            with open(cert_path) as f:
```

#### 120. [python/ray/autoscaler/_private/vsphere/cluster_operator_client.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/cluster_operator_client.py#L156) (Line 156)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/cluster_operator_client.py#L156
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ClusterOperatorClient._create_tls_secrets`
- **Arguments:** `key_path`
- **Keywords:** `{}`

```python
            with open(key_path) as f:
```

#### 121. [python/ray/autoscaler/_private/vsphere/cluster_operator_client.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/cluster_operator_client.py#L673) (Line 673)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/cluster_operator_client.py#L673
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ClusterOperatorClient._create_ssh_secret`
- **Arguments:** `private_key_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(private_key_path, "rb") as ssh_key:
```

#### 122. [python/ray/autoscaler/_private/vsphere/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/config.py#L141) (Line 141)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/config.py#L141
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_create_ssh_keys`
- **Arguments:** `PRIVATE_KEY_PATH, 'wb'`
- **Keywords:** `{}`

```python
    with open(PRIVATE_KEY_PATH, "wb") as pvt_key:
```

#### 123. [python/ray/autoscaler/_private/vsphere/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/config.py#L146) (Line 146)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/_private/vsphere/config.py#L146
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_create_ssh_keys`
- **Arguments:** `PUBLIC_KEY_PATH, 'wb'`
- **Keywords:** `{}`

```python
    with open(PUBLIC_KEY_PATH, "wb") as pub_key:
```

#### 124. [python/ray/autoscaler/launch_and_verify_cluster.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/launch_and_verify_cluster.py#L173) (Line 173)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/launch_and_verify_cluster.py#L173
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `azure_authenticate`
- **Arguments:** `cert_path, 'w'`
- **Keywords:** `{}`

```python
    with open(cert_path, "w") as f:
```

#### 125. [python/ray/autoscaler/v2/instance_manager/config.py](https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/v2/instance_manager/config.py#L471) (Line 471)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/autoscaler/v2/instance_manager/config.py#L471
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `FileConfigReader._read`
- **Arguments:** `self._config_file_path`
- **Keywords:** `{}`

```python
        with open(self._config_file_path) as f:
```

#### 126. [python/ray/cluster_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/cluster_utils.py#L62) (Line 62)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/cluster_utils.py#L62
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AutoscalingCluster._generate_config`
- **Arguments:** `os.path.join(os.path.dirname(ray.__file__), 'autoscaler/_private/fake_multi_node/example.yaml')`
- **Keywords:** `{}`

```python
            open(
                os.path.join(
                    os.path.dirname(ray.__file__),
                    "autoscaler/_private/fake_multi_node/example.yaml",
                )
            )
```

#### 127. [python/ray/cluster_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/cluster_utils.py#L92) (Line 92)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/cluster_utils.py#L92
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AutoscalingCluster.start`
- **Arguments:** `fake_config, 'w'`
- **Keywords:** `{}`

```python
        with open(fake_config, "w") as f:
```

#### 128. [python/ray/dashboard/k8s_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/k8s_utils.py#L71) (Line 71)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/k8s_utils.py#L71
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_cpu_usage`
- **Arguments:** `CPU_USAGE_PATH`
- **Keywords:** `{}`

```python
        return int(open(CPU_USAGE_PATH).read())
```

#### 129. [python/ray/dashboard/k8s_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/k8s_utils.py#L74) (Line 74)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/k8s_utils.py#L74
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_cpu_usage`
- **Arguments:** `CPU_USAGE_PATH_V2`
- **Keywords:** `{}`

```python
        cpu_stat_text = open(CPU_USAGE_PATH_V2).read()
```

#### 130. [python/ray/dashboard/k8s_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/k8s_utils.py#L94) (Line 94)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/k8s_utils.py#L94
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_system_usage`
- **Arguments:** `PROC_STAT_PATH`
- **Keywords:** `{}`

```python
    cpu_summary_str = open(PROC_STAT_PATH).read().split("\n")[0]
```

#### 131. [python/ray/dashboard/k8s_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/k8s_utils.py#L108) (Line 108)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/k8s_utils.py#L108
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_host_num_cpus`
- **Arguments:** `PROC_STAT_PATH`
- **Keywords:** `{}`

```python
        proc_stat_lines = open(PROC_STAT_PATH).read().split("\n")
```

#### 132. [python/ray/dashboard/modules/dashboard_sdk.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/dashboard_sdk.py#L63) (Line 63)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/dashboard_sdk.py#L63
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `parse_runtime_env_args`
- **Arguments:** `runtime_env, 'r'`
- **Keywords:** `{}`

```python
        with open(runtime_env, "r") as f:
```

#### 133. [python/ray/dashboard/modules/event/event_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/event/event_utils.py#L73) (Line 73)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/event/event_utils.py#L73
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_read_file`
- **Arguments:** `file, 'rb'`
- **Keywords:** `{'closefd': 'closefd'}`

```python
    with open(file, "rb", closefd=closefd) as f:
```

#### 134. [python/ray/dashboard/modules/job/job_log_storage_client.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/job_log_storage_client.py#L22) (Line 22)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/job_log_storage_client.py#L22
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `JobLogStorageClient.get_logs`
- **Arguments:** `self.get_log_file_path(job_id), 'r'`
- **Keywords:** `{}`

```python
            with open(self.get_log_file_path(job_id), "r") as f:
```

#### 135. [python/ray/dashboard/modules/job/job_manager.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/job_manager.py#L335) (Line 335)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/job_manager.py#L335
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `JobManager._monitor_job_internal`
- **Arguments:** `log_path, 'a'`
- **Keywords:** `{}`

```python
                    with open(log_path, "a") as log_file:
```

#### 136. [python/ray/dashboard/modules/job/job_supervisor.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/job_supervisor.py#L178) (Line 178)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/job_supervisor.py#L178
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `JobSupervisor._exec_entrypoint`
- **Arguments:** `logs_path, 'a'`
- **Keywords:** `{}`

```python
        with open(logs_path, "a") as logs_file:
```

#### 137. [python/ray/dashboard/modules/job/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/utils.py#L69) (Line 69)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/utils.py#L69
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `file_tail_iterator`
- **Arguments:** `path, 'r'`
- **Keywords:** `{}`

```python
    with open(path, "r") as f:
```

#### 138. [python/ray/dashboard/modules/job/utils.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/utils.py#L332) (Line 332)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/job/utils.py#L332
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `fast_tail_last_n_lines`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    with open(path, "rb") as f:
```

#### 139. [python/ray/dashboard/modules/log/log_agent.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/log/log_agent.py#L366) (Line 366)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/log/log_agent.py#L366
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LogAgentV1Grpc.StreamLog`
- **Arguments:** `filepath, 'rb'`
- **Keywords:** `{}`

```python
            with open(filepath, "rb") as f:
```

#### 140. [python/ray/dashboard/modules/metrics/grafana_dashboard_factory.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/grafana_dashboard_factory.py#L206) (Line 206)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/grafana_dashboard_factory.py#L206
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_generate_grafana_dashboard`
- **Arguments:** `os.path.join(os.path.dirname(__file__), 'dashboards', base_file_name)`
- **Keywords:** `{}`

```python
        open(os.path.join(os.path.dirname(__file__), "dashboards", base_file_name))
```

#### 141. [python/ray/dashboard/modules/metrics/install_and_start_prometheus.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/install_and_start_prometheus.py#L44) (Line 44)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/install_and_start_prometheus.py#L44
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `download_file`
- **Arguments:** `filename, 'wb'`
- **Keywords:** `{}`

```python
        with open(filename, "wb") as file:
```

#### 142. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L231) (Line 231)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L231
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_config_output_path, 'grafana.ini'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_config_output_path,
                "grafana.ini",
            ),
            "w",
        ) as f:
```

#### 143. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L252) (Line 252)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L252
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(dashboard_provisioning_path, 'default.yml'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                dashboard_provisioning_path,
                "default.yml",
            ),
            "w",
        ) as f:
```

#### 144. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L290) (Line 290)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L290
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(data_sources_path, 'default.yml'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                data_sources_path,
                "default.yml",
            ),
            "w",
        ) as f:
```

#### 145. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L311) (Line 311)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L311
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_dashboard_output_dir, 'default_grafana_dashboard.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_dashboard_output_dir,
                "default_grafana_dashboard.json",
            ),
            "w",
        ) as f:
```

#### 146. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L323) (Line 323)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L323
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_dashboard_output_dir, 'serve_grafana_dashboard.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_dashboard_output_dir,
                "serve_grafana_dashboard.json",
            ),
            "w",
        ) as f:
```

#### 147. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L332) (Line 332)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L332
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_dashboard_output_dir, 'serve_deployment_grafana_dashboard.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_dashboard_output_dir,
                "serve_deployment_grafana_dashboard.json",
            ),
            "w",
        ) as f:
```

#### 148. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L344) (Line 344)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L344
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_dashboard_output_dir, 'serve_llm_grafana_dashboard.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_dashboard_output_dir,
                "serve_llm_grafana_dashboard.json",
            ),
            "w",
        ) as f:
```

#### 149. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L356) (Line 356)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L356
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_dashboard_output_dir, 'serve_llm_sglang_grafana_dashboard.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_dashboard_output_dir,
                "serve_llm_sglang_grafana_dashboard.json",
            ),
            "w",
        ) as f:
```

#### 150. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L368) (Line 368)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L368
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_dashboard_output_dir, 'data_grafana_dashboard.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_dashboard_output_dir,
                "data_grafana_dashboard.json",
            ),
            "w",
        ) as f:
```

#### 151. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L380) (Line 380)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L380
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_dashboard_output_dir, 'data_llm_grafana_dashboard.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_dashboard_output_dir,
                "data_llm_grafana_dashboard.json",
            ),
            "w",
        ) as f:
```

#### 152. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L392) (Line 392)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L392
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_grafana_configs`
- **Arguments:** `os.path.join(self._grafana_dashboard_output_dir, 'train_grafana_dashboard.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(
                self._grafana_dashboard_output_dir,
                "train_grafana_dashboard.json",
            ),
            "w",
        ) as f:
```

#### 153. [python/ray/dashboard/modules/metrics/metrics_head.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L427) (Line 427)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/metrics/metrics_head.py#L427
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MetricsHead._create_default_prometheus_configs`
- **Arguments:** `prometheus_config_output_path, 'w'`
- **Keywords:** `{}`

```python
        with open(prometheus_config_output_path, "w") as f:
```

#### 154. [python/ray/dashboard/modules/reporter/gpu_profile_manager.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/reporter/gpu_profile_manager.py#L147) (Line 147)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/reporter/gpu_profile_manager.py#L147
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GpuProfilingManager.start_monitoring_daemon`
- **Arguments:** `self._daemon_log_file_path, 'ab'`
- **Keywords:** `{}`

```python
            with open(self._daemon_log_file_path, "ab") as log_file:
```

#### 155. [python/ray/dashboard/modules/reporter/profile_manager.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/reporter/profile_manager.py#L201) (Line 201)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/reporter/profile_manager.py#L201
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CpuProfilingManager.cpu_profile`
- **Arguments:** `profile_file_path, 'rb'`
- **Keywords:** `{}`

```python
            return True, open(profile_file_path, "rb").read()
```

#### 156. [python/ray/dashboard/modules/reporter/profile_manager.py](https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/reporter/profile_manager.py#L276) (Line 276)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/dashboard/modules/reporter/profile_manager.py#L276
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MemoryProfilingManager.get_profile_result`
- **Arguments:** `profile_visualize_path, 'rb'`
- **Keywords:** `{}`

```python
        return True, open(profile_visualize_path, "rb").read()
```

#### 157. [python/ray/data/_internal/datasource/_lerobot_compat.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40) (Line 40)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40
- **Target Call:** `fsspec.open(video_path, **opts).__enter__` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CredsVideoDecoderCache.get_decoder`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    file_handle = fsspec.open(video_path, **opts).__enter__()
```

#### 158. [python/ray/data/_internal/datasource/_lerobot_compat.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40) (Line 40)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/_lerobot_compat.py#L40
- **Target Call:** `fsspec.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_CredsVideoDecoderCache.get_decoder`
- **Arguments:** `video_path`
- **Keywords:** `{}`

```python
                    file_handle = fsspec.open(video_path, **opts).__enter__()
```

#### 159. [python/ray/data/_internal/datasource/bigquery_datasink.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/bigquery_datasink.py#L94) (Line 94)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/bigquery_datasink.py#L94
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BigQueryDatasink._write_single_block`
- **Arguments:** `fp, 'rb'`
- **Keywords:** `{}`

```python
                    with open(fp, "rb") as source_file:
```

#### 160. [python/ray/data/_internal/datasource/databricks_uc_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/databricks_uc_datasource.py#L193) (Line 193)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/databricks_uc_datasource.py#L193
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `DatabricksUCDatasource.read_fn`
- **Arguments:** `mock_setup_fn_path, 'rb'`
- **Keywords:** `{}`

```python
                    with open(mock_setup_fn_path, "rb") as f:
```

#### 161. [python/ray/data/_internal/datasource/kafka_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L792) (Line 792)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L792
- **Target Call:** `start_offset.get(topic_name, {}).get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `KafkaDatasource.get_read_tasks`
- **Arguments:** `partition_id, 'earliest'`
- **Keywords:** `{}`

```python
                start_offset.get(topic_name, {}).get(partition_id, "earliest")
```

#### 162. [python/ray/data/_internal/datasource/kafka_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L792) (Line 792)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L792
- **Target Call:** `start_offset.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `KafkaDatasource.get_read_tasks`
- **Arguments:** `topic_name, {}`
- **Keywords:** `{}`

```python
                start_offset.get(topic_name, {}).get(partition_id, "earliest")
```

#### 163. [python/ray/data/_internal/datasource/kafka_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L797) (Line 797)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L797
- **Target Call:** `end_offset.get(topic_name, {}).get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `KafkaDatasource.get_read_tasks`
- **Arguments:** `partition_id, 'latest'`
- **Keywords:** `{}`

```python
                end_offset.get(topic_name, {}).get(partition_id, "latest")
```

#### 164. [python/ray/data/_internal/datasource/kafka_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L797) (Line 797)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/kafka_datasource.py#L797
- **Target Call:** `end_offset.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `KafkaDatasource.get_read_tasks`
- **Arguments:** `topic_name, {}`
- **Keywords:** `{}`

```python
                end_offset.get(topic_name, {}).get(partition_id, "latest")
```

#### 165. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L235) (Line 235)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L235
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_build_schema`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    with fs.open(path, "rb") as f:
```

#### 166. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L412) (Line 412)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L412
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `root_uri`
- **Keywords:** `{}`

```python
    protocol, rest = split_protocol(root_uri)
```

#### 167. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L433) (Line 433)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L433
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `filesystem`
- **Keywords:** `{}`

```python
            fs = ArrowFSWrapper(filesystem)
```

#### 168. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L446) (Line 446)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L446
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `video_root_uri`
- **Keywords:** `{}`

```python
        _, fs_root = split_protocol(video_root_uri)
```

#### 169. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L451) (Line 451)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L451
- **Target Call:** `fsspec.core.url_to_fs` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `video_root_uri`
- **Keywords:** `{}`

```python
        fs, fs_root = fsspec.core.url_to_fs(video_root_uri, **video_storage_options)
```

#### 170. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L461) (Line 461)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L461
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_resolve_filesystem`
- **Arguments:** `pa_fs`
- **Keywords:** `{}`

```python
        fs = ArrowFSWrapper(pa_fs)
```

#### 171. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L477) (Line 477)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L477
- **Target Call:** `fs.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_lerobot_metadata`
- **Arguments:** `f'{fs_root}/meta/info.json'`
- **Keywords:** `{}`

```python
    if not fs.exists(f"{fs_root}/meta/info.json"):
```

#### 172. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L491) (Line 491)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L491
- **Target Call:** `fs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_lerobot_metadata`
- **Arguments:** `f'{fs_root}/meta', os.path.join(local_root, 'meta')`
- **Keywords:** `{'recursive': 'True'}`

```python
    fs.get(f"{fs_root}/meta", os.path.join(local_root, "meta"), recursive=True)
```

#### 173. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L813) (Line 813)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L813
- **Target Call:** `fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_read_lerobot_segment`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
        with fs.open(path, "rb") as f:
```

#### 174. [python/ray/data/_internal/datasource/lerobot_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1290) (Line 1290)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/lerobot_datasource.py#L1290
- **Target Call:** `root.fs.open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_decode_image_frames`
- **Arguments:** `p, 'rb'`
- **Keywords:** `{}`

```python
                with root.fs.open(p, "rb") as fh:
```

#### 175. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L317) (Line 317)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L317
- **Target Call:** `fsspec.filesystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `'zip'`
- **Keywords:** `{'fo': 'self.paths[0]'}`

```python
            self._fs = fsspec.filesystem("zip", fo=self.paths[0])
```

#### 176. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L327) (Line 327)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L327
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `pa_fs`
- **Keywords:** `{}`

```python
            self._fs = ArrowFSWrapper(pa_fs)
```

#### 177. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L337) (Line 337)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L337
- **Target Call:** `ArrowFSWrapper` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `filesystem`
- **Keywords:** `{}`

```python
                self._fs = ArrowFSWrapper(filesystem)
```

#### 178. [python/ray/data/_internal/datasource/zarrv2_datasource.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L353) (Line 353)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/datasource/zarrv2_datasource.py#L353
- **Target Call:** `split_protocol` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZarrV2Datasource.__init__`
- **Arguments:** `self.paths[0]`
- **Keywords:** `{}`

```python
                _, store_path = split_protocol(self.paths[0])
```

#### 179. [python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py#L334) (Line 334)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/execution/operators/shuffle_operators/external_shuffle_runtime.py#L334
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ShuffleFlightServer.do_action`
- **Arguments:** `fpath, 'rb'`
- **Keywords:** `{}`

```python
                with open(fpath, "rb") as f:
```

#### 180. [python/ray/data/_internal/logging.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/logging.py#L182) (Line 182)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/logging.py#L182
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_logging_config`
- **Arguments:** `config_path`
- **Keywords:** `{}`

```python
        with open(config_path) as file:
```

#### 181. [python/ray/data/_internal/util.py](https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/util.py#L1455) (Line 1455)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/_internal/util.py#L1455
- **Target Call:** `self._fs.move` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RetryingPyFileSystemHandler.move`
- **Arguments:** `src, dest`
- **Keywords:** `{}`

```python
            lambda: self._fs.move(src, dest), f"move from {src} to {dest}"
```

#### 182. [python/ray/data/datasource/path_util.py](https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/path_util.py#L39) (Line 39)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/datasource/path_util.py#L39
- **Target Call:** `HTTPFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_get_fsspec_http_filesystem`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    return PyFileSystem(FSSpecHandler(HTTPFileSystem()))
```

#### 183. [python/ray/data/read_api.py](https://github.com/ray-project/ray/blob/master/python/ray/data/read_api.py#L4582) (Line 4582)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/data/read_api.py#L4582
- **Target Call:** `fsspec.implementations.http.HTTPFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `from_huggingface`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                http = fsspec.implementations.http.HTTPFileSystem()
```

#### 184. [python/ray/experimental/raysort/main.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L174) (Line 174)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L174
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `generate_input`
- **Arguments:** `constants.INPUT_MANIFEST_FILE, 'w'`
- **Keywords:** `{}`

```python
    with open(constants.INPUT_MANIFEST_FILE, "w") as fout:
```

#### 185. [python/ray/experimental/raysort/main.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L187) (Line 187)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L187
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_manifest`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
    with open(path) as fin:
```

#### 186. [python/ray/experimental/raysort/main.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L255) (Line 255)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L255
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_merge_impl`
- **Arguments:** `pinfo.path, 'wb'`
- **Keywords:** `{}`

```python
        with open(pinfo.path, "wb") as fout:
```

#### 187. [python/ray/experimental/raysort/main.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L392) (Line 392)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L392
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `sort_main`
- **Arguments:** `constants.OUTPUT_MANIFEST_FILE, 'w'`
- **Keywords:** `{}`

```python
        with open(constants.OUTPUT_MANIFEST_FILE, "w") as fout:
```

#### 188. [python/ray/experimental/raysort/main.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L417) (Line 417)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/raysort/main.py#L417
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `validate_part`
- **Arguments:** `sum_path, 'rb'`
- **Keywords:** `{}`

```python
    with open(sum_path, "rb") as fin:
```

#### 189. [python/ray/experimental/sandbox/_internal/image_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L258) (Line 258)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L258
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `extract_tar_layer`
- **Arguments:** `target_path, 'wb'`
- **Keywords:** `{}`

```python
                with open(target_path, "wb") as f_out:
```

#### 190. [python/ray/experimental/sandbox/_internal/image_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L310) (Line 310)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L310
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `pull_and_extract_container_image`
- **Arguments:** `lock_path, 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
    with open(lock_path, "w", encoding="utf-8") as f_lock:
```

#### 191. [python/ray/experimental/sandbox/_internal/image_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L333) (Line 333)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L333
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `pull_and_extract_container_image`
- **Arguments:** `image, 'rb'`
- **Keywords:** `{}`

```python
                    with open(image, "rb") as f:
```

#### 192. [python/ray/experimental/sandbox/_internal/image_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L342) (Line 342)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L342
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `pull_and_extract_container_image`
- **Arguments:** `tar_path, 'rb'`
- **Keywords:** `{}`

```python
                    with open(tar_path, "rb") as f:
```

#### 193. [python/ray/experimental/sandbox/_internal/image_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L422) (Line 422)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L422
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `pull_and_extract_container_image`
- **Arguments:** `os.path.join(tmp_extract_dir, '.image_config.json'), 'wb'`
- **Keywords:** `{}`

```python
                                with open(
                                    os.path.join(tmp_extract_dir, ".image_config.json"),
                                    "wb",
                                ) as f_cfg:
```

#### 194. [python/ray/experimental/sandbox/_internal/image_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L468) (Line 468)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/_internal/image_utils.py#L468
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `pull_and_extract_container_image`
- **Arguments:** `os.path.join(tmp_extract_dir, '.extracted'), 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
            with open(
                os.path.join(tmp_extract_dir, ".extracted"), "w", encoding="utf-8"
            ) as f_mark:
```

#### 195. [python/ray/experimental/sandbox/backend/gvisor.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L102) (Line 102)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/backend/gvisor.py#L102
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `GVisorSandboxBackend.create_sandbox`
- **Arguments:** `stderr_log_path, 'w+'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        stderr_file = open(stderr_log_path, "w+", encoding="utf-8")
```

#### 196. [python/ray/experimental/sandbox/image_manager.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/image_manager.py#L29) (Line 29)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/image_manager.py#L29
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_default_oci_spec`
- **Arguments:** `config_path, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with open(config_path, "r", encoding="utf-8") as f:
```

#### 197. [python/ray/experimental/sandbox/image_manager.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/image_manager.py#L262) (Line 262)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/image_manager.py#L262
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ImageManager.get_image_config`
- **Arguments:** `config_path, 'r'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
                with open(config_path, "r", encoding="utf-8") as f:
```

#### 198. [python/ray/experimental/sandbox/image_manager.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/image_manager.py#L442) (Line 442)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/image_manager.py#L442
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ImageManager.prepare_oci_bundle`
- **Arguments:** `config_json_path, 'w'`
- **Keywords:** `{'encoding': "'utf-8'"}`

```python
        with open(config_json_path, "w", encoding="utf-8") as f:
```

#### 199. [python/ray/experimental/sandbox/runtime.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/runtime.py#L172) (Line 172)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/runtime.py#L172
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SandboxRuntime.upload_file`
- **Arguments:** `local_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(local_path, "rb") as f:
```

#### 200. [python/ray/experimental/sandbox/runtime.py](https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/runtime.py#L190) (Line 190)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/experimental/sandbox/runtime.py#L190
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `SandboxRuntime.download_file`
- **Arguments:** `local_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(local_path, "wb") as f:
```

#### 201. [python/ray/llm/_internal/common/base_pydantic.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/base_pydantic.py#L30) (Line 30)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/base_pydantic.py#L30
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BaseModelExtended.from_file`
- **Arguments:** `path, 'r'`
- **Keywords:** `{}`

```python
        with open(path, "r") as f:
```

#### 202. [python/ray/llm/_internal/common/utils/cloud_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L184) (Line 184)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L184
- **Target Call:** `fs_class.get_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CloudFileSystem.get_file`
- **Arguments:** `object_uri, decode_as_utf_8`
- **Keywords:** `{}`

```python
        return fs_class.get_file(object_uri, decode_as_utf_8)
```

#### 203. [python/ray/llm/_internal/common/utils/cloud_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L245) (Line 245)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L245
- **Target Call:** `fs_class.get_file` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CloudFileSystem.download_model`
- **Arguments:** `hash_uri`
- **Keywords:** `{'decode_as_utf_8': 'True'}`

```python
            hash_content = fs_class.get_file(hash_uri, decode_as_utf_8=True)
```

#### 204. [python/ray/llm/_internal/common/utils/cloud_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L263) (Line 263)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L263
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CloudFileSystem.download_model`
- **Arguments:** `os.path.join(main_dir, 'main'), 'w'`
- **Keywords:** `{}`

```python
            with open(os.path.join(main_dir, "main"), "w") as f:
```

#### 205. [python/ray/llm/_internal/common/utils/cloud_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L320) (Line 320)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L320
- **Target Call:** `refs_main.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CloudFileSystem.upload_model`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            if refs_main.exists():
```

#### 206. [python/ray/llm/_internal/common/utils/cloud_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L322) (Line 322)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/cloud_utils.py#L322
- **Target Call:** `refs_main.read_text` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `CloudFileSystem.upload_model`
- **Arguments:** ``
- **Keywords:** `{}`

```python
                    local_path, "snapshots", refs_main.read_text().strip()
```

#### 207. [python/ray/llm/_internal/common/utils/download_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/download_utils.py#L93) (Line 93)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/download_utils.py#L93
- **Target Call:** `model_dir_refs_main.exists` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_model_location_on_disk`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        if model_dir_refs_main.exists():
```

#### 208. [python/ray/llm/_internal/common/utils/download_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/download_utils.py#L98) (Line 98)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/llm/_internal/common/utils/download_utils.py#L98
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `get_model_location_on_disk`
- **Arguments:** `model_dir_refs_main, 'r'`
- **Keywords:** `{}`

```python
            with open(model_dir_refs_main, "r") as f:
```

#### 209. [python/ray/serve/_private/deployment_state.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/deployment_state.py#L721) (Line 721)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/deployment_state.py#L721
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `print_verbose_scaling_log`
- **Arguments:** `log_path`
- **Keywords:** `{}`

```python
        with open(log_path) as f:
```

#### 210. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L208) (Line 208)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L208
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_write_if_changed`
- **Arguments:** `path`
- **Keywords:** `{}`

```python
        with open(path) as f:
```

#### 211. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L213) (Line 213)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L213
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_write_if_changed`
- **Arguments:** `path, 'w'`
- **Keywords:** `{}`

```python
    with open(path, "w") as f:
```

#### 212. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L221) (Line 221)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L221
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_tail_file`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
        with open(path, "rb") as f:
```

#### 213. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L922) (Line 922)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L922
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HAProxyApi._initialize_directories_and_error_files`
- **Arguments:** `error_file_path, 'w'`
- **Keywords:** `{}`

```python
        with open(error_file_path, "w") as ef:
```

#### 214. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L991) (Line 991)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L991
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HAProxyApi._is_our_haproxy`
- **Arguments:** `f'/proc/{pid}/cmdline', 'rb'`
- **Keywords:** `{}`

```python
            with open(f"/proc/{pid}/cmdline", "rb") as f:
```

#### 215. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1120) (Line 1120)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1120
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HAProxyApi._start_and_wait_for_haproxy`
- **Arguments:** `stdout_path, 'wb'`
- **Keywords:** `{'buffering': '0'}`

```python
        with open(stdout_path, "wb", buffering=0) as stdout_file, open(
```

#### 216. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1120) (Line 1120)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1120
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HAProxyApi._start_and_wait_for_haproxy`
- **Arguments:** `stderr_path, 'wb'`
- **Keywords:** `{'buffering': '0'}`

```python
        with open(stdout_path, "wb", buffering=0) as stdout_file, open(
            stderr_path, "wb", buffering=0
        ) as stderr_file:
```

#### 217. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1154) (Line 1154)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1154
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HAProxyApi._save_server_state`
- **Arguments:** `self.cfg.server_state_file, 'w'`
- **Keywords:** `{}`

```python
        with open(self.cfg.server_state_file, "w") as f:
```

#### 218. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1425) (Line 1425)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1425
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HAProxyApi._generate_config_file_internal`
- **Arguments:** `lock_file_path, 'w'`
- **Keywords:** `{}`

```python
            with open(lock_file_path, "w") as lock_f:
```

#### 219. [python/ray/serve/_private/haproxy.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1428) (Line 1428)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/haproxy.py#L1428
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HAProxyApi._generate_config_file_internal`
- **Arguments:** `self.config_file_path, 'w'`
- **Keywords:** `{}`

```python
                    with open(self.config_file_path, "w") as f:
```

#### 220. [python/ray/serve/_private/tracing_utils.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/tracing_utils.py#L81) (Line 81)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/_private/tracing_utils.py#L81
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `default_tracing_exporter`
- **Arguments:** `spans_file, 'a'`
- **Keywords:** `{}`

```python
    out_file = open(spans_file, "a")
```

#### 221. [python/ray/serve/scripts.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/scripts.py#L229) (Line 229)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/scripts.py#L229
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_generate_config_from_file_or_import_path`
- **Arguments:** `config_path, 'r'`
- **Keywords:** `{}`

```python
        with open(config_path, "r") as config_file:
```

#### 222. [python/ray/serve/scripts.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/scripts.py#L482) (Line 482)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/scripts.py#L482
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `run`
- **Arguments:** `config_path, 'r'`
- **Keywords:** `{}`

```python
        with open(config_path, "r") as config_file:
```

#### 223. [python/ray/serve/scripts.py](https://github.com/ray-project/ray/blob/master/python/ray/serve/scripts.py#L938) (Line 938)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/serve/scripts.py#L938
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `build`
- **Arguments:** `output_path, 'w'`
- **Keywords:** `{}`

```python
    with open(output_path, "w") if output_path else sys.stdout as f:
```

#### 224. [python/ray/train/_checkpoint.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_checkpoint.py#L289) (Line 289)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/_checkpoint.py#L289
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Checkpoint.as_directory`
- **Arguments:** `del_lock_path, 'a'`
- **Keywords:** `{}`

```python
            open(del_lock_path, "a").close()
```

#### 225. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L465) (Line 465)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L465
- **Target Call:** `Path(self.storage_fs_path).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self.storage_fs_path = Path(self.storage_fs_path).as_posix()
```

#### 226. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L498) (Line 498)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L498
- **Target Call:** `Path(self.experiment_fs_path, _VALIDATE_STORAGE_MARKER_FILENAME).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext._create_validation_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        valid_file = Path(
            self.experiment_fs_path, _VALIDATE_STORAGE_MARKER_FILENAME
        ).as_posix()
```

#### 227. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L507) (Line 507)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L507
- **Target Call:** `Path(self.experiment_fs_path, _VALIDATE_STORAGE_MARKER_FILENAME).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext._check_validation_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        valid_file = Path(
            self.experiment_fs_path, _VALIDATE_STORAGE_MARKER_FILENAME
        ).as_posix()
```

#### 228. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L617) (Line 617)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L617
- **Target Call:** `Path(self.storage_fs_path, self.experiment_dir_name).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext.experiment_fs_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return Path(self.storage_fs_path, self.experiment_dir_name).as_posix()
```

#### 229. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L657) (Line 657)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L657
- **Target Call:** `Path(self.experiment_fs_path, self.trial_dir_name).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext.trial_fs_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return Path(self.experiment_fs_path, self.trial_dir_name).as_posix()
```

#### 230. [python/ray/train/_internal/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L713) (Line 713)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/_internal/storage.py#L713
- **Target Call:** `Path(self.trial_fs_path, self.checkpoint_dir_name).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext.checkpoint_fs_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return Path(self.trial_fs_path, self.checkpoint_dir_name).as_posix()
```

#### 231. [python/ray/train/base_trainer.py](https://github.com/ray-project/ray/blob/master/python/ray/train/base_trainer.py#L380) (Line 380)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/base_trainer.py#L380
- **Target Call:** `Path(fs_path, _TRAINER_PKL).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BaseTrainer.restore`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        trainer_pkl_path = Path(fs_path, _TRAINER_PKL).as_posix()
```

#### 232. [python/ray/train/base_trainer.py](https://github.com/ray-project/ray/blob/master/python/ray/train/base_trainer.py#L455) (Line 455)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/base_trainer.py#L455
- **Target Call:** `Path(fs_path, _TRAINER_PKL).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BaseTrainer.can_restore`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        trainer_pkl_path = Path(fs_path, _TRAINER_PKL).as_posix()
```

#### 233. [python/ray/train/horovod/config.py](https://github.com/ray-project/ray/blob/master/python/ray/train/horovod/config.py#L59) (Line 59)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/horovod/config.py#L59
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HorovodConfig.__post_init__`
- **Arguments:** `self.ssh_identity_file, 'w'`
- **Keywords:** `{}`

```python
            with open(self.ssh_identity_file, "w") as f:
```

#### 234. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L408) (Line 408)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L408
- **Target Call:** `Path(self.storage_fs_path).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        self.storage_fs_path = Path(self.storage_fs_path).as_posix()
```

#### 235. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L429) (Line 429)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L429
- **Target Call:** `Path(self.experiment_fs_path, VALIDATE_STORAGE_MARKER_FILENAME).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext._create_validation_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        valid_file = Path(
            self.experiment_fs_path, VALIDATE_STORAGE_MARKER_FILENAME
        ).as_posix()
```

#### 236. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L438) (Line 438)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L438
- **Target Call:** `Path(self.experiment_fs_path, VALIDATE_STORAGE_MARKER_FILENAME).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext._check_validation_file`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        valid_file = Path(
            self.experiment_fs_path, VALIDATE_STORAGE_MARKER_FILENAME
        ).as_posix()
```

#### 237. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L520) (Line 520)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L520
- **Target Call:** `Path(self.storage_fs_path, self.experiment_dir_name).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext.experiment_fs_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return Path(self.storage_fs_path, self.experiment_dir_name).as_posix()
```

#### 238. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L535) (Line 535)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L535
- **Target Call:** `Path(self.experiment_fs_path, CHECKPOINT_MANAGER_SNAPSHOT_FILENAME).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext.checkpoint_manager_snapshot_path`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return Path(
            self.experiment_fs_path, CHECKPOINT_MANAGER_SNAPSHOT_FILENAME
        ).as_posix()
```

#### 239. [python/ray/train/v2/_internal/execution/storage.py](https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L573) (Line 573)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/train/v2/_internal/execution/storage.py#L573
- **Target Call:** `Path(self.experiment_fs_path, checkpoint_name).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `StorageContext.build_checkpoint_path_from_name`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return Path(self.experiment_fs_path, checkpoint_name).as_posix()
```

#### 240. [python/ray/tune/analysis/experiment_analysis.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/analysis/experiment_analysis.py#L127) (Line 127)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/analysis/experiment_analysis.py#L127
- **Target Call:** `experiment_fs_path.parent.as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ExperimentAnalysis._load_trials`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            new_storage.storage_fs_path = experiment_fs_path.parent.as_posix()
```

#### 241. [python/ray/tune/analysis/experiment_analysis.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/analysis/experiment_analysis.py#L142) (Line 142)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/analysis/experiment_analysis.py#L142
- **Target Call:** `Path(trial.storage.trial_fs_path, EXPR_RESULT_FILE).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ExperimentAnalysis._fetch_trial_dataframe`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        json_fs_path = Path(trial.storage.trial_fs_path, EXPR_RESULT_FILE).as_posix()
```

#### 242. [python/ray/tune/analysis/experiment_analysis.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/analysis/experiment_analysis.py#L143) (Line 143)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/analysis/experiment_analysis.py#L143
- **Target Call:** `Path(trial.storage.trial_fs_path, EXPR_PROGRESS_FILE).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ExperimentAnalysis._fetch_trial_dataframe`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        csv_fs_path = Path(trial.storage.trial_fs_path, EXPR_PROGRESS_FILE).as_posix()
```

#### 243. [python/ray/tune/execution/experiment_state.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/execution/experiment_state.py#L61) (Line 61)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/execution/experiment_state.py#L61
- **Target Call:** `Path(experiment_fs_path, filename).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_find_newest_experiment_checkpoint`
- **Arguments:** ``
- **Keywords:** `{}`

```python
    return Path(experiment_fs_path, filename).as_posix()
```

#### 244. [python/ray/tune/execution/experiment_state.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/execution/experiment_state.py#L268) (Line 268)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/execution/experiment_state.py#L268
- **Target Call:** `Path(self._storage.experiment_fs_path, relpath).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ExperimentCheckpointManager.sync_down_experiment_state`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            fs_path = Path(self._storage.experiment_fs_path, relpath).as_posix()
```

#### 245. [python/ray/tune/execution/tune_controller.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/execution/tune_controller.py#L346) (Line 346)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/execution/tune_controller.py#L346
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TuneController.save_to_dir`
- **Arguments:** `Path(driver_staging_path, self.experiment_state_file_name), 'w'`
- **Keywords:** `{}`

```python
        with open(
            Path(driver_staging_path, self.experiment_state_file_name),
            "w",
        ) as f:
```

#### 246. [python/ray/tune/experiment/trial.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L768) (Line 768)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L768
- **Target Call:** `Path(self.storage.trial_fs_path, error_filename).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Trial.get_pickled_error`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        pickled_error_fs_path = Path(
            self.storage.trial_fs_path, error_filename
        ).as_posix()
```

#### 247. [python/ray/tune/experiment/trial.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L789) (Line 789)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L789
- **Target Call:** `Path(self.storage.trial_fs_path, error_filename).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Trial.get_error`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        txt_error_fs_path = Path(self.storage.trial_fs_path, error_filename).as_posix()
```

#### 248. [python/ray/tune/experiment/trial.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L840) (Line 840)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L840
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Trial.handle_error`
- **Arguments:** `self.pickled_error_file, 'wb'`
- **Keywords:** `{}`

```python
                with open(self.pickled_error_file, "wb") as f:
```

#### 249. [python/ray/tune/experiment/trial.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L842) (Line 842)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/experiment/trial.py#L842
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Trial.handle_error`
- **Arguments:** `self.error_file, 'a+'`
- **Keywords:** `{}`

```python
            with open(self.error_file, "a+") as f:
```

#### 250. [python/ray/tune/impl/tuner_internal.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/impl/tuner_internal.py#L184) (Line 184)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/impl/tuner_internal.py#L184
- **Target Call:** `Path(storage.experiment_fs_path, _TUNER_PKL).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TunerInternal.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            Path(storage.experiment_fs_path, _TUNER_PKL).as_posix()
```

#### 251. [python/ray/tune/impl/tuner_internal.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/impl/tuner_internal.py#L379) (Line 379)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/impl/tuner_internal.py#L379
- **Target Call:** `Path(fs_path, _TUNER_PKL).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TunerInternal._restore_from_path_or_uri`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        with fs.open_input_file(Path(fs_path, _TUNER_PKL).as_posix()) as f:
```

#### 252. [python/ray/tune/logger/logger.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/logger.py#L122) (Line 122)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/logger/logger.py#L122
- **Target Call:** `Path(trial.storage.trial_fs_path, file_name).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `LoggerCallback._restore_from_remote`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        remote_file = Path(trial.storage.trial_fs_path, file_name).as_posix()
```

#### 253. [python/ray/tune/schedulers/async_hyperband.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/async_hyperband.py#L186) (Line 186)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/async_hyperband.py#L186
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AsyncHyperBandScheduler.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as outputFile:
```

#### 254. [python/ray/tune/schedulers/async_hyperband.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/async_hyperband.py#L190) (Line 190)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/async_hyperband.py#L190
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AsyncHyperBandScheduler.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as inputFile:
```

#### 255. [python/ray/tune/schedulers/pbt.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/pbt.py#L779) (Line 779)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/pbt.py#L779
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PopulationBasedTraining._log_config_on_step`
- **Arguments:** `os.path.join(trial.local_experiment_path, 'pbt_global.txt'), 'a+'`
- **Keywords:** `{}`

```python
        with open(
            os.path.join(trial.local_experiment_path, "pbt_global.txt"), "a+"
        ) as f:
```

#### 256. [python/ray/tune/schedulers/pbt.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/pbt.py#L787) (Line 787)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/pbt.py#L787
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PopulationBasedTraining._log_config_on_step`
- **Arguments:** `trial_path, 'a+'`
- **Keywords:** `{}`

```python
        with open(trial_path, "a+") as f:
```

#### 257. [python/ray/tune/schedulers/pbt.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/pbt.py#L1114) (Line 1114)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/pbt.py#L1114
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `PopulationBasedTrainingReplay._load_policy`
- **Arguments:** `policy_file, 'rt'`
- **Keywords:** `{}`

```python
        with open(policy_file, "rt") as fp:
```

#### 258. [python/ray/tune/schedulers/resource_changing_scheduler.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/resource_changing_scheduler.py#L802) (Line 802)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/resource_changing_scheduler.py#L802
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ResourceChangingScheduler.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as outputFile:
```

#### 259. [python/ray/tune/schedulers/resource_changing_scheduler.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/resource_changing_scheduler.py#L806) (Line 806)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/schedulers/resource_changing_scheduler.py#L806
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ResourceChangingScheduler.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as inputFile:
```

#### 260. [python/ray/tune/search/ax/ax_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/ax/ax_search.py#L470) (Line 470)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/ax/ax_search.py#L470
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AxSearch.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as outputFile:
```

#### 261. [python/ray/tune/search/ax/ax_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/ax/ax_search.py#L474) (Line 474)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/ax/ax_search.py#L474
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AxSearch.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as inputFile:
```

#### 262. [python/ray/tune/search/bayesopt/bayesopt_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/bayesopt/bayesopt_search.py#L428) (Line 428)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/bayesopt/bayesopt_search.py#L428
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BayesOptSearch.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as f:
```

#### 263. [python/ray/tune/search/bayesopt/bayesopt_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/bayesopt/bayesopt_search.py#L433) (Line 433)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/bayesopt/bayesopt_search.py#L433
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `BayesOptSearch.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as f:
```

#### 264. [python/ray/tune/search/bohb/bohb_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/bohb/bohb_search.py#L373) (Line 373)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/bohb/bohb_search.py#L373
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TuneBOHB.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as outputFile:
```

#### 265. [python/ray/tune/search/bohb/bohb_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/bohb/bohb_search.py#L377) (Line 377)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/bohb/bohb_search.py#L377
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TuneBOHB.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as inputFile:
```

#### 266. [python/ray/tune/search/hebo/hebo_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/hebo/hebo_search.py#L361) (Line 361)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/hebo/hebo_search.py#L361
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HEBOSearch.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as f:
```

#### 267. [python/ray/tune/search/hebo/hebo_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/hebo/hebo_search.py#L366) (Line 366)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/hebo/hebo_search.py#L366
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HEBOSearch.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as f:
```

#### 268. [python/ray/tune/search/hyperopt/hyperopt_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/hyperopt/hyperopt_search.py#L439) (Line 439)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/hyperopt/hyperopt_search.py#L439
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HyperOptSearch.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as f:
```

#### 269. [python/ray/tune/search/hyperopt/hyperopt_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/hyperopt/hyperopt_search.py#L443) (Line 443)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/hyperopt/hyperopt_search.py#L443
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `HyperOptSearch.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as f:
```

#### 270. [python/ray/tune/search/nevergrad/nevergrad_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/nevergrad/nevergrad_search.py#L312) (Line 312)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/nevergrad/nevergrad_search.py#L312
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `NevergradSearch.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as outputFile:
```

#### 271. [python/ray/tune/search/nevergrad/nevergrad_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/nevergrad/nevergrad_search.py#L316) (Line 316)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/nevergrad/nevergrad_search.py#L316
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `NevergradSearch.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as inputFile:
```

#### 272. [python/ray/tune/search/optuna/optuna_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/optuna/optuna_search.py#L635) (Line 635)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/optuna/optuna_search.py#L635
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OptunaSearch.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as outputFile:
```

#### 273. [python/ray/tune/search/optuna/optuna_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/optuna/optuna_search.py#L639) (Line 639)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/optuna/optuna_search.py#L639
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OptunaSearch.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as inputFile:
```

#### 274. [python/ray/tune/search/zoopt/zoopt_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/zoopt/zoopt_search.py#L315) (Line 315)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/zoopt/zoopt_search.py#L315
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZOOptSearch.save`
- **Arguments:** `checkpoint_path, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "wb") as outputFile:
```

#### 275. [python/ray/tune/search/zoopt/zoopt_search.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/search/zoopt/zoopt_search.py#L319) (Line 319)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/search/zoopt/zoopt_search.py#L319
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ZOOptSearch.restore`
- **Arguments:** `checkpoint_path, 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_path, "rb") as inputFile:
```

#### 276. [python/ray/tune/tuner.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/tuner.py#L316) (Line 316)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/tuner.py#L316
- **Target Call:** `Path(fs_path, _TUNER_PKL).as_posix` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Tuner.can_restore`
- **Arguments:** ``
- **Keywords:** `{}`

```python
        return _exists_at_fs_path(fs, Path(fs_path, _TUNER_PKL).as_posix())
```

#### 277. [python/ray/tune/utils/mock_trainable.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/mock_trainable.py#L49) (Line 49)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/mock_trainable.py#L49
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MyTrainableClass.save_checkpoint`
- **Arguments:** `path, 'w'`
- **Keywords:** `{}`

```python
        with open(path, "w") as f:
```

#### 278. [python/ray/tune/utils/mock_trainable.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/mock_trainable.py#L54) (Line 54)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/mock_trainable.py#L54
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `MyTrainableClass.load_checkpoint`
- **Arguments:** `path, 'r'`
- **Keywords:** `{}`

```python
        with open(path, "r") as f:
```

#### 279. [python/ray/tune/utils/release_test_util.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/release_test_util.py#L69) (Line 69)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/release_test_util.py#L69
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `TestDurableTrainable.save_checkpoint`
- **Arguments:** `checkpoint_file, 'wb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_file, "wb") as fp:
```

#### 280. [python/ray/tune/utils/release_test_util.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/release_test_util.py#L97) (Line 97)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/release_test_util.py#L97
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `function_trainable`
- **Arguments:** `checkpoint_file, 'wb'`
- **Keywords:** `{}`

```python
                    with open(checkpoint_file, "wb") as fp:
```

#### 281. [python/ray/tune/utils/release_test_util.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/release_test_util.py#L169) (Line 169)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/release_test_util.py#L169
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `timed_tune_run`
- **Arguments:** `test_output_json, 'wt'`
- **Keywords:** `{}`

```python
    with open(test_output_json, "wt") as f:
```

#### 282. [python/ray/tune/utils/util.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/util.py#L425) (Line 425)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/util.py#L425
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_atomic_save`
- **Arguments:** `tmp_search_ckpt_path, 'wb'`
- **Keywords:** `{}`

```python
    with open(tmp_search_ckpt_path, "wb") as f:
```

#### 283. [python/ray/tune/utils/util.py](https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/util.py#L451) (Line 451)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/tune/utils/util.py#L451
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_load_newest_checkpoint`
- **Arguments:** `most_recent_checkpoint, 'rb'`
- **Keywords:** `{}`

```python
    with open(most_recent_checkpoint, "rb") as f:
```

#### 284. [python/ray/util/client/api.py](https://github.com/ray-project/ray/blob/master/python/ray/util/client/api.py#L357) (Line 357)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/client/api.py#L357
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_ClientAPI.timeline`
- **Arguments:** `filename, 'w'`
- **Keywords:** `{}`

```python
            with open(filename, "w") as outfile:
```

#### 285. [python/ray/util/client/server/server.py](https://github.com/ray-project/ray/blob/master/python/ray/util/client/server/server.py#L417) (Line 417)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/client/server/server.py#L417
- **Target Call:** `self.object_refs[client_id].get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RayletServicer._async_get_object`
- **Arguments:** `rid, None`
- **Keywords:** `{}`

```python
        ref = self.object_refs[client_id].get(rid, None)
```

#### 286. [python/ray/util/client/server/server.py](https://github.com/ray-project/ray/blob/master/python/ray/util/client/server/server.py#L488) (Line 488)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/client/server/server.py#L488
- **Target Call:** `self.object_refs[client_id].get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RayletServicer._get_object`
- **Arguments:** `rid, None`
- **Keywords:** `{}`

```python
            ref = self.object_refs[client_id].get(rid, None)
```

#### 287. [python/ray/util/client/server/server.py](https://github.com/ray-project/ray/blob/master/python/ray/util/client/server/server.py#L644) (Line 644)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/client/server/server.py#L644
- **Target Call:** `self.actor_refs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `RayletServicer._schedule_method`
- **Arguments:** `task.payload_id`
- **Keywords:** `{}`

```python
        actor_handle = self.actor_refs.get(task.payload_id)
```

#### 288. [python/ray/util/multiprocessing/pool.py](https://github.com/ray-project/ray/blob/master/python/ray/util/multiprocessing/pool.py#L231) (Line 231)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/multiprocessing/pool.py#L231
- **Target Call:** `self._new_object_refs.put` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ResultThread.add_object_ref`
- **Arguments:** `object_ref`
- **Keywords:** `{}`

```python
        self._new_object_refs.put(object_ref)
```

#### 289. [python/ray/util/multiprocessing/pool.py](https://github.com/ray-project/ray/blob/master/python/ray/util/multiprocessing/pool.py#L247) (Line 247)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/multiprocessing/pool.py#L247
- **Target Call:** `self._new_object_refs.get` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `ResultThread.run`
- **Arguments:** ``
- **Keywords:** `{'block': 'block'}`

```python
                    new_object_ref = self._new_object_refs.get(block=block)
```

#### 290. [python/ray/util/spark/cluster_init.py](https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L374) (Line 374)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L374
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_preallocate_ray_worker_port_range`
- **Arguments:** `port_alloc_file`
- **Keywords:** `{'mode': "'r'"}`

```python
            with open(port_alloc_file, mode="r") as fp:
```

#### 291. [python/ray/util/spark/cluster_init.py](https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L385) (Line 385)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L385
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_preallocate_ray_worker_port_range`
- **Arguments:** `port_alloc_file`
- **Keywords:** `{'mode': "'w'"}`

```python
            with open(port_alloc_file, mode="w"):
```

#### 292. [python/ray/util/spark/cluster_init.py](https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L409) (Line 409)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L409
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_preallocate_ray_worker_port_range`
- **Arguments:** `port_alloc_file`
- **Keywords:** `{'mode': "'w'"}`

```python
        with open(port_alloc_file, mode="w") as fp:
```

#### 293. [python/ray/util/spark/cluster_init.py](https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L1764) (Line 1764)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L1764
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AutoscalingCluster._generate_config`
- **Arguments:** `os.path.join(os.path.dirname(ray.__file__), 'autoscaler/spark/defaults.yaml')`
- **Keywords:** `{}`

```python
            open(
                os.path.join(
                    os.path.dirname(ray.__file__),
                    "autoscaler/spark/defaults.yaml",
                )
            )
```

#### 294. [python/ray/util/spark/cluster_init.py](https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L1818) (Line 1818)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/spark/cluster_init.py#L1818
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `AutoscalingCluster.start`
- **Arguments:** `autoscale_config, 'w'`
- **Keywords:** `{}`

```python
        with open(autoscale_config, "w") as f:
```

#### 295. [python/ray/util/tracing/setup_local_tmp_tracing.py](https://github.com/ray-project/ray/blob/master/python/ray/util/tracing/setup_local_tmp_tracing.py#L22) (Line 22)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/util/tracing/setup_local_tmp_tracing.py#L22
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `setup_tracing`
- **Arguments:** `f'{spans_dir}{os.getpid()}.txt', 'w'`
- **Keywords:** `{}`

```python
                out=open(f"{spans_dir}{os.getpid()}.txt", "w"),
```

#### 296. [python/ray/widgets/render.py](https://github.com/ray-project/ray/blob/master/python/ray/widgets/render.py#L12) (Line 12)
- **Line Link:** https://github.com/ray-project/ray/blob/master/python/ray/widgets/render.py#L12
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Template.__init__`
- **Arguments:** `pathlib.Path(__file__).parent / 'templates' / file, 'r'`
- **Keywords:** `{}`

```python
        with open(pathlib.Path(__file__).parent / "templates" / file, "r") as f:
```

#### 297. [rllib/algorithms/algorithm.py](https://github.com/ray-project/ray/blob/master/rllib/algorithms/algorithm.py#L3141) (Line 3141)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/algorithms/algorithm.py#L3141
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Algorithm.save_checkpoint`
- **Arguments:** `state_file, 'wb'`
- **Keywords:** `{}`

```python
            with open(state_file, "wb") as f:
```

#### 298. [rllib/algorithms/algorithm.py](https://github.com/ray-project/ray/blob/master/rllib/algorithms/algorithm.py#L3145) (Line 3145)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/algorithms/algorithm.py#L3145
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Algorithm.save_checkpoint`
- **Arguments:** `checkpoint_dir / 'rllib_checkpoint.json', 'w'`
- **Keywords:** `{}`

```python
            with open(checkpoint_dir / "rllib_checkpoint.json", "w") as f:
```

#### 299. [rllib/algorithms/algorithm.py](https://github.com/ray-project/ray/blob/master/rllib/algorithms/algorithm.py#L4349) (Line 4349)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/algorithms/algorithm.py#L4349
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Algorithm._checkpoint_info_to_algorithm_state`
- **Arguments:** `checkpoint_info['state_file'], 'rb'`
- **Keywords:** `{}`

```python
        with open(checkpoint_info["state_file"], "rb") as f:
```

#### 300. [rllib/algorithms/algorithm.py](https://github.com/ray-project/ray/blob/master/rllib/algorithms/algorithm.py#L4430) (Line 4430)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/algorithms/algorithm.py#L4430
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Algorithm._checkpoint_info_to_algorithm_state`
- **Arguments:** `policy_state_file, 'rb'`
- **Keywords:** `{}`

```python
                with open(policy_state_file, "rb") as f:
```

#### 301. [rllib/algorithms/mock.py](https://github.com/ray-project/ray/blob/master/rllib/algorithms/mock.py#L65) (Line 65)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/algorithms/mock.py#L65
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_MockTrainer.save_checkpoint`
- **Arguments:** `path, 'wb'`
- **Keywords:** `{}`

```python
        with open(path, "wb") as f:
```

#### 302. [rllib/algorithms/mock.py](https://github.com/ray-project/ray/blob/master/rllib/algorithms/mock.py#L71) (Line 71)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/algorithms/mock.py#L71
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_MockTrainer.load_checkpoint`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
        with open(path, "rb") as f:
```

#### 303. [rllib/offline/json_writer.py](https://github.com/ray-project/ray/blob/master/rllib/offline/json_writer.py#L106) (Line 106)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/offline/json_writer.py#L106
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `JsonWriter._get_file`
- **Arguments:** `path, 'w'`
- **Keywords:** `{}`

```python
                self.cur_file = open(path, "w")
```

#### 304. [rllib/offline/offline_data.py](https://github.com/ray-project/ray/blob/master/rllib/offline/offline_data.py#L69) (Line 69)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/offline/offline_data.py#L69
- **Target Call:** `gcsfs.GCSFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OfflineData.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.filesystem_object = gcsfs.GCSFileSystem(**self.filesystem_kwargs)
```

#### 305. [rllib/offline/offline_env_runner.py](https://github.com/ray-project/ray/blob/master/rllib/offline/offline_env_runner.py#L86) (Line 86)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/offline/offline_env_runner.py#L86
- **Target Call:** `gcsfs.GCSFileSystem` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `OfflineSingleAgentEnvRunner.__init__`
- **Arguments:** ``
- **Keywords:** `{}`

```python
            self.filesystem_object = gcsfs.GCSFileSystem(**self.filesystem_kwargs)
```

#### 306. [rllib/policy/policy.py](https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L314) (Line 314)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L314
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Policy.from_checkpoint`
- **Arguments:** `checkpoint_info['state_file'], 'rb'`
- **Keywords:** `{}`

```python
                with open(checkpoint_info["state_file"], "rb") as f:
```

#### 307. [rllib/policy/policy.py](https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L341) (Line 341)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L341
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Policy.from_checkpoint`
- **Arguments:** `policy_checkpoint_info['state_file'], 'rb'`
- **Keywords:** `{}`

```python
                        with open(policy_checkpoint_info["state_file"], "rb") as f:
```

#### 308. [rllib/policy/policy.py](https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L352) (Line 352)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L352
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Policy.from_checkpoint`
- **Arguments:** `checkpoint_info['state_file'], 'rb'`
- **Keywords:** `{}`

```python
            with open(checkpoint_info["state_file"], "rb") as f:
```

#### 309. [rllib/policy/policy.py](https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L1126) (Line 1126)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L1126
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Policy.export_checkpoint`
- **Arguments:** `os.path.join(export_dir, state_file), 'w+b'`
- **Keywords:** `{}`

```python
            with open(os.path.join(export_dir, state_file), "w+b") as f:
```

#### 310. [rllib/policy/policy.py](https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L1138) (Line 1138)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L1138
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Policy.export_checkpoint`
- **Arguments:** `os.path.join(export_dir, state_file), 'w+b'`
- **Keywords:** `{}`

```python
            with open(os.path.join(export_dir, state_file), "w+b") as f:
```

#### 311. [rllib/policy/policy.py](https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L1142) (Line 1142)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/policy/policy.py#L1142
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `Policy.export_checkpoint`
- **Arguments:** `os.path.join(export_dir, 'rllib_checkpoint.json'), 'w'`
- **Keywords:** `{}`

```python
        with open(os.path.join(export_dir, "rllib_checkpoint.json"), "w") as f:
```

#### 312. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L976) (Line 976)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L976
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `convert_to_msgpack_checkpoint`
- **Arguments:** `state_file, 'wb'`
- **Keywords:** `{}`

```python
    with open(state_file, "wb") as f:
```

#### 313. [rllib/utils/checkpoints.py](https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L980) (Line 980)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/utils/checkpoints.py#L980
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `convert_to_msgpack_checkpoint`
- **Arguments:** `os.path.join(msgpack_checkpoint_dir, 'rllib_checkpoint.json'), 'w'`
- **Keywords:** `{}`

```python
    with open(os.path.join(msgpack_checkpoint_dir, "rllib_checkpoint.json"), "w") as f:
```

#### 314. [rllib/utils/from_config.py](https://github.com/ray-project/ray/blob/master/rllib/utils/from_config.py#L233) (Line 233)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/utils/from_config.py#L233
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `from_file`
- **Arguments:** `path, 'rt'`
- **Keywords:** `{}`

```python
    with open(path, "rt") as fp:
```

#### 315. [rllib/utils/policy.py](https://github.com/ray-project/ray/blob/master/rllib/utils/policy.py#L124) (Line 124)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/utils/policy.py#L124
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `parse_policy_specs_from_checkpoint`
- **Arguments:** `path, 'rb'`
- **Keywords:** `{}`

```python
    with open(path, "rb") as f:
```

#### 316. [rllib/utils/tf_run_builder.py](https://github.com/ray-project/ray/blob/master/rllib/utils/tf_run_builder.py#L100) (Line 100)
- **Line Link:** https://github.com/ray-project/ray/blob/master/rllib/utils/tf_run_builder.py#L100
- **Target Call:** `open` | **Cache_Type:** `NOT_EXPLICIT` | **Is Specified Keyword:** `False`
- **Context:** `_run_timeline`
- **Arguments:** `outf, 'w'`
- **Keywords:** `{}`

```python
        trace_file = open(outf, "w")
```
