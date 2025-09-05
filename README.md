<p align="center">
  <img width="2500" height="857" alt="SEL Schweitzer Engineering Laboratories" src="Logo.png" />
</p>

# SEL_Rdb

A Python package for analyzing and creating SEL (Schweitzer Engineering Laboratories) `.rdb` relay database files.

Developed by **AOUF Nihed**, Electrical Engineering student at **ESGEE (École Supérieure de Génie Électrique)**, during an internship with **Ateam Pro-tech** (official partner of **SEL Schweitzer Engineering Laboratories**), as part of building [SEL_Connect](https://github.com/AoufNihed/SELConnect.git).

---

## Documentation

The package provides utilities to:

- Analyze SEL .rdb files and extract their internal structure
- Extract logic sections containing protection and control logic
- Convert text-based relay settings into valid .rdb format
- Work with SEL relay configuration data programmatically

📖 [Read the full documentation](https://aoufnihed.github.io/SEL_RDB/)

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
git clone https://github.com/<your-username>/SEL_Rdb.git
cd SEL_Rdb
pip install .
```
---

## Usage

### Command-line tools
```bash
#### Analyze an RDB file
sel-rdb-analyze path/to/file.rdb

#### List streams in an RDB file
sel-rdb-list path/to/file.rdb

#### Extract logic sections
sel-rdb-extract-logic path/to/file.rdb

#### Create an RDB file from a text file
sel-rdb-create path/to/settings.txt path/to/output.rdb
```
### As a Python library
```bash
import sel_rdb

#### Analyze an RDB file
sel_rdb.analyze_rdb_file("path/to/file.rdb")

#### List streams
streams = sel_rdb.list_streams("path/to/file.rdb")

#### Extract logic
logic = sel_rdb.extract_logic_from_file("path/to/file.rdb")

#### Create an RDB file
sel_rdb.create_rdb_file("path/to/settings.txt", "path/to/output.rdb")
```
---


## Case Studies

The package includes three real-world case studies demonstrating different types of SEL relays:

1. **SEL-710 Motor Protection Relay** - Comprehensive motor protection with overcurrent, voltage, and frequency protection
2. **SEL-710-5 Advanced Motor Protection Relay** - Enhanced motor protection with additional features
3. **SEL-751A Feeder Protection Relay** - Distribution feeder protection with reclosing and breaker failure functions

These case studies are located in the `Case_Study` directory and can be converted to RDB format using the package. 
For detailed instructions, see the [Case Studies Documentation](docs/Case_Study/index.md) or try the 
[examples/case_studies_workflow.py](examples/case_studies_workflow.py) script.

## Technical Details

- SEL .rdb files use the OLE2 structured storage format.
- Streams typically store configuration, logic equations, device info, communications, and metering data.
- Implementation uses the olefile library for parsing and a template-based approach for creating valid .rdb files.

---

## Requirements
```bash
- Python 3.6+
- olefile
- openpyxl
```
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

