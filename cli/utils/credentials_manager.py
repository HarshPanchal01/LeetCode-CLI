import keyring

class CredentialsManager:
    SERVICE_NAME = "leetcode-cli"

    def set_cookies(self, username, session, csrftoken):
        keyring.set_password(self.SERVICE_NAME, "username", username)
        keyring.set_password(self.SERVICE_NAME, "LEETCODE_SESSION", session)
        keyring.set_password(self.SERVICE_NAME, "csrftoken", csrftoken)

    def get_cookies(self):
        session = keyring.get_password(self.SERVICE_NAME, "LEETCODE_SESSION")
        csrftoken = keyring.get_password(self.SERVICE_NAME, "csrftoken")
        return session, csrftoken

    def get_username(self):
        return keyring.get_password(self.SERVICE_NAME, "username")

    def delete_cookies(self):
        try:
            keyring.delete_password(self.SERVICE_NAME, "username")
            keyring.delete_password(self.SERVICE_NAME, "LEETCODE_SESSION")
            keyring.delete_password(self.SERVICE_NAME, "csrftoken")
        except keyring.errors.PasswordDeleteError:
            pass
