import pytest
import pandas as pd
from data import Data


@pytest.fixture
def tmpdir(tmpdir):
    tmp_dir = tmpdir.mkdir("tmp_files")

    log_file = tmp_dir.join("test_log_file.logs")
    log_file.write(
        "[2022-05-16 10:04:10]: Email has been sent to 'kyra05@pollich.com'\n"
        "[2022-05-16 10:04:44]: Email has been sent to 'abigayle.davis@jenkins.com'\n"
        "[2022-05-16 10:05:08]: Email has been sent to 'ccrist@yahoo.com'\n"
        "[2022-05-16 10:05:41]: Email has been sent to 'mcglynn.magdalena@yahoo.com'\n"
        "[2022-05-16 10:06:24]: Email has been sent to 'ivy.hodkiewicz@hotmail.com'\n"
        "[2022-05-16 10:07:14]: Email has been sent to 'johnston.vicente@senger.com'\n"
        "[2022-05-16 10:46:59]: Email has been sent to 'cgislason@steuber.com'\n"
        "[2022-05-16 15:24:04]: Email has been sent to 'greenfelder.deangelo@yahoo.com'\n"
        "[2022-05-16 14:54:00]: Email has been sent to 'makenna90@hessel.net'\n"
        "[2022-05-16 14:03:06]: Email has been sent to 'okon.adrianna@hotmail.com'\n"
        "[2022-05-16 15:05:49]: Email has been sent to 'opal69@reynolds.biz'\n"
        "[2022-05-16 10:15:40]: Email has been sent to 'pmayer@leuschke.net'\n"
        "[2022-05-16 16:37:35]: Email has been sent to 'walker.providenci@mcclure.com'"
    )

    f_1 = tmp_dir.join("test_emails_file.txt")
    f_1.write(
        ".com\n"
        "com\n"
        "@hegmann.info\n"
        "nernserhickle.biz\n"
        "walker.providenci@mcclure.com\n"
        "walker.providenci@mcclure.com\n"
        "walker.providenci@mcclure.com\n"
        "brad84gmail.com\n"
        "breilly@yahoo.com\n"
        "yahoo.com\n"
        "opal69@reynolds.biz\n"
        "pmayer@leuschke.net\n"
        "com\n"
        "com\n"
        "wyman.com\n"
        "ynolanjones.com\n"
        "extra@.com\n"
        "extra_1@o.commm\n"
        "extra_2@oo.^o^\n"
        "extra_3@@oo.com\n"
        "extra@5@oo.com\n"
        "e*tra_6@oo.c02"
    )

    f_2 = tmp_dir.join("test_emails_file.csv")
    f_2.write(
        "username;email\n"
        "cgislason;cgislason@steuber.com\n"
        "greenfelder;greenfelder.deangelo@yahoo.com\n"
        "greenfelder;greenfelder.deangelo@yahoo.com\n"
        "makenna90;makenna90@hessel.net\n"
        "hill;hill.delmer@hotmail.com\n"
        "okon;okon.adrianna@hotmail.com"
    )

    f_3 = tmp_dir.join("test_emails_file.img")
    f_3.write("")

    f_4 = tmp_dir.join("test_emails_file.xxx")
    f_4.write("")

    str_dir = str(tmp_dir)

    return str_dir


@pytest.fixture
def merged_expected_series_data():
    expected_series = pd.Series(
        data=[
            "cgislason@steuber.com",
            "greenfelder.deangelo@yahoo.com",
            "greenfelder.deangelo@yahoo.com",
            "makenna90@hessel.net",
            "hill.delmer@hotmail.com",
            "okon.adrianna@hotmail.com",
            ".com",
            "com",
            "@hegmann.info",
            "nernserhickle.biz",
            "walker.providenci@mcclure.com",
            "walker.providenci@mcclure.com",
            "walker.providenci@mcclure.com",
            "brad84gmail.com",
            "breilly@yahoo.com",
            "yahoo.com",
            "opal69@reynolds.biz",
            "pmayer@leuschke.net",
            "com",
            "com",
            "wyman.com",
            "ynolanjones.com",
            "extra@.com",
            "extra_1@o.commm",
            "extra_2@oo.^o^",
            "extra_3@@oo.com",
            "extra@5@oo.com",
            "e*tra_6@oo.c02",
        ],
        name="email",
    ).sort_values()

    return expected_series


@pytest.fixture
def filtered_expected_series_data():
    expected_series = pd.Series(
        data=[
            "walker.providenci@mcclure.com",
            "walker.providenci@mcclure.com",
            "walker.providenci@mcclure.com",
            "breilly@yahoo.com",
            "opal69@reynolds.biz",
            "pmayer@leuschke.net",
            "cgislason@steuber.com",
            "greenfelder.deangelo@yahoo.com",
            "greenfelder.deangelo@yahoo.com",
            "makenna90@hessel.net",
            "hill.delmer@hotmail.com",
            "okon.adrianna@hotmail.com",
        ],
        name="email",
    ).sort_values()

    return expected_series
