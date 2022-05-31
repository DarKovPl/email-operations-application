from data import Data
import pandas as pd


class SearchEmails(Data):

    def __init__(self, str_phrase):
        super(SearchEmails, self).__init__()
        self.str_phrase = str_phrase
        self.founded_emails = pd.Series([], dtype=pd.StringDtype())

    def search_emails_by_text(self):
        self.founded_emails = self.drop_email_duplicates()[self.drop_email_duplicates().str.contains(self.str_phrase)]

    def count_founded_emails(self):
        number_of_founded_emails = self.founded_emails.count()

        return number_of_founded_emails

    def __str__(self):
        return f"Found emails with '{self.str_phrase}' in email ({self.count_founded_emails()}):\n\t" + '\n\t'.join(self.founded_emails)
