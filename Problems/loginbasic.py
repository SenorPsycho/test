
# USERNAME AND PASSWORD
USERNAME = "omthapa"
PASSWORD = "password"

# Prompt user for credentials
input_username = input("Enter username: ")
if input_username == "":
    print("Username cannot be empty.")
    exit()
input_password = input("Enter password: ")
if input_password == "":
    print("Password cannot be empty.")
    exit()

# Check credentials
# if input_username == USERNAME and input_password == PASSWORD:
    print("Login successful!")
else:
    print("Login failed. Invalid username or password.")
