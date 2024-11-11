# Import the os library to handle renaming files
import os

def rename_file(old_name, new_name):
    """
    Renames a file from old_name to new_name.
    
    Parameters:
    old_name (str): The current name of the file.
    new_name (str): The new name for the file.
    """
    try:
        os.rename(old_name, new_name)  # Attempt to rename the file
        print(f"File renamed from '{old_name}' to '{new_name}'.")  # Confirm rename
    except FileNotFoundError:  # If the file with old_name is not found
        print(f"File '{old_name}' not found.")  # Print an error message
