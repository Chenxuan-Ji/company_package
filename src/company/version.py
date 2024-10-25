# src/company/version.py

try:
    from setuptools_scm import get_version
    __version__ = get_version(root='..', relative_to=__file__)
except (ImportError, LookupError):
    __version__ = "0.0.0"  # Fallback version if setuptools_scm is not available