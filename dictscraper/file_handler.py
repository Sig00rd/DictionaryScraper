import os.path
import config


class FileHandler:
    def __init__(self):
        home_directory_path = os.path.expanduser("~")
        self.file_path = os.path.join(home_directory_path, config.CSV_FILE_PATH)
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def append_to_file(self, string_to_append):
        self.file.write(string_to_append + "\n")
