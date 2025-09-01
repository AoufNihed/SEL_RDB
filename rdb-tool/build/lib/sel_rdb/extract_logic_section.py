#!/usr/bin/env python3

"""
This tool extracts a pile of settings based on the hierachy of Quickset
"""

import collections
import os
import re

import olefile

# Fix the relative import
try:
    from . import sel_logic_count
except (ImportError, ValueError):
    import sel_logic_count

LINE_INFO = ['Lines Used (w/ comment lines)', 'Lines Used (w/o comment lines)']

LOGIC_INFO = [ 'PSV', 'PMV', 'PLT', 'PCT', 'PST', 'PCN',
                'ASV', 'AMV', 'ALT',        'AST', 'ACN']

TOTAL_SEL_PROTECTION_LINES = 250
TOTAL_SEL_AUTOMATION_LINES = 1000



# this probably needs to be expanded
SEL_FILES_TO_GROUP = {
    'G': ['SET_G1'],
    'G1': ['SET_S1.TXT', 'SET_L1.TXT', 'SET_1.TXT'], # Groups
    'G2': ['SET_S2.TXT', 'SET_L2.TXT', 'SET_2.TXT'],
    'G3': ['SET_S3.TXT', 'SET_L3.TXT', 'SET_3.TXT'],
    'G4': ['SET_S4.TXT', 'SET_L4.TXT', 'SET_4.TXT'],
    'G5': ['SET_S5.TXT', 'SET_L5.TXT', 'SET_5.TXT'],
    'G6': ['SET_S6.TXT', 'SET_L6.TXT', 'SET_6.TXT'],

    'P1': ['SET_P1.TXT'], # Ports
    'P2': ['SET_P2.TXT'],
    'P3': ['SET_P3.TXT'],
    'P5': ['SET_P5.TXT'],
    'PF': ['SET_PF.TXT'], # Front Port
    'P87': ['SET_P87.TXT'], # Differential Port Settings

    'A1': ['SET_A1.TXT'], # Automation
    'A2': ['SET_A2.TXT'],
    'A3': ['SET_A3.TXT'],
    'A4': ['SET_A4.TXT'],
    'A5': ['SET_A5.TXT'],
    'A6': ['SET_A6.TXT'],
    'A7': ['SET_A7.TXT'],
    'A8': ['SET_A8.TXT'],
    'A9': ['SET_A9.TXT'],
    'A10': ['SET_A10.TXT'],
    'A11': ['SET_A11.TXT'],
    'A12': ['SET_A12.TXT'],
    'A13': ['SET_A13.TXT'],
    'A14': ['SET_A14.TXT'],
    'A15': ['SET_A15.TXT'],

    'R': ['SET_R1.TXT', 'SET_R.TXT'], # Report

    'M': ['SET_M.TXT'], # Metering
    'T': ['SET_T.TXT'], # Time
    'C': ['SET_C.TXT'], # Communications
    'F': ['SET_F.TXT'], # Front Panel/RTU
}

def process_file(path, group):
    try:
        ole = olefile.OleFileIO(path)
    except:
        print("File {} could not be opened".format(path))
        return

    streams = ole.listdir()

    stream_name = 'Relays/New Settings 2/set_{}.txt'.format(group)

    try:
        stream = ole.openstream(stream_name)
    except:
        #print("Stream {} not found in file {}".format(stream_name, path))
        return

    data = stream.read()

    try:
        text = data.decode('utf-8')
    except UnicodeError:
        text = data.decode('latin1')

    # find all the logic lines
    logic = []
    p = re.compile('SV[0-9]+,.*')
    for line in text.splitlines():
        m = p.match(line)
        if m:
            logic.append(m.group(0))

    #print(logic)
    return logic

def extract_logic_from_file(path):
    """
    Extract logic from all streams in an RDB file.
    
    Args:
        path (str): Path to the RDB file
        
    Returns:
        dict: Dictionary with group names as keys and logic lists as values
    """
    print("Extracting logic from all streams in {}...".format(path))
    
    groups = {}
    
    protection = ['G1', 'G2', 'G3']
    automation = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10']
    
    for group in protection + automation:
        logic = process_file(path, group)
        if logic:
            groups[group] = logic
    
    return groups

def main():
    """Main function for command line usage."""
    import sys
    
    if len(sys.argv) != 2:
        print("Usage: python extract_logic_section.py <rdb_file>")
        sys.exit(1)
    
    path = sys.argv[1]
    
    # Extract logic from file
    groups = extract_logic_from_file(path)
    
    # Write to output file
    with open('output.txt', 'w') as f:
        for group, logic in groups.items():
            f.write("Group: {}\n".format(group))
            for line in logic:
                f.write("{}\n".format(line))
            f.write("\n")
    
    print("Extraction complete. Results saved to output.txt.")

if __name__ == "__main__":
    main()