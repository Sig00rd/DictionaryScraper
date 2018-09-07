import config


class MjpRowParser:
    def __init__(self):
        self.current_column = 0
        self.cells = []
        self.meanings = []
        self.INCLUDE_ROMAJI = config.INCLUDE_ROMAJI
        self.MEANING_LIMIT = config.MEANING_LIMIT
        self.LAZY_MEANINGS = config.LAZY_MEANINGS

    def build_from_cell_list(self, cell_list):
        self.cells = cell_list
        self.current_column = 0

    def increment(self):
        self.current_column += 1

    def parse_cell_to_string(self):
        cell = self.cells[self.current_column]

        if self.at_romaji_column():
            if self.is_romaji_enabled():
                romaji = cell.find_all(text=True)
                content = "".join(romaji)
            else:
                content = ""

        elif self.at_meaning_column():
            content = self.handle_meaning_column(cell)

        else:
            content = cell.find(text=True)

        return content

    def handle_meaning_column(self, cell):
        self.meanings = cell.find_all(text=True)
        if self.is_meaning_limit_set():
            self.cut_meanings_above_limit()
        else:
            self.let_user_choose_meanings()

        content = ", ".join(self.meanings)
        return content

    def let_user_choose_meanings(self):
        pass

    def cut_meanings_above_limit(self):
        self.meanings = self.meanings[:self.MEANING_LIMIT]

    def at_romaji_column(self):
        if self.current_column == 2:
            return True
        return False

    def at_meaning_column(self):
        if self.current_column == 3:
            return True
        return False

    def is_romaji_enabled(self):
        if self.INCLUDE_ROMAJI:
            return True
        return False

    def is_meaning_limit_set(self):
        if self.MEANING_LIMIT and self.LAZY_MEANINGS:
            return True
        return False
