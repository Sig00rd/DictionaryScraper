import bs4


class MjpPageSoup:
    def __init__(self):
        self.soup = bs4.BeautifulSoup("", "html.parser")

    def build_from_html(self, scrapped_html):
        self.soup = bs4.BeautifulSoup(scrapped_html, "html.parser")

    def find_result_table_in_soup(self):
        result_table = self.soup.find(
            "table", {"id": "wordDictionaryFindWordResult"})
        return result_table

    def get_content(self):
        return self.soup

    def get_result_table_rows(self):
        result_table = self.find_result_table_in_soup()
        result_table_body = result_table.find("tfood")
        result_table_rows = result_table_body.find_all("tr")
        return result_table_rows




