import bs4


class MjpPageSoup:
    def __init__(self):
        self.content = bs4.BeautifulSoup()

    def build_from_html(self, scrapped_html):
        html = scrapped_html
        self.content = bs4.BeautifulSoup(html, 'html.parser')

    def prettify(self):
        self.content.prettify()