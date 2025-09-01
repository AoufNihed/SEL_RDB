#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
RDB File Analyzer
This script analyzes SEL .rdb files and lists their streams.
"""

import olefile
import sys
import os

def analyze_rdb_file(rdb_path):
    """
    Analyze an RDB file and list its streams
    """
    if not os.path.exists(rdb_path):
        print(f"Error: File {rdb_path} does not exist")
        return False
    
    try:
        # Open the RDB file
        ole = olefile.OleFileIO(rdb_path)
        
        # List all streams
        streams = ole.listdir()
        print(f"Streams/groups in {rdb_path}:")
        for stream in streams:
            print("/".join(stream))
            
            # Try to read the stream content
            try:
                stream_path = "/".join(stream)
                stream_data = ole.openstream(stream_path).read()
                print(f"  Size: {len(stream_data)} bytes")
                
                # Try to decode as text
                try:
                    text_content = stream_data.decode('utf-8')
                    # Show first few lines
                    lines = text_content.split('\n')
                    print(f"  Content (first 3 lines):")
                    for i, line in enumerate(lines[:3]):
                        if line.strip():
                            print(f"    {line}")
                    if len(lines) > 3:
                        print("    ...")
                except UnicodeDecodeError:
                    print("  Content: Binary data")
            except Exception as e:
                print(f"  Error reading stream: {e}")
            print()
            
        # Close the file
        ole.close()
        return True
        
    except Exception as e:
        print(f"Error analyzing RDB file: {e}")
        return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python rdb_analyzer.py <rdb_file>")
        print("Example: python rdb_analyzer.py Relay710.rdb")
        sys.exit(1)
    
    rdb_path = sys.argv[1]
    success = analyze_rdb_file(rdb_path)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()