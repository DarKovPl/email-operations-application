from data import Data
import pandas as pd


class IncorrectEmails(Data):

    def __init__(self):
        super(IncorrectEmails, self).__init__()
        self.incorrect_emails = pd.Series([], dtype=pd.StringDtype())

    def search_incorrect_emails(self):
        self.incorrect_emails = self.create_one_emails_dataset()[~self.filter_correct_emails()]

    def count_incorrect_emails(self) -> int:
        number_of_incorrect_emails = self.incorrect_emails.count()

        return number_of_incorrect_emails

    def __str__(self):
        return f"Invalid emails ({self.count_incorrect_emails()}):\n\t" + '\n\t'.join(self.incorrect_emails)
