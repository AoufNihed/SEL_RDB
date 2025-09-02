# Installation Guide

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation Methods

### From PyPI (Recommended)

To install SEL_RDB from PyPI, simply run:

```bash
pip install SEL_Rdb
```

### Developer Installation (Editable Mode)

For development purposes, you can install the package in editable mode:

```bash
pip install -e ".[dev]"
```

### From Source

To install directly from the source code:

```bash
git clone https://github.com/AoufNihed/SEL_Rdb.git
cd SEL_Rdb
pip install .
```

## Dependencies

SEL_RDB requires the following Python packages:
- `olefile`: For reading and manipulating OLE2 structured storage files
- `openpyxl`: For Excel file handling (used in some conversion approaches)

These dependencies will be automatically installed when you install SEL_RDB using pip.

## Verification

To verify that the installation was successful, you can test the import:

```python
import sel_rdb
print(sel_rdb.__version__)
```

You should see the version number of the installed package.

## Troubleshooting

### Common Issues

1. **Permission errors**: If you encounter permission errors during installation, try using the `--user` flag:
   ```bash
   pip install --user SEL_Rdb
   ```

2. **Python version compatibility**: Ensure you're using Python 3.8 or higher:
   ```bash
   python --version
   ```

3. **Missing dependencies**: If you encounter import errors, try reinstalling:
   ```bash
   pip install --upgrade --force-reinstall SEL_Rdb
   ```

### Platform-specific Notes

- **Windows**: No special considerations
- **macOS**: No special considerations
- **Linux**: No special considerations

SEL_RDB is designed to be cross-platform compatible.