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

    def test_slugify_huruf_kecil(self):
        self.assertEqual(slugify("HALO DUNIA"), "halo-dunia")

    def test_slugify_trim_spasi_tepi(self):
        self.assertEqual(slugify("   halo   "), "halo")

    def test_slugify_spasi_garis_bawah_jadi_hubung(self):
        self.assertEqual(slugify("a b_c"), "a-b-c")

    def test_slugify_buang_karakter_non_ascii(self):
        self.assertEqual(slugify("a!b@c#d$e%"), "abcde")
        self.assertEqual(slugify("héllo wörld"), "hllo-wrld")

    def test_slugify_gabung_hubung_berurutan(self):
        self.assertEqual(slugify("a - b"), "a-b")
        self.assertEqual(slugify("a__b"), "a-b")
        self.assertEqual(slugify("a!-b"), "a-b")

    def test_slugify_tanpa_hubung_di_tepi(self):
        self.assertEqual(slugify("-halo-"), "halo")
        self.assertEqual(slugify("!halo!_"), "halo")

    def test_slugify_kosong_dan_hanya_simbol(self):
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("!!!"), "")
        self.assertEqual(slugify("___"), "")
        self.assertEqual(slugify("- -"), "")


if __name__ == "__main__":
    unittest.main()
