"""
This script consists of the necessary functions for performing file operations.

Author: Kaleel Barrett
Date: 2024-11-11
"""

# Necessary standard and external libraries
import os

def create_file(file_name):
    """
    Creates an empty file with the given name.

    Parameters:
    file_name (str): The name of the file to be created.
    """
    # Open a file in write mode. 'w' mode will create a new file if it doesn't exist.
    with open(file_name, "w") as f:
        f.write("")  # Write an empty string to create an empty file
    print(f"File '{file_name}' created.")  # Confirm that the file was created


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
