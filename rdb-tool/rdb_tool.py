#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SEL RDB Tools - Main Entry Point
================================

This script provides a unified interface to work with SEL .rdb files.
It can analyze RDB files, extract logic sections, and convert text settings to RDB format.

Usage:
    python rdb_tool.py analyze <rdb_file>
    python rdb_tool.py extract-logic <rdb_file>
    python rdb_tool.py convert <txt_file> <rdb_file>
"""

import sys
import os

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    
    command = sys.argv[1]
    
    if command == "analyze":
        if len(sys.argv) != 3:
            print("Usage: python rdb_tool.py analyze <rdb_file>")
            return 1
        
        from rdb_analyzer import analyze_rdb_file
        rdb_file = sys.argv[2]
        return 0 if analyze_rdb_file(rdb_file) else 1
    
    elif command == "extract-logic":
        if len(sys.argv) != 3:
            print("Usage: python rdb_tool.py extract-logic <rdb_file>")
            return 1
        
        # Run the extract_logic_section.py script directly
        import subprocess
        try:
            result = subprocess.run([
                sys.executable, 
                os.path.join(os.path.dirname(__file__), 'src', 'extract_logic_section.py'),
                sys.argv[2]
            ], check=True, capture_output=True, text=True)
            print(result.stdout)
            return 0
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            print(f"Stderr: {e.stderr}")
            return 1
    
    elif command == "convert":
        if len(sys.argv) != 4:
            print("Usage: python rdb_tool.py convert <txt_file> <rdb_file>")
            return 1
        
        # For now, we'll just print a message as the conversion is complex
        print("Conversion functionality is not fully implemented yet.")
        print("Please use the create_rdb_template.py script in the src directory for template-based conversion.")
        return 1
    
    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        return 1

if __name__ == "__main__":
    sys.exit(main())