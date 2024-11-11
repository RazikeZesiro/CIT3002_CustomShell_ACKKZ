# Import the os library to perform file operations
import os

def delete_file(file_name):
    """
    Deletes a file with the given name if it exists.
    
    Parameters:
    file_name (str): The name of the file to delete.
    """
    try:
        os.remove(file_name)  # Attempt to delete the file
        print(f"File '{file_name}' deleted.")  # Confirm deletion
    except FileNotFoundError:  # If the file is not found
        print(f"File '{file_name}' not found.")  # Print an error message
