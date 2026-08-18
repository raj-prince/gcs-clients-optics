"""
Unit tests for simulation module.
"""

import pytest
from gcs_clients_optics.simulation.simulator import run_fsspec_simulation


def test_simulation_runs_successfully():
    results = run_fsspec_simulation(verbose=False)
    assert results["directories_created"] == 5
    assert results["files_created"] >= 10
    assert results["files_read"] >= 1
    assert results["traversal_matches"] >= 3
