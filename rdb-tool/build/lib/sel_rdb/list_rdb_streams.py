import olefile
import sys

def list_streams(rdb_path):
    """
    List all streams in an RDB file.
    
    Args:
        rdb_path (str): Path to the RDB file
        
    Returns:
        list: List of stream paths
    """
    try:
        ole = olefile.OleFileIO(rdb_path)
        streams = ole.listdir()
        return ["/".join(stream) for stream in streams]
    except Exception as e:
        raise Exception(f"Failed to read OLE streams: {e}")

def main():
    """Main function for command line usage."""
    if len(sys.argv) < 2:
        print("Usage: python list_rdb_streams.py <Relay710.rdb>")
        sys.exit(1)
    
    rdb_path = sys.argv[1]
    try:
        streams = list_streams(rdb_path)
        print(f"Streams/groups in {rdb_path}:")
        for stream in streams:
            print(stream)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()