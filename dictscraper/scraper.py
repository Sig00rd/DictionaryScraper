import requests

from src.dictscraper import jmp_page


class Scraper:
    def __init__(self):
        self.address = ""
        self.soup = jmp_page.MjpPageSoup()

    def set_address(self, _address):
        self.address = _address

    def get_html_from_mjp(self):
        result = requests.get(self.address)
        return result.content

    def do_magic(self):
        html = self.get_html_from_mjp()
        self.soup.build_from_html(html)

    def print_pretty_page_content(self):
        self.soup.prettify()
        print(self.soup.content)

