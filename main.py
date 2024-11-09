# Import necessary standard and external libraries for the script
import os  # Provides functions to interact with the operating system
import sys  # Provides access to some variables and functions used or maintained by the interpreter
import subprocess  # Used to spawn new processes and connect to their input/output/error pipes
from prompt_toolkit import PromptSession  # Provides an interactive prompt session
from prompt_toolkit.completion import WordCompleter  # Enables auto-completion of commands
from prompt_toolkit.styles import Style  # Allows for styling of command-line prompt
from termcolor import colored  # Enables colored terminal text output

# Import custom functions from additional scripts that handle specific shell commands
from create_file import create_file  # Function to create a file
from delete_file import delete_file  # Function to delete a file
from rename_file import rename_file  # Function to rename a file
from manage_directory import make_directory, remove_directory, change_directory  # Directory management functions
from modify_permissions import modify_permissions  # Function to modify file permissions
from list_attributes import list_attributes  # Function to list file attributes
from help import display_help  # Function to display help information
from exit_shell import exit_shell  # Function to exit the shell gracefully
from error_handling import handle_invalid_command  # Handles invalid command errors

# Define a style dictionary for the command-line prompt appearance
style = Style.from_dict(
    {
        "prompt": "ansigreen bold",  # Set the main prompt text color to green and bold
        "cwd": "ansiblue",  # Set the current working directory text color to blue
    }
)

# Define a list of commands that the shell supports
commands = [
    "create",  # Command to create a file
    "delete",  # Command to delete a file
    "rename",  # Command to rename a file
    "make",    # Command to create a directory
    "remove",  # Command to remove a directory
    "change",  # Command to change the working directory
    "modify",  # Command to modify file permissions
    "list",    # Command to list file attributes
    "help",    # Command to display help information
    "exit",    # Command to exit the shell
]
# Initialize a completer with the list of commands for auto-completion, ignoring case sensitivity
command_completer = WordCompleter(commands, ignore_case=True)

# Function to display the prompt with user and current directory information
def display_prompt():
    user = os.getenv("USER") or os.getenv("USERNAME")  # Get the username from environment variables
    cwd = os.getcwd()  # Get the current working directory
    prompt = [
        ("class:prompt", f"{user}"),  # Display username with prompt style
        ("class:cwd", f":{cwd}"),  # Display current directory with cwd style
        ("class:prompt", "$ "),  # Display a dollar sign to indicate readiness for command
    ]
    return prompt  # Return the styled prompt

# Function to split a command into individual parts based on whitespace
def parse_command(command):
    return command.strip().split()  # Remove extra whitespace and split by spaces

# Function to execute commands based on parsed arguments
def execute_command(args):
    # Ensure there is at least one argument (the command itself)
    if not args:
        return  # Ignore empty commands

    command = args[0]  # The first argument is the command
    # Combine the rest of the arguments into a single string to handle multi-word file or directory names
    arguments = " ".join(args[1:])

    try:
        # Match the command to the correct function, passing the arguments
        if command == "create":
            create_file(arguments)  # Creates a file
        elif command == "delete":
            delete_file(arguments)  # Deletes a file
        elif command == "rename":
            # Rename requires exactly two arguments: old and new file names
            old_name, new_name = arguments.split(" ", 1)
            rename_file(old_name, new_name)
        elif command == "make":
            make_directory(arguments)  # Creates a directory
        elif command == "remove":
            remove_directory(arguments)  # Removes a directory
        elif command == "change":
            change_directory(arguments)  # Changes current working directory
        elif command == "modify":
            # Modify requires permissions and filename as separate arguments
            permissions, file_name = arguments.split(" ", 1)
            modify_permissions(permissions, file_name)
        elif command == "list" and arguments == "-l":
            list_attributes()  # Lists file attributes in long format
        elif command == "help":
            display_help()  # Shows help information
        elif command == "exit":
            exit_shell()  # Exits the shell
        else:
            # Handle commands involving pipes and redirection
            handle_redirection_and_piping(" ".join(args))
    except ValueError as e:
        # Handles cases where arguments are missing or incorrect
        print(colored("Error: Incorrect number of arguments.", "red"))
    except Exception as e:
        # Handles any other exceptions that may occur
        print(colored(f"Error: {e}", "red"))

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


# The main function sets up the shell and runs the interactive loop
def main():
    session = PromptSession(
        completer=command_completer, style=style
    )  # Create a prompt session with autocompletion and styling
    while True:
        try:
            command = session.prompt(
                display_prompt()
            )  # Display the prompt and get user input
            args = parse_command(command)  # Split the input into command and arguments
            execute_command(args)  # Execute the parsed command
        except KeyboardInterrupt:
            # Handle interruption with Ctrl+C, displaying a helpful message
            print(
                colored("\nShell interrupted. Type 'exit' or 'quit' to exit.", "yellow")
            )
        except EOFError:
            # Handle end-of-file (Ctrl+D), exiting the shell gracefully
            print(colored("\nEOF detected. Exiting shell...", "red"))
            break


# Run the main function only if the script is executed directly
if __name__ == "__main__":
    main()
