"""
This script consists of the necessary functions for parsing commands, handling user input and executing shell commands.

Author: Zavier Jackson
Date: 2024-11-04
"""

# Necessary standard and external libraries
import os                       # Functions to interact with the operating system
import subprocess               # Spawn new processes and connect to their input/output/error pipes
import shlex                    # shlex.split() splits a string into parts, based on certain delimiters
from termcolor import colored   # Colored terminal text output

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

# from error_handling import handle_invalid_command  # Handles invalid command errors

def parse_command(command: str):
    """
    Splits a command string into individual parts based on whitespace or double quotes.

    Parameters:
        command (str): The command string to be parsed.

    Returns:
        list: A list of command arguments where the first element is the first substring
              and subsequent elements are either delimited by whitespace or enclosed in double quotes.
    """
    return shlex.split(command)

# Function to handle pipes and redirection in commands
def handle_redirection_and_piping(command):
    # Split the command by pipe symbol to separate piped commands
    commands = command.split("|")
    num_commands = len(commands)
    input_data = None  # Holds data to pass between piped commands

    for i, cmd in enumerate(commands):
        # Expand any environment variables in the command (e.g., $HOME)
        cmd = os.path.expandvars(cmd.strip())

        # Handle output redirection (>)
        if ">" in cmd:
            cmd, output_file = cmd.split(">", 1)  # Separate command and output file
            cmd = cmd.strip()
            output_file = output_file.strip()
            args = parse_command(cmd)  # Parse the command part
            with open(output_file, "w") as f:  # Open file for writing output
                result = subprocess.run(
                    args, input=input_data, text=True, stdout=f, stderr=subprocess.PIPE
                )
                if result.stderr:
                    print(colored(result.stderr, "red"))
            input_data = None  # Reset input_data after redirection

        # Handle input redirection (<)
        elif "<" in cmd:
            cmd, input_file = cmd.split("<", 1)  # Separate command and input file
            cmd = cmd.strip()
            input_file = input_file.strip()
            args = parse_command(cmd)  # Parse the command part
            with open(input_file, "r") as f:  # Open file for reading input
                input_data = f.read()
            result = subprocess.run(
                args, input=input_data, text=True, capture_output=True
            )
            # If there is output, store it in input_data to pass to the next command
            if result.stdout:
                input_data = (
                    result.stdout
                )  # Pass output to the next command in the pipeline
            if result.stderr:
                print(
                    colored(result.stderr, "red")
                )  # Print any error messages in red for visibility

        else:
            # This section handles regular commands, or commands in a pipeline (without redirection)
            args = parse_command(cmd.strip())  # Parse the command to get arguments

            # Check if this is the last command in the pipeline
            if i == num_commands - 1:
                # Run the final command, print its output directly
                result = subprocess.run(
                    args, input=input_data, text=True, capture_output=True
                )
                if result.stdout:
                    print(
                        result.stdout
                    )  # Print the final command output to the console
                if result.stderr:
                    print(colored(result.stderr, "red"))  # Print any errors in red

            else:
                # For intermediate commands in the pipeline
                result = subprocess.run(
                    args, input=input_data, text=True, capture_output=True
                )
                if result.stdout:
                    input_data = (
                        result.stdout
                    )  # Pass output to the next command in the pipeline
                if result.stderr:
                    print(colored(result.stderr, "red"))  # Print any errors in red


def execute_command(args : list[str]):
    """
    Executes shell commands based on parsed arguments.

    This function maps parsed command arguments to specific functions and
    handles pipes and redirection if necessary.

    Parameters:
        args (list): A list of parsed command arguments.

    Exceptions:
        ValueError: Raised if the arguments are missing or incorrect.
        Exception: Any other exceptions that may occur during execution will be printed as error messages.
    """
    # Ensure there is at least one argument (the command itself)
    if not args:
        return          # Ignore empty commands

    command = (args[0]).lower()   # The first argument is the command
    # Combine the rest of the arguments into a single string to handle multi-word file or directory names
    arguments = args[1:]

    try:
        # A dictionary of supported commands and their corresponding # of arguments
        commands_arguments = {
            # File operations
            "create" : 1,
            "delete" : 1,
            "rename" : 2,
            # Directory operations
            "make"   : 1,
            "remove" : 1,
            "change" : 1,
            # File access/permissions
            "modify" : 2,
            "list"   : 0,
            # Built-in commands
            "help"   : 0,
            "exit"   : 0
        }
        # If a command is present in the dictionary
        if command in commands_arguments:
            # If the # of arguments are not equal to that being expected by the command
            if len(arguments) != commands_arguments[command]:
                raise ValueError

        file_dir_name = "".join(arguments)

        # Map commands to user-defined functions
        if command == "create":
            create_file(file_dir_name)
        elif command == "delete":
            delete_file(file_dir_name)
        elif command == "rename":
            old_name = arguments[1]
            new_name = arguments[2]
            rename_file(old_name, new_name)
        elif command == "make":
            make_directory(file_dir_name)
        elif command == "remove":
            remove_directory(file_dir_name)
        elif command == "change":
            change_directory(file_dir_name)
        elif command == "modify":
            permissions, file_name = arguments.split(" ", 1)
            modify_permissions(permissions, file_name)
        elif command == "list" and file_dir_name.upper() == "-l":
            list_attributes()               # Lists file attributes in long format
        elif command == "help":
            show_help()
        elif command == "exit":
            exit_shell()
        else:
            # Handle commands involving pipes and redirection
            handle_redirection_and_piping(" ".join(args))
    except ValueError as e:
        # Handles cases where arguments are missing or incorrect
        print(colored(f"Error: \"{command}\" command expects {commands_arguments[command]} argument(s).", "red"))
    except Exception as e:
        # Handles any other exceptions that may occur
        print(colored(f"Error: {e}", "red"))
