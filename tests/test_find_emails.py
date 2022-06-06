import os

import pandas as pd
from find_emails import FindEmails

import pytest


@pytest.fixture(name="find_emails")
def fixture_find_emails(tmpdir, monkeypatch):
    find_emails = FindEmails("ll")

    monkeypatch.setattr(find_emails, "folder_for_emails", tmpdir)
    monkeypatch.setattr(
        find_emails, "emails_logs_file_path", os.path.join(tmpdir, "test_log_file.logs")
    )

    find_emails.find_emails_not_in_logs()

    yield find_emails
    print("The end of the tests")


def test_find_emails_init(find_emails):
    assert find_emails


def test_find_emails_not_in_logs(find_emails):
    series_from_app = find_emails.emails_not_in_log

    expected_series = pd.Series(
        data=["hill.delmer@hotmail.com", "breilly@yahoo.com", "extra_6@oo.c02", "extra_7@oo.667"], name="email"
    ).sort_values()

    pd.testing.assert_series_equal(series_from_app, expected_series, check_index=False)


def test_count_emails_not_sent(find_emails):
    assert find_emails.count_emails_not_sent() == 4
