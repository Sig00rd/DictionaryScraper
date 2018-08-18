import os.path
from src.dictscraper import config

class FileHandler:
    def __init__(self):
        home_directory_path = os.path.expanduser("~")
        print(home_directory_path)
        self.file_path = os.path.join(home_directory_path, config.CSV_FILE_PATH)
