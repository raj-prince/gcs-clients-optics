# Complete 4-Column Summary Table of All 310 FSSPEC & Filesystem Methods

This reference summary table documents **every single distinct method call** identified by the AST crawler across scanned codebases, matching the summary format (`Target Call` | `Occurrences` | `Major Repositories` | `Usage Pattern`).

| Target Call | Occurrences | Major Repositories | Primary Usage Pattern |
| :--- | :---: | :--- | :--- |
| **`open`** | **1229** | `pytorch/pytorch`, `ray-project/ray`, `mlflow/mlflow` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`fsspec.open`** | **56** | `intake/intake`, `huggingface/datasets`, `pandas-dev/pandas` | fsspec module: Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`fs.open`** | **42** | `dask/dask`, `Lightning-AI/pytorch-lightning`, `huggingface/datasets` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`sync_wrapper`** | **35** | `fsspec/s3fs`, `fsspec/adlfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`fs.exists`** | **34** | `Lightning-AI/pytorch-lightning`, `iterative/dvc`, `modin-project/modin` | Checking existence of a file or directory node on local or remote filesystem |
| **`url_to_fs`** | **33** | `huggingface/datasets`, `modin-project/modin`, `Lightning-AI/pytorch-lightning` | Decomposing protocol URI string (`s3://...`, `gs://...`) into abstract `(filesystem, path)` tuple |
| **`fs.join`** | **25** | `iterative/dvc`, `pytorch/pytorch` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`fs.isdir`** | **23** | `iterative/dvc`, `Lightning-AI/pytorch-lightning`, `huggingface/datasets` | Verify whether a path points to an abstract directory container node |
| **`fs.info`** | **18** | `iterative/dvc`, `huggingface/datasets`, `intake/intake` | Give details and metadata dictionary of entry at path (`size`, `type`, `created`, `mtime`) |
| **`asyn.sync_wrapper`** | **18** | `fsspec/gcsfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`fsspec.core.url_to_fs`** | **17** | `modin-project/modin`, `intake/intake`, `feast-dev/feast` | Decomposing protocol URI string (`s3://...`, `gs://...`) into abstract `(filesystem, path)` tuple |
| **`self.fs.exists`** | **16** | `Lightning-AI/pytorch-lightning`, `iterative/dvc`, `pytorch/pytorch` | Instance method: Checking existence of a file or directory node on local or remote filesystem |
| **`fs.isfile`** | **16** | `huggingface/datasets`, `Lightning-AI/pytorch-lightning`, `iterative/dvc` | Verify whether a target path resolves to a leaf file node (not a directory) |
| **`asyn.sync`** | **16** | `fsspec/gcsfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`fs.get`** | **15** | `Lightning-AI/pytorch-lightning`, `feast-dev/feast`, `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fs.sep.join`** | **14** | `dask/dask` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`open_files`** | **13** | `dask/dask`, `intake/intake` | Batch context manager opening multiple matching file stream handles simultaneously |
| **`fs.makedirs`** | **10** | `Lightning-AI/pytorch-lightning`, `huggingface/datasets`, `iterative/dvc` | Recursively create directory tree hierarchy (`exist_ok=True`) |
| **`fsspec.filesystem`** | **10** | `kedro-org/kedro`, `intake/intake`, `ray-project/ray` | fsspec module: Instantiating filesystem driver class by protocol string (e.g. `fsspec.filesystem('s3')`) |
| **`stringify_path`** | **10** | `dask/dask`, `fsspec/gcsfs` | Coercing pathlib.Path or abstract path objects to normalized string path representation |
| **`sync`** | **10** | `fsspec/adlfs`, `fsspec/s3fs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`self.fs.join`** | **9** | `iterative/dvc` | Instance method: Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`state.offset_to_index.get`** | **8** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`offsets.size`** | **8** | `pytorch/pytorch` | Return size in bytes of a target file |
| **`self.fs.abspath`** | **8** | `iterative/dvc` | Instance method: Resolving abstract relative path to fully qualified URI path from working directory |
| **`self.fs.relpath`** | **8** | `iterative/dvc` | Instance method: Calculating relative path string from a reference parent or root directory |
| **`self.fs.open`** | **7** | `apache/arrow`, `modin-project/modin`, `pytorch/pytorch` | Instance method: Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`self._fs.exists`** | **7** | `Lightning-AI/pytorch-lightning`, `huggingface/datasets` | Checking existence of a file or directory node on local or remote filesystem |
| **`self._fs.ls`** | **7** | `Lightning-AI/pytorch-lightning`, `kedro-org/kedro` | List direct children of a directory (`detail=False` for paths, `detail=True` for info dicts) |
| **`fs.glob`** | **7** | `huggingface/datasets`, `modin-project/modin`, `pydata/xarray` | Wildcard expression matching (`*`, `?`, `[...]`, `**`) across remote or local directory trees |
| **`fs.find`** | **7** | `iterative/dvc`, `dask/dask` | Recursively find all file paths inside a directory subtree matching optional criteria |
| **`fs.ls`** | **7** | `iterative/dvc`, `intake/intake`, `pytorch/torchtitan` | List direct children of a directory (`detail=False` for paths, `detail=True` for info dicts) |
| **`get_fs_token_paths`** | **7** | `dask/dask` | Parsing URL path string into `(fs, fs_token, paths)` for distributed serialization |
| **`state.offset_to_inst.get`** | **6** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`self.fs.rm`** | **6** | `apache/arrow`, `pytorch/pytorch`, `Lightning-AI/pytorch-lightning` | Instance method: Delete files or directory trees (`recursive=True/False`) |
| **`self.fs.ls`** | **6** | `pytorch/pytorch`, `Lightning-AI/pytorch-lightning`, `iterative/dvc` | Instance method: List direct children of a directory (`detail=False` for paths, `detail=True` for info dicts) |
| **`self.fs.info`** | **6** | `fsspec/adlfs`, `Lightning-AI/pytorch-lightning`, `apache/arrow` | Instance method: Give details and metadata dictionary of entry at path (`size`, `type`, `created`, `mtime`) |
| **`self._fs.open`** | **6** | `Lightning-AI/pytorch-lightning`, `huggingface/datasets`, `kedro-org/kedro` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`self.fs.isdir`** | **6** | `iterative/dvc`, `apache/arrow` | Instance method: Verify whether a path points to an abstract directory container node |
| **`self.fs.getcwd`** | **6** | `iterative/dvc` | Instance method: Querying current working directory path of abstract filesystem instance |
| **`tokenize`** | **6** | `iterative/dvc`, `fsspec/s3fs` | Generating deterministic token hash of filesystem configuration and URL paths |
| **`repo.fs.join`** | **6** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`repo.fs.relpath`** | **6** | `iterative/dvc` | Calculating relative path string from a reference parent or root directory |
| **`split_protocol`** | **5** | `ray-project/ray`, `intake/intake` | Splitting raw string URL into `(protocol, path)` component pair |
| **`ArrowFSWrapper`** | **5** | `ray-project/ray`, `dask/dask` | Instantiating PyArrow filesystem interface wrapper around fsspec driver |
| **`fs.rm`** | **5** | `Lightning-AI/pytorch-lightning`, `dask/dask`, `pytorch/torchtitan` | Delete files or directory trees (`recursive=True/False`) |
| **`self._fs.isfile`** | **5** | `Lightning-AI/pytorch-lightning`, `kedro-org/kedro` | Verify whether a target path resolves to a leaf file node (not a directory) |
| **`fs.walk`** | **5** | `iterative/dvc`, `huggingface/datasets`, `modin-project/modin` | Pythonic recursive generator yielding `(root, dirs, files)` tuples across directory tree |
| **`self.fs.isfile`** | **5** | `apache/arrow`, `iterative/dvc`, `modin-project/modin` | Instance method: Verify whether a target path resolves to a leaf file node (not a directory) |
| **`fs.normpath`** | **5** | `iterative/dvc` | Normalizing redundant dot/double-dot and slash segments in paths |
| **`self.repo.fs.relparts`** | **5** | `iterative/dvc` | Deconstructing absolute path into tuple of relative path segment strings |
| **`self.repo.fs.join`** | **5** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`self.fs.relparts`** | **5** | `iterative/dvc` | Instance method: Deconstructing absolute path into tuple of relative path segment strings |
| **`self.fs.isin`** | **5** | `iterative/dvc` | Instance method: Verifying whether a child path is contained within a given parent tree root |
| **`self.fs.parts`** | **5** | `iterative/dvc` | Instance method: Splitting path string into ordered component segments tuple |
| **`fs.relpath`** | **5** | `iterative/dvc` | Calculating relative path string from a reference parent or root directory |
| **`repo.fs.relparts`** | **5** | `iterative/dvc` | Deconstructing absolute path into tuple of relative path segment strings |
| **`asyn._run_coros_in_chunks`** | **5** | `fsspec/gcsfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`offs.size`** | **4** | `pytorch/pytorch` | Return size in bytes of a target file |
| **`infer_storage_options`** | **4** | `pola-rs/polars`, `fsspec/adlfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`self._fs.isdir`** | **4** | `Lightning-AI/pytorch-lightning`, `kedro-org/kedro` | Verify whether a path points to an abstract directory container node |
| **`self._fs.listdir`** | **4** | `Lightning-AI/pytorch-lightning` | Alias of `ls`; list raw names inside target directory node |
| **`self._fs.makedirs`** | **4** | `Lightning-AI/pytorch-lightning`, `huggingface/datasets` | Recursively create directory tree hierarchy (`exist_ok=True`) |
| **`DirFileSystem`** | **4** | `huggingface/datasets` | Wrapping directory root so relative paths operate within a sub-tree sandbox |
| **`dirfs.glob`** | **4** | `huggingface/datasets` | Wildcard expression matching (`*`, `?`, `[...]`, `**`) across remote or local directory trees |
| **`self.fs.normpath`** | **4** | `iterative/dvc` | Instance method: Normalizing redundant dot/double-dot and slash segments in paths |
| **`fs.relparts`** | **4** | `iterative/dvc` | Deconstructing absolute path into tuple of relative path segment strings |
| **`fs.abspath`** | **4** | `iterative/dvc` | Resolving abstract relative path to fully qualified URI path from working directory |
| **`OpenFile`** | **4** | `dask/dask` | Low-level context-managed open file stream handle object wrapper |
| **`make_path_posix`** | **4** | `intake/intake` | Converting native platform separator path to standardized POSIX forward-slash path |
| **`fsspec.open_local`** | **4** | `intake/intake` | fsspec module: Open remote path by caching to temporary local disk and returning local path string |
| **`fsspec.open(data.url, **data.storage_options or {}).open`** | **4** | `intake/intake` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`NoOpCallback`** | **4** | `fsspec/gcsfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`get_loop`** | **4** | `fsspec/adlfs` | Bulk Data Transfer API method detected across storage interactions |
| **`self.fs.makedirs`** | **3** | `pytorch/pytorch`, `Lightning-AI/pytorch-lightning`, `iterative/dvc` | Instance method: Recursively create directory tree hierarchy (`exist_ok=True`) |
| **`fs.put`** | **3** | `Lightning-AI/pytorch-lightning` | Bulk batch uploading of local file(s) or directories up to remote filesystem target |
| **`fs.read_text`** | **3** | `huggingface/datasets` | Get the contents of the file directly decoded as a string |
| **`fsspec.get_fs_token_paths`** | **3** | `huggingface/datasets`, `pydata/xarray`, `intake/intake` | fsspec module: Parsing URL path string into `(fs, fs_token, paths)` for distributed serialization |
| **`self.fs.find`** | **3** | `modin-project/modin`, `apache/arrow` | Instance method: Recursively find all file paths inside a directory subtree matching optional criteria |
| **`self.repo.fs.relpath`** | **3** | `iterative/dvc` | Calculating relative path string from a reference parent or root directory |
| **`localfs.join`** | **3** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`self.fs.split`** | **3** | `iterative/dvc` | Instance method: Splitting abstract path into `(head, tail)` tuple pair |
| **`out.fs.isin`** | **3** | `iterative/dvc` | Verifying whether a child path is contained within a given parent tree root |
| **`repo.fs.getcwd`** | **3** | `iterative/dvc` | Querying current working directory path of abstract filesystem instance |
| **`fs_index.close`** | **3** | `iterative/dvc` | Close file stream handle and release buffer resources |
| **`fs.get('featureService', {}).get('spec', {}).get`** | **3** | `feast-dev/feast` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fs.get('featureService', {}).get`** | **3** | `feast-dev/feast` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fs.get('spec', {}).get`** | **3** | `feast-dev/feast` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`refs_raw.split`** | **3** | `feast-dev/feast` | Splitting abstract path into `(head, tail)` tuple pair |
| **`asyn.trailing_sep`** | **3** | `fsspec/gcsfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`fsspec.asyn.sync`** | **3** | `fsspec/gcsfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`self.fs.rename`** | **2** | `pytorch/pytorch` | Instance method: Alias of `mv`; rename or move an object path within filesystem storage |
| **`self.fs.mkdir`** | **2** | `pytorch/pytorch`, `apache/arrow` | Instance method: Create single directory container node at path (`create_parents=False`) |
| **`fs_class.get_file`** | **2** | `ray-project/ray` | Download a single remote file to local target filename path |
| **`Path(self.storage_fs_path).as_posix`** | **2** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(self.experiment_fs_path, _VALIDATE_STORAGE_MARKER_FILENAME).as_posix`** | **2** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(self.storage_fs_path, self.experiment_dir_name).as_posix`** | **2** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(fs_path, _TRAINER_PKL).as_posix`** | **2** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(self.experiment_fs_path, VALIDATE_STORAGE_MARKER_FILENAME).as_posix`** | **2** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(self.storage.trial_fs_path, error_filename).as_posix`** | **2** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(fs_path, _TUNER_PKL).as_posix`** | **2** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`self.object_refs[client_id].get`** | **2** | `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`gcsfs.GCSFileSystem`** | **2** | `ray-project/ray` | Instantiating Google Cloud Storage (`gs://`) filesystem driver |
| **`LocalFileSystem`** | **2** | `Lightning-AI/pytorch-lightning`, `dask/dask` | Instantiating explicit local host disk filesystem driver (`file://`) |
| **`self._fsdp_kwargs.get`** | **2** | `Lightning-AI/pytorch-lightning` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fs.listdir`** | **2** | `Lightning-AI/pytorch-lightning`, `huggingface/datasets` | Alias of `ls`; list raw names inside target directory node |
| **`self._open_with_fsspec().open`** | **2** | `huggingface/datasets` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`hffs.read_text`** | **2** | `huggingface/datasets` | Get the contents of the file directly decoded as a string |
| **`hffs.open`** | **2** | `huggingface/datasets` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`fs.get_file`** | **2** | `huggingface/datasets`, `iterative/dvc` | Download a single remote file to local target filename path |
| **`_repo.fs.join`** | **2** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`localfs.as_posix`** | **2** | `iterative/dvc` | Format path with standardized POSIX forward slash separators |
| **`self.repo.fs.exists`** | **2** | `iterative/dvc` | Checking existence of a file or directory node on local or remote filesystem |
| **`self.repo.fs.getcwd`** | **2** | `iterative/dvc` | Querying current working directory path of abstract filesystem instance |
| **`self.dvcfs.close`** | **2** | `iterative/dvc` | Close file stream handle and release buffer resources |
| **`repo.fs.isin`** | **2** | `iterative/dvc` | Verifying whether a child path is contained within a given parent tree root |
| **`fs.du`** | **2** | `iterative/dvc` | Calculate cumulative disk byte space consumed across a directory tree subtree |
| **`dep.fs.parts`** | **2** | `iterative/dvc` | Splitting path string into ordered component segments tuple |
| **`out.fs.relparts`** | **2** | `iterative/dvc` | Deconstructing absolute path into tuple of relative path segment strings |
| **`repo.fs.normpath`** | **2** | `iterative/dvc` | Normalizing redundant dot/double-dot and slash segments in paths |
| **`fs.getcwd`** | **2** | `iterative/dvc` | Querying current working directory path of abstract filesystem instance |
| **`fs.parts`** | **2** | `iterative/dvc` | Splitting path string into ordered component segments tuple |
| **`fs.ukey`** | **2** | `dask/dask` | Unique version hash or entity tag (`ETag`) for cache invalidation |
| **`read_block`** | **2** | `dask/dask` | Read a fixed-size byte block range from file stream without reading entire file |
| **`infer_compression`** | **2** | `dask/dask` | Detect compression format (`gzip`, `bz2`, `zip`, `zstd`) from file extension suffix |
| **`open_file`** | **2** | `dask/dask` | Open individual file handle inside protocol catalog or dataset interface |
| **`expand_paths_if_needed`** | **2** | `dask/dask` | Expanding wildcard glob strings into explicit path lists if glob syntax present |
| **`feature_refs.split`** | **2** | `feast-dev/feast` | Splitting abstract path into `(head, tail)` tuple pair |
| **`odfv_feature_refs.get`** | **2** | `feast-dev/feast` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`edp_mesh['efsdp'].size`** | **2** | `pytorch/torchtitan` | Return size in bytes of a target file |
| **`h.cat`** | **2** | `intake/intake` | Fetch (potentially multiple) paths' byte contents as a dictionary |
| **`fsspec.open_files`** | **2** | `intake/intake` | fsspec module: Batch context manager opening multiple matching file stream handles simultaneously |
| **`compressions.values`** | **2** | `intake/intake` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`gcsfs.split_path`** | **2** | `fsspec/gcsfs` | Path Arithmetic & Topologies API method detected across storage interactions |
| **`fs.offset_to_index.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fs.offset_to_inst.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`view_state.offset_to_index.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`self._slotdefs.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`all_bufs.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`group_n_to_bufs_after_swap_dealloc_by_candidate.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`V.graph.graph_input_storage_offsets.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`mod_refs.__dict__.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`torch._refs.__dict__.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`torch._refs._conversions.__dict__.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`self.fs.rm_file`** | **1** | `pytorch/pytorch` | Instance method: Delete a single leaf file node from storage driver |
| **`cast(torch.Tensor, fsdp_param._sharded_post_forward_param_data).size`** | **1** | `pytorch/pytorch` | Return size in bytes of a target file |
| **`fqn_to_fsdp_param_info.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`shard_dim_to_global_offsets.get`** | **1** | `pytorch/pytorch` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fsspec.open(path, 'wb', **storage_options or {}).open`** | **1** | `pandas-dev/pandas` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`self._str_offsets[js].copy`** | **1** | `pandas-dev/pandas` | Copy file(s) within two locations on the filesystem without downloading to local disk |
| **`object_refs.get`** | **1** | `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`Path(fs_path, EXPR_RESULT_FILE).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(fs_path, EXPR_PROGRESS_FILE).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`cls._read_file_as_str(fs, result_json_file).split`** | **1** | `ray-project/ray` | Splitting abstract path into `(head, tail)` tuple pair |
| **`Path(fs_path, checkpoint_dir_name).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(fs_path, EXPR_ERROR_PICKLE_FILE).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`fsspec.open(video_path, **opts).__enter__`** | **1** | `ray-project/ray` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`start_offset.get(topic_name, {}).get`** | **1** | `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`start_offset.get`** | **1** | `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`end_offset.get(topic_name, {}).get`** | **1** | `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`end_offset.get`** | **1** | `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`root.fs.open`** | **1** | `ray-project/ray` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`self._fs.move`** | **1** | `ray-project/ray` | Alias of `mv`; move file(s) from one location to another |
| **`HTTPFileSystem`** | **1** | `ray-project/ray` | Protocol Resolution & Driver Lifecycle API method detected across storage interactions |
| **`fsspec.implementations.http.HTTPFileSystem`** | **1** | `ray-project/ray` | Protocol Resolution & Driver Lifecycle API method detected across storage interactions |
| **`refs_main.exists`** | **1** | `ray-project/ray` | Checking existence of a file or directory node on local or remote filesystem |
| **`refs_main.read_text`** | **1** | `ray-project/ray` | Get the contents of the file directly decoded as a string |
| **`model_dir_refs_main.exists`** | **1** | `ray-project/ray` | Checking existence of a file or directory node on local or remote filesystem |
| **`Path(self.experiment_fs_path, self.trial_dir_name).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(self.trial_fs_path, self.checkpoint_dir_name).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(self.experiment_fs_path, CHECKPOINT_MANAGER_SNAPSHOT_FILENAME).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(self.experiment_fs_path, checkpoint_name).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`experiment_fs_path.parent.as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(trial.storage.trial_fs_path, EXPR_RESULT_FILE).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(trial.storage.trial_fs_path, EXPR_PROGRESS_FILE).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(experiment_fs_path, filename).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(self._storage.experiment_fs_path, relpath).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(storage.experiment_fs_path, _TUNER_PKL).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`Path(trial.storage.trial_fs_path, file_name).as_posix`** | **1** | `ray-project/ray` | Format path with standardized POSIX forward slash separators |
| **`self.actor_refs.get`** | **1** | `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`self._new_object_refs.put`** | **1** | `ray-project/ray` | Bulk batch uploading of local file(s) or directories up to remote filesystem target |
| **`self._new_object_refs.get`** | **1** | `ray-project/ray` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`requested_paths.lazy().with_columns(pl.col('path').str.replace('^lakefs://', 's3://').str.strip_prefix(file_prefix)).join`** | **1** | `pola-rs/polars` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`self._fs.rmdir`** | **1** | `Lightning-AI/pytorch-lightning` | Remove an empty directory container node |
| **`self._fs.rm`** | **1** | `Lightning-AI/pytorch-lightning` | Delete files or directory trees (`recursive=True/False`) |
| **`self._fs.rm_file`** | **1** | `Lightning-AI/pytorch-lightning` | Delete a single leaf file node from storage driver |
| **`self._fsdp_kwargs.copy`** | **1** | `Lightning-AI/pytorch-lightning` | Copy file(s) within two locations on the filesystem without downloading to local disk |
| **`fsspec.utils.get_protocol`** | **1** | `Lightning-AI/pytorch-lightning` | Bulk Data Transfer API method detected across storage interactions |
| **`json.loads(fs.read_text(config.DATASETDICT_INFOS_FILENAME, encoding='utf-8')).get`** | **1** | `huggingface/datasets` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fs.info(path).get`** | **1** | `huggingface/datasets` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fsspec.register_implementation`** | **1** | `huggingface/datasets` | fsspec module: Register custom filesystem driver implementation under a protocol scheme |
| **`fs.mv`** | **1** | `huggingface/datasets` | Move/rename file(s) from source path to destination path |
| **`self._open_with_fsspec().fs.info`** | **1** | `huggingface/datasets` | Give details and metadata dictionary of entry at path (`size`, `type`, `created`, `mtime`) |
| **`fsspec.asyn.reset_lock`** | **1** | `huggingface/datasets` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`hffs.exists`** | **1** | `huggingface/datasets` | Checking existence of a file or directory node on local or remote filesystem |
| **`hffs.isfile`** | **1** | `huggingface/datasets` | Verify whether a target path resolves to a leaf file node (not a directory) |
| **`can_be_local`** | **1** | `huggingface/datasets` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`strip_protocol`** | **1** | `huggingface/datasets` | Remove scheme prefix from URI path string |
| **`fs.size`** | **1** | `huggingface/datasets` | Return size in bytes of a target file |
| **`fsspec.available_protocols`** | **1** | `huggingface/datasets` | fsspec module: List all registered filesystem protocol schemes currently installed |
| **`cls._jvm().org.apache.hadoop.fs.FileSystem.get`** | **1** | `mlflow/mlflow` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`cls._fs().exists`** | **1** | `mlflow/mlflow` | Checking existence of a file or directory node on local or remote filesystem |
| **`self.fs.listdir`** | **1** | `apache/arrow` | Instance method: Alias of `ls`; list raw names inside target directory node |
| **`self.fs.mv`** | **1** | `apache/arrow` | Instance method: Move/rename file(s) from source path to destination path |
| **`self.fs.copy`** | **1** | `apache/arrow` | Instance method: Copy file(s) within two locations on the filesystem without downloading to local disk |
| **`_repo.fs.relparts`** | **1** | `iterative/dvc` | Deconstructing absolute path into tuple of relative path segment strings |
| **`fs_cls.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`self.local.fs.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`repo.fs.parts`** | **1** | `iterative/dvc` | Splitting path string into ordered component segments tuple |
| **`self.wfs.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`to.fs.info`** | **1** | `iterative/dvc` | Give details and metadata dictionary of entry at path (`size`, `type`, `created`, `mtime`) |
| **`self.repo.fs.isfile`** | **1** | `iterative/dvc` | Verify whether a target path resolves to a leaf file node (not a directory) |
| **`localfs.makedirs`** | **1** | `iterative/dvc` | Recursively create directory tree hierarchy (`exist_ok=True`) |
| **`dvc_fs.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`self.repo.fs.isin`** | **1** | `iterative/dvc` | Verifying whether a child path is contained within a given parent tree root |
| **`self.repo.fs.isdir`** | **1** | `iterative/dvc` | Verify whether a path points to an abstract directory container node |
| **`self._datafss.get`** | **1** | `iterative/dvc` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`self.repo.fs.open`** | **1** | `iterative/dvc` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`dvc_fs.open`** | **1** | `iterative/dvc` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`dvc_fs.info`** | **1** | `iterative/dvc` | Give details and metadata dictionary of entry at path (`size`, `type`, `created`, `mtime`) |
| **`dvc_fs.ls`** | **1** | `iterative/dvc` | List direct children of a directory (`detail=False` for paths, `detail=True` for info dicts) |
| **`fs_infos.get`** | **1** | `iterative/dvc` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`dvc_fs.fs.index.info`** | **1** | `iterative/dvc` | Give details and metadata dictionary of entry at path (`size`, `type`, `created`, `mtime`) |
| **`self.repo.fs.get_file`** | **1** | `iterative/dvc` | Download a single remote file to local target filename path |
| **`dvc_fs.get_file`** | **1** | `iterative/dvc` | Download a single remote file to local target filename path |
| **`self.fs._repo_kwargs.get`** | **1** | `iterative/dvc` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`self.fs.close`** | **1** | `iterative/dvc` | Instance method: Close file stream handle and release buffer resources |
| **`self.fs.chdir`** | **1** | `iterative/dvc` | Instance method: Changing current working directory context of filesystem wrapper |
| **`self.fs.walk`** | **1** | `iterative/dvc` | Instance method: Pythonic recursive generator yielding `(root, dirs, files)` tuples across directory tree |
| **`self.fs.as_posix`** | **1** | `iterative/dvc` | Instance method: Format path with standardized POSIX forward slash separators |
| **`fs_path.relparts`** | **1** | `iterative/dvc` | Deconstructing absolute path into tuple of relative path segment strings |
| **`self.fs.move`** | **1** | `iterative/dvc` | Instance method: Alias of `mv`; move file(s) from one location to another |
| **`from_fs.isdir`** | **1** | `iterative/dvc` | Verify whether a path points to an abstract directory container node |
| **`self.fs.sep.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`self.resolver.fs.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`self.fs.normpath(path).split`** | **1** | `iterative/dvc` | Splitting abstract path into `(head, tail)` tuple pair |
| **`out.fs.abspath`** | **1** | `iterative/dvc` | Resolving abstract relative path to fully qualified URI path from working directory |
| **`self.repo.fs.normpath`** | **1** | `iterative/dvc` | Normalizing redundant dot/double-dot and slash segments in paths |
| **`localfs.exists`** | **1** | `iterative/dvc` | Checking existence of a file or directory node on local or remote filesystem |
| **`localfs.commonpath`** | **1** | `iterative/dvc` | Find longest common sub-path prefix across multiple paths |
| **`repo.fs.chdir`** | **1** | `iterative/dvc` | Changing current working directory context of filesystem wrapper |
| **`cache_fs.exists`** | **1** | `iterative/dvc` | Checking existence of a file or directory node on local or remote filesystem |
| **`obj.fs.open`** | **1** | `iterative/dvc` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`left_fs.find`** | **1** | `iterative/dvc` | Recursively find all file paths inside a directory subtree matching optional criteria |
| **`right_fs.exists`** | **1** | `iterative/dvc` | Checking existence of a file or directory node on local or remote filesystem |
| **`left_fs.relpath`** | **1** | `iterative/dvc` | Calculating relative path string from a reference parent or root directory |
| **`left_fs.get_file`** | **1** | `iterative/dvc` | Download a single remote file to local target filename path |
| **`repo.fs.makedirs`** | **1** | `iterative/dvc` | Recursively create directory tree hierarchy (`exist_ok=True`) |
| **`src_fs.exists`** | **1** | `iterative/dvc` | Checking existence of a file or directory node on local or remote filesystem |
| **`localfs.parts`** | **1** | `iterative/dvc` | Splitting path string into ordered component segments tuple |
| **`fs_cache.fs.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`self.repo.fs.parts`** | **1** | `iterative/dvc` | Splitting path string into ordered component segments tuple |
| **`_LocalFileSystem`** | **1** | `iterative/dvc` | Protocol Resolution & Driver Lifecycle API method detected across storage interactions |
| **`repo.fs.abspath`** | **1** | `iterative/dvc` | Resolving abstract relative path to fully qualified URI path from working directory |
| **`fs.commonpath`** | **1** | `iterative/dvc` | Find longest common sub-path prefix across multiple paths |
| **`loader.fs.exists`** | **1** | `iterative/dvc` | Checking existence of a file or directory node on local or remote filesystem |
| **`loader.fs.isdir`** | **1** | `iterative/dvc` | Verify whether a path points to an abstract directory container node |
| **`self.repo.fs.abspath`** | **1** | `iterative/dvc` | Resolving abstract relative path to fully qualified URI path from working directory |
| **`out.fs.parts`** | **1** | `iterative/dvc` | Splitting path string into ordered component segments tuple |
| **`git_fs.open('.gitattributes').read`** | **1** | `iterative/dvc` | Read bytes from cache/stream, fetching chunks as necessary |
| **`git_fs.open`** | **1** | `iterative/dvc` | Return a file-like object from the filesystem (`fs.open(path, mode)`) |
| **`local_fs.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`from_fs.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`from_fs.exists`** | **1** | `iterative/dvc` | Checking existence of a file or directory node on local or remote filesystem |
| **`from_fs.find`** | **1** | `iterative/dvc` | Recursively find all file paths inside a directory subtree matching optional criteria |
| **`from_fs.relpath`** | **1** | `iterative/dvc` | Calculating relative path string from a reference parent or root directory |
| **`from_fs.as_posix`** | **1** | `iterative/dvc` | Format path with standardized POSIX forward slash separators |
| **`to_fs.join`** | **1** | `iterative/dvc` | Cross-platform abstract POSIX path joining without OS separator assumptions |
| **`to_fs.exists`** | **1** | `iterative/dvc` | Checking existence of a file or directory node on local or remote filesystem |
| **`to_fs.find`** | **1** | `iterative/dvc` | Recursively find all file paths inside a directory subtree matching optional criteria |
| **`fs_tokenize`** | **1** | `dask/dask` | Protocol Resolution & Driver Lifecycle API method detected across storage interactions |
| **`fs.expand_path`** | **1** | `dask/dask` | Turn one or more glob patterns or directories into a list of all matching concrete paths |
| **`fs.checksum`** | **1** | `dask/dask` | Unique hash/version value for current contents of file (ETag, CRC32, MD5) |
| **`build_name_function`** | **1** | `dask/dask` | Path Arithmetic & Topologies API method detected across storage interactions |
| **`fsspec_parquet.open_parquet_file`** | **1** | `dask/dask` | Parquet-specific byte open call supporting column group section precaching (`parts`) |
| **`dfs[0].copy`** | **1** | `modin-project/modin` | Copy file(s) within two locations on the filesystem without downloading to local disk |
| **`self.fs.glob`** | **1** | `modin-project/modin` | Instance method: Wildcard expression matching (`*`, `?`, `[...]`, `**`) across remote or local directory trees |
| **`fs_handle.glob`** | **1** | `modin-project/modin` | Wildcard expression matching (`*`, `?`, `[...]`, `**`) across remote or local directory trees |
| **`fs_handle.find`** | **1** | `modin-project/modin` | Recursively find all file paths inside a directory subtree matching optional criteria |
| **`fs_handle.exists`** | **1** | `modin-project/modin` | Checking existence of a file or directory node on local or remote filesystem |
| **`fs_resp.get`** | **1** | `feast-dev/feast` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`jvm.org.apache.hadoop.fs.FileSystem.get`** | **1** | `feast-dev/feast` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`refs_str.split`** | **1** | `feast-dev/feast` | Splitting abstract path into `(head, tail)` tuple pair |
| **`fs_yaml_file.exists`** | **1** | `feast-dev/feast` | Checking existence of a file or directory node on local or remote filesystem |
| **`fsspec.core.get_fs_token_paths`** | **1** | `pydata/xarray` | Parsing URL path string into `(fs, fs_token, paths)` for distributed serialization |
| **`self._fs.glob`** | **1** | `kedro-org/kedro` | Wildcard expression matching (`*`, `?`, `[...]`, `**`) across remote or local directory trees |
| **`dbfs_api.put_file`** | **1** | `kedro-org/kedro` | Upload a single local file to remote target path |
| **`diffs.get`** | **1** | `pytorch/torchtitan` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fsdp_config['mesh'].size`** | **1** | `pytorch/torchtitan` | Return size in bytes of a target file |
| **`self.fsdp_param_module_order.get`** | **1** | `pytorch/torchtitan` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`efsdp_mesh.size`** | **1** | `pytorch/torchtitan` | Return size in bytes of a target file |
| **`AsyncFileSystemWrapper`** | **1** | `zarr-developers/zarr-python` | Protocol Resolution & Driver Lifecycle API method detected across storage interactions |
| **`get_filesystem_class`** | **1** | `intake/intake` | Locate and return the filesystem driver class registered for a given protocol |
| **`get_mapper`** | **1** | `intake/intake` | Create a mutable mapping (key/value dict-like) store based on this filesystem |
| **`fs.info(url2, refresh=True).get`** | **1** | `intake/intake` | Bulk batch downloading of remote cloud or distributed files to local directory disk |
| **`fs.cat_file`** | **1** | `intake/intake` | Get the complete byte content of a single file |
| **`fsspec.core.split_protocol`** | **1** | `intake/intake` | Splitting raw string URL into `(protocol, path)` component pair |
| **`_fs.cat_file`** | **1** | `intake/intake` | Get the complete byte content of a single file |
| **`fs.fs.get_file`** | **1** | `intake/intake` | Download a single remote file to local target filename path |
| **`setup_logger`** | **1** | `fsspec/s3fs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`_run_coros_in_chunks`** | **1** | `fsspec/s3fs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`self.fs.cat`** | **1** | `fsspec/s3fs` | Instance method: Fetch (potentially multiple) paths' byte contents as a dictionary |
| **`self.fs.touch`** | **1** | `fsspec/s3fs` | Instance method: Create empty 0-byte file, or update timestamp if file already exists |
| **`register_cache`** | **1** | `fsspec/gcsfs` | Protocol Resolution & Driver Lifecycle API method detected across storage interactions |
| **`setup_logging`** | **1** | `fsspec/gcsfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`get_client`** | **1** | `fsspec/gcsfs` | Bulk Data Transfer API method detected across storage interactions |
| **`other_paths`** | **1** | `fsspec/gcsfs` | Driver Instances & Wrapper Bridges API method detected across storage interactions |
| **`self.fs.cat_file`** | **1** | `fsspec/gcsfs` | Instance method: Get the complete byte content of a single file |
| **`_get_batch_size`** | **1** | `fsspec/adlfs` | Metadata & Existence Checks API method detected across storage interactions |
| **`fs.service_client.close`** | **1** | `fsspec/adlfs` | Close file stream handle and release buffer resources |
