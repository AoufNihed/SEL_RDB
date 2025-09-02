# Quickstart Guide

This guide will help you get started with SEL_RDB quickly.

## Command-line Usage

### Analyze an RDB file

To analyze an RDB file and display its internal structure:

```bash
sel-rdb-analyze path/to/file.rdb
```

### List streams in an RDB file

To list all streams within an RDB file:

```bash
sel-rdb-list path/to/file.rdb
```

### Extract logic sections

To extract logic sections from an RDB file:

```bash
sel-rdb-extract-logic path/to/file.rdb
```

### Create an RDB file from a text file

To create an RDB file from a text file:

```bash
sel-rdb-create path/to/settings.txt path/to/output.rdb
```

## Python Library Usage

### Basic import and analysis

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

## Text File Format for RDB Creation

To create an RDB file from a text file, you need to format your settings in a specific way:

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

## Example Output

When you analyze an RDB file, you'll see output like:

```
Streams/groups in examples/Relay710.rdb:
Relays/New Settings 2/Misc/Cfg.txt
  Size: 1024 bytes
  Content (first 3 lines):
    [INFO]
    RELAYTYPE=SEL-710
    FID=SEL-710-Rxxx-Vx-Z008004-Dxxxxxxxx
...

Relays/New Settings 2/set_1.txt
  Size: 2048 bytes
  Content (first 3 lines):
    [INFO]
    RELAYTYPE=SEL-710
    [1]
...
```

This gives you a comprehensive view of the internal structure of the RDB file.