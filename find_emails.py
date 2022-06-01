from data import Data
import pandas as pd


class FindEmails(Data):

    def __init__(self, emails_not_in_logs_path):
        super(FindEmails, self).__init__(emails_not_in_logs_path)
        self.emails_not_in_log = pd.Series([], dtype=pd.StringDtype())

    def find_emails_not_in_logs(self):
        self.emails_not_in_log = self.drop_email_duplicates()[~ self.drop_email_duplicates().isin(self.filter_email_logs())].sort_values()

    def count_emails_not_sent(self):
        counted_emails_not_sent = self.emails_not_in_log.count()

        return counted_emails_not_sent

    def __str__(self):
        return f"Emails not sent ({self.count_emails_not_sent()}):\n\t" + '\n\t'.join(self.emails_not_in_log)
