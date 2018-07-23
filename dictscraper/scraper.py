import bs4
import requests


class Scraper:
    def get_html_from_mjp(self, address):
        result = requests.get(address)
        return result.content