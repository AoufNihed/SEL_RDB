# Usage Examples

This section provides detailed examples of how to use SEL_RDB in various scenarios.

## Command-line Examples

### Analyzing RDB Files

To analyze an RDB file and see its internal structure:

```bash
sel-rdb-analyze examples/Relay710.rdb
```

This will display all streams in the file along with their content previews.

### Listing Streams

To get just a list of streams without content details:

```bash
sel-rdb-list examples/Relay710.rdb
```

### Extracting Logic Sections

To extract all logic equations from an RDB file:

```bash
sel-rdb-extract-logic examples/Relay710.rdb
```

This creates an `output.txt` file with all extracted logic equations.

### Creating RDB Files

To create an RDB file from a text configuration:

```bash
sel-rdb-create examples/relay710.txt output.rdb
```

## Python Library Examples

### Basic Analysis

```python
import sel_rdb

# Analyze an RDB file
sel_rdb.analyze_rdb_file("examples/Relay710.rdb")

# List streams only
streams = sel_rdb.list_streams("examples/Relay710.rdb")
for stream in streams:
    print(stream)
```

### Logic Extraction

```python
import sel_rdb

# Extract logic from an RDB file
logic_data = sel_rdb.extract_logic_from_file("examples/Relay710.rdb")

# Process the extracted logic
for group, equations in logic_data.items():
    print(f"Group: {group}")
    for equation in equations:
        print(f"  {equation}")
```

### Creating RDB Files

```python
import sel_rdb

# Create an RDB file from a text configuration
sel_rdb.create_rdb_file("examples/relay710.txt", "output.rdb")

# Create with a custom template
sel_rdb.create_rdb_file(
    "examples/relay710.txt", 
    "output.rdb", 
    template_rdb_path="custom_template.rdb"
)
```

## Working with Text Configuration Files

The text configuration file format follows this structure:

```ini
[Device]
Model=SEL-710-5
Serial=7105-654321

[Protection - Overcurrent]
50P Pickup=120
50P Delay=0.5
51P Pickup=100
51P Time Dial=2.0

[Protection - Voltage]
27P Undervoltage=0.8
59P Overvoltage=1.2

[Logic Settings]
SELogic Equation1=50P AND 51P → TRIP
SELogic Equation2=27P OR 59P → ALARM

[Communications]
Protocol=Modbus
Address=1
Baud=9600
```

## Advanced Usage

### Custom Stream Processing

```python
import olefile
import sel_rdb

# Open an RDB file directly for custom processing
ole = olefile.OleFileIO("examples/Relay710.rdb")

# List all streams
streams = ole.listdir()
for stream in streams:
    print("/".join(stream))

# Read a specific stream
stream_data = ole.openstream("Relays/New Settings 2/set_1.txt").read()
text_content = stream_data.decode('utf-8')
print(text_content)

# Close the file
ole.close()
```

### Batch Processing

```python
import os
import sel_rdb

# Process all RDB files in a directory
rdb_files = [f for f in os.listdir("rdb_files") if f.endswith(".rdb")]

for rdb_file in rdb_files:
    file_path = os.path.join("rdb_files", rdb_file)
    
    # List streams
    streams = sel_rdb.list_streams(file_path)
    
    # Save stream list to a file
    with open(f"{rdb_file}_streams.txt", "w") as f:
        for stream in streams:
            f.write(f"{stream}\n")
```

## Error Handling

```python
import sel_rdb

try:
    # Attempt to analyze a file
    sel_rdb.analyze_rdb_file("nonexistent.rdb")
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(f"An error occurred: {e}")
```

These examples demonstrate the core functionality of SEL_RDB and show how to integrate it into your workflows for working with SEL relay configuration files.