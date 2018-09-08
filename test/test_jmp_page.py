import unittest

from dictscraper.jmp_page import MjpPageSoup


class WordTestCase(unittest.TestCase):

    def test_constructor(self):
        soup = MjpPageSoup()


if __name__ == "__main__":
    unittest.main()
