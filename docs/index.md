# SEL_RDB Documentation

Welcome to the technical documentation for SEL_RDB, a Python package for analyzing and creating SEL (Schweitzer Engineering Laboratories) `.rdb` relay database files.

## Table of Contents

- [Introduction](#introduction)
- [Installation](installation.md)
- [Quickstart](quickstart.md)
- [Usage Examples](usage.md)
- [API Reference](api.md)
- [Contributing](contributing.md)
- [License](license.md)

## Introduction

SEL_RDB is a specialized Python toolkit designed to work with SEL (Schweitzer Engineering Laboratories) .rdb relay database files. These files contain configuration data for SEL protective relays, which are widely used in power system protection applications.

This toolkit provides utilities to:
- Analyze SEL .rdb files and extract their internal structure
- Extract logic sections containing protection and control logic
- Convert text-based relay settings to valid .rdb format
- Work with SEL relay configuration data programmatically

### Key Features

- **RDB Analysis**: Analyze SEL .rdb files and extract their contents including streams and internal structure
- **Logic Extraction**: Extract logic sections from RDB files containing protection and control equations
- **Format Conversion**: Convert text-based relay settings to valid .rdb format using template-based approach
- **Stream Listing**: List all streams within an RDB file to understand its internal structure
- **Programmatic Access**: Use as a Python library for integration with other applications
- **Command-line Tools**: Standalone CLI tools for common operations

### Technical Approach

The toolkit uses the `olefile` library to read and manipulate the OLE2 structured storage format used by SEL .rdb files. For creating new RDB files, it employs a template-based approach:

1. **Template Copying**: Copy a valid RDB template file
2. **Stream Modification**: Modify specific streams with new configuration data
3. **Validation**: Ensure the resulting file maintains proper structure

This approach is more reliable than creating OLE2 files from scratch, which is complex and error-prone.