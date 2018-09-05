import requests

import jmp_page
import io_utils
from cell_parser import MjpRowParser
from word import Word
from file_handler import FileHandler


class Scraper:
    def __init__(self):
        self.address = ""
        self.mjp_soup = jmp_page.MjpPageSoup()
        self.word_csvs = []
        self.file_handler = FileHandler()
        self.cell_parser = MjpRowParser()

    def set_address(self, _address):
        self.address = _address

    def get_html_from_mjp(self):
        result = requests.get(self.address)
        return result.content

    def build_soup_from_html(self):
        html = self.get_html_from_mjp()
        self.mjp_soup.build_from_html(html)

    def print_pretty_page_content(self):
        self.mjp_soup.prettify()
        print(self.mjp_soup.soup)

    def clear_csvs(self):
        self.word_csvs = []

    def build_word_csvs_from_page(self):
        rows = self.mjp_soup.get_result_table_rows()
        for row in rows:
            word = self.parse_row_to_word(row)
            self.word_csvs.append(word.csv())

    def parse_row_to_word(self, row):
        cells = row.find_all("td")
        self.cell_parser.build_from_cell_list(cells)
        word = Word()
        for i in range(5):
            content = self.cell_parser.parse_cell_to_string()
            word.append_field(content)
            self.cell_parser.increment()
        return word

    def save_user_selected_words(self):
        self.present_words_to_user()
        word_numbers = self.get_desired_words_numbers_from_user()
        valid_numbers = self.cut_numbers_bigger_than_words_list_size(word_numbers)
        for number in valid_numbers:
            self.append_word_to_file(number)

    def present_words_to_user(self):
        io_utils.print_words(self.word_csvs)

    def get_desired_words_numbers_from_user(self):
        return io_utils.get_word_numbers_from_user_input()

    def cut_numbers_bigger_than_words_list_size(self, numbers):
        for number in numbers:
            if number >= len(self.word_csvs):
                numbers.remove(number)
        return numbers

    def append_word_to_file(self, word_number):
        word_to_append = self.word_csvs[word_number]
        self.file_handler.append_to_file(word_to_append)
