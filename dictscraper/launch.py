import requests

import scraper
import config
from not_found_file import NotFoundFile
import io_utils
import address_constants


def get_html_from_mjp(address):
    result = requests.get(address)
    return result.content


def handle_connection_error(requested_word, stash_file):
    io_utils.print_connection_error_message()
    if config.QUEUE_IF_CONNECTION_ERROR:
        io_utils.print_saving_message(requested_word)
        stash_file.save(word)


scraper = scraper.Scraper()
not_found_file = NotFoundFile()
requested_words = io_utils.get_requested_words_from_user_input()

for word in requested_words:
    address_elements = (address_constants.PRE_WORD, word, address_constants.POST_WORD)
    result_address = "".join(address_elements)

    try:
        result_html = get_html_from_mjp(result_address)
        scraper.build_soup_from_html(result_html)
        scraper.build_word_csvs_from_page()
        scraper.save_user_selected_words()
        scraper.clear_csvs()
    except requests.ConnectionError:
        handle_connection_error(word, not_found_file)
