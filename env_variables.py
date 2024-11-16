"""
This script provides the necessary functions for managing environment variables in the custom shell.

Author: Amhik Johnson
Date: 2024-11-14
"""


# Internal dictionary to store shell-specific environment variables
shell_vars = {}

def validate_key(key: str) -> str:
    """
    Validates and formats the key to ensure it starts with '$' and is in uppercase.

    Parameters:
        key (str): The raw key input.

    Returns:
        str: The formatted key in uppercase.

    Exceptions:
        ValueError: If the key does not start with '$'.
    """
    if not key.startswith('$'):
        raise ValueError(f"Environment variable name '{key}' must start with '$'.")
    return key.upper()

def set_variable(key: str, value: str):
    """
    Sets or updates a shell-specific environment variable.

    Parameters:
        key (str): The name of the environment variable.
        value (str): The value of the environment variable.

    Exceptions:
        ValueError: If the key is invalid.
    """
    formatted_key = validate_key(key)
    shell_vars[formatted_key] = value
    print(f"Environment variable '{formatted_key}' set to '{value}'.")

def get_variable(key: str):
    """
    Retrieves the value of a shell-specific environment variable.

    Parameters:
        key (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable.

    Exceptions:
        KeyError: If the variable is not found.
    """
    formatted_key = validate_key(key)
    if formatted_key in shell_vars:
        return shell_vars[formatted_key]
    else:
        raise KeyError(f"Environment variable '{formatted_key}' not found.")

def list_variables():
    """
    Lists all shell-specific environment variables and their values.
    """
    if not shell_vars:
        print("No environment variables set.")
        return
    for key, value in shell_vars.items():
        print(f"{key} = '{value}'")

def unset_variable(key: str):
    """
    Deletes a shell-specific environment variable.

    Parameters:
        key (str): The name of the environment variable.

    Exceptions:
        KeyError: If the variable is not found.
    """
    formatted_key = validate_key(key)
    if formatted_key in shell_vars:
        del shell_vars[formatted_key]
        print(f"Environment variable '{formatted_key}' has been unset.")
    else:
        raise KeyError(f"Environment variable '{formatted_key}' not found.")