<p align="center">
  <img width="2500" height="857" alt="SEL Schweitzer Engineering Laboratories" src="https://github.com/user-attachments/assets/94070905-4cbe-4ed5-8e6e-878911bbd5e2" />
</p>

# SEL_Rdb

A Python package for analyzing and creating SEL (Schweitzer Engineering Laboratories) `.rdb` relay database files.

Developed by **AOUF Nihed**, Electrical Engineering student at **ESGEE (École Supérieure de Génie Électrique)**, during an internship with **Ateam Pro-tech** (official partner of **SEL Schweitzer Engineering Laboratories**), as part of building [SEL_Connect](https://github.com/AoufNihed/SELConnect.git).

[![PyPI version](https://badge.fury.io/py/SEL-Rdb.svg)](https://badge.fury.io/py/SEL-Rdb)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## Documentation

Comprehensive documentation is available at [https://aoufnihed.github.io/SEL_Rdb/](https://aoufnihed.github.io/SEL_Rdb/).

The package provides utilities to:

- Analyze SEL .rdb files and extract their internal structure
- Extract logic sections containing protection and control logic
- Convert text-based relay settings into valid .rdb format
- Work with SEL relay configuration data programmatically

---

## Installation

### From PyPI
```bash
pip install SEL_Rdb
```
### Developer installation (editable mode)
```bash
pip install -e ".[dev]"
```
### From source
```bash
git clone https://github.com/AoufNihed/SEL_Rdb.git
cd SEL_Rdb
pip install .
```
---

## Quick Start

### Command-line tools

#### Analyze an RDB file
```bash
sel-rdb-analyze path/to/file.rdb
```
#### List streams in an RDB file
```bash
sel-rdb-list path/to/file.rdb
```
#### Extract logic sections
```bash
sel-rdb-extract-logic path/to/file.rdb
```
#### Create an RDB file from a text file
```bash
sel-rdb-create path/to/settings.txt path/to/output.rdb
```

### As a Python library

```python
import sel_rdb

# Analyze an RDB file and display its internal structure
sel_rdb.analyze_rdb_file("path/to/file.rdb")

# List streams in an RDB file
streams = sel_rdb.list_streams("path/to/file.rdb")
print(streams)

# Extract logic from an RDB file
logic = sel_rdb.extract_logic_from_file("path/to/file.rdb")
print(logic)

# Create an RDB file from a text file
sel_rdb.create_rdb_file("path/to/settings.txt", "path/to/output.rdb")
```

### Text File Format for RDB Creation

To create an RDB file from a text file, format your settings like this:

```ini
[Device]
Model=SEL-710

[Protection - Overcurrent]
50P Pickup=OFF
51P Pickup=OFF

[Protection - Voltage]
27P Undervoltage=OFF
59P Overvoltage=OFF

[Logic Settings]
SELogic Equation1=INPUT1 → OUTPUT1

[Communications]
Protocol=Modbus
Address=1
```

---

## Technical Details

- SEL .rdb files use the OLE2 structured storage format.
- Streams typically store configuration, logic equations, device info, communications, and metering data.
- Implementation uses the olefile library for parsing and a template-based approach for creating valid .rdb files.

---

## Requirements
```bash
- Python 3.8+
- olefile
- openpyxl
```
---

## Contributing

We welcome contributions! Please see our [contributing guidelines](https://aoufnihed.github.io/SEL_Rdb/contributing/) for more information.

---

## Citation

If you use this package in your research, please cite it as:

```bibtex
@misc{SEL_Rdb,
    author       = {Aouf, Nihed},
    title        = {SEL_Rdb: A Python toolkit for SEL relay .rdb database files},
    year         = {2025},
    journal      = {GitHub},
    howpublished = {\url{https://github.com/AoufNihed/SEL_Rdb}},
}

```

