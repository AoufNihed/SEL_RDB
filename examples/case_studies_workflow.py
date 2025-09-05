#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SEL_RDB Case Studies Workflow Example
=====================================

This script demonstrates the complete workflow for working with the SEL_RDB 
case studies:

1. Convert text files to RDB format
2. Analyze the RDB files
3. Extract logic sections
4. Export reports

Usage:
    python case_studies_workflow.py
"""

import os
import sys


# Add the project root to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# Now we can import sel_rdb
import sel_rdb

def main():
    # Define case study files
    case_studies = [
        ("Case_Study/SEL-710 Motor.txt", "output/SEL-710_Motor.rdb"),
        ("Case_Study/SEL-710-5.txt", "output/SEL-710-5.rdb"),
        ("Case_Study/SEL-751A Relay.txt", "output/SEL-751A.rdb")
    ]
    
    print("SEL_RDB Case Studies Workflow Example")
    print("=" * 40)
    
    # Process each case study
    for txt_file, rdb_file in case_studies:
        if os.path.exists(txt_file):
            print(f"\nProcessing {txt_file}...")
            
            # Step 1: Convert .txt to .rdb
            print("  1. Converting to RDB format...")
            try:
                sel_rdb.create_rdb_file(txt_file, rdb_file)
                print(f"     [OK] Successfully created {rdb_file}")
            except Exception as e:
                print(f"     [ERROR] Failed to create {rdb_file}: {e}")
                continue
            
            # Step 2: Analyze the RDB file
            print("  2. Analyzing RDB file...")
            try:
                # Redirect output to a file
                with open(f"reports/{os.path.basename(rdb_file)}_analysis.txt", "w") as f:
                    import sys
                    original_stdout = sys.stdout
                    sys.stdout = f
                    
                    sel_rdb.analyze_rdb_file(rdb_file)
                    
                    sys.stdout = original_stdout
                
                print(f"     [OK] Analysis saved to reports/{os.path.basename(rdb_file)}_analysis.txt")
            except Exception as e:
                print(f"     [ERROR] Failed to analyze {rdb_file}: {e}")
            
            # Step 3: Extract logic
            print("  3. Extracting logic sections...")
            try:
                logic = sel_rdb.extract_logic_from_file(rdb_file)
                
                # Save logic to file
                with open(f"reports/{os.path.basename(rdb_file)}_logic.txt", "w") as f:
                    f.write(f"Logic sections extracted from {rdb_file}:\n")
                    f.write("=" * 50 + "\n")
                    if logic:
                        f.write(logic)
                    else:
                        f.write("No logic sections found.")
                
                print(f"     [OK] Logic extraction saved to reports/{os.path.basename(rdb_file)}_logic.txt")
            except Exception as e:
                print(f"     [ERROR] Failed to extract logic from {rdb_file}: {e}")
        else:
            print(f"\nSkipping {txt_file} (file not found)")
    
    print("\nWorkflow completed!")
    print("Check the 'output' directory for RDB files and 'reports' directory for analysis results.")

if __name__ == "__main__":
    main()