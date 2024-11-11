# Import the os library for directory operations
import os

def make_directory(directory_name):
    """
    Creates a new directory with the specified name.
    
    Parameters:
    directory_name (str): The name of the directory to create.
    """
    os.makedirs(directory_name, exist_ok=True)  # Create the directory if it doesn’t exist
    print(f"Directory '{directory_name}' created.")  # Confirm creation

def remove_directory(directory_name):
    """
    Removes a directory if it is empty.
    
    Parameters:
    directory_name (str): The name of the directory to remove.
    """
    try:
        os.rmdir(directory_name)  # Attempt to remove the directory
        print(f"Directory '{directory_name}' removed.")  # Confirm removal
    except FileNotFoundError:  # If directory is not found
        print(f"Directory '{directory_name}' not found.")  # Print an error message
    except OSError:  # If the directory cannot be removed (e.g., it’s not empty)
        print(f"Directory '{directory_name}' is not empty or cannot be removed.")

def change_directory(directory_name):
    """
    Changes the current working directory to the specified directory.
    
    Parameters:
    directory_name (str): The name of the directory to switch to.
    """
    try:
        os.chdir(directory_name)  # Attempt to change to the specified directory
        print(f"Changed to directory '{directory_name}'.")  # Confirm directory change
    except FileNotFoundError:  # If the directory does not exist
        print(f"Directory '{directory_name}' not found.")  # Print an error message
