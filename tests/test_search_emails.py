import os

from search_emails import SearchEmails
import pytest


@pytest.fixture(name="find_emails")
def fixture_group_emails(tmpdir, monkeypatch):
    find_emails = SearchEmails("init_test")

    monkeypatch.setattr(find_emails, "folder_for_emails", tmpdir)
    monkeypatch.setattr(
        find_emails, "emails_logs_file_path", os.path.join(tmpdir, "test_log_file.logs")
    )

    find_emails.search_emails_by_text()

    yield find_emails
    print("The end of the tests")


def test_group_emails_init(find_emails):
    assert find_emails


@pytest.mark.parametrize(
    "phrase, expected",
    [
        ("nn", ["makenna90@hessel.net", "okon.adrianna@hotmail.com"]),
        ("9", ["opal69@reynolds.biz", "makenna90@hessel.net"]),
        (
            "@h",
            [
                "makenna90@hessel.net",
                "hill.delmer@hotmail.com",
                "okon.adrianna@hotmail.com",
            ],
        ),
        (" ", []),
    ],
)
def test_search_emails_by_text(phrase, expected, monkeypatch, tmpdir):
    find_emails_local = SearchEmails(phrase)

    monkeypatch.setattr(find_emails_local, "folder_for_emails", tmpdir)
    monkeypatch.setattr(
        find_emails_local,
        "emails_logs_file_path",
        os.path.join(tmpdir, "test_log_file.logs"),
    )

    find_emails_local.search_emails_by_text()
    founded_emails = find_emails_local.founded_emails.sort_values()

    assert founded_emails.to_list() == sorted(expected)


def test_count_founded_emails(find_emails):
    assert find_emails.count_founded_emails() == 0
