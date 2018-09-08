import jmp_page
import io_utils
import config
from cell_parser import MjpRowParser
from word import Word
from file_handler import FileHandler


class Scraper:
    def __init__(self):
        self.mjp_soup = jmp_page.MjpPageSoup()
        self.words = []
        self.chosen_words = []
        self.word_csvs = []
        self.to_save_numbers = []
        self.file_handler = FileHandler()
        self.cell_parser = MjpRowParser()

    def build_soup_from_html(self, html):
        self.mjp_soup.build_from_html(html)

    def reset(self):
        self.word_csvs = []
        self.chosen_words = []
        self.word_csvs = []
        self.to_save_numbers = []

    def build_word_cells_from_soup(self):
        result_table_rows = self.mjp_soup.get_result_table_rows()

        for row in result_table_rows:
            cells = row.find_all("td")
            word = Word()
            word.set_cells(cells)
            self.words.append(word)

    def build_words_start_from_page(self):
        for word in self.words:
            writing_cell, reading_cell = word.get_writing_and_reading_cells()
            word.append_field(self.cell_parser.parse_writing_reading_or_info(writing_cell))
            word.append_field(self.cell_parser.parse_writing_reading_or_info(reading_cell))

    def build_chosen_words_array(self):
        self.chosen_words = [self.words[number] for number in self.to_save_numbers]

    def build_words_meanings_and_info_from_page(self):
        chosen_words = [self.words[number] for number in self.to_save_numbers]

        for word in chosen_words:
            meanings, additional_info = word.get_meanings_and_additional_info_cells()
            word.set_meanings(self.cell_parser.parse_meanings(meanings))
            word.set_additional_info(self.cell_parser.parse_writing_reading_or_info(additional_info))

    def build_chosen_words_last_fields(self):
        for word in self.chosen_words:
            meanings_to_save_numbers = self.let_user_choose_words_meanings(word)
            word.append_meanings_field(meanings_to_save_numbers)
            word.append_field(word.additional_info)

    def let_user_choose_words_meanings(self, word):
        writing_and_meaning = word.csv()
        io_utils.print_words_or_meanings(writing_and_meaning, word.meanings)
        meanings_to_save_numbers = io_utils.get_meaning_numbers_from_user_input()
        return meanings_to_save_numbers

    def build_words_start_csvs_from_page(self):
        for word in self.words:
            self.word_csvs.append(word.csv())

    def build_chosen_words_cvs(self):
        for number in self.to_save_numbers:
            csv_to_append = self.words[number].csv()
            self.word_csvs.append(csv_to_append)

    # def parse_row_to_word(self, row):
    #     cells = row.find_all("td")
    #     self.cell_parser.build_from_cell_list(cells)
    #     word = Word()
    #     for i in range(5):
    #         content = self.cell_parser.parse_cell_to_string()
    #         word.append_field(content)
    #         self.cell_parser.increment()
    #     return word

    # def save_user_selected_words(self):
    #     self.present_words_to_user()
    #     word_numbers = self.get_desired_words_numbers_from_user()
    #     valid_numbers = self.cut_numbers_bigger_than_words_list_size(word_numbers)
    #     for number in valid_numbers:
    #         self.append_word_to_file(number)

    def save_user_selected_words(self):
        for word in self.chosen_words:
            self.append_word_to_file(word)
        # for number in self.to_save_numbers:
        #     self.append_word_to_file(number)

    def get_user_to_choose_words(self):
        io_utils.print_words_or_meanings("Znalezione słowa: ", self.word_csvs)
        to_save_numbers = self.get_desired_words_numbers_from_user()
        self.to_save_numbers = to_save_numbers

    # def present_words_to_user(self):
    #     io_utils.print_words_or_meanings("", self.word_csvs)

    def get_desired_words_numbers_from_user(self):
        return io_utils.get_word_numbers_from_user_input()

    def cut_numbers_bigger_than_words_list_size(self, numbers):
        for number in numbers:
            if number >= len(self.word_csvs):
                numbers.remove(number)
        return numbers

    # def append_word_to_file(self, word_number):
    #     word_to_append = self.word_csvs[word_number]
    #     self.file_handler.append_to_file(word_to_append)

    def append_word_to_file(self, word):
        csv = word.csv()
        self.file_handler.append_to_file(csv)
