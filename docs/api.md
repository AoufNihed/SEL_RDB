# API Reference

This document provides detailed information about the SEL_RDB API.

## Main Package Functions

### `analyze_rdb_file(rdb_path)`

Analyze an RDB file and list its streams with content previews.

**Parameters:**
- `rdb_path` (str): Path to the RDB file to analyze

**Returns:**
- `bool`: True if successful, False otherwise

**Example:**
```python
import sel_rdb
sel_rdb.analyze_rdb_file("examples/Relay710.rdb")
```

### `list_streams(rdb_path)`

List all streams in an RDB file.

**Parameters:**
- `rdb_path` (str): Path to the RDB file

**Returns:**
- `list`: List of stream paths

**Example:**
```python
import sel_rdb
streams = sel_rdb.list_streams("examples/Relay710.rdb")
```

### `extract_logic_from_file(rdb_path)`

Extract logic sections from an RDB file.

**Parameters:**
- `rdb_path` (str): Path to the RDB file

**Returns:**
- `dict`: Dictionary with group names as keys and logic lists as values

**Example:**
```python
import sel_rdb
logic = sel_rdb.extract_logic_from_file("examples/Relay710.rdb")
```

### `create_rdb_file(input_txt_path, output_rdb_path, template_rdb_path=None)`

Convert a relay settings text file to a valid SEL .rdb file by copying a template and modifying its contents.

**Parameters:**
- `input_txt_path` (str): Path to the input text file with relay settings
- `output_rdb_path` (str): Path where the output RDB file will be created
- `template_rdb_path` (str, optional): Path to the template RDB file. If not provided, will look for Relay710.rdb in the package directory.

**Example:**
```python
import sel_rdb
sel_rdb.create_rdb_file("examples/relay710.txt", "output.rdb")
```

## Module-level Documentation

### `rdb_analyzer` Module

Contains functions for comprehensive RDB file analysis.

**Functions:**
- `analyze_rdb_file(rdb_path)`: Main function for analyzing RDB files
- `main()`: Command-line interface function

### `list_rdb_streams` Module

Contains functions for listing streams in RDB files.

**Functions:**
- `list_streams(rdb_path)`: Main function for listing streams
- `main()`: Command-line interface function

### `extract_logic_section` Module

Contains functions for extracting logic sections from RDB files.

**Functions:**
- `process_file(path, group)`: Process a specific file and group
- `extract_logic_from_file(path)`: Extract logic from all streams in an RDB file
- `main()`: Command-line interface function

### `create_rdb_template` Module

Contains functions for template-based RDB creation.

**Functions:**
- `create_rdb_file(input_txt_path, output_rdb_path, template_rdb_path=None)`: Main function for creating RDB files
- `parse_txt_content(content)`: Parse text content into sections
- `write_required_streams(ole, sections)`: Write required streams to the OLE file
- `create_cfg_content(sections)`: Create Cfg.txt content
- `write_setting_files(ole, sections, base_path)`: Write setting files
- `create_*_content(sections)`: Functions for creating content for different setting files
- `main()`: Command-line interface function

### `logic_analyzer` Module

Contains functions for analyzing logic equations.

### `sel_logic_count` Module

Contains functions for counting logic elements.

### `extract_settings` Module

Contains functions for extracting settings from RDB files.

### `utils` Module

Contains general utility functions.

**Functions:**
- `flatten(l)`: Flatten list of lists by 1
- `unique(l)`: Get unique items in a list
- `remove_empty(mylist)`: Remove empty items from a list
- `hasNumbers(inputString)`: Check if string contains numbers
- `multiple_replace(text, repldict)`: Replace multiple strings while supporting backreferences
- `build_replacer(cases)`: Build a replacer function
- `absolute_backreference(text, n)`: Handle absolute backreferences
- `multireplace(text, repldict, prefix='', suffix='')`: Perform multiple replacements

## Exception Handling

The SEL_RDB package may raise the following exceptions:

- `FileNotFoundError`: When a specified file does not exist
- `olefile.OleError`: When there are issues with OLE file processing
- `UnicodeError`: When there are encoding issues with file content
- `ValueError`: When there are issues with stream operations
- `Exception`: General exceptions for other error conditions

Always wrap calls to SEL_RDB functions in try-except blocks for production code.