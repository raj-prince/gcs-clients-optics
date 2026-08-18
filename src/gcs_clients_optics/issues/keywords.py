"""
Keyword and label definitions for filtering and scoring filesystem & performance issues.
"""

from typing import List, Set, Tuple

FILESYSTEM_KEYWORDS: Set[str] = {
    "fsspec",
    "gcsfs",
    "s3fs",
    "abfs",
    "pyarrow.fs",
    "filesystem",
    "abstractfilesystem",
    "gcsfilesystem",
    "s3filesystem",
    "open_files",
    "url_to_fs",
    "cache_type",
    "simple_cache",
    "readahead",
    "blockcache",
    "mmap",
    "parts",
}

PERFORMANCE_KEYWORDS: Set[str] = {
    "performance",
    "slow",
    "slowness",
    "latency",
    "throughput",
    "bottleneck",
    "benchmark",
    "speed",
    "speedup",
    "hang",
    "hanging",
    "stall",
    "stalled",
    "timeout",
    "memory leak",
    "high memory",
    "oom",
    "cpu utilization",
    "prefetch",
    "prefetching",
    "caching",
    "cache",
    "chunk_size",
    "block_size",
    "range request",
    "io",
    "i/o",
    "concurrent",
    "multithreading",
}

PERFORMANCE_LABELS: Set[str] = {
    "performance",
    "perf",
    "speed",
    "latency",
    "memory",
    "io",
    "storage",
    "gcs",
    "fsspec",
}

DEFAULT_TARGET_REPOS: List[Tuple[str, str]] = [
    ("Dask", "dask/dask"),
    ("pandas", "pandas-dev/pandas"),
    ("xarray", "pydata/xarray"),
    ("zarr", "zarr-developers/zarr-python"),
    ("Apache Arrow", "apache/arrow"),
    ("Hugging Face Datasets", "huggingface/datasets"),
    ("PyTorch", "pytorch/pytorch"),
    ("Ray", "ray-project/ray"),
]
