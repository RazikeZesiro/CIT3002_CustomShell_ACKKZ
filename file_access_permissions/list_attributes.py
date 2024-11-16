"""
This script consists of the necessary function for displaying file attributes.

Author: Chevon Sutherland
Date: 2024-11-12
"""

# Necessary standard and external libraries
import os   # Functions to interact with the operating system
import stat # Function that converts file's mode to human-readable string
import time # Function to retrieve the last modification times
from prettytable import PrettyTable # Functions for tabular-formatted output


def list_attributes():
    """
    Lists the file attributes such as permissions, size, and last modification time
    for each entry in the current working directory.

    Exceptions:
        PermissionError: If there are permission issues while reading the directory.
    """
    try:
        current_directory = os.getcwd()  # Get current working directory
        table = PrettyTable()  # Create a PrettyTable object
        table.field_names = [
            "Permissions",
            "Size (bytes)",
            "Last Modified",
            "Name",
        ]  # Define column headers

        # List all of the entries in the current directory
        for entry in os.listdir(current_directory):
            entry_path = os.path.join(current_directory, entry)
            stat_info = os.stat(entry_path)  # Get file stats

            # Get human-readable permissions
            permissions = stat.filemode(stat_info.st_mode)
            size = stat_info.st_size  # Get file size
            last_modified = time.ctime(stat_info.st_mtime)  # Get last modification time

            # Add a row to the table
            table.add_row([permissions, size, last_modified, entry])

        # Print the table
        print(table)
    except PermissionError:
        raise PermissionError(
            f"Permission denied while trying to read directory '{current_directory}'."
        )