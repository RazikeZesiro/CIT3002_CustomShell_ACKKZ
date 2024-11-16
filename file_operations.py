"""
This script provides the necessary functions for performing file operations.

Author: Kaleel Barrett
Date: 2024-11-11
"""

# Necessary standard and external libraries
import os  # Functions to interact with the operating system

# Custom functions from additional scripts
from dir_operations import make_directory


def create_file(file_path: str):
    """
    Creates an empty file with the given path and name if it does not exist.

    Parameters:
        file_path (str): The path and name of the file to be created.

    Exceptions:
        FileExistsError: If the file already exists.
        PermissionError: If there are permission issues while creating the file.
    """
    try:
        # Ensure the directory exists
        directory_name = os.path.dirname(file_path)
        if directory_name:
            make_directory(directory_name)

        # Check if the file already exists
        if os.path.exists(file_path):
            raise FileExistsError(f"File '{file_path}' already exists.")

        # Open a file in write mode to create it
        with open(file_path, "w") as f:
            f.write("")
        print(f"File '{file_path}' created.")
    except PermissionError:
        raise PermissionError(
            f"Permission denied while trying to create file '{file_path}'."
        )


def delete_file(file_path: str):
    """
    Deletes a file with the given path and name if it exists.

    Parameters:
        file_path (str): The path and name of the file to delete.

    Exceptions:
        FileNotFoundError: If the file is not found.
        PermissionError: If there are permission issues while deleting the file.
    """
    try:
        # Delete the file
        os.remove(file_path)
        print(f"File '{file_path}' deleted.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_path}' not found.")
    except PermissionError:
        raise PermissionError(
            f"Permission denied while trying to delete file '{file_path}'."
        )


def rename_file(old_name: str, new_name: str):
    """
    Renames a file from old_name to new_name.

    Parameters:
        old_name (str): The current name of the file.
        new_name (str): The new name for the file.

    Exceptions:
        FileNotFoundError: If the file is not found.
        PermissionError: If there are permission issues while renaming the file.
    """
    try:
        # Rename the file
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{old_name}' not found.")
    except PermissionError:
        raise PermissionError(
            f"Permission denied while trying to rename file '{old_name}'."
        )