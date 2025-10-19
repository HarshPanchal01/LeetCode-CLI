import requests
from typing import List
from .models.problems import Problem

API_URL = "https://alfa-leetcode-api.onrender.com/problems"

def fetch_problems(limit: int = 20, tags: List[str] = None, difficulty: str = None) -> List[Problem]:
    params = {"limit": limit}
    if tags:
        params["tags"] = "+".join(tags)
    if difficulty:
        params["difficulty"] = difficulty.upper()

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    problems_data = response.json().get("problemsetQuestionList", [])
    problems = [
        Problem(
            id=problem.get("frontendQuestionId"),
            title=problem.get("title"),
            difficulty=problem.get("difficulty"),
            paid_only=problem.get("paidOnly"),
            tags=[tag.get("name") for tag in problem.get("topicTags", [])]
        )
        for problem in problems_data
    ]
    return problems

def display_problems(problems: List[Problem]):
    for problem in problems:
        print(f"{problem.id}. {problem.title} ({problem.difficulty})")

def fetch_problem(title_slug: str) -> Problem:
    response = requests.get(f"{API_URL.replace('/problems', '/select')}?titleSlug={title_slug}")
    response.raise_for_status()

    problem_data = response.json()
    problem = Problem(
        id=problem_data.get("questionId"),
        title=problem_data.get("title"),
        difficulty=problem_data.get("difficulty"),
        paid_only=problem_data.get("paidOnly"),
        tags=[tag.get("name") for tag in problem_data.get("topicTags", [])]
    )
    return problem

def display_problem_details(problem: Problem):
    print(f"ID: {problem.id}")
    print(f"Title: {problem.title}")
    print(f"Difficulty: {problem.difficulty}")
    print(f"Paid Only: {problem.paid_only}")
    print(f"Tags: {', '.join(problem.tags)}")

def get_question_id(title_slug: str) -> int:
    problem = fetch_problem(title_slug)
    return problem.id
