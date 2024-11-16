"""
This script provides the necessary functions for modifying file permissions.

Author: Chevon Sutherland
Date: 2024-11-08
"""

# Necessary standard and external libraries
import os        # Functions to interact with the operating system
import platform  # Function to determine current operating system


def apply_permissions_linux(path: str, permissions: str):
    """
    Applies permissions to a file or directory on Linux.

    Parameters:
        path (str): Directory/file path.
        permissions (str): String representation of linux permissions.

    Exceptions:
        ValueError: If the permissions string cannot convert to an integer.
        PermissionError: If there are permission issues while modifying permissions.
    """
    try:
        mode = int(permissions, 8)
        os.chmod(path, mode)
    except ValueError:
        raise ValueError(
            "Invalid permissions format. Please use octal format for Linux."
        )
    except PermissionError:
        raise PermissionError


def apply_permissions_windows(path: str, permissions: str):
    """
    Applies permissions to a file or directory on Windows.

    Parameters:
        path (str): Directory/file path.
        permissions (str): Windows permissions, delimited by '~'.

    Exceptions:
        ValueError: If the permissions string is invalid.
        PermissionError: If there are permission issues while modifying permissions.
    """
    # Constants for valid permissions
    VALID_PERMISSIONS = ["F",   # Full control
                          "R",  # Read
                          "RX", # Read & Execute
                          "W",  # Write
                          "M"]  # Modify

    # Split the permissions string by '~' and validate each permission
    permissions_list = permissions.upper().split("~")
    for permission in permissions_list:
        if permission not in VALID_PERMISSIONS:
            raise ValueError(
                "Invalid permissions format. Please use 'F', 'R', 'RX', 'W', 'M', or combinations delimited by '~'."
            )

    # Deny all existing permissions for "Everyone"
    # '> NUL 2>&1' suppresses additional output by icacls Windows command
    os.system(f'icacls "{path}" /deny *S-1-1-0:F > NUL 2>&1')

    # Grant each validated permission to "Everyone"
    for permission in permissions_list:
        result = os.system(f'icacls "{path}" /grant *S-1-1-0:{permission} > NUL 2>&1')
        if result != 0:
            raise PermissionError


def modify_permissions(path: str, permissions: str):
    """
    Modifies file or directory permissions.

    Parameters:
        path (str): The file or directory path.
        permissions (str): The permissions to set (octal format for Linux, symbolic format for Windows, delimited by '~').

    Exceptions:
        PermissionError: If there are permission issues while modifying permissions.
    """
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File or directory '{path}' not found.")
        # Get current OS
        os_type = platform.system()
        if os_type == "Windows":
            apply_permissions_windows(path, permissions)
        else:
            apply_permissions_linux(path, permissions)
        print(f"Permissions for '{path}' modified to '{permissions.upper()}'.")
    except PermissionError:
        raise PermissionError(
            f"Permission denied while modifying permissions for '{path}'."
        )