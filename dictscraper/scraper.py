import jmp_page
import io_utils
from cell_parser import MjpRowParser
from word import Word
from file_handler import FileHandler


class Scraper:
    def __init__(self):
        self.mjp_soup = jmp_page.MjpPageSoup()
        self.words = []
        self.word_csvs = []
        self.to_save_numbers = []
        self.file_handler = FileHandler()
        self.cell_parser = MjpRowParser()

    # initial word list has word objects for all words that the dictionary returns,
    # but as it's initial, those word objects only have writing and reading fields
    def build_initial_word_list(self, html):
        self.build_soup_from_html(html)
        self.build_word_cells_from_soup()
        self.build_words_start_from_page()
        self.build_words_start_csvs_from_page()

    def expand_chosen_words(self):
        self.build_chosen_words_array()
        self.build_words_meanings_and_info_from_page()
        self.build_chosen_words_last_fields()

    def reset(self):
        self.words = []
        self.word_csvs = []
        self.to_save_numbers = []

    def build_soup_from_html(self, html):
        self.mjp_soup.build_from_html(html)

    def build_word_cells_from_soup(self):
        result_table_rows = self.mjp_soup.get_result_table_rows()

        for row in result_table_rows:
            cells = row.find_all("td")
            self.append_word_from_cells(cells)

    def append_word_from_cells(self, cell_list):
        word = Word()
        word.set_cells(cell_list)
        self.words.append(word)

    def build_words_start_from_page(self):
        for word in self.words:
            writing_cell, reading_cell = word.get_writing_and_reading_cells()
            word.append_field(self.cell_parser.parse_writing_reading_or_info(writing_cell))
            word.append_field(self.cell_parser.parse_writing_reading_or_info(reading_cell))

    def build_words_start_csvs_from_page(self):
        for word in self.words:
            self.word_csvs.append(word.csv())

    def get_user_to_choose_words(self):
        io_utils.print_words_or_meanings("Znalezione słowa: ", self.word_csvs)
        to_save_numbers = io_utils.get_word_numbers_from_user_input()
        self.to_save_numbers = to_save_numbers

    def build_chosen_words_array(self):
        self.words = [self.words[number] for number in self.to_save_numbers]

    def build_words_meanings_and_info_from_page(self):
        for word in self.words:
            meanings, additional_info = word.get_meanings_and_additional_info_cells()
            word.set_meanings(self.cell_parser.parse_meanings(meanings))
            word.set_additional_info(self.cell_parser.parse_writing_reading_or_info(additional_info))

    def set_to_save_numbers(self, numbers):
        self.to_save_numbers = numbers

    def build_chosen_words_csvs(self):
        for number in self.to_save_numbers:
            csv_to_append = self.words[number].csv()
            self.word_csvs.append(csv_to_append)

    def cut_numbers_bigger_than_words_list_size(self):
        for number in self.to_save_numbers:
            if number >= len(self.word_csvs):
                self.to_save_numbers.remove(number)

    def save_user_selected_words(self):
        for word in self.words:
            self.append_word_to_file(word)

    def append_word_to_file(self, word):
        csv = word.csv()
        self.file_handler.append_to_file(csv)

    def get_word_csvs(self):
        return self.word_csvs

    def meanings_writings_indexes(self):
        for index, word in enumerate(self.words):
            yield word.get_meanings(), word.csv(), index

    def build_word_last_fields(self, word_index, meanings_to_save_numbers):
        word = self.words[word_index]
        word.append_meanings_field(meanings_to_save_numbers)
        word.append_additional_info()
