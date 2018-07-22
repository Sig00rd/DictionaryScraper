class Word:
    def __init__(self, *args):
        self.fields = []

        for arg in args:
            self.fields.append(arg)

    def csv(self):
        output = str.join("; ", self.fields)

        return output


