import getpass

def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    
    # Here you would add the actual authentication logic.
    # For demonstration, we'll assume authentication is successful.
    # Replace this with real authentication (e.g., API call to LeetCode).
    
    auth_success = True  # Placeholder for authentication result
    
    if auth_success:
        print(f"Logged in as {username}")
    else:
        print("Authentication failed. Please check your credentials.")