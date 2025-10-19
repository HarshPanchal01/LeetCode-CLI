import unittest
from unittest.mock import patch
from cli.services.submission_service import SubmissionService
import requests

class TestSubmissionService(unittest.TestCase):

    def setUp(self):
        self.submission_service = SubmissionService()
        self.title_slug = "two-sum"
        self.question_id = 1
        self.language = "python"
        self.code = "class Solution:\n    def twoSum(self, nums, target):\n        return []"

    @patch('cli.utils.credentials_manager.keyring')
    @patch('requests.post')
    def test_submit_solution_success(self, mock_post, mock_keyring):
        mock_keyring.get_password.side_effect = ["test_session", "test_csrftoken"]
        mock_post.return_value.status_code = 200

        result = self.submission_service.submit_solution(self.title_slug, self.question_id, self.language, self.code)
        self.assertTrue(result)

    @patch('cli.utils.credentials_manager.keyring')
    @patch('requests.post')
    def test_submit_solution_failure(self, mock_post, mock_keyring):
        mock_keyring.get_password.side_effect = ["test_session", "test_csrftoken"]
        mock_post.return_value.raise_for_status.side_effect = requests.exceptions.RequestException("Test Exception")

        result = self.submission_service.submit_solution(self.title_slug, self.question_id, self.language, self.code)
        self.assertFalse(result)

    @patch('cli.utils.credentials_manager.keyring')
    def test_submit_solution_no_login(self, mock_keyring):
        mock_keyring.get_password.return_value = None

        result = self.submission_service.submit_solution(self.title_slug, self.question_id, self.language, self.code)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
