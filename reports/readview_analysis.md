# 🚀 ReadView & Zero-Copy Optimization Analysis Report

Evaluated **24** repository targets in **269.53s**.

## 📊 Executive Summary

- **Total Read Operations Evaluated**: `1321`
- **Zero-Copy `readview` Ready (Descoped Ownership)**: `1011` (**76.5%**)
- **Retained / Escaping Ownership (Requires Copy)**: `310`

## 📋 Repository ReadView Feasibility Breakdown

| Repository | Files Scanned | Total Reads | Zero-Copy Ready | % Descoped | Top Consumer Pattern |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **`GitHub:pytorch/pytorch (main)`** | 2554 | 417 | 316 | **75.8%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:pandas-dev/pandas (main)`** | 300 | 125 | 97 | **77.6%** | `DIRECT_CALL_ARGUMENT` |
| **`GitHub:ray-project/ray (master)`** | 2018 | 230 | 195 | **84.8%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:pola-rs/polars (main)`** | 212 | 13 | 13 | **100.0%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:Lightning-AI/pytorch-lightning (main)`** | 457 | 37 | 33 | **89.2%** | `LOCAL_TRANSIENT` |
| **`GitHub:duckdb/duckdb (main)`** | 15 | 2 | 2 | **100.0%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:huggingface/datasets (main)`** | 141 | 68 | 38 | **55.9%** | `ESCAPING_RETURN` |
| **`GitHub:mlflow/mlflow (master)`** | 1300 | 81 | 64 | **79.0%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:apache/arrow (main)`** | 80 | 25 | 20 | **80.0%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:iterative/dvc (main)`** | 258 | 18 | 14 | **77.8%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:dask/dask (main)`** | 184 | 27 | 19 | **70.4%** | `DESCUPED_LOCAL_VARIABLE` |
| **`great-expectations/great_expectations`** | 0 | 0 | 0 | **0.0%** | `None` |
| **`GitHub:modin-project/modin (main)`** | 283 | 26 | 25 | **96.2%** | `LOCAL_TRANSIENT` |
| **`GitHub:flyteorg/flyte (main)`** | 242 | 0 | 0 | **0.0%** | `None` |
| **`GitHub:feast-dev/feast (master)`** | 599 | 31 | 29 | **93.5%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:pydata/xarray (main)`** | 123 | 3 | 0 | **0.0%** | `ESCAPING_RETURN` |
| **`GitHub:kedro-org/kedro (main)`** | 104 | 10 | 10 | **100.0%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:pytorch/torchtitan (main)`** | 313 | 69 | 50 | **72.5%** | `DESCUPED_LOCAL_VARIABLE` |
| **`GitHub:delta-io/delta-rs (main)`** | 18 | 0 | 0 | **0.0%** | `None` |
| **`GitHub:zarr-developers/zarr-python (main)`** | 173 | 10 | 10 | **100.0%** | `DIRECT_CALL_ARGUMENT` |
| **`GitHub:intake/intake (master)`** | 52 | 101 | 50 | **49.5%** | `ESCAPING_RETURN` |
| **`GitHub:fsspec/s3fs (main)`** | 10 | 17 | 17 | **100.0%** | `LOCAL_TRANSIENT` |
| **`GitHub:fsspec/gcsfs (main)`** | 30 | 8 | 7 | **87.5%** | `LOCAL_TRANSIENT` |
| **`GitHub:fsspec/adlfs (main)`** | 6 | 3 | 2 | **66.7%** | `LOCAL_TRANSIENT` |

## 🔍 Actionable Zero-Copy Candidate Snippets

### `GitHub:pytorch/pytorch (main)`
- **.ci/lumen_cli/cli/lib/core/vllm/lib.py:137** (`resp.read` ➔ `JSON_LOADS`)
  *Reason*: Direct in-place consumer 'json.loads' (safe zero-copy candidate)
  *Link*: [.ci/lumen_cli/cli/lib/core/vllm/lib.py#L137](https://github.com/pytorch/pytorch/blob/main/.ci/lumen_cli/cli/lib/core/vllm/lib.py#L137)
  ```python
          req = urllib.request.Request(url, headers=headers)
          with urllib.request.urlopen(req, timeout=30) as resp:
              issue = json.loads(resp.read())
          body = issue.get("body", "") or ""
          entries = _parse_disabled_tests_from_issue_body(body)
  ```
- **.ci/pytorch/print_sccache_log.py:7** (`f.readlines` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'lines' (ownership discarded at function exit)
  *Link*: [.ci/pytorch/print_sccache_log.py#L7](https://github.com/pytorch/pytorch/blob/main/.ci/pytorch/print_sccache_log.py#L7)
  ```python
  
  with open(log_file_path) as f:
      lines = f.readlines()
  
  for line in lines:
  ```
- **.ci/pytorch/smoke_test/check_wheel_tags.py:36** (`zf.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .decode()
  *Link*: [.ci/pytorch/smoke_test/check_wheel_tags.py#L36](https://github.com/pytorch/pytorch/blob/main/.ci/pytorch/smoke_test/check_wheel_tags.py#L36)
  ```python
          if not wheel_files:
              return tags
          content = zf.read(wheel_files[0]).decode("utf-8")
          for line in content.splitlines():
              if line.startswith("Tag:"):
  ```

### `GitHub:pandas-dev/pandas (main)`
- **generate_pxi.py:9** (`f.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'tmpl' (ownership discarded at function exit)
  *Link*: [generate_pxi.py#L9](https://github.com/pandas-dev/pandas/blob/main/generate_pxi.py#L9)
  ```python
  def process_tempita(pxifile, outfile) -> None:
      with open(pxifile, encoding="utf-8") as f:
          tmpl = f.read()
      pyxcontent = Tempita.sub(tmpl)
  ```
- **pandas/compat/_cpu.py:19** (`fh.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .strip()
  *Link*: [pandas/compat/_cpu.py#L19](https://github.com/pandas-dev/pandas/blob/main/pandas/compat/_cpu.py#L19)
  ```python
      try:
          with open(path, encoding="utf-8") as fh:
              return int(fh.read().strip())
      except (OSError, ValueError):
          return None
  ```
- **pandas/compat/_cpu.py:31** (`fh.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .strip()
  *Link*: [pandas/compat/_cpu.py#L31](https://github.com/pandas-dev/pandas/blob/main/pandas/compat/_cpu.py#L31)
  ```python
      try:
          with open(path, encoding="utf-8") as fh:
              return fh.read().strip()
      except (OSError, ValueError):
          return None
  ```

### `GitHub:ray-project/ray (master)`
- **bazel/pyzip.py:40** (`f.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'content' (ownership discarded at function exit)
  *Link*: [bazel/pyzip.py#L40](https://github.com/ray-project/ray/blob/master/bazel/pyzip.py#L40)
  ```python
  
                  with open(file_path, "rb") as f:
                      content = f.read()
                  output.writestr(zip_info, content, compress_type=zipfile.ZIP_STORED)
  ```
- **python/ray/_common/utils.py:400** (`f.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .strip()
  *Link*: [python/ray/_common/utils.py#L400](https://github.com/ray-project/ray/blob/master/python/ray/_common/utils.py#L400)
  ```python
      if os.path.exists(memory_limit_filename):
          with open(memory_limit_filename, "r") as f:
              docker_limit = int(f.read().strip())
      elif os.path.exists(memory_limit_filename_v2):
          with open(memory_limit_filename_v2, "r") as f:
  ```
- **python/ray/_common/utils.py:404** (`f.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .strip()
  *Link*: [python/ray/_common/utils.py#L404](https://github.com/ray-project/ray/blob/master/python/ray/_common/utils.py#L404)
  ```python
          with open(memory_limit_filename_v2, "r") as f:
              # Don't forget to strip() the newline:
              max_file = f.read().strip()
              if max_file.isnumeric():
                  docker_limit = int(max_file)
  ```

### `GitHub:pola-rs/polars (main)`
- **py-polars/debug/launch.py:41** (`f.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'launch_info' (ownership discarded at function exit)
  *Link*: [py-polars/debug/launch.py#L41](https://github.com/pola-rs/polars/blob/main/py-polars/debug/launch.py#L41)
  ```python
          raise RuntimeError(msg)
      with launch_file.open("r") as f:
          launch_info = f.read()
  
      # Overwrite the pid found in launch.json with the pid for the current process.
  ```
- **py-polars/debug/launch.py:71** (`fh.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'script_contents' (ownership discarded at function exit)
  *Link*: [py-polars/debug/launch.py#L71](https://github.com/pola-rs/polars/blob/main/py-polars/debug/launch.py#L71)
  ```python
      sys.argv.pop(0)
      with Path(sys.argv[0]).open() as fh:
          script_contents = fh.read()
  
      # Run the originally requested file by reading in the script, compiling, and
  ```
- **py-polars/runtime/template.py:31** (`f.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'cargo_toml' (ownership discarded at function exit)
  *Link*: [py-polars/runtime/template.py#L31](https://github.com/pola-rs/polars/blob/main/py-polars/runtime/template.py#L31)
  ```python
  
          with (basedir / "Cargo.toml").open() as f:
              cargo_toml = f.read()
          with (basedir / "pyproject.toml").open() as f:
              pyproject_toml = f.read()
  ```

### `GitHub:Lightning-AI/pytorch-lightning (main)`
- **.actions/assistant.py:350** (`fo.readlines` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'lines' (ownership discarded at function exit)
  *Link*: [.actions/assistant.py#L350](https://github.com/Lightning-AI/pytorch-lightning/blob/main/.actions/assistant.py#L350)
  ```python
          with open(fp, encoding="utf-8") as fo:
              try:
                  lines = fo.readlines()
              except UnicodeDecodeError:
                  # a binary file, skip
  ```
- **.actions/assistant.py:411** (`fo.read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [.actions/assistant.py#L411](https://github.com/Lightning-AI/pytorch-lightning/blob/main/.actions/assistant.py#L411)
  ```python
      def _replace_min(fname: str) -> None:
          with open(fname, encoding="utf-8") as fo:
              req = fo.read().replace(">=", "==")
          with open(fname, "w", encoding="utf-8") as fw:
              fw.write(req)
  ```
- **.actions/assistant.py:500** (`fopen.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'page' (ownership discarded at function exit)
  *Link*: [.actions/assistant.py#L500](https://github.com/Lightning-AI/pytorch-lightning/blob/main/.actions/assistant.py#L500)
  ```python
          """Copy RST page with optional inserting orphan statement."""
          with open(rst_in, encoding="utf-8") as fopen:
              page = fopen.read()
          if as_orphan and ":orphan:" not in page:
              page = ":orphan:\n\n" + page
  ```

### `GitHub:duckdb/duckdb (main)`
- **data/parquet-testing/pyarrow-generate-parquet.py:57** (`f.readlines` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'lines' (ownership discarded at function exit)
  *Link*: [data/parquet-testing/pyarrow-generate-parquet.py#L57](https://github.com/duckdb/duckdb/blob/main/data/parquet-testing/pyarrow-generate-parquet.py#L57)
  ```python
      """ Replace empty values with 'NULL' """
      with open(path, 'r') as f:
          lines = f.readlines()
  
      with open(path, 'w') as f:
  ```
- **tools/swift/create_package.py:66** (`f.read` ➔ `DIRECT_CALL_ARGUMENT`)
  *Reason*: Passed directly to consumer function 'Template'
  *Link*: [tools/swift/create_package.py#L66](https://github.com/duckdb/duckdb/blob/main/tools/swift/create_package.py#L66)
  ```python
  package_manifest_path = os.path.join(package_dir, 'Package.swift')
  with open('Package.swift.template', 'r') as f:
      src = Template(f.read())
      result = src.substitute(content)
      with open(package_manifest_path, 'w') as f:
  ```

### `GitHub:huggingface/datasets (main)`
- **setup.py:249** (`open.read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [setup.py#L249](https://github.com/huggingface/datasets/blob/main/setup.py#L249)
  ```python
      version="5.0.2.dev0",  # expected format is one of x.y.z.dev0, or x.y.z.rc1 or x.y.z (no to dashes, yes to dots)
      description="HuggingFace community-driven open-source library of datasets",
      long_description=open("README.md", encoding="utf-8").read(),
      long_description_content_type="text/markdown",
      author="HuggingFace Inc.",
  ```
- **src/datasets/features/features.py:1194** (`f.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .split()
  *Link*: [src/datasets/features/features.py#L1194](https://github.com/huggingface/datasets/blob/main/src/datasets/features/features.py#L1194)
  ```python
      def _load_names_from_file(names_filepath):
          with open(names_filepath, encoding="utf-8") as f:
              return [name.strip() for name in f.read().split("\n") if name.strip()]  # Filter empty names
  
  ```
- **src/datasets/features/image.py:189** (`f.read` ➔ `BYTESIO_STREAM`)
  *Reason*: Direct in-place consumer 'BytesIO' (safe zero-copy candidate)
  *Link*: [src/datasets/features/image.py#L189](https://github.com/huggingface/datasets/blob/main/src/datasets/features/image.py#L189)
  ```python
                      download_config = DownloadConfig(token=token)
                      with xopen(path, "rb", download_config=download_config) as f:
                          bytes_ = BytesIO(f.read())
                      image = PIL.Image.open(bytes_)
          else:
  ```

### `GitHub:mlflow/mlflow (master)`
- **.claude/hooks/validate_pr_body.py:31** (`sys.stdin.read` ➔ `JSON_LOADS`)
  *Reason*: Direct in-place consumer 'json.loads' (safe zero-copy candidate)
  *Link*: [.claude/hooks/validate_pr_body.py#L31](https://github.com/mlflow/mlflow/blob/master/.claude/hooks/validate_pr_body.py#L31)
  ```python
  def main() -> None:
      try:
          input_data = json.loads(sys.stdin.read())
      except (json.JSONDecodeError, OSError):
          return
  ```
- **.claude/skills/src/skills/commands/fetch_diff.py:58** (`f.readline` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'first_line' (ownership discarded at function exit)
  *Link*: [.claude/skills/src/skills/commands/fetch_diff.py#L58](https://github.com/mlflow/mlflow/blob/master/.claude/skills/src/skills/commands/fetch_diff.py#L58)
  ```python
      if path.suffix == ".java" and path.exists():
          with path.open() as f:
              first_line = f.readline()
          if "Generated by the protocol buffer compiler" in first_line:
              return True
  ```
- **.claude/skills/src/skills/github/uploads.py:69** (`path.read_bytes` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [.claude/skills/src/skills/github/uploads.py#L69](https://github.com/mlflow/mlflow/blob/master/.claude/skills/src/skills/github/uploads.py#L69)
  ```python
      request = urllib.request.Request(
          f"{UPLOAD_URL}?{query}",
          data=path.read_bytes(),
          method="POST",
          headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
  ```

### `GitHub:apache/arrow (main)`
- **c_glib/tool/generate-version-header.py:83** (`input_file.read` ➔ `DIRECT_CALL_ARGUMENT`)
  *Reason*: Passed directly to consumer function 're.sub'
  *Link*: [c_glib/tool/generate-version-header.py#L83](https://github.com/apache/arrow/blob/main/c_glib/tool/generate-version-header.py#L83)
  ```python
  
      output_file.write(re.sub(
          r"@([A-Z_]+)@", lambda match: replacements[match[1]], input_file.read()))
  
  ```
- **cpp/build-support/asan_symbolize.py:83** (`self.pipe.stdout.readline` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [cpp/build-support/asan_symbolize.py#L83](https://github.com/apache/arrow/blob/main/cpp/build-support/asan_symbolize.py#L83)
  ```python
        self.pipe.stdin.write('\n')
        while True:
          function_name = self.pipe.stdout.readline().rstrip()
          if not function_name:
            break
  ```
- **cpp/build-support/asan_symbolize.py:86** (`self.pipe.stdout.readline` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [cpp/build-support/asan_symbolize.py#L86](https://github.com/apache/arrow/blob/main/cpp/build-support/asan_symbolize.py#L86)
  ```python
          if not function_name:
            break
          file_name = self.pipe.stdout.readline().rstrip()
          file_name = fix_filename(file_name)
          if (not function_name.startswith('??') and
  ```

### `GitHub:iterative/dvc (main)`
- **dvc/commands/cache.py:17** (`self.config.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'conf' (ownership discarded at function exit)
  *Link*: [dvc/commands/cache.py#L17](https://github.com/iterative/dvc/blob/main/dvc/commands/cache.py#L17)
  ```python
  
              if self.args.level:
                  conf = self.config.read(level=self.args.level)
              else:
                  # Use merged config with default values
  ```
- **dvc/commands/config.py:74** (`self.config.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'conf' (ownership discarded at function exit)
  *Link*: [dvc/commands/config.py#L74](https://github.com/iterative/dvc/blob/main/dvc/commands/config.py#L74)
  ```python
  
          for level in levels:
              conf = self.config.read(level)
              prefix = self._config_file_prefix(self.args.show_origin, self.config, level)
              configs = list(self._format_config(conf, prefix))
  ```
- **dvc/commands/config.py:88** (`self.config.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'conf' (ownership discarded at function exit)
  *Link*: [dvc/commands/config.py#L88](https://github.com/iterative/dvc/blob/main/dvc/commands/config.py#L88)
  ```python
  
          for level in levels:
              conf = self.config.read(level)
              if remote_or_db:
                  conf = conf[remote_or_db]
  ```

### `GitHub:dask/dask (main)`
- **dask/bag/avro.py:18** (`fo.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'c' (ownership discarded at function exit)
  *Link*: [dask/bag/avro.py#L18](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L18)
  ```python
  def read_long(fo):
      """variable-length, zig-zag encoding."""
      c = fo.read(1)
      b = ord(c)
      n = b & 0x7F
  ```
- **dask/bag/avro.py:23** (`fo.read` ➔ `DIRECT_CALL_ARGUMENT`)
  *Reason*: Passed directly to consumer function 'ord'
  *Link*: [dask/bag/avro.py#L23](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L23)
  ```python
      shift = 7
      while (b & 0x80) != 0:
          b = ord(fo.read(1))
          n |= (b & 0x7F) << shift
          shift += 7
  ```
- **dask/bag/avro.py:47** (`fo.read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [dask/bag/avro.py#L47](https://github.com/dask/dask/blob/main/dask/bag/avro.py#L47)
  ```python
      fo: file-like
      """
      assert fo.read(len(MAGIC)) == MAGIC, "Magic avro bytes missing"
      meta = {}
      out = {"meta": meta}
  ```

### `GitHub:modin-project/modin (main)`
- **modin/core/io/text/excel_dispatcher.py:116** (`ex.read` ➔ `STANDALONE_DRAIN`)
  *Reason*: Result discarded immediately after execution
  *Link*: [modin/core/io/text/excel_dispatcher.py#L116](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L116)
  ```python
          try:
              ex = ExcelReader(io_file, read_only=True)
              ex.read()
              wb = ex.wb
  ```
- **modin/core/io/text/excel_dispatcher.py:145** (`f.read` ➔ `BYTESIO_STREAM`)
  *Reason*: Direct in-place consumer 'BytesIO' (safe zero-copy candidate)
  *Link*: [modin/core/io/text/excel_dispatcher.py#L145](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L145)
  ```python
  
              f = z.open("xl/worksheets/{}.xml".format(sheet_name))
              f = BytesIO(f.read())
              total_bytes = cls.file_size(f)
  ```
- **modin/core/io/text/excel_dispatcher.py:152** (`f.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'sheet_block' (ownership discarded at function exit)
  *Link*: [modin/core/io/text/excel_dispatcher.py#L152](https://github.com/modin-project/modin/blob/main/modin/core/io/text/excel_dispatcher.py#L152)
  ```python
              # because that is where the column names are. The header information will
              # be extracted and sent to all of the nodes.
              sheet_block = f.read(EXCEL_READ_BLOCK_SIZE)
              end_of_row_tag = b"</row>"
              while end_of_row_tag not in sheet_block:
  ```

### `GitHub:feast-dev/feast (master)`
- **sdk/python/feast/credentials.py:324** (`f.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .strip()
  *Link*: [sdk/python/feast/credentials.py#L324](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/credentials.py#L324)
  ```python
          try:
              with open(ns_path) as f:
                  return f.read().strip()
          except FileNotFoundError:
              return "default"
  ```
- **sdk/python/feast/demos.py:68** (`fh.read` ➔ `DIRECT_CALL_ARGUMENT`)
  *Reason*: Passed directly to consumer function 'os.path.expandvars'
  *Link*: [sdk/python/feast/demos.py#L68](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/demos.py#L68)
  ```python
  def _parse_yaml(yaml_path: pathlib.Path) -> dict[str, Any]:
      with open(yaml_path) as fh:
          return yaml.safe_load(os.path.expandvars(fh.read())) or {}
  
  ```
- **sdk/python/feast/file_utils.py:29** (`f.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'contents' (ownership discarded at function exit)
  *Link*: [sdk/python/feast/file_utils.py#L29](https://github.com/feast-dev/feast/blob/master/sdk/python/feast/file_utils.py#L29)
  ```python
      """
      with open(file_path, "r") as f:
          contents = f.read()
      contents = contents.replace(match_str, sub_str)
      with open(file_path, "wt") as f:
  ```

### `GitHub:kedro-org/kedro (main)`
- **features/steps/cli_steps.py:401** (`context.result.stdout.readline` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'stdout' (ownership discarded at function exit)
  *Link*: [features/steps/cli_steps.py#L401](https://github.com/kedro-org/kedro/blob/main/features/steps/cli_steps.py#L401)
  ```python
      # FIXME: Will continue iterating after the process has returned
      while time() < timeout_start + timeout:
          stdout = context.result.stdout.readline()
          if "http://127.0.0.1:" in stdout:
              # Take a breath, and declare success
  ```
- **features/steps/cli_steps.py:611** (`context.result.stdout.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .decode()
  *Link*: [features/steps/cli_steps.py#L611](https://github.com/kedro-org/kedro/blob/main/features/steps/cli_steps.py#L611)
  ```python
  
      if isinstance(context.result, ChildTerminatingPopen):
          stdout = context.result.stdout.read().decode()
          context.result.terminate()
      else:
  ```
- **features/steps/cli_steps.py:628** (`context.result.stdout.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .decode()
  *Link*: [features/steps/cli_steps.py#L628](https://github.com/kedro-org/kedro/blob/main/features/steps/cli_steps.py#L628)
  ```python
  
      if isinstance(context.result, ChildTerminatingPopen):
          stdout = context.result.stdout.read().decode()
          context.result.terminate()
      else:
  ```

### `GitHub:pytorch/torchtitan (main)`
- **torchtitan/components/tokenizer.py:158** (`f.read` ➔ `DIRECT_CALL_ARGUMENT`)
  *Reason*: Passed directly to consumer function 'self.set_chat_template'
  *Link*: [torchtitan/components/tokenizer.py#L158](https://github.com/pytorch/torchtitan/blob/main/torchtitan/components/tokenizer.py#L158)
  ```python
              if os.path.exists(jinja_path):
                  with open(jinja_path) as f:
                      self.set_chat_template(f.read())
              elif "chat_template" in self._hf_config:
                  self.set_chat_template(self._hf_config["chat_template"])
  ```
- **torchtitan/distributed/linear.py:261** (`torch.cat` ➔ `DIRECT_CALL_ARGUMENT`)
  *Reason*: Passed directly to consumer function 'torch.ops.symm_mem.fused_matmul_reduce_scatter'
  *Link*: [torchtitan/distributed/linear.py#L261](https://github.com/pytorch/torchtitan/blob/main/torchtitan/distributed/linear.py#L261)
  ```python
          # weight-sized copy, cheaper than a second reduce-scatter.
          grad_x_shard_m = torch.ops.symm_mem.fused_matmul_reduce_scatter(
              torch.cat(grad_ys, dim=1),
              torch.cat((wa_shard_n, wb_shard_n), dim=0),
              "sum",
  ```
- **torchtitan/distributed/linear.py:262** (`torch.cat` ➔ `DIRECT_CALL_ARGUMENT`)
  *Reason*: Passed directly to consumer function 'torch.ops.symm_mem.fused_matmul_reduce_scatter'
  *Link*: [torchtitan/distributed/linear.py#L262](https://github.com/pytorch/torchtitan/blob/main/torchtitan/distributed/linear.py#L262)
  ```python
          grad_x_shard_m = torch.ops.symm_mem.fused_matmul_reduce_scatter(
              torch.cat(grad_ys, dim=1),
              torch.cat((wa_shard_n, wb_shard_n), dim=0),
              "sum",
              0,
  ```

### `GitHub:zarr-developers/zarr-python (main)`
- **src/zarr/codecs/sharding.py:1003** (`self._get_inner_pipeline.read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [src/zarr/codecs/sharding.py#L1003](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/codecs/sharding.py#L1003)
  ```python
  
          # decoding chunks and writing them into the output buffer
          await self._get_inner_pipeline(shard_spec).read(
              [
                  (
  ```
- **src/zarr/codecs/sharding.py:1071** (`self._get_inner_pipeline.read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [src/zarr/codecs/sharding.py#L1071](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/codecs/sharding.py#L1071)
  ```python
  
          # decoding chunks and writing them into the output buffer
          await self._get_inner_pipeline(shard_spec).read(
              [
                  (
  ```
- **src/zarr/core/array.py:5480** (`codec_pipeline.read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [src/zarr/core/array.py#L5480](https://github.com/zarr-developers/zarr-python/blob/main/src/zarr/core/array.py#L5480)
  ```python
                  prototype=prototype,
              )
          results = await codec_pipeline.read(
              [
                  (
  ```

### `GitHub:intake/intake (master)`
- **intake/catalog/local.py:648** (`f.read` ➔ `CHAINED_TRANSFORMATION`)
  *Reason*: Immediately transformed in-place via .decode()
  *Link*: [intake/catalog/local.py#L648](https://github.com/intake/intake/blob/master/intake/catalog/local.py#L648)
  ```python
  
              with file_open as f:
                  text = f.read().decode()
              if "!template " in text:
                  logger.warning("Use of '!template' deprecated - fixing")
  ```
- **intake/interface/gui.py:111** (`source.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'cat' (ownership discarded at function exit)
  *Link*: [intake/interface/gui.py#L111](https://github.com/intake/intake/blob/master/intake/interface/gui.py#L111)
  ```python
              elif "Catalog" in getattr(source, "output_instance", ""):
                  if name not in self._cats:
                      cat = source.read()
                      self._cats[name] = cat
                      self._children.setdefault(catname, []).append(name)
  ```
- **intake/interface/source/defined_plots.py:283** (`self.source.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'data' (ownership discarded at function exit)
  *Link*: [intake/interface/source/defined_plots.py#L283](https://github.com/intake/intake/blob/master/intake/interface/source/defined_plots.py#L283)
  ```python
                  data = self.source.to_dask()
              except NotImplementedError:
                  data = self.source.read()
              if not isinstance(data, (xarray.DataArray, xarray.Dataset)):
                  data = xarray.DataArray(data)
  ```

### `GitHub:fsspec/s3fs (main)`
- **s3fs/core.py:1325** (`read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [s3fs/core.py#L1325](https://github.com/fsspec/s3fs/blob/main/s3fs/core.py#L1325)
  ```python
              )
              try:
                  return await resp["Body"].read()
              finally:
                  resp["Body"].close()
  ```
- **s3fs/core.py:1370** (`read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [s3fs/core.py#L1370](https://github.com/fsspec/s3fs/blob/main/s3fs/core.py#L1370)
  ```python
                  **kw,
              )
              data = await resp["Body"].read()
              resp["Body"].close()
              return start, data
  ```
- **s3fs/core.py:1494** (`f0.read` ➔ `DESCUPED_LOCAL_VARIABLE`)
  *Reason*: Local transient variable 'chunk' (ownership discarded at function exit)
  *Link*: [s3fs/core.py#L1494](https://github.com/fsspec/s3fs/blob/main/s3fs/core.py#L1494)
  ```python
          with open(lpath, "rb") as f0:
              if size < min(5 * 2**30, 2 * chunksize):
                  chunk = f0.read()
                  await self._call_s3(
                      "put_object", Bucket=bucket, Key=key, Body=chunk, **kwargs, **match
  ```

### `GitHub:fsspec/gcsfs (main)`
- **gcsfs/core.py:120** (`r.read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [gcsfs/core.py#L120](https://github.com/fsspec/gcsfs/blob/main/gcsfs/core.py#L120)
  ```python
  async def _req_to_text(r):
      async with r:
          return (await r.read()).decode()
  
  ```
- **gcsfs/core.py:537** (`r.read` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [gcsfs/core.py#L537](https://github.com/fsspec/gcsfs/blob/main/gcsfs/core.py#L537)
  ```python
              headers = r.headers
              info = r.request_info  # for debug only
              contents = await r.read()
  
              validate_response(status, contents, path, args)
  ```
- **gcsfs/core.py:1772** (`f0.read` ➔ `DIRECT_CALL_ARGUMENT`)
  *Reason*: Passed directly to consumer function 'simple_upload'
  *Link*: [gcsfs/core.py#L1772](https://github.com/fsspec/gcsfs/blob/main/gcsfs/core.py#L1772)
  ```python
                      bucket,
                      key,
                      f0.read(),
                      consistency=consistency,
                      metadatain=metadata,
  ```

### `GitHub:fsspec/adlfs (main)`
- **adlfs/spec.py:1597** (`self.cat_file` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [adlfs/spec.py#L1597](https://github.com/fsspec/adlfs/blob/main/adlfs/spec.py#L1597)
  ```python
              for path in paths:
                  try:
                      out[path] = self.cat_file(path, **kwargs)
                  except Exception as e:
                      if on_error == "raise":
  ```
- **adlfs/spec.py:1865** (`stream.readinto` ➔ `LOCAL_TRANSIENT`)
  *Reason*: Local scope execution without explicit escape detected
  *Link*: [adlfs/spec.py#L1865](https://github.com/fsspec/adlfs/blob/main/adlfs/spec.py#L1865)
  ```python
                  )
                  with open(lpath, "wb") as my_blob:
                      await stream.readinto(my_blob)
          except ResourceNotFoundError as exception:
              raise FileNotFoundError(
  ```
