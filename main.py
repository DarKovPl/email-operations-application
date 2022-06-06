import os.path

from incorrect_emails import IncorrectEmailsAddresses
from search_emails import SearchEmails
from group_emails import GroupEmails
from find_emails import FindEmails

import argparse
import sys


def incorrect_emails():
    wrong_emails = IncorrectEmailsAddresses()
    wrong_emails.search_incorrect_emails()
    print(wrong_emails.__str__())


def search_emails(str_phrase):
    founded_emails = SearchEmails(str_phrase)
    founded_emails.search_emails_by_text()
    print(founded_emails.__str__())


def group_emails():
    grouped_emails = GroupEmails()
    grouped_emails.group_emails()
    print(grouped_emails.__str__())


def find_emails_not_in_logs(path):
    not_in_log = FindEmails(path)
    not_in_log.find_emails_not_in_logs()
    print(not_in_log.__str__())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="In a Docker container the main.py file is run automatically, "
                    "and you have to write only parameters that you want to launch. "
                    "Example app usage: docker run interapp --incorrect-emails; "
                    "Example test mode usage: docker run --entrypoint pytest -vv interapp"
    )

    parser.add_argument(
        "-ic", "--incorrect-emails", action="store_true", help="Show incorrect emails."
    )
    parser.add_argument(
        "-s",
        "--search",
        action="store",
        type=str,
        metavar="[Write phrase of searching emails addresses]",
        help="Search emails by phrase.",
    )
    parser.add_argument(
        "-gbd", "--group-by-domain", action="store_true", help="Group emails by domain."
    )

    parser.add_argument(
        "-feil",
        "--find-emails-not-in-logs",
        type=str,
        metavar="Write a path to logs file",
        nargs='?',
        const=str(os.path.join('files', 'email-sent.logs')),
        help="Find emails that are not in the logs file. "
             "There is a set path by default, but you can write your own path to a .logs file.",
    )

    args = parser.parse_args(args=None if sys.argv[1:] else ["--help"])

    if args.incorrect_emails:
        incorrect_emails()

    elif args.search:
        search_emails(args.search)

    elif args.group_by_domain:
        group_emails()

    elif args.find_emails_not_in_logs:
        find_emails_not_in_logs(args.find_emails_not_in_logs)
