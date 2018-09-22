import unittest

from dictscraper.word import Word


class WordTestCase(unittest.TestCase):
    def setUp(self):
        self.w1 = Word()

        for field in ["foo", "bar", "foo,bar"]:
            self.w1.append_field(field)

    def test_word_fields(self):
        self.assertEqual(self.w1.fields, ["foo", "bar", "foo,bar"])

    def test_word_csv(self):
        csv_line = self.w1.csv()
        self.assertEqual(csv_line, "foo;bar;foo,bar")


if __name__ == "__main__":
    unittest.main()
