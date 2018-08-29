import os.path
import config


class FileHandler:
    def __init__(self):
        home_directory_path = os.path.expanduser("~")
        self.file_path = os.path.join(home_directory_path, config.CSV_FILE_PATH)
        self.file = open(self.file_path, "a+")
        self.file_empty = self.is_file_empty()

    def __del__(self):
        self.file.close()

    def is_file_empty(self):
        if os.path.getsize(self.file_path) > 0:
            return False
        return True

    def append_to_file(self, string_to_append):
        if self.file_empty:
            self.file.write(string_to_append)
            self.file_empty = False

        else:
            self.file.write("\n" + string_to_append)
