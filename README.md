# User Management Script

This Python script allows you to add users to the system (Linux, macOS, or Windows) and securely hash their passwords using `bcrypt`. The script determines the operating system and runs the appropriate commands to create the user.

## Features

- Hashes passwords using `bcrypt` for secure storage.
- Adds users on both Unix-based systems (Linux/macOS) and Windows.
- Uses platform detection to run OS-specific commands for user creation.

## Requirements

- Python 3.x
- `bcrypt` library

## Installation

1. Clone the repository or download the script.
2. Install the required dependencies by running:
   ```bash
   pip install bcrypt
###

# Usage
1. Run the script:
    ```bash
    python AUTS.py
2. The script will prompt you to enter a username and password:
- Username: The name of the user to be added.
- Password: The password for the new user.
- The script hashes the password using `bcrypt` and adds the user to the system based on your operating system.


# Example
```
Enter the username: john_doe
Enter the password: ********
User john_doe added successfully.
```
# Supported Operating Systems
- Linux: Uses the `useradd` and `chpasswd` commands.
- macOS: Uses the same commands as Linux.
- Windows: Uses the `net user` command.

# Error Handling
If an error occurs during user creation, it will be displayed in the console:
```
An error occurred: <error message>
```

# License
### This project is licensed under the MIT License.