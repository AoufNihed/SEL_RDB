# SEL RDB Tools - Project Structure

## Directory Structure

```
rdb-tool/
├── docs/
│   ├── images/
│   │   └── README.md (logo placeholder)
│   ├── PROJECT_SUMMARY.md
│   ├── RDB_Creation_Summary.md
│   ├── README.md
│   └── requirements.txt
├── examples/
│   ├── output.txt
│   ├── relay710_template.rdb
│   ├── Relay710.rdb
│   ├── relay710.txt
│   └── test_template.rdb
├── src/
│   ├── convert_txt_to_rdb.py
│   ├── create_minimal_rdb_openpyxl.py
│   ├── create_minimal_rdb.py
│   ├── create_placeholder_rdb.py
│   ├── create_rdb_com.py
│   ├── create_rdb_template.py
│   ├── extract_logic_section.py
│   ├── extract_settings.py
│   ├── interval_utils.py
│   ├── list_rdb_streams.py
│   ├── logic_analyzer.py
│   ├── logic_changer.py
│   ├── logic_manipulator_functions.py
│   ├── rdb_analyzer.py
│   ├── sel_logic_count.py
│   ├── utils.py
│   └── Relay710.rdb
├── tests/
│   └── test_suite.py
├── rdb_tool.py
└── README.md
```

## File Descriptions

### Root Directory
- `rdb_tool.py` - Main entry point for all tools
- `README.md` - Project overview and usage instructions

### docs/
- `images/` - Directory for logo and other images
- `PROJECT_SUMMARY.md` - Comprehensive project summary
- `RDB_Creation_Summary.md` - Detailed analysis of RDB creation approaches
- `README.md` - Documentation overview
- `requirements.txt` - Python dependencies

### examples/
- `output.txt` - Sample output from logic extraction
- `relay710_template.rdb` - Template-based RDB file
- `Relay710.rdb` - Original sample RDB file
- `relay710.txt` - Sample relay settings in text format
- `test_template.rdb` - Test RDB file created by template approach

### src/
- `convert_txt_to_rdb.py` - Experimental text to RDB conversion
- `create_minimal_rdb_openpyxl.py` - Create minimal RDB using openpyxl
- `create_minimal_rdb.py` - Create minimal RDB using xlwt
- `create_placeholder_rdb.py` - Create placeholder RDB file
- `create_rdb_com.py` - COM-based RDB creation (experimental)
- `create_rdb_template.py` - Template-based RDB creation
- `extract_logic_section.py` - Extract logic sections from RDB files
- `extract_settings.py` - Extract settings from RDB files
- `interval_utils.py` - Time interval utilities
- `list_rdb_streams.py` - List streams in RDB files
- `logic_analyzer.py` - Analyze logic equations
- `logic_changer.py` - Modify logic in RDB files
- `logic_manipulator_functions.py` - Logic manipulation functions
- `rdb_analyzer.py` - Comprehensive RDB file analysis
- `sel_logic_count.py` - Count logic elements
- `utils.py` - General utility functions
- `Relay710.rdb` - Template RDB file for conversion tools

### tests/
- `test_suite.py` - Automated test suite for all tools

## Usage

### Main Interface
```bash
python rdb_tool.py analyze <rdb_file>
python rdb_tool.py extract-logic <rdb_file>
python rdb_tool.py convert <txt_file> <rdb_file>
```

### Individual Tools
All tools in the `src/` directory can be run directly:
```bash
python src/list_rdb_streams.py <rdb_file>
python src/rdb_analyzer.py <rdb_file>
python src/extract_logic_section.py <rdb_file>
python src/create_rdb_template.py <txt_file> <rdb_file>
```

## Test Suite
Run all tests to verify functionality:
```bash
python tests/test_suite.py
```