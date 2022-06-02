from data import Data
import pandas as pd


class GroupEmails(Data):
    def __init__(self):
        super(GroupEmails, self).__init__()
        self.grouped_emails = pd.DataFrame([], dtype=pd.StringDtype())

    def group_emails(self):
        emails_df = pd.DataFrame(self.drop_email_duplicates())
        emails_df["domain"] = emails_df["email"].str.split("@").str[1]

        self.grouped_emails = emails_df.copy(deep=True)
        self.grouped_emails.reset_index(inplace=True)
        self.grouped_emails.set_index(["domain", "email"], inplace=True)
        self.grouped_emails.sort_index(inplace=True)

    def __str__(self):
        domains = list(sorted(set(d for d, _, in self.grouped_emails.index)))

        output = ""
        for domain in domains:

            emails = "\n\t".join(
                self.grouped_emails.loc[domain].reset_index()["email"].values.tolist()
            )
            output += f"Domain {domain} ({len(self.grouped_emails.loc[domain])}) \n\t{emails}\n"

        return output
