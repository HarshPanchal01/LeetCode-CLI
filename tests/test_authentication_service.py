import unittest
from unittest.mock import patch
from cli.services.authentication_service import AuthenticationService
from cli.utils.credentials_manager import CredentialsManager

class TestAuthenticationService(unittest.TestCase):

    @patch('cli.utils.credentials_manager.keyring')
    def test_login_success(self, mock_keyring):
        auth_service = AuthenticationService()

        session = "testsession"
        csrftoken = "testcsrftoken"

        result = auth_service.login(session, csrftoken)
        self.assertTrue(result)
        self.assertEqual(auth_service.session.cookies.get("LEETCODE_SESSION"), session)
        self.assertEqual(auth_service.session.cookies.get("csrftoken"), csrftoken)

    def test_logout(self):
        auth_service = AuthenticationService()
        auth_service.login("testsession", "testcsrftoken")
        auth_service.logout()
        self.assertEqual(len(auth_service.session.cookies), 0)

if __name__ == '__main__':
    unittest.main()
