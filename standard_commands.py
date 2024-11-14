"""
This script consists of the necessary functions for built-in commands.

Author: Khaleel White
Date: 2024-11-13
"""

# Necessary standard and external libraries
import sys  # provides access to some system-specific parameters and functions


def exit_shell():
    print("Exiting shell.")
    sys.exit(0)


def show_help():
    # shows help message when  function is called upon
    help_text = """

   ******************************************************************************************************************
   ****************************************************  HELP   *****************************************************
   ******************************************************************************************************************

    Notes:
     Commands are case-sensitive, so use lowercase for all commands.
     If you enter an unknown command, the shell will display a helpful message.

    Available Commands:

     create : creates a file
     delete : deletes a file
     rename : rename file
     make   : make
     remove : remove files
     change : change
     modify : Modify files
     list   : Displays list of files
     help   : Displays this help message, listing available commands and their descriptions.
     exit   : Exits the shell gracefully.

    Usage Examples:
    Type 'create' and press Enter to create a new file.
     Type 'delete' and press Enter to close the shell.
     Type 'rename' and press Enter to rename files in the shell.
     Type 'change' and press Enter to ###.
     Type 'modify' and press Enter to modify files in the shell.
     Type 'list' and press Enter to display a list of files.
     Type 'help' and press Enter to see this help message.
     Type 'exit' and press Enter to close the shell.



    """
    print(help_text)
