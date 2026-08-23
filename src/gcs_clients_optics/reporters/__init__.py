"""
Export formatters and report generators.
"""

from gcs_clients_optics.reporters.categorization import (
    FSSPEC_BASE_SPEC_METHODS,
    FSSPEC_CATEGORIES,
    USAGE_PATTERNS,
    categorize_method,
    get_method_description,
)
from gcs_clients_optics.reporters.code_reports import (
    CACHE_DESCRIPTIONS,
    export_csv_report,
    export_json_report,
    export_markdown_report,
)
from gcs_clients_optics.reporters.matrix import generate_method_matrix
from gcs_clients_optics.reporters.summary_table import generate_summary_table

__all__ = [
    "CACHE_DESCRIPTIONS",
    "export_csv_report",
    "export_json_report",
    "export_markdown_report",
    "generate_method_matrix",
    "generate_summary_table",
    "FSSPEC_CATEGORIES",
    "FSSPEC_BASE_SPEC_METHODS",
    "USAGE_PATTERNS",
    "categorize_method",
    "get_method_description",
]
