import requests

from src.dictscraper import jmp_page
from src.dictscraper import config
from src.dictscraper.word import Word


class Scraper:
    def __init__(self):
        self.address = ""
        self.mjp_soup = jmp_page.MjpPageSoup()

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
            self.build_word_from_row(row)

    def build_word_from_row(self, row):
        cells = row.find_all("td")
        word = Word()
        for index, cell in enumerate(cells):
            if index == 2 and not config.INCLUDE_ROMAJI:
                continue
            elif index == 2:
                romaji = cell.find_all(text=True)
                content = "".join(romaji)
            elif index == 3:
                meanings = cell.find_all(text=True)
                if config.MEANING_LIMIT:
                    meanings = meanings[:config.MEANING_LIMIT]
                content = ", ".join(meanings)
            else:
                content = cell.find(text=True)
            word.append_field(content)
        print(word.csv())