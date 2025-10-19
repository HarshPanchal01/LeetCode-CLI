from ..utils.credentials_manager import CredentialsManager
import requests

class SubmissionService:
    API_URL = "https://leetcode-361923.wl.r.appspot.com/api/v1/leetcode/questions"

    def __init__(self):
        self.credentials_manager = CredentialsManager()

    def submit_solution(self, title_slug: str, question_id: int, language: str, code: str) -> bool:
        session, csrftoken = self.credentials_manager.get_cookies()
        if not session or not csrftoken:
            print("You are not logged in. Please log in first.")
            return False

        headers = {
            "Content-Type": "application/json",
            "X-CSRF-Token": csrftoken,
            "Cookie": f"LEETCODE_SESSION={session}; csrftoken={csrftoken}",
        }

        payload = {
            "lang": language,
            "question_id": question_id,
            "typed_code": code,
        }

        try:
            response = requests.post(f"{self.API_URL}/{title_slug}/submit", headers=headers, json=payload)
            response.raise_for_status()

            # The API returns a submission ID, but for now, we'll just check for a successful status code.
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while submitting the solution: {e}")
            return False
