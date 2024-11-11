def create_file(file_name):
    """
    Creates an empty file with the given name.
    
    Parameters:
    file_name (str): The name of the file to be created.
    """
    # Open a file in write mode. 'w' mode will create a new file if it doesn't exist.
    with open(file_name, 'w') as f:
        f.write("")  # Write an empty string to create an empty file
    print(f"File '{file_name}' created.")  # Confirm that the file was created
