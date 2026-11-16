import unittest

from app.text import count_words, shout


class TestText(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("halo"), "HALO!")

    def test_count_words(self):
        self.assertEqual(count_words("satu dua tiga"), 3)


if __name__ == "__main__":
    unittest.main()
