from incorrect_emails import IncorrectEmails
from search_emails import SearchEmails
from group_emails import GroupEmails
from find_emails import FindEmails

import argparse
import sys


def incorrect_emails():
    wrong_emails = IncorrectEmails()
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
    parser = argparse.ArgumentParser()

    parser.add_argument('-ic', '--incorrect-emails', action='store_true', help='give argument')
    parser.add_argument('-s', '--search', action='store', type=str, help='sjnjs')
    parser.add_argument('-gbd', '--group-by-domain', action='store_true')
    parser.add_argument('-feil', '--find-emails-not-in-logs', action='store', type=str)

    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])

    if args.incorrect_emails:
        incorrect_emails()

    elif args.search:
        search_emails(args.search)

    elif args.group_by_domain:
        group_emails()

    elif args.find_emails_not_in_logs:
        find_emails_not_in_logs(args.find_emails_not_in_logs)
