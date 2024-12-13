import argparse
from .authentication.login import login
from .authentication.logout import logout

def main():
    parser = argparse.ArgumentParser(description='LeetCode CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Login command
    subparsers.add_parser('login', help='Login to LeetCode')

    # Logout command
    subparsers.add_parser('logout', help='Logout of LeetCode')

    args = parser.parse_args()

    if args.command == 'login':
        login()
    elif args.command == 'logout':
        logout()
    else:
        parser.print_help()