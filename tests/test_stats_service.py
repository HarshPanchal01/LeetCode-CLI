import unittest
import requests_mock
from cli.services.stats_service import StatsService, API_URL
from cli.models.user_stats import UserStats
from cli.models.submissions import Submission

class TestStatsService(unittest.TestCase):

    def setUp(self):
        self.stats_service = StatsService()
        self.username = "testuser"

    @requests_mock.Mocker()
    def test_get_user_stats(self, m):
        mock_response = {
            "totalQuestions": 100,
            "solvedProblem": 50,
            "acceptanceRate": 50.0
        }
        m.get(f"{API_URL}/{self.username}/solved", json=mock_response)

        stats = self.stats_service.get_user_stats(self.username)
        self.assertIsInstance(stats, UserStats)
        self.assertEqual(stats.total_problems, 100)
        self.assertEqual(stats.solved_problems, 50)
        self.assertEqual(stats.acceptance_rate, 50.0)

    @requests_mock.Mocker()
    def test_get_submissions(self, m):
        mock_response = {
            "submission": [
                {
                    "id": 1,
                    "statusDisplay": "Accepted",
                    "title": "Two Sum",
                    "runtime": "100ms",
                    "memory": "15MB"
                }
            ]
        }
        m.get(f"{API_URL}/{self.username}/submission?limit=20", json=mock_response)

        submissions = self.stats_service.get_submissions(self.username)
        self.assertIsInstance(submissions, list)
        self.assertIsInstance(submissions[0], Submission)
        self.assertEqual(submissions[0].id, 1)
        self.assertEqual(submissions[0].title, "Two Sum")

if __name__ == '__main__':
    unittest.main()
