# SEL_RDB Case Studies

This directory contains three real-world case studies for SEL relays that demonstrate the capabilities of the SEL_RDB package:

1. **SEL-710 Motor.txt** - Configuration for a motor protection relay
2. **SEL-710-5.txt** - Configuration for an advanced motor protection relay
3. **SEL-751A Relay.txt** - Configuration for a feeder protection relay

## Usage

These case studies can be converted to .rdb format using the SEL_RDB package:

```bash
# Using the command-line tool
sel-rdb-create "Case_Study/SEL-710 Motor.txt" "output/SEL-710_Motor.rdb"

# Using the Python library
import sel_rdb
sel_rdb.create_rdb_file("Case_Study/SEL-710 Motor.txt", "output/SEL-710_Motor.rdb")
```

For detailed instructions on how to use these case studies, please refer to the [documentation](../docs/Case_Study/index.md).

## Documentation

For complete documentation on using these case studies with the SEL_RDB package, see:
- [Case Studies Documentation](../docs/Case_Study/index.md)
- [Quickstart Guide](../docs/quickstart.md)
- [Usage Examples](../docs/usage.md)