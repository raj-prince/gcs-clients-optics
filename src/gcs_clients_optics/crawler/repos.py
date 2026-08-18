"""
Default target repositories configuration for code crawling.
"""

from pathlib import Path
from typing import List, Optional, Tuple, Union


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


def get_default_target_repos(
    repo_file: Optional[Union[str, Path]] = None,
    min_stars: int = 0,
    limit: Optional[int] = None,
) -> List[Tuple[str, str]]:
    """
    Get target repositories, loading from a dependents file if available.

    Checks:
    1. Explicit `repo_file`
    2. `data/default_dependents.json` (workspace relative)
    3. Packaged `gcs_clients_optics/data/default_dependents.json`
    4. Fallback to `DEFAULT_TARGET_REPOS`
    """
    from gcs_clients_optics.crawler.dependents import load_repos_from_file

    candidates = []
    if repo_file:
        candidates.append(Path(repo_file))

    candidates.extend([
        Path("data/default_dependents.json"),
        Path(__file__).parent.parent / "data" / "default_dependents.json",
    ])

    for cand in candidates:
        if cand.exists() and cand.is_file():
            loaded = load_repos_from_file(cand, min_stars=min_stars, limit=limit)
            if loaded:
                return loaded

    return DEFAULT_TARGET_REPOS

