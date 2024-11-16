"""
This script provides the necessary functions for parsing commands, handling user input and executing shell commands.

Author: Zavier Jackson
Date: 2024-11-04
"""

# Necessary standard and external libraries
import shlex  # shlex.split() splits a string into parts, based on certain delimiters
from termcolor import colored  # Colored terminal text output

# Custom functions from additional scripts
from file_operations import (
    create_file,
    delete_file,
    rename_file,
)  # Functions for file operations
from dir_operations import (
    make_directory,
    remove_directory,
    change_directory,
)  # Functions for directory management
from file_access_permissions.modify_permissions import (
    modify_permissions,
)  # Function to modify file permissions
from file_access_permissions.list_attributes import (
    list_attributes,
)  # Function to list file attributes
from standard_commands import (
    show_help,
    exit_shell,
)  # Functions representing built-in commands
from env_variables import (
    set_variable,
    get_variable,
    list_variables,
    unset_variable,
)  # Functions for environment variable management


def parse_command(command: str):
    """
    Splits a command string into various parts based on whitespace or double quotes.
    Replaces any environment variable keys (strings starting with '$') with their values.

    Parameters:
        command (str): The command string to be parsed.

    Returns:
        list: A list of command arguments with environment variables substituted.
    """
    # Split the command into parts
    parts = shlex.split(command)

    # Replace environment variables with their values
    if not parts[0].lower() in ("set", "get", "list_env", "unset"):
        for i, part in enumerate(parts):
            if part.startswith("$"):  # Check if the part is an environment variable key
                parts[i] = get_variable(
                    part
                )  # Replace with the environment variable value

    return parts


def execute_command(args: list[str]):
    """
    Maps parsed command arguments to specific functions and
    handles pipes and redirection if necessary.

    Parameters:
        args (list): A list of parsed command arguments.

    Exceptions:
        ValueError: If a command's arguments are missing or incorrect.
        Exception: Any other exceptions that may occur during execution.
    """
    if not args:
        return  # Ignore empty commands

    command = (args[0]).lower()  # The first array element is the command
    # Place actual command arguments into a separate array
    arguments = args[1:]

    try:
        # A dictionary of supported commands and their corresponding # of arguments
        commands_arguments = {
            # File operations
            "create": 1,
            "delete": 1,
            "rename": 2,
            # Directory operations
            "mkdir": 1,
            "rmdir": 1,
            "chdir": 1,
            # File attributes/permissions
            "mod_perm": 2,
            "list_attr": 0,
            # Built-in commands
            "help": 0,
            "exit": 0,
            # Environment variable commands
            "set": 2,
            "get": 1,
            "list_env": 0,
            "unset": 1,
        }
        # If a command is present in the dictionary
        if command in commands_arguments:
            # If the # of arguments are not equal to that being expected by the command
            if len(arguments) != commands_arguments[command]:
                raise ValueError(
                    f"'{command}' command expects {commands_arguments[command]} argument(s)."
                )
        else:
            raise ValueError(f"'{command}' command not found or supported.")

        name = "".join(arguments)

        # Map commands to user-defined functions
        if command == "create":
            create_file(name)
        elif command == "delete":
            delete_file(name)
        elif command == "rename":
            old_name, new_name = arguments
            rename_file(old_name, new_name)
        elif command == "mkdir":
            make_directory(name, print_already_exists=True)
        elif command == "rmdir":
            remove_directory(name)
        elif command == "chdir":
            change_directory(name)
        elif command == "mod_perm":
            path, permissions = arguments
            modify_permissions(path, permissions)
        elif command == "list_attr":
            list_attributes()
        elif command == "set":
            key, value = arguments
            set_variable(key, value)
        elif command == "get":
            get_variable(name)
        elif command == "list_env":
            list_variables()
        elif command == "unset":
            unset_variable(name)
        elif command == "help":
            show_help()
        elif command == "exit":
            exit_shell()
    except Exception as e:
        # Handles any other exceptions that may occur
        print(colored(f"Error: {e}", "red"))
