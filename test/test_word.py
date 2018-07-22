import unittest

from dictscraper.word import Word


class WordTestCase(unittest.TestCase):

    def test_csv_template(self):
        w1 = Word("foo", "bar", "foo, bar")
        self.assertEqual("foo; bar; foo, bar", w1.csv())

    def test_word_constructor_fields(self):
        w1 = Word("foo", "bar", "foo, bar")
        self.assertEqual(w1.fields, ["foo", "bar", "foo, bar"])


if __name__ == "__main__":
    unittest.main()
