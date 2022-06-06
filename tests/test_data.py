import os

import pandas as pd
import pytest

from data import Data
from error_handling import FileNotFoundException


@pytest.fixture(name="data")
def fixture_data(tmpdir, monkeypatch):
    data = Data()

    monkeypatch.setattr(data, "folder_for_emails", tmpdir)
    monkeypatch.setattr(
        data, "emails_logs_file_path", os.path.join(tmpdir, "test_log_file.logs")
    )

    yield data
    print("The end of the tests")


def test_data_init(data):
    assert data


def test_folder_for_emails_path(data):
    assert data.folder_for_emails.endswith("tmp_files")


def test_emails_logs_file_path(data):
    assert data.emails_logs_file_path.endswith(
        os.path.join("tmp_files", "test_log_file.logs")
    )


def test_get_email_data_path(data):
    for path in data.get_email_data_path():
        assert path.endswith(("test_emails_file.txt", "test_emails_file.csv"))


def test_get_logs_data_path(data):
    assert data.get_logs_data_path().endswith("test_log_file.logs")


def test_get_logs_data_path_fail(data, monkeypatch):

    monkeypatch.setattr(data, "emails_logs_file_path", "/some/wrong/path")

    with pytest.raises(FileNotFoundException) as e_info:
        data.get_logs_data_path()

    assert str(e_info.value) == (
        "Probably you wrote the wrong file path because this is not a expected logs file. "
        "Check your file path spelling: /some/wrong/path"
    )


def test_filter_emails_logs(data):
    series_from_app = data.filter_email_logs()

    expected_series = pd.Series(
        data=[
            "kyra05@pollich.com",
            "abigayle.davis@jenkins.com",
            "ccrist@yahoo.com",
            "mcglynn.magdalena@yahoo.com",
            "ivy.hodkiewicz@hotmail.com",
            "johnston.vicente@senger.com",
            "cgislason@steuber.com",
            "greenfelder.deangelo@yahoo.com",
            "makenna90@hessel.net",
            "okon.adrianna@hotmail.com",
            "opal69@reynolds.biz",
            "pmayer@leuschke.net",
            "walker.providenci@mcclure.com",
        ],
        name=7,
    )

    pd.testing.assert_series_equal(series_from_app, expected_series)


def test_create_one_emails_dataset(data, merged_expected_series_data):
    series_from_app = data.create_one_emails_dataset()

    pd.testing.assert_series_equal(
        series_from_app, merged_expected_series_data, check_index=False
    )


def test_filter_correct_emails(
    data, merged_expected_series_data, filtered_expected_series_data
):
    series_from_app: pd.Series(bool) = data.filter_correct_emails()
    filtered_series_from_app = merged_expected_series_data[series_from_app]

    pd.testing.assert_series_equal(
        filtered_series_from_app, filtered_expected_series_data, check_index=False
    )


def test_drop_email_duplicates(data):
    series_from_app = data.drop_email_duplicates()

    expected_series = pd.Series(
        data=[
            "walker.providenci@mcclure.com",
            "breilly@yahoo.com",
            "opal69@reynolds.biz",
            "pmayer@leuschke.net",
            "cgislason@steuber.com",
            "greenfelder.deangelo@yahoo.com",
            "makenna90@hessel.net",
            "hill.delmer@hotmail.com",
            "okon.adrianna@hotmail.com",
            "extra_6@oo.c02",
            "extra_7@oo.667"
        ],
        name="email",
    ).sort_values()

    pd.testing.assert_series_equal(series_from_app, expected_series, check_index=False)
