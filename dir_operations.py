"""
This script provides the necessary functions for directory management.

Author: Kaleel Barrett
Date: 2024-11-12
"""

# Necessary standard and external libraries
import os       # Functions to interact with the operating system
import shutil   # Function for removal of directory with content


def make_directory(dir_path: str, print_already_exists: bool = False):
    """
    Makes a new directory with the specified path.

    Parameters:
        dir_path (str): The path of the directory to make.
        print_already_exists (bool): If True, print message if directory already exists.

    Exceptions:
        FileExistsError: If the directory already exists.
        PermissionError: If there are permission issues while creating the directory.
    """
    try:
        if os.path.exists(dir_path):
            if print_already_exists:
                raise FileExistsError(f"Directory '{dir_path}' already exists.")
        else:
            # Make the directory if it does not exist
            os.makedirs(dir_path, exist_ok=True)
            print(f"Directory '{dir_path}' made.")
    except PermissionError:
        raise PermissionError(f"Permission denied while trying to make directory '{dir_path}'.")


def remove_directory(dir_path: str):
    """
    Removes a directory if it is empty. If not, seeks confirmation for removal and
    proceeds to remove the directory and all its content if confirmed.

    Parameters:
        dir_path (str): The path of the directory to remove.

    Exceptions:
        FileNotFoundError: If the directory is not found.
        PermissionError: If there are permission issues while removing the directory.
    """
    try:
        # Attempt to remove the directory if it is empty
        os.rmdir(dir_path)
        print(f"Directory '{dir_path}' removed.")
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory '{dir_path}' not found.")
    except OSError:
        print(f"Directory '{dir_path}' is not empty or cannot be removed.")
        confirmation = input("Do you want to remove the directory and all its contents? (y/default = n): ")
        if confirmation.lower() == "y":
            try:
                shutil.rmtree(dir_path)  # Remove the directory and all its contents
                print(f"Directory '{dir_path}' and all its contents have been removed.")
            except PermissionError:
                # For directory with content
                raise PermissionError(f"Permission denied while trying to remove directory '{dir_path}'.")
    except PermissionError:
        # For empty directory
        raise PermissionError(f"Permission denied while trying to remove directory '{dir_path}'.")


def change_directory(cwd_path: str):
    """
    Changes the current working directory to the specified directory.

    Parameters:
        cwd_path (str): The path of the directory to switch to.

    Exceptions:
        FileNotFoundError: If the directory is not found.
        PermissionError: If there are permission issues while changing to the directory.
    """
    try:
        # Attempt to change to the specified directory
        os.chdir(cwd_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory '{cwd_path}' not found.")
    except PermissionError:
        raise PermissionError(
            f"Permission denied while trying to change cwd to '{cwd_path}'."
        )