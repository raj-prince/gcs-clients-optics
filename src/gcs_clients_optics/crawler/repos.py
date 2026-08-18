"""
Default target repositories configuration for code crawling.
"""

from typing import List, Tuple

DEFAULT_TARGET_REPOS: List[Tuple[str, str]] = [
    ("Dask", "dask/dask"),
    ("Intake", "intake/intake"),
    ("pandas", "pandas-dev/pandas"),
    ("xarray", "pydata/xarray"),
    ("zarr", "zarr-developers/zarr-python"),
    ("DVC", "iterative/dvc"),
    ("Kedro", "kedro-org/kedro"),
    ("Hugging Face Datasets", "huggingface/datasets"),
    ("PyTorch", "pytorch/pytorch"),
    ("PyTorch Lightning", "Lightning-AI/pytorch-lightning"),
    ("TorchTitan", "pytorch/torchtitan"),
    ("Ray", "ray-project/ray"),
    ("Apache Arrow", "apache/arrow"),
]
