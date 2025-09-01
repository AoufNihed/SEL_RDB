# SEL_RDB

<img width="2500" height="857" alt="image" src="https://github.com/user-attachments/assets/94070905-4cbe-4ed5-8e6e-878911bbd5e2" />

A comprehensive toolkit for working with SEL (Schweitzer Engineering Laboratories) .rdb relay database files.

Developed by **AOUF Nihed**, an Electrical Engineering student at **ESGEE (École Supérieure de Génie Électrique)**, as part of a project in collaboration with **Ateam Pro-tech**, an official partner of **SEL Schweitzer Engineering Laboratories**.

## Table of Contents

- [Project Overview](#project-overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
  - [As a command-line tool](#as-a-command-line-tool)
  - [Creating an RDB file from a text file](#creating-an-rdb-file-from-a-text-file)
  - [As a Python library](#as-a-python-library)
- [Technical Details](#technical-details)
- [Requirements](#requirements)
- [License](#license)

## Project Overview

The SEL_Rdb toolkit is a specialized Python package designed to work with SEL (Schweitzer Engineering Laboratories) .rdb relay database files. These files contain configuration data for SEL protective relays, which are widely used in power system protection applications.

This toolkit provides utilities to:
- Analyze SEL .rdb files and extract their internal structure
- Extract logic sections containing protection and control logic
- Convert text-based relay settings to valid .rdb format
- Work with SEL relay configuration data programmatically

## Project Structure

```
sel_rdb/
├── __init__.py                 # Package initialization and main exports
├── rdb_analyzer.py             # Comprehensive RDB file analysis tool
├── list_rdb_streams.py         # List streams in RDB files
├── extract_logic_section.py    # Extract logic sections from RDB files
├── create_rdb_template.py      # Template-based RDB creation
├── logic_analyzer.py           # Analyze logic equations
├── sel_logic_count.py          # Count logic elements
├── extract_settings.py         # Extract settings from RDB files
├── convert_txt_to_rdb.py       # Convert text files to RDB format
├── utils.py                    # General utility functions
├── Relay710.rdb                # Template RDB file
```

## Installation

```bash
pip install SEL_Rdb
```

## Features

- **RDB Analysis**: Analyze SEL .rdb files and extract their contents including streams and internal structure
- **Logic Extraction**: Extract logic sections from RDB files containing protection and control equations
- **Format Conversion**: Convert text-based relay settings to valid .rdb format using template-based approach
- **Stream Listing**: List all streams within an RDB file to understand its internal structure
- **Programmatic Access**: Use as a Python library for integration with other applications
- **Command-line Tools**: Standalone CLI tools for common operations

## Usage

### As a command-line tool:

```bash
# Analyze an RDB file and display its internal structure
sel-rdb-analyze path/to/file.rdb

# List streams in an RDB file
sel-rdb-list path/to/file.rdb

# Extract logic sections from an RDB file
sel-rdb-extract-logic path/to/file.rdb

# Create an RDB file from a text file
sel-rdb-create path/to/settings.txt path/to/output.rdb
```

### Creating an RDB file from a text file

To create an RDB file from a text file, you can use the `sel-rdb-create` command:

```bash
sel-rdb-create path/to/settings.txt path/to/output.rdb
```

The input text file should follow a specific format with sections and key-value pairs:

```ini
[Device]
Model=SEL-710

[Protection - Overcurrent]
50P Pickup=OFF
50P Delay=0.00
51P Pickup=OFF
51P Time Dial=3.00

[Protection - Voltage]
27P Undervoltage=OFF
59P Overvoltage=OFF

[Protection - Frequency]
81U Underfrequency=OFF
81O Overfrequency=OFF

[Motor Protection]
Jam Detection=OFF
Locked Rotor=OFF

[Alarms and Events]
Trip Message=Motor Trip Detected

[Logic Settings]
SELogic Equation1=INPUT1 → OUTPUT1

[Communications]
Protocol=Modbus
Address=1

[Metering]
Demand Interval=15
Energy Format=kWh

[Testing]
TestMode=Disabled
```

### As a Python library:

```python
import sel_rdb

# Analyze an RDB file and display its internal structure
sel_rdb.analyze_rdb_file("path/to/file.rdb")

# List streams in an RDB file
streams = sel_rdb.list_streams("path/to/file.rdb")

# Extract logic from an RDB file
logic = sel_rdb.extract_logic_from_file("path/to/file.rdb")

# Create an RDB file from a text file
sel_rdb.create_rdb_file("path/to/settings.txt", "path/to/output.rdb")
```

## Technical Details

### RDB File Format

SEL .rdb files use the OLE2 (Object Linking and Embedding) structured storage format, which organizes data in a hierarchical structure similar to a filesystem. The files contain multiple streams, each storing different types of configuration data:

- **Configuration Settings**: Protection settings, pickup values, time delays
- **Logic Equations**: SELogic equations defining protection and control logic
- **Device Information**: Model numbers, serial numbers, firmware versions
- **Communication Settings**: Protocol configurations, addresses
- **Metering Data**: Energy calculations, demand intervals

### Implementation Approach

The toolkit uses the `olefile` library to read and manipulate the OLE2 structured storage format. For creating new RDB files, it employs a template-based approach:

1. **Template Copying**: Copy a valid RDB template file
2. **Stream Modification**: Modify specific streams with new configuration data
3. **Validation**: Ensure the resulting file maintains proper structure

This approach is more reliable than creating OLE2 files from scratch, which is complex and error-prone.

### Logic Extraction

The logic extraction functionality identifies and parses SELogic equations from the RDB files. These equations use a specific syntax:
- `SV` variables for status variables
- `MV` variables for metering variables
- `LT` variables for logic timers
- `CN` variables for counters

### Stream Structure

RDB files typically contain streams organized in paths like:
- `Relays/New Settings 2/set_g1.txt`
- `Relays/New Settings 2/Misc/Cfg.txt`
- `Relays/New Settings 2/Misc/DatabaseVersion.txt`

Each stream contains specific types of configuration data in text format.

## Requirements

- Python 3.6+
- olefile
- openpyxl

## License

This project is licensed under the MIT License."SEL_RDB"  
