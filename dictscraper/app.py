import requests

from scraper import Scraper
from resources import config
from not_found_file import NotFoundFile
import io_utils
import address_constants


class App:
    def __init__(self):
        self.scraper = Scraper()
        self.not_found_file = NotFoundFile()
        self.requested_expressions = []

    def build_requested_expressions(self):
        self.requested_expressions = io_utils.get_requested_expressions_from_user_input()

    def run(self):
        self.build_requested_expressions()

        for expression in self.requested_expressions:
            self.handle_expression(expression)

    def handle_expression(self, expression):
        address_elements = (address_constants.PRE_WORD, expression, address_constants.POST_WORD)
        result_address = "".join(address_elements)

        try:
            result_html = self.get_html_from_mjp(result_address)
            self.scraper.build_initial_word_list(result_html)
            writings_and_meanings = self.scraper.get_word_csvs()
            words_to_save_numbers = io_utils.get_numbers_of_words_to_save_from_user(writings_and_meanings)
            self.scraper.set_to_save_numbers(words_to_save_numbers)
            self.scraper.build_chosen_words_array()
            self.scraper.build_words_meanings_and_info_from_page()
            for meanings, writing, index in self.scraper.meanings_writings_indexes():
                meanings_to_save_numbers = self.ask_user_to_choose_meanings(writing, meanings)
                self.scraper.build_word_last_fields(index, meanings_to_save_numbers)
            self.scraper.save_user_selected_words()
            self.scraper.reset()

        except requests.ConnectionError:
            self.handle_connection_error(expression)

    def get_html_from_mjp(self, address):
        result = requests.get(address)
        return result.content

    def handle_connection_error(self, requested_word):
        io_utils.print_connection_error_message()
        if config.QUEUE_IF_CONNECTION_ERROR:
            io_utils.print_saving_message(requested_word)
            self.not_found_file.save(requested_word)

    def ask_user_to_choose_meanings(self, word_writing, meaning_list):
        prompt = "Proszę wybrać znaczenia słowa  " + word_writing + "  do zapisu: "
        io_utils.print_words_or_meanings(prompt, meaning_list)
        numbers_to_save = io_utils.get_word_numbers_from_user_input()
        return io_utils.cut_numbers_above_list_size(numbers_to_save, meaning_list)

