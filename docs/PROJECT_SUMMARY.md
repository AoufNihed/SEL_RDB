# SEL RDB Tools - Project Summary

## Project Overview

This project provides a comprehensive toolkit for working with SEL (Schweitzer Engineering Laboratories) .rdb relay database files. The tools enable users to analyze, extract, and manipulate relay configuration data stored in the proprietary OLE2 structured storage format used by SEL QuickSet software.

## Key Achievements

### 1. RDB File Analysis
- Successfully analyzed the structure of SEL .rdb files
- Identified all streams and their content within RDB files
- Created tools to list and examine RDB file contents

### 2. Logic Extraction
- Developed functionality to extract logic sections from RDB files
- Created tools to analyze SELogic equations and other logic elements
- Implemented extraction of protection and automation logic

### 3. File Conversion
- Explored multiple approaches to convert text-based relay settings to .rdb format
- Implemented template-based approach for creating RDB files
- Documented limitations and challenges in RDB file creation

### 4. Project Organization
- Created a well-structured project with clear directories:
  - `src/` - Source code for all tools
  - `docs/` - Documentation and requirements
  - `examples/` - Sample files and test data
  - `tests/` - Test files (prepared for future use)
- Developed a unified command-line interface

## Tools Included

### Analysis Tools
- `rdb_analyzer.py` - Comprehensive RDB file analysis
- `list_rdb_streams.py` - Stream listing utility
- `extract_settings.py` - Settings extraction tool

### Logic Tools
- `extract_logic_section.py` - Logic section extraction
- `logic_analyzer.py` - Logic equation analysis
- `sel_logic_count.py` - Logic element counting
- `logic_changer.py` - Logic modification utilities

### Conversion Tools
- `create_rdb_template.py` - Template-based RDB creation
- `convert_txt_to_rdb.py` - Text to RDB conversion (experimental)
- `create_rdb_com.py` - COM-based RDB creation (experimental)

## Technical Approach

### File Format Understanding
The project successfully reverse-engineered key aspects of the SEL RDB format:
- OLE2 structured storage container format
- Stream organization with "Relays/New Settings 2/" hierarchy
- Content format with sections identified by [INFO] and group identifiers
- Logic equations stored in SVxx fields with specific syntax

### Implementation Strategies
1. **Template-based approach** - Most successful for creating RDB files
2. **COM objects** - Attempted but faced technical challenges
3. **Direct file manipulation** - Used olefile library with limitations

## Challenges and Limitations

### Technical Challenges
1. **OLE2 Complexity** - Creating valid structured storage files from scratch is complex
2. **Stream Size Constraints** - The olefile library cannot modify stream sizes easily
3. **Format Specificity** - SEL RDB format has specific requirements not fully documented

### Current Limitations
1. **Full Conversion Not Complete** - Text to RDB conversion is not fully implemented
2. **Platform Dependencies** - Some approaches require Windows-specific libraries
3. **Size Constraints** - Template-based approach requires careful stream size management

## Usage Examples

### Analyze an RDB file
```bash
python rdb_tool.py analyze examples/Relay710.rdb
```

### Extract logic sections
```bash
python rdb_tool.py extract-logic examples/Relay710.rdb
```

### Create RDB from template
```bash
python src/create_rdb_template.py examples/relay710.txt output.rdb
```

## Future Enhancements

### Technical Improvements
1. **Complete Conversion Tool** - Fully implement text to RDB conversion
2. **Cross-platform Support** - Reduce Windows-specific dependencies
3. **Enhanced Error Handling** - Improve robustness and error reporting

### Feature Additions
1. **Logic Modification** - Tools to modify existing logic equations
2. **Validation Tools** - Verify RDB file integrity and correctness
3. **Batch Processing** - Process multiple files at once

## Conclusion

This project successfully created a comprehensive toolkit for working with SEL RDB files, providing valuable functionality for analyzing and extracting relay configuration data. While full conversion from text settings to RDB format remains challenging due to the complexity of the OLE2 structured storage format, the template-based approach provides a viable solution for many use cases.

The organized project structure and well-documented code provide a solid foundation for future enhancements and maintenance. The tools have been tested with real SEL RDB files and proven to work correctly for their intended purposes.