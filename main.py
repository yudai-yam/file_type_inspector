import os
import sys
from pathlib import Path

def get_extension(item_name: str):
    # Get file extension from name
    extension = item_name.split(".")[-1]
    return extension

def is_checked(extensions: list, extension: str):
    return extension in extensions

def read_binary(file: Path):
    try:
        with file.open("rb") as f:
            file_start = f.read(6)  # Read first 6 bytes
            
            # Get file size and seek to 6 bytes from end
            f.seek(0, 2)  # Seek to end of file
            file_size = f.tell()
            f.seek(max(0, file_size - 6))  # Seek to 6 bytes from end
            file_end = f.read(6)  # Read last 6 bytes

            print(file_start)
            print(file_end)

            return file_start, file_end
    except Exception as e:
        print(f"Error reading file {file}: {e}")
        return None, None

def traverse_directory(root: Path):

    checked_extensions = []

    for item in root.rglob('*'):
        extension = get_extension(item.name) 
        print(extension)

        # if not is_checked(checked_extensions, extension):
        # get the start and end
        read_binary(item)
        
       
        checked_extensions.append(extension)

        



def main():

    root = Path("./test_directory")

    print(root.name)

    traverse_directory(root)




    


if __name__ == "__main__":
    main()



