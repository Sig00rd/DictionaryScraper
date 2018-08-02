import bs4


class MjpPageSoup:
    def __init__(self):
        self.content = bs4.BeautifulSoup("", "html.parser")

    def build_from_html(self, scrapped_html):
        self.content = bs4.BeautifulSoup(scrapped_html, 'html.parser')

    def prettify(self):
        self.content.prettify()

    def get_content(self):
        return self.content
