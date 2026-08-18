"""
Optics Use Cases package and registry.
"""

from typing import Dict, List, Optional

from gcs_clients_optics.usecases.async_sync import AsyncSyncUseCase
from gcs_clients_optics.usecases.base import BaseUseCase
from gcs_clients_optics.usecases.cache_type import CacheTypeUseCase
from gcs_clients_optics.usecases.fsspec_methods import FsspecMethodsUseCase
from gcs_clients_optics.usecases.issues_performance import (
    IssuesPerformanceUseCase,
)
from gcs_clients_optics.usecases.protocols import ProtocolsUseCase

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
register_use_case(CacheTypeUseCase())
register_use_case(IssuesPerformanceUseCase())
register_use_case(ProtocolsUseCase())
register_use_case(AsyncSyncUseCase())

__all__ = [
    "BaseUseCase",
    "FsspecMethodsUseCase",
    "CacheTypeUseCase",
    "IssuesPerformanceUseCase",
    "ProtocolsUseCase",
    "AsyncSyncUseCase",
    "USE_CASES",
    "register_use_case",
    "get_use_case",
    "list_use_cases",
]
