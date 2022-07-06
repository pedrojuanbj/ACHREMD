"""
Unit and regression test for the ACHREMD package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import ACHREMD


def test_ACHREMD_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "ACHREMD" in sys.modules
