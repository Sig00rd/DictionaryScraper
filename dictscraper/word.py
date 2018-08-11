class Word:
    def __init__(self, *args):
        self.fields = []
        for arg in args:
            self.fields.append(arg)

    def append_field(self, content):
        # print(content)
        # print(content.replace("\n", ""))
        self.fields.append(content.replace("\n", ""))
        # self.fields.append(content)

    def csv(self):
        if self.is_kanji_field_empty:
            self.insert_kana_as_kanji()
        output = str.join("; ", self.fields)
        return output

    def is_kanji_field_empty(self):
        if not self.fields[0] and self.fields[1]:
            return 1
        else:
            return 0

    def insert_kana_as_kanji(self):
            self.fields[0], self.fields[1] = self.fields[1], self.fields[0]


