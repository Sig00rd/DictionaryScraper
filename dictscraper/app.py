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

    def get_requested_expressions(self):
        self.requested_expressions = io_utils.get_requested_expressions_from_user_input()

    def run(self):
        for expression in self.requested_expressions:
            address_elements = (address_constants.PRE_WORD, expression, address_constants.POST_WORD)
            result_address = "".join(address_elements)

            try:
                result_html = self.get_html_from_mjp(result_address)
                self.scraper.build_soup_from_html(result_html)
                self.scraper.build_word_list()
                self.scraper.get_user_to_choose_words()
                self.scraper.expand_chosen_words()
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

    # for expression in requested_expressions:
    #     address_elements = (address_constants.PRE_WORD, expression, address_constants.POST_WORD)
    #     result_address = "".join(address_elements)
