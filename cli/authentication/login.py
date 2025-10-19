from getpass import getpass
from ..services.authentication_service import AuthenticationService
from ..utils.credentials_manager import CredentialsManager

def login():
    username = input("Username: ")
    leetcode_session = getpass("Enter your LEETCODE_SESSION cookie: ")
    csrftoken = getpass("Enter your csrftoken cookie: ")
    
    auth_service = AuthenticationService()
    if auth_service.login(leetcode_session, csrftoken):
        creds_manager = CredentialsManager()
        creds_manager.set_cookies(username, leetcode_session, csrftoken)
        print("Logged in successfully.")
    else:
        print("Authentication failed. Please check your cookies.")
