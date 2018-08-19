from src.dictscraper import scraper
from src.dictscraper import io_utils
from src.dictscraper import address_constants

scraper = scraper.Scraper()
requested_words = io_utils.get_requested_words_from_user_input()

for word in requested_words:
    address_elements = (address_constants.PRE_WORD, word, address_constants.POST_WORD)
    address = "".join(address_elements)
    scraper.set_address(address)
# scraper.print_pretty_page_content()
    scraper.build_soup_from_html()
    scraper.build_word_csvs_from_page()
    scraper.save_user_selected_words()
    scraper.clear_csvs()
