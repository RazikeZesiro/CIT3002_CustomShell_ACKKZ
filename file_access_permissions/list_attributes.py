"""
This script consists of the necessary function for displaying file attributes.

Author: Chevon Sutherland
Date: 2024-11-12
"""

# Necessary standard and external libraries
import os

def list_attributes():
    """List file attributes in the current directory"""
    try:
        current_directory = os.getcwd() # Gets current working directory

        # This lists all of the entries in the current directory
        for entry in os.listdir(current_directory):
            stat_info = os.stat(entry) # Gets files stats

            # Gets permissions in an octal form (last 3 digits)
            permissions = oct(stat_info.st_mode)[-3:]
            size = stat_info.st_size # This Gets the file size

            #Outputs the file attributes
            print (f"{permissions} {size} bytes - {entry}")
    except Exception as e:
        print(f"Error listing the attributes: {e}")

# Example
# list_attributes()
