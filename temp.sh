#!/bin/bash

# Print a welcome message
echo "Hello, World! Your shell script is running."

# List files in the current directory
echo "Listing files in the current directory:"
ls -l

# Create a new directory
echo "Creating a new directory named 'test_dir'"
mkdir test_dir

# Change to the new directory
cd test_dir

# Create a new file in the new directory
echo "Creating a new file named 'test_file.txt'"
touch test_file.txt

# List files in the new directory
echo "Listing files in 'test_dir':"
ls -l

# Print a completion message
echo "Script execution completed."