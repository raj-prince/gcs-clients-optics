"""
Optics Use Cases package and registry.
"""

from typing import Dict, List, Optional

from gcs_clients_optics.usecases.base import BaseUseCase
from gcs_clients_optics.usecases.fsspec_methods import FsspecMethodsUseCase

USE_CASES: Dict[str, BaseUseCase] = {}


def register_use_case(use_case: BaseUseCase) -> None:
    """Register a new use-case instance in the global registry."""
    USE_CASES[use_case.name] = use_case
    for alias in use_case.aliases:
        USE_CASES[alias] = use_case


def get_use_case(name_or_alias: str) -> Optional[BaseUseCase]:
    """Retrieve a registered use-case by its name or alias."""
    return USE_CASES.get(name_or_alias)


def list_use_cases() -> List[BaseUseCase]:
    """Return a deduplicated list of all registered primary use cases."""
    seen = set()
    unique = []
    for uc in USE_CASES.values():
        if uc.name not in seen:
            seen.add(uc.name)
            unique.append(uc)
    return unique


# Register default built-in use cases
register_use_case(FsspecMethodsUseCase())

__all__ = [
    "BaseUseCase",
    "FsspecMethodsUseCase",
    "USE_CASES",
    "register_use_case",
    "get_use_case",
    "list_use_cases",
]
