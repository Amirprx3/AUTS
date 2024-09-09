import bcrypt
import subprocess
import platform

print(
    '''
  /$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$ 
 /$$__  $$| $$  | $$|__  $$__//$$__  $$
| $$  \ $$| $$  | $$   | $$  | $$  \__/
| $$$$$$$$| $$  | $$   | $$  |  $$$$$$ 
| $$__  $$| $$  | $$   | $$   \____  $$
| $$  | $$| $$  | $$   | $$   /$$  \ $$
| $$  | $$|  $$$$$$/   | $$  |  $$$$$$/
|__/  |__/ \______/    |__/   \______/ 
   (ADD)    (USER)     (TO)   (SYSTEM)

GITHUB: https://github.com/Amirprx3    
MADE BY: Amirprx3
    '''
)

def hash_password(password):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed

def add_user(username, password):
    hashed_password = hash_password(password)
    system = platform.system()

    try:
        if system == 'Linux' or system == 'Darwin':
            # Command for Unix-based systems
            subprocess.run(['sudo', 'useradd', '-m', username], check=True)
            subprocess.run(['sudo', 'chpasswd'], input=f"{username}:{password}".encode(), check=True)
        elif system == 'Windows':
            # Command for Windows
            subprocess.run(['net', 'user', username, password, '/add'], check=True)
        print(f"User {username} added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    user = input("Enter the username: ")
    pwd = input("Enter the password: ")
    add_user(user, pwd)

# Made by: Amirprx3