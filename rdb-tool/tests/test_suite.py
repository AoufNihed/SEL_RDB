#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test Script for SEL RDB Tools
============================

This script runs a series of tests to verify that all the tools in the SEL RDB Tools
project are working correctly.
"""

import os
import sys
import subprocess

def run_test(command, description):
    """Run a test command and report the result."""
    print(f"Testing: {description}")
    try:
        result = subprocess.run(
            command, 
            check=True, 
            capture_output=True, 
            text=True,
            shell=True
        )
        print("  Result: PASSED")
        if result.stdout.strip():
            print(f"  Output: {result.stdout.strip()[:100]}{'...' if len(result.stdout.strip()) > 100 else ''}")
        return True
    except subprocess.CalledProcessError as e:
        print("  Result: FAILED")
        print(f"  Error: {e}")
        if e.stderr.strip():
            print(f"  Stderr: {e.stderr.strip()[:100]}{'...' if len(e.stderr.strip()) > 100 else ''}")
        return False

def main():
    """Run all tests."""
    print("SEL RDB Tools - Test Suite")
    print("=" * 50)
    
    # Test 1: List RDB streams
    test1 = run_test(
        "python rdb-tool/src/list_rdb_streams.py rdb-tool/examples/Relay710.rdb",
        "List RDB streams"
    )
    
    # Test 2: Analyze RDB file
    test2 = run_test(
        "python rdb-tool/rdb_tool.py analyze rdb-tool/examples/Relay710.rdb",
        "Analyze RDB file"
    )
    
    # Test 3: Extract logic
    test3 = run_test(
        "python rdb-tool/rdb_tool.py extract-logic rdb-tool/examples/Relay710.rdb",
        "Extract logic sections"
    )
    
    # Test 4: Check if output file was created
    test4 = os.path.exists("rdb-tool/examples/output.txt")
    print(f"Testing: Output file creation")
    if test4:
        print("  Result: PASSED")
        # Check file size
        size = os.path.getsize("rdb-tool/examples/output.txt")
        print(f"  Output: File size {size} bytes")
    else:
        print("  Result: FAILED")
        print("  Error: output.txt not found")
    
    # Test 5: Create template RDB
    test5 = run_test(
        "python rdb-tool/src/create_rdb_template.py rdb-tool/examples/relay710.txt rdb-tool/examples/test_template.rdb",
        "Create template RDB file"
    )
    
    # Test 6: Verify template RDB was created
    test6 = os.path.exists("rdb-tool/examples/test_template.rdb")
    print(f"Testing: Template RDB file creation")
    if test6:
        print("  Result: PASSED")
        # Check file size
        size = os.path.getsize("rdb-tool/examples/test_template.rdb")
        print(f"  Output: File size {size} bytes")
    else:
        print("  Result: FAILED")
        print("  Error: test_template.rdb not found")
    
    # Summary
    print("\n" + "=" * 50)
    print("Test Summary:")
    tests = [test1, test2, test3, test4, test5, test6]
    passed = sum(tests)
    total = len(tests)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("All tests PASSED!")
        return 0
    else:
        print("Some tests FAILED!")
        return 1

if __name__ == "__main__":
    sys.exit(main())