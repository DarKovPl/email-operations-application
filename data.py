import os
import pandas as pd
import re as regex


class Data:

    def __init__(self, emails_not_in_logs_path=None):

        self.folder_path = ["files", "emails"]
        self.folder_for_emails = os.path.join(os.getcwd(), *self.folder_path)
        self.emails_not_in_logs_path = emails_not_in_logs_path
        self.correct_email_pattern: str = '[0-9a-zA-Z._%+-]+@[0-9a-zA-Z.-]+\\.[A-Za-z]{2,4}'

    def get_email_data_path(self) -> list:
        files_paths: list = []
        for file in os.listdir(self.folder_for_emails):

            if file.endswith(('.txt', '.csv')):
                file_path = os.path.join(self.folder_for_emails, file)
                files_paths.append(file_path)
        return files_paths

    def get_logs_data_path(self) -> str: ##### try except
        file_path = self.emails_not_in_logs_path
        return file_path

    def filter_email_logs(self):
        logs = pd.read_csv(self.get_logs_data_path(), delimiter=' ', header=None)
        logs = logs[[7]].squeeze()
        logs = logs.str.strip("'")

        return logs

    def create_one_emails_dataset(self) -> pd.Series:
        emails = [
            pd.read_csv(file, names=['email']) if file.endswith('.txt') else pd.read_csv(file, sep=';',
                                                                                         usecols=['email']) for file in
            self.get_email_data_path()]

        emails_df: pd.DataFrame = pd.concat(emails)
        emails_df.reset_index(drop=True, inplace=True)
        merged_emails = emails_df.squeeze()
        return merged_emails

    def filter_correct_emails(self) -> pd.Series:
        correct_emails = self.create_one_emails_dataset().map(
            lambda x: bool(regex.match(self.correct_email_pattern, x)))

        return correct_emails

    def drop_email_duplicates(self) -> pd.Series:
        no_duplicated_correct_emails = self.create_one_emails_dataset()[self.filter_correct_emails()].drop_duplicates()

        return no_duplicated_correct_emails
