"""
This script provides the necessary functions for built-in commands.

Author: Khaleel White
Date: 2024-11-13
"""

# Necessary standard and external libraries
import sys  # System-specific parameters and functions


def exit_shell():
    print("Exiting shell.")
    sys.exit(0)


def show_help():
    # Updated help message to include all supported commands with detailed descriptions
    help_text = """
    **************************************************************************************************
    ******************************************* HELP *************************************************
    **************************************************************************************************

    Notes:
    - Commands are case-sensitive; use lowercase for all commands.
    - Ensure correct arguments are provided for each command.
    - Environment variables must start with a `$` (e.g., `$VAR_NAME`).

    Available Commands:

    **File Operations**
    1. create <file_name>
       - Creates a new file. If directories in the path do not exist, they will be created automatically.
       - Example: create documents/notes.txt

    2. delete <file_name>
       - Deletes an existing file.
       - Example: delete notes.txt

    3. rename <old_name> <new_name>
       - Renames a file from <old_name> to <new_name>.
       - Example: rename old.txt new.txt

    **Directory Operations**
    4. mkdir <dir_name>
       - Creates a new directory. If it already exists, a warning is displayed.
       - Example: mkdir projects

    5. rmdir <dir_name>
       - Deletes a directory. If it is not empty, user confirmation is required before deleting contents.
       - Example: rmdir projects

    6. chdir <dir_name>
       - Changes the current working directory to the specified directory.
       - Example: chdir projects

    **File Attributes and Permissions**
    7. mod_perm <file_name> <permissions>
       - Modifies file or directory permissions.
       - For Linux: Use octal format (e.g., 755).
       - For Windows: Use symbolic format (e.g., F for Full Control, R for Read).
       - Example (Linux): mod_perm file.txt 755
       - Example (Windows): mod_perm file.txt F

    8. list_attr
       - Displays attributes (permissions, size, and last modified time) of all files and directories in the current directory.
       - Example: list_attr

    **Environment Variable Management**
    9. set <variable_name> <value>
       - Sets or updates a shell-specific environment variable.
       - Variable names must start with a '$'.
       - Example: set $USERNAME John

    10. get <variable_name>
        - Retrieves the value of a shell-specific environment variable.
        - Example: get $USERNAME

    11. list_env
        - Lists all shell-specific environment variables and their values.
        - Example: list_env

    12. unset <variable_name>
        - Deletes a specific shell-specific environment variable.
        - Example: unset $USERNAME

    **Built-in Commands**
    13. help
        - Displays this help message, listing all available commands and their descriptions.
        - Example: help

    14. exit
        - Exits the shell gracefully.
        - Example: exit

    **Usage Tips**
    - Use tab for auto-completion of commands.
    - Commands that require paths accept relative or absolute paths.

    **************************************************************************************************
    """
    print(help_text)
