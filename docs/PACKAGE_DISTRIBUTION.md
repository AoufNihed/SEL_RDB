# SEL_Rdb Package - Distribution Summary

## Package Information

- **Name**: SEL_Rdb
- **Version**: 1.0.0
- **Author**: AOUF Nihed
- **Affiliation**: ESGEE (École Supérieure de Génie Électrique)
- **Partnership**: Ateam Pro-tech (Official SEL Partner)
- **License**: MIT

## Package Contents

The SEL_Rdb package includes the following modules:

1. **rdb_analyzer** - Comprehensive RDB file analysis
2. **list_rdb_streams** - List streams in RDB files
3. **extract_logic_section** - Extract logic sections from RDB files
4. **create_rdb_template** - Template-based RDB creation
5. **logic_analyzer** - Analyze logic equations
6. **sel_logic_count** - Count logic elements
7. **extract_settings** - Extract settings from RDB files
8. **utils** - General utility functions

## Installation

### From PyPI (when published):
```bash
pip install SEL_Rdb
```

### From local distribution files:
```bash
# Install from wheel file
pip install dist/SEL_Rdb-1.0.0-py3-none-any.whl

# Or install from source distribution
pip install dist/sel_rdb-1.0.0.tar.gz
```

## Usage

### As a Command-Line Tool:

```bash
# List streams in an RDB file
sel-rdb-list path/to/file.rdb

# Analyze an RDB file
sel-rdb-analyze path/to/file.rdb

# Extract logic sections from an RDB file
sel-rdb-extract-logic path/to/file.rdb

# Create an RDB file from a text file
sel-rdb-create path/to/settings.txt path/to/output.rdb
```

### As a Python Library:

```python
import sel_rdb

# List streams in an RDB file
streams = sel_rdb.list_streams("path/to/file.rdb")

# Analyze an RDB file
sel_rdb.analyze_rdb_file("path/to/file.rdb")

# Extract logic from an RDB file
logic = sel_rdb.extract_logic_from_file("path/to/file.rdb")

# Create an RDB file from a text file
sel_rdb.create_rdb_file("path/to/settings.txt", "path/to/output.rdb")
```

## Requirements

- Python 3.6+
- olefile
- openpyxl

## Distribution Files

The following distribution files have been created:

1. **Wheel File**: `dist/SEL_Rdb-1.0.0-py3-none-any.whl`
   - Platform-independent binary distribution
   - Ready for installation with pip

2. **Source Distribution**: `dist/sel_rdb-1.0.0.tar.gz`
   - Source code distribution
   - Can be installed on any platform with compatible Python version

## Package Structure

```
sel_rdb/
├── __init__.py
├── rdb_analyzer.py
├── list_rdb_streams.py
├── extract_logic_section.py
├── create_rdb_template.py
├── logic_analyzer.py
├── sel_logic_count.py
├── extract_settings.py
├── utils.py
├── Relay710.rdb          # Template file for RDB creation
└── ...
```

## Entry Points

The package provides the following command-line entry points:

- `sel-rdb-list` - List streams in RDB files
- `sel-rdb-analyze` - Analyze RDB files
- `sel-rdb-extract-logic` - Extract logic sections
- `sel-rdb-create` - Create RDB files from text settings

## Development Information

This package was developed as part of a final year project by **AOUF Nihed**, an Electrical Engineering student at **ESGEE (École Supérieure de Génie Électrique)**, in collaboration with **Ateam Pro-tech**, an official partner of **SEL Schweitzer Engineering Laboratories**.

## Future Enhancements

Potential future enhancements for the package:

1. **Improved Documentation**: More comprehensive API documentation
2. **Extended Functionality**: Additional tools for RDB file manipulation
3. **Better Error Handling**: More robust error handling and reporting
4. **Enhanced Testing**: More comprehensive test suite
5. **Python 3.11+ Support**: Optimization for newer Python versions

## License

This project is licensed under the MIT License - see the LICENSE file for details.