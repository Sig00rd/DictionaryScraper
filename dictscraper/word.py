class Word:
    # csv layout: expression - kana - romaji (optional) - meaning(s) - additional info
    def __init__(self):
        self.fields = [] # strings
        self.cells = [] # result table cells scrapped from mjp
        self.additional_info = ""
        self.meanings = []

    def append_field(self, content):
        self.fields.append(content.replace("\n", ""))

    def csv(self):
        if self.is_expression_field_empty():
            self.replace_kana_with_kanji()
        output = str.join(";", self.fields)
        return output

    def append_meanings_field(self, number_list):
        chosen_meanings = []
        for number in number_list:
            chosen_meanings.append(self.meanings[number])
        self.append_field(",".join(chosen_meanings))

    def is_expression_field_empty(self):
        if not self.fields[0]:
            return True
        else:
            return False

    def get_cells(self):
        return self.cells

    def get_writing_and_reading_cells(self):
        return self.cells[0], self.cells[1]

    def get_meanings_and_additional_info_cells(self):
        return self.cells[3], self.cells[4]

    def set_cells(self, cells):
        self.cells = cells

    def set_meanings(self, meanings):
        self.meanings = meanings

    def set_additional_info(self, additional_info):
        self.additional_info = additional_info

    def get_meanings(self):
        return self.meanings

    def replace_kana_with_kanji(self):
            self.fields[0], self.fields[1] = self.fields[1], self.fields[0]


