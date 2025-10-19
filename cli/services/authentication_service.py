import requests

class AuthenticationService:
    def __init__(self):
        self.session = requests.Session()

    def login(self, leetcode_session, csrftoken):
        cookies = {
            "LEETCODE_SESSION": leetcode_session,
            "csrftoken": csrftoken
        }
        self.session.cookies.update(cookies)
        # We can't truly verify the cookies are valid without making a request to a protected endpoint.
        # For now, we'll assume they are correct if provided.
        return True

    def logout(self):
        self.session.cookies.clear()
