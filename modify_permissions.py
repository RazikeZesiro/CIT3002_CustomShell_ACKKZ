import os

def modify_permissions(file_name, permissions):
    try:
        mode = int(permissions, 8) # This converts the permissions from string to octal numbers
        os.chmod(file_name, mode) # This changes the file permissions
        
        # Confirmation for the change that was done
        print(f"Permissions for '{file_name}' modified to '{permissions}'.")
        
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        
    except ValueError:
        print("Error: Invalid permissions format. Please use octal fomat")
        
    except PermissionError:
        print(f"Error: Insufficient permissions to modify '{file_name}'.")
    
    except Exception as e:
        print(f"Error modifying permissions for '{file_name}' : {e}")
        
#Example
# modify_permissions('example.txt', '755')