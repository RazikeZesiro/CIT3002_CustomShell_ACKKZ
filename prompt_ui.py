"""
This script consists of the necessary functions for customizing the prompt interface or UI aspects.

Author: Zavier Jackson
Date: 2024-11-05
"""

# Necessary standard and external libraries
import os                                   # Functions to interact with the operating system
from prompt_toolkit import PromptSession    # Provides an interactive prompt session
from prompt_toolkit.completion import (
    WordCompleter,
)                                           # Auto-completion of commands
from prompt_toolkit.styles import Style     # Styling of command-line prompt

# A list of commands that the shell supports
commands = [
    # File operations
    "create",
    "delete",
    "rename",
    # Directory operations
    "make",
    "remove",
    "change",
    # File attributes/permissions
    "modify",
    "list",
    # Built-in commands
    "help",
    "exit",
]
# A completer with the list of commands for auto-completion (case-insensitive)
command_completer = WordCompleter(commands, ignore_case=True)

# A style dictionary for the command-line prompt appearance
style = Style.from_dict(
    {
        "prompt": "ansigreen bold", # Set the main prompt text color to green and bold
        "cwd": "ansiblue",          # Set the current working directory text color to blue
    }
)

def prompt_session():
    """
    Creates and returns a PromptSession with autocompletion and styling.

    Returns:
        PromptSession: A prompt session configured with the specified completer and style.
    """
    return PromptSession(completer=command_completer, style=style)


def display_prompt():
    """
    Constructs and returns a styled prompt containing the username and current working directory.

    Returns:
        list: A list of tuples representing the styled prompt components.
    """
    user = os.getenv("USER") or os.getenv("USERNAME")   # Get username from environment variables
    cwd = os.getcwd()                                   # Get current working directory
    prompt = [
        ("class:prompt", f"{user}"),
        ("class:cwd", f":{cwd}"),
        ("class:prompt", "$ "),  # A dollar sign to indicate readiness for command
    ]
    return prompt
