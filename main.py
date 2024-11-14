"""
This script provides the main function that starts the interactive custom shell.

Author: Zavier Jackson
Date: 2024-11-04
"""

# Necessary standard and external libraries
from termcolor import colored  # Colored terminal text output

# Custom functions from additional scripts
from command_handler import parse_command, execute_command
from prompt_ui import prompt_session, display_prompt

def main():
    """
    The main function that starts an interactive shell session.

    This function sets up a prompt session and enters an infinite loop where it waits for user commands. It handles user input, parses the commands, and executes them accordingly. The loop can be interrupted by the user using Ctrl+C or Ctrl+D.

    Exceptions:
        KeyboardInterrupt: Catches interruption with Ctrl+C and displays a message.
        EOFError: Catches end-of-file (Ctrl+D) and exits the shell gracefully.
    """
    session = prompt_session()
    while True:
        try:
            command = session.prompt(
                display_prompt()
            )  # Display the prompt and get user input
            args = parse_command(command)  # Split the input into command and arguments
            execute_command(args)  # Execute the parsed command
        except KeyboardInterrupt:
            # Handle interruption with Ctrl+C
            print(
                colored("\nShell interrupted. Type 'exit' or 'quit' to exit.", "yellow")
            )
        except EOFError:
            # Handle end-of-file (Ctrl+D)
            print(colored("\nEOF detected. Exiting shell...", "red"))
            break

# Run the main function only if the script is executed directly
if __name__ == "__main__":
    main()
