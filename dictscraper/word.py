class Word:
    # csv layout: kanji - kana - romaji (optional) - meaning(s) - additional info
    def __init__(self):
        self.fields = [] # strings
        self.cells = [] # result table cells scrapped from mjp

    def append_field(self, content):
        self.fields.append(content.replace("\n", ""))

    def csv(self):
        if self.is_kanji_field_empty():
            self.replace_kana_with_kanji()
        output = str.join(";", self.fields)
        return output

    def is_kanji_field_empty(self):
        if not self.fields[0]:
            return True
        else:
            return False

    def get_cells(self):
        return self.cells

    def set_cells(self, cells):
        self.cells = cells

    def replace_kana_with_kanji(self):
            self.fields[0], self.fields[1] = self.fields[1], self.fields[0]


