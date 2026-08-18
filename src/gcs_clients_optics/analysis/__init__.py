"""
Analysis, cross-repository matrix, categorization, and summary table generation.
"""

from gcs_clients_optics.analysis.categorization import (
    FSSPEC_BASE_SPEC_METHODS,
    FSSPEC_CATEGORIES,
    USAGE_PATTERNS,
    categorize_method,
    get_method_description,
    get_methods_in_category,
    is_fsspec_base_method,
)
from gcs_clients_optics.analysis.matrix import generate_method_matrix
from gcs_clients_optics.analysis.summary_table import generate_summary_table

__all__ = [
    "FSSPEC_BASE_SPEC_METHODS",
    "FSSPEC_CATEGORIES",
    "USAGE_PATTERNS",
    "categorize_method",
    "get_method_description",
    "get_methods_in_category",
    "is_fsspec_base_method",
    "generate_method_matrix",
    "generate_summary_table",
]
