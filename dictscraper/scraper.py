import requests

from src.dictscraper import jmp_page
from src.dictscraper.cell_parser import MjpRowParser
from src.dictscraper.word import Word


class Scraper:
    def __init__(self):
        self.address = ""
        self.mjp_soup = jmp_page.MjpPageSoup()
        self.words = []

    def set_address(self, _address):
        self.address = _address

    def get_html_from_mjp(self):
        result = requests.get(self.address)
        return result.content

    def do_magic(self):
        html = self.get_html_from_mjp()
        self.mjp_soup.build_from_html(html)

    def print_pretty_page_content(self):
        self.mjp_soup.prettify()
        print(self.mjp_soup.soup)

    def build_words_from_page(self):
        rows = self.mjp_soup.get_result_table_rows()
        for row in rows:
            word = self.parse_row_to_word(row)
            self.words.append(word)

    def parse_row_to_word(self, row):
        cells = row.find_all("td")
        cell_parser = MjpRowParser()
        cell_parser.build_from_cell_list(cells)
        word = Word()
        for i in range(5):
            content = cell_parser.parse_cell_to_string()
            word.append_field(content)
            cell_parser.increment()

        print(word.csv())
        return word
