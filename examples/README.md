# SEL_RDB Case Studies Examples

This directory contains examples demonstrating how to use the SEL_RDB package with the provided case studies.

## Files

- `case_studies_workflow.py` - A complete workflow example that processes all three case studies
- `relay710.txt` - An example text file showing the required format for RDB creation
- `relay710_template.rdb` - A template RDB file used for creating new RDB files
- `Relay710.rdb` - Another template RDB file

## Case Studies Workflow

The `case_studies_workflow.py` script demonstrates the complete workflow:

1. **Convert** text files to RDB format
2. **Analyze** the RDB files
3. **Extract** logic sections
4. **Export** reports

To run the workflow:

```bash
python examples/case_studies_workflow.py
```

This will:
- Convert all three case study text files to RDB format (saved in the `output` directory)
- Analyze each RDB file (reports saved in the `reports` directory)
- Extract logic sections from each RDB file (saved in the `reports` directory)

## Case Study Files

The case study files are located in the `Case_Study` directory:

1. `SEL-710 Motor.txt` - Configuration for a motor protection relay
2. `SEL-710-5.txt` - Configuration for an advanced motor protection relay
3. `SEL-751A Relay.txt` - Configuration for a feeder protection relay

## Text File Format

To create valid RDB files, the text files must follow a specific format with sections and key-value pairs:

```ini
[Device]
Model=SEL-710

[Protection - Overcurrent]
50P Pickup=OFF
51P Pickup=OFF

[Logic Settings]
SELogic Equation1=INPUT1 → OUTPUT1
```

For complete documentation on the case studies and how to use them, see:
- [Case Studies Documentation](../docs/Case_Study/index.md)
- [Quickstart Guide](../docs/quickstart.md)