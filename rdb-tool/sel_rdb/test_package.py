"""
Test script to verify that the SEL_Rdb package works correctly.
"""

def test_imports():
    """Test that all modules can be imported."""
    try:
        import sel_rdb
        print("✓ Main package imported successfully")
        
        # Test importing submodules
        from sel_rdb import rdb_analyzer
        print("✓ rdb_analyzer imported successfully")
        
        from sel_rdb import list_rdb_streams
        print("✓ list_rdb_streams imported successfully")
        
        from sel_rdb import extract_logic_section
        print("✓ extract_logic_section imported successfully")
        
        from sel_rdb import create_rdb_template
        print("✓ create_rdb_template imported successfully")
        
        # Test importing functions
        from sel_rdb import analyze_rdb_file
        print("✓ analyze_rdb_file imported successfully")
        
        from sel_rdb import list_streams
        print("✓ list_streams imported successfully")
        
        from sel_rdb import extract_logic_from_file
        print("✓ extract_logic_from_file imported successfully")
        
        from sel_rdb import create_rdb_file
        print("✓ create_rdb_file imported successfully")
        
        print("\nAll imports successful!")
        return True
        
    except Exception as e:
        print(f"✗ Import failed: {e}")
        return False

def test_function_calls():
    """Test that functions can be called (without actually processing files)."""
    try:
        import sel_rdb
        
        # Test that functions exist and are callable
        assert callable(sel_rdb.analyze_rdb_file)
        assert callable(sel_rdb.list_streams)
        assert callable(sel_rdb.extract_logic_from_file)
        assert callable(sel_rdb.create_rdb_file)
        
        print("✓ All functions are callable")
        return True
        
    except Exception as e:
        print(f"✗ Function call test failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing SEL_Rdb package...")
    print("=" * 40)
    
    import_test = test_imports()
    function_test = test_function_calls()
    
    print("\n" + "=" * 40)
    if import_test and function_test:
        print("All tests passed! Package is ready for use.")
    else:
        print("Some tests failed. Please check the errors above.")