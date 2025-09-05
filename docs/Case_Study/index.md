# SEL_RDB Case Studies

This documentation provides step-by-step instructions on how to use the SEL_RDB package with the provided case studies. The package allows you to convert text-based relay settings (.txt) into SEL .rdb files, analyze them, and run various analytics.

## Case Studies Included

### 1. SEL-710 Motor Protection Relay
**File:** `SEL-710 Motor.txt`
A comprehensive motor protection relay configuration with overcurrent, voltage, frequency, and motor-specific protection settings.

### 2. SEL-710-5 Advanced Motor Protection Relay
**File:** `SEL-710-5.txt`
An advanced motor protection relay with additional features including negative sequence overload protection and enhanced communication settings.

### 3. SEL-751A Feeder Protection Relay
**File:** `SEL-751A Relay.txt`
A feeder protection relay with reclosing, breaker failure, and sectionalizer functions for distribution feeder protection.

## Workflow

The workflow for using the SEL_RDB package with case studies includes three main steps:

1. **Convert .txt to .rdb** - Use the SEL_RDB package to convert text-based relay settings into a valid .rdb file format.
2. **Analyze the .rdb File** - Run various analytics on the .rdb file to extract streams, logic sections, and other configuration data.
3. **Export Reports** - Export the analysis results to various formats for documentation and sharing.

## Example Usage Code

### Converting a .txt Case Study to .rdb

Command-line approach:
```bash
sel-rdb-create "Case_Study/SEL-710 Motor.txt" "output/SEL-710_Motor.rdb"
```

Python library approach:
```python
import sel_rdb
sel_rdb.create_rdb_file("Case_Study/SEL-710 Motor.txt", "output/SEL-710_Motor.rdb")
```

### Running Analytics on .rdb Files

Command-line approach:
```bash
sel-rdb-analyze "output/SEL-710_Motor.rdb"
sel-rdb-list "output/SEL-710_Motor.rdb"
sel-rdb-extract-logic "output/SEL-710_Motor.rdb"
```

Python library approach:
```python
import sel_rdb

# Analyze the RDB file structure
sel_rdb.analyze_rdb_file("output/SEL-710_Motor.rdb")

# List all streams in the RDB file
streams = sel_rdb.list_streams("output/SEL-710_Motor.rdb")
print("Streams in RDB file:", streams)

# Extract logic sections
logic = sel_rdb.extract_logic_from_file("output/SEL-710_Motor.rdb")
print("Logic sections:", logic)
```

### Exporting Reports

```python
# Save analysis results to a text file
import sel_rdb

with open("reports/SEL-710_Motor_analysis.txt", "w") as f:
    # Redirect print output to file
    import sys
    original_stdout = sys.stdout
    sys.stdout = f
    
    sel_rdb.analyze_rdb_file("output/SEL-710_Motor.rdb")
    
    # Reset stdout
    sys.stdout = original_stdout

print("Analysis report saved to reports/SEL-710_Motor_analysis.txt")
```

## Available Case Studies

- `case1_sel710.txt` - SEL-710 Motor Protection Relay
- `case2_sel710-5.txt` - SEL-710-5 Advanced Motor Protection Relay
- `case3_sel751a.txt` - SEL-751A Feeder Protection Relay

## Next Steps

Try running the workflow on all three case studies to familiarize yourself with the SEL_RDB package capabilities:

1. Convert each .txt file to .rdb format
2. Analyze the generated .rdb files
3. Extract logic sections from each file
4. Compare the different relay configurations
5. Export reports for documentation

---

Developed by AOUF Nihed

Contact:
- Email: [aouf_nihed@esgee-oran.dz](mailto:aouf_nihed@esgee-oran.dz)
- LinkedIn: [https://www.linkedin.com/in/nihed-aouf/](https://www.linkedin.com/in/nihed-aouf/)
- GitHub: [https://github.com/AoufNihed](https://github.com/AoufNihed)