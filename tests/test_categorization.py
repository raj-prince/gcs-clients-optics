"""
Unit tests for fsspec base specification categorization and method mapping.
"""

import pytest
import inspect
from fsspec.spec import AbstractFileSystem, AbstractBufferedFile
from gcs_clients_optics.analysis.categorization import (
    CATEGORY_MUTATION,
    CATEGORY_METADATA,
    CATEGORY_PROTOCOL_LIFECYCLE,
    CATEGORY_STREAM_IO,
    CATEGORY_TOPOLOGY,
    CATEGORY_TRANSFER,
    CATEGORY_TRAVERSAL,
    CATEGORY_WRAPPERS,
    FSSPEC_BASE_SPEC_METHODS,
    FSSPEC_CATEGORIES,
    categorize_method,
    get_method_description,
    get_methods_in_category,
    is_fsspec_base_method,
)


def test_fsspec_categories_count():
    assert len(FSSPEC_CATEGORIES) == 8
    assert CATEGORY_STREAM_IO in FSSPEC_CATEGORIES
    assert CATEGORY_METADATA in FSSPEC_CATEGORIES
    assert CATEGORY_TRAVERSAL in FSSPEC_CATEGORIES
    assert CATEGORY_MUTATION in FSSPEC_CATEGORIES
    assert CATEGORY_TRANSFER in FSSPEC_CATEGORIES
    assert CATEGORY_TOPOLOGY in FSSPEC_CATEGORIES
    assert CATEGORY_PROTOCOL_LIFECYCLE in FSSPEC_CATEGORIES
    assert CATEGORY_WRAPPERS in FSSPEC_CATEGORIES


def test_all_abstract_filesystem_methods_mapped():
    """Verify that every non-dunder method in fsspec.spec.AbstractFileSystem is mapped."""
    afs_methods = [
        name
        for name, member in inspect.getmembers(AbstractFileSystem)
        if (inspect.isfunction(member) or inspect.ismethod(member))
        and not (name.startswith("__") and name.endswith("__"))
    ]

    for m in afs_methods:
        assert (
            m in FSSPEC_BASE_SPEC_METHODS
        ), f"AbstractFileSystem method '{m}' is missing from FSSPEC_BASE_SPEC_METHODS!"
        cat = categorize_method(m)
        assert cat in FSSPEC_CATEGORIES
        assert len(get_method_description(m)) > 5


def test_all_abstract_buffered_file_methods_mapped():
    """Verify that file stream methods (readinto, readinto1, etc.) from AbstractBufferedFile are mapped."""
    abf_methods = [
        name
        for name, member in inspect.getmembers(AbstractBufferedFile)
        if (inspect.isfunction(member) or inspect.ismethod(member))
        and not (name.startswith("__") and name.endswith("__"))
    ]

    for m in abf_methods:
        assert (
            m in FSSPEC_BASE_SPEC_METHODS
        ), f"AbstractBufferedFile method '{m}' is missing from FSSPEC_BASE_SPEC_METHODS!"
        cat = categorize_method(m)
        assert cat in FSSPEC_CATEGORIES


def test_readinto_and_stream_methods():
    assert "readinto" in FSSPEC_BASE_SPEC_METHODS
    assert "readinto1" in FSSPEC_BASE_SPEC_METHODS
    assert categorize_method("readinto") == CATEGORY_STREAM_IO
    assert categorize_method("readinto1") == CATEGORY_STREAM_IO
    assert categorize_method("f.readinto") == CATEGORY_STREAM_IO
    assert categorize_method("self.file.readinto1") == CATEGORY_STREAM_IO
    assert is_fsspec_base_method("readinto") is True
    assert is_fsspec_base_method("readinto1") is True


def test_composite_instance_method_categorization():
    assert categorize_method("self.fs.open") == CATEGORY_STREAM_IO
    assert categorize_method("fs.exists") == CATEGORY_METADATA
    assert categorize_method("self.fs.glob") == CATEGORY_TRAVERSAL
    assert categorize_method("fs.find") == CATEGORY_TRAVERSAL
    assert categorize_method("self.fs.mkdir") == CATEGORY_MUTATION
    assert categorize_method("fs.get") == CATEGORY_TRANSFER
    assert categorize_method("self.fs.relparts") == CATEGORY_TOPOLOGY
    assert categorize_method("fsspec.filesystem") == CATEGORY_PROTOCOL_LIFECYCLE
    assert categorize_method("url_to_fs") == CATEGORY_PROTOCOL_LIFECYCLE
    assert categorize_method("ArrowFSWrapper") == CATEGORY_WRAPPERS


def test_helper_functions():
    assert is_fsspec_base_method("open") is True
    assert is_fsspec_base_method("self.fs.ls") is True
    assert is_fsspec_base_method("custom_unknown_method_xyz") is False

    stream_methods = get_methods_in_category(CATEGORY_STREAM_IO)
    assert "open" in stream_methods
    assert "cat" in stream_methods
    assert "read_block" in stream_methods
    assert "readinto" in stream_methods
    assert "readinto1" in stream_methods

    traversal_methods = get_methods_in_category(CATEGORY_TRAVERSAL)
    assert "ls" in traversal_methods
    assert "glob" in traversal_methods
    assert "find" in traversal_methods
    assert "walk" in traversal_methods
