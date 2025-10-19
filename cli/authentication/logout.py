from ..services.authentication_service import AuthenticationService
from ..utils.credentials_manager import CredentialsManager

def logout():
    creds_manager = CredentialsManager()
    creds_manager.delete_cookies()
    auth_service = AuthenticationService()
    auth_service.logout()
    print("Logged out successfully.")
