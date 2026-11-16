import unittest

from app.text import count_words, shout, slugify


class TestText(unittest.TestCase):
    def test_shout(self):
        self.assertEqual(shout("halo"), "HALO!")

    def test_count_words(self):
        self.assertEqual(count_words("satu dua tiga"), 3)

    def test_slugify_dasar(self):
        self.assertEqual(slugify("Halo Dunia"), "halo-dunia")

    def test_slugify_simbol(self):
        self.assertEqual(slugify("  Python_Is Fun!  "), "python-is-fun")


if __name__ == "__main__":
    unittest.main()
