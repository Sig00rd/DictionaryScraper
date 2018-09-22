from resources import config

class MjpRowParser:
    def __init__(self):
        self.INCLUDE_ROMAJI = config.INCLUDE_ROMAJI
        self.MEANING_LIMIT = config.MEANING_LIMIT
        self.LAZY_MEANINGS = config.LAZY_MEANINGS

    def parse_writing_reading_or_info(self, cell):
        return cell.find(text=True)

    def parse_romaji(self, romaji_cell):
        romaji = romaji_cell.find_all(text=True)
        return "".join(romaji)

    def parse_meanings(self, meanings_cell):
        meanings = meanings_cell.find_all(text=True)
        meanings = [meaning.replace("\n", "") for meaning in meanings]

        if self.is_meaning_limit_set():
            meanings = self.cut_meanings_above_limit(meanings)
        return meanings

    def cut_meanings_above_limit(self, array):
        return array[:self.MEANING_LIMIT]

    def is_romaji_enabled(self):
        if self.INCLUDE_ROMAJI:
            return True
        return False

    def is_meaning_limit_set(self):
        if self.MEANING_LIMIT and self.LAZY_MEANINGS:
            return True
        return False
