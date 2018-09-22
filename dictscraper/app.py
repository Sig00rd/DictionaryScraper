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
            self.scraper.scrap_to_csv(result_html)

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
