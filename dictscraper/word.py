class Word:
    # csv layout: kanji - kana - meaning - additional info
    def __init__(self, *args):
        self.fields = []
        for arg in args:
            self.fields.append(arg)

    def append_field(self, content):
        self.fields.append(content.replace("\n", ""))

    def csv(self):
        if self.is_kanji_field_empty():
            self.replace_kana_with_kanji()
        output = str.join(";", self.fields)
        return output

    def is_kanji_field_empty(self):
        if not self.fields[0]:
            return 1
        else:
            return 2

    def replace_kana_with_kanji(self):
            self.fields[0], self.fields[1] = self.fields[1], self.fields[0]


