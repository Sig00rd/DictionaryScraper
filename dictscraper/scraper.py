import requests

from src.dictscraper import jmp_page


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

    def print_table_rows(self):
        for row in self.mjp_soup.get_result_table_rows():
            col = row.find_all("td")
            for stuff in col:
                print(stuff.find(text=True))
