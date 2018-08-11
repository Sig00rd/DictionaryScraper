import requests

from src.dictscraper import jmp_page
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

    # def print_table_rows(self):
    #     for row in self.mjp_soup.get_result_table_rows():
    #         cells = row.find_all("td")
    #         for cell in cells:
    #             print(cell.find(text=True))

    def build_words_from_page(self):
        # rows = self.mjp_soup.get_result_table_rows()
        # self.build_word_from_row(rows[0])
        rows = self.mjp_soup.get_result_table_rows()
        for row in rows:
            self.build_word_from_row(row)

    def build_word_from_row(self, row):
        cells = row.find_all("td")
        word = Word()
        for index, cell in enumerate(cells):
            if index == 2:
                continue
            content = cell.find(text=True)
            word.append_field(content)
        print(word.csv())
