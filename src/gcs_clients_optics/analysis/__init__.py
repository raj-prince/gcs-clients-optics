"""
Analysis, cross-repository matrix, and summary table generation.
"""

from gcs_clients_optics.analysis.categorization import (
    USAGE_PATTERNS,
    categorize_method,
)
from gcs_clients_optics.analysis.matrix import generate_method_matrix
from gcs_clients_optics.analysis.summary_table import generate_summary_table

__all__ = [
    "USAGE_PATTERNS",
    "categorize_method",
    "generate_method_matrix",
    "generate_summary_table",
]
