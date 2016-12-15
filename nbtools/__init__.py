"""Initialisation of nbtools package."""
# convenience imports
from .progressbars import display_multi_progress
from .progressbars import ListProgressBar
from .parallel import execute_in_parallel

import pkg_resources

__version__ = pkg_resources.get_distribution('nbtools').version
