"""
Test the SEL_Rdb package functionality.
"""

def test_basic_import():
    """Test basic import of the package."""
    try:
        import sel_rdb
        print("[PASS] Basic import successful")
        return True
    except Exception as e:
        print(f"[FAIL] Basic import failed: {e}")
        return False

def test_module_imports():
    """Test importing specific modules."""
    try:
        from sel_rdb import rdb_analyzer
        from sel_rdb import list_rdb_streams
        from sel_rdb import extract_logic_section
        from sel_rdb import create_rdb_template
        print("[PASS] Module imports successful")
        return True
    except Exception as e:
        print(f"[FAIL] Module imports failed: {e}")
        return False

def test_function_imports():
    """Test importing specific functions."""
    try:
        from sel_rdb import analyze_rdb_file
        from sel_rdb import list_streams
        from sel_rdb import extract_logic_from_file
        from sel_rdb import create_rdb_file
        print("[PASS] Function imports successful")
        return True
    except Exception as e:
        print(f"[FAIL] Function imports failed: {e}")
        return False

def test_version():
    """Test accessing package version."""
    try:
        import sel_rdb
        version = getattr(sel_rdb, '__version__', None)
        if version:
            print(f"[PASS] Package version: {version}")
            return True
        else:
            print("[FAIL] Package version not found")
            return False
    except Exception as e:
        print(f"[FAIL] Version test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing SEL_Rdb package...")
    print("=" * 40)
    
    tests = [
        test_basic_import,
        test_module_imports,
        test_function_imports,
        test_version
    ]
    
    results = []
    for test in tests:
        results.append(test())
        print()
    
    print("=" * 40)
    passed = sum(results)
    total = len(results)
    
    if passed == total:
        print(f"All {total} tests passed! Package is ready for use.")
    else:
        print(f"{passed}/{total} tests passed. Some issues need to be addressed.")