import sys

sys.tracebacklimit = 0


class FileNotFoundException(Exception):
    def __init__(self, user_path):
        self.file_not_found_message = (
            f"Probably you wrote the wrong file path because this is not a expected logs file. "
            f"Check your file path spelling: {user_path}"
        )

    def __str__(self):
        return self.file_not_found_message
