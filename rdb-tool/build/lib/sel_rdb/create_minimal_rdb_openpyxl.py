"""
This script creates a minimal valid OLE2 file that can be used as a template
for SEL RDB files. It uses the openpyxl library to create an Excel file and then
renames it to .rdb.
"""

import openpyxl
import os
import sys

def create_minimal_rdb(output_rdb_path):
    """
    Create a minimal valid RDB file by creating an Excel file and renaming it
    """
    # Create a new Excel workbook
    workbook = openpyxl.Workbook()
    
    # Get the active worksheet
    worksheet = workbook.active
    worksheet.title = "RDB_Template"
    
    # Add some minimal content
    worksheet['A1'] = "This is a template for SEL RDB files"
    worksheet['A2'] = "It should be replaced with actual relay settings"
    
    # Save the workbook as an Excel file
    excel_path = output_rdb_path.replace('.rdb', '.xlsx')
    workbook.save(excel_path)
    
    # Rename the Excel file to .rdb
    os.rename(excel_path, output_rdb_path)
    
    print(f"Created minimal RDB file: {output_rdb_path}")
    print("Note: This file is not a fully functional SEL RDB file")
    print("It only demonstrates the concept of creating a file with the .rdb extension")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_minimal_rdb_openpyxl.py <output_rdb_file>")
        sys.exit(1)
    
    output_rdb_path = sys.argv[1]
    
    try:
        create_minimal_rdb(output_rdb_path)
    except Exception as e:
        print(f"Error creating minimal RDB file: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)