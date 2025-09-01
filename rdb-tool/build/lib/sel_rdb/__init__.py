"""
SEL RDB Tools
=============

A comprehensive toolkit for working with SEL (Schweitzer Engineering Laboratories) .rdb relay database files.

This package provides tools to:
- Analyze SEL .rdb files and extract their contents
- Extract logic sections from RDB files
- Convert text-based relay settings to .rdb format
- Work with SEL relay configuration data

Developed by AOUF Nihed, Electrical Engineering student at ESGEE, as part of a final year project
in collaboration with Ateam Pro-tech, an official partner of SEL Schweitzer Engineering Laboratories.

Modules:
    rdb_analyzer: Comprehensive RDB file analysis
    list_rdb_streams: List streams in RDB files
    extract_logic_section: Extract logic sections from RDB files
    create_rdb_template: Template-based RDB creation
    logic_analyzer: Analyze logic equations
    sel_logic_count: Count logic elements
    extract_settings: Extract settings from RDB files
    utils: General utility functions
"""

__version__ = "1.0.0"
__author__ = "AOUF Nihed"
__email__ = "aouf.nihed@esgee.edu"
__license__ = "MIT"

# Import key functions for easier access
from .rdb_analyzer import analyze_rdb_file
from .list_rdb_streams import list_streams
from .extract_logic_section import extract_logic_from_file
from .create_rdb_template import create_rdb_file

# Package metadata
__all__ = [
    "analyze_rdb_file",
    "list_streams",
    "extract_logic_from_file",
    "create_rdb_file",
    "rdb_analyzer",
    "list_rdb_streams",
    "extract_logic_section",
    "create_rdb_template",
    "logic_analyzer",
    "sel_logic_count",
    "extract_settings",
    "utils"
]