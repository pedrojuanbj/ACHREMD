"""Atom-Charge Hamiltonian Replica Exchange Molecular Dynamics package for enhanced sampling"""

# Add imports here
from .main import *

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
