import argparse
from .authentication.login import login
from .authentication.logout import logout
from .problems import fetch_problems, display_problems, fetch_problem, display_problem_details
from .services.submission_service import SubmissionService
from .services.stats_service import StatsService
from .utils.credentials_manager import CredentialsManager

def main():
    parser = argparse.ArgumentParser(description='LeetCode CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Login command
    subparsers.add_parser('login', help='Login to LeetCode')

    # Logout command
    subparsers.add_parser('logout', help='Logout of LeetCode')

    # Problems command
    problems_parser = subparsers.add_parser('problems', help='Fetch and display problems')
    problems_parser.add_argument('--limit', type=int, default=20, help='Number of problems to fetch')
    problems_parser.add_argument('--tags', nargs='+', help='Filter problems by tags')
    problems_parser.add_argument('--difficulty', choices=['EASY', 'MEDIUM', 'HARD'], help='Filter problems by difficulty')

    # View command
    view_parser = subparsers.add_parser('view', help='View a specific problem')
    view_parser.add_argument('title_slug', help='The title slug of the problem to view')

    # Submit command
    submit_parser = subparsers.add_parser('submit', help='Submit a solution')
    submit_parser.add_argument('title_slug', help='The title slug of the problem to submit')
    submit_parser.add_argument('language', help='The programming language of the solution')
    submit_parser.add_argument('file_path', help='The path to the solution file')

    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Get submission stats')
    stats_parser.add_argument('--submissions', action='store_true', help='Get the last 20 submissions')

    args = parser.parse_args()

    if args.command == 'login':
        login()
    elif args.command == 'logout':
        logout()
    elif args.command == 'problems':
        problems = fetch_problems(limit=args.limit, tags=args.tags, difficulty=args.difficulty)
        display_problems(problems)
    elif args.command == 'view':
        problem = fetch_problem(args.title_slug)
        display_problem_details(problem)
    elif args.command == 'submit':
        from .problems import get_question_id
        question_id = get_question_id(args.title_slug)
        with open(args.file_path, 'r') as f:
            code = f.read()
        submission_service = SubmissionService()
        if submission_service.submit_solution(args.title_slug, question_id, args.language, code):
            print("Solution submitted successfully!")
        else:
            print("Failed to submit solution.")
    elif args.command == 'stats':
        creds_manager = CredentialsManager()
        username = creds_manager.get_username()
        if not username:
            print("You are not logged in. Please log in first.")
            return

        stats_service = StatsService()
        if args.submissions:
            submissions = stats_service.get_submissions(username)
            for sub in submissions:
                print(f"{sub.id}. {sub.title} ({sub.status}) - {sub.runtime}, {sub.memory}")
        else:
            stats = stats_service.get_user_stats(username)
            print(f"Total problems: {stats.total_problems}")
            print(f"Solved problems: {stats.solved_problems}")
            print(f"Acceptance rate: {stats.acceptance_rate}%")
    else:
        parser.print_help()