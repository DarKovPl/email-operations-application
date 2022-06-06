import os

import pandas as pd

from incorrect_emails import IncorrectEmailsAddresses
import pytest


@pytest.fixture(name="wrong_addresses")
def fixture_incorrect_emails(tmpdir, monkeypatch):
    wrong_addresses = IncorrectEmailsAddresses()

    monkeypatch.setattr(wrong_addresses, "folder_for_emails", tmpdir)
    monkeypatch.setattr(
        wrong_addresses,
        "emails_logs_file_path",
        os.path.join(tmpdir, "test_log_file.logs"),
    )

    wrong_addresses.search_incorrect_emails()

    yield wrong_addresses
    print("The end of the tests")


def test_incorrect_emails_init(wrong_addresses):
    assert wrong_addresses


def test_search_incorrect_emails(wrong_addresses):
    series_from_app = wrong_addresses.incorrect_emails_addresses.sort_values()

    expected_series = pd.Series(
        [
            ".com",
            "com",
            "@hegmann.info",
            "nernserhickle.biz",
            "brad84gmail.com",
            "yahoo.com",
            "com",
            "com",
            "wyman.com",
            "ynolanjones.com",
            "extra@.com",
            "extra_1@o.commm",
            "extra_2@oo.^o^",
            "extra_3@@oo.com",
            "extra@5@oo.com",
            "extra_8@oo."
        ],
        name="email",
    ).sort_values()

    pd.testing.assert_series_equal(series_from_app, expected_series, check_index=False)


def test_count_incorrect_emails(wrong_addresses):
    assert wrong_addresses.count_incorrect_emails() == 16
