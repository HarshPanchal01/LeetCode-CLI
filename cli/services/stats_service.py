import requests
from typing import List
from ..models.submissions import Submission
from ..models.user_stats import UserStats

API_URL = "https://alfa-leetcode-api.onrender.com"

class StatsService:
    def get_user_stats(self, username: str) -> UserStats:
        response = requests.get(f"{API_URL}/{username}/solved")
        response.raise_for_status()

        stats_data = response.json()
        return UserStats(
            total_problems=stats_data.get("totalQuestions"),
            solved_problems=stats_data.get("solvedProblem"),
            acceptance_rate=stats_data.get("acceptanceRate")
        )

    def get_submissions(self, username: str, limit: int = 20) -> List[Submission]:
        response = requests.get(f"{API_URL}/{username}/submission?limit={limit}")
        response.raise_for_status()

        submissions_data = response.json().get("submission", [])
        submissions = [
            Submission(
                id=submission.get("id"),
                status=submission.get("statusDisplay"),
                title=submission.get("title"),
                runtime=submission.get("runtime"),
                memory=submission.get("memory")
            )
            for submission in submissions_data
        ]
        return submissions
