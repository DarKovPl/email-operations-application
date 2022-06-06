import os

import pandas as pd

from group_emails import GroupEmails
import pytest


@pytest.fixture(name="group_emails")
def fixture_group_emails(tmpdir, monkeypatch):
    group_emails = GroupEmails()

    monkeypatch.setattr(group_emails, "folder_for_emails", tmpdir)
    monkeypatch.setattr(
        group_emails,
        "emails_logs_file_path",
        os.path.join(tmpdir, "test_log_file.logs"),
    )

    group_emails.group_emails()

    yield group_emails
    print("The end of the tests")


def test_group_emails_init(group_emails):
    assert group_emails


def test_group_emails(group_emails):
    frame_from_app = group_emails.grouped_emails

    multi_index = pd.DataFrame(
        [
            ["hessel.net", "makenna90@hessel.net"],
            ["hotmail.com", "hill.delmer@hotmail.com"],
            ["hotmail.com", "okon.adrianna@hotmail.com"],
            ["leuschke.net", "pmayer@leuschke.net"],
            ["mcclure.com", "walker.providenci@mcclure.com"],
            ["oo.667", "extra_7@oo.667"],
            ["oo.c02", "extra_6@oo.c02"],
            ["reynolds.biz", "opal69@reynolds.biz"],
            ["steuber.com", "cgislason@steuber.com"],
            ["yahoo.com", "breilly@yahoo.com"],
            ["yahoo.com", "greenfelder.deangelo@yahoo.com"],
        ],
        columns=["domain", "email"],
    )
    expected_frame = pd.DataFrame(
        index=pd.MultiIndex.from_frame(multi_index),
        columns=["index"],
        data=[3, 4, 5, 17, 12, 28, 27, 16, 0, 14, 2],
    )

    pd.testing.assert_frame_equal(frame_from_app, expected_frame)
