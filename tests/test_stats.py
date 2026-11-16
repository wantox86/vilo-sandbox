import unittest

from app.stats import mean, median


class MeanTest(unittest.TestCase):
    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            mean([])

    def test_odd_count(self):
        result = mean([1, 2, 3])
        self.assertEqual(result, 2.0)
        self.assertIsInstance(result, float)

    def test_even_count(self):
        self.assertEqual(mean([1, 2, 3, 4]), 2.5)

    def test_negative_values(self):
        self.assertEqual(mean([-3, -1, -2]), -2.0)


class MedianTest(unittest.TestCase):
    def test_empty_raises(self):
        with self.assertRaises(ValueError):
            median([])

    def test_odd_count(self):
        self.assertEqual(median([3, 1, 2]), 2)

    def test_even_count(self):
        self.assertEqual(median([1, 2, 3, 4]), 2.5)

    def test_negative_values(self):
        self.assertEqual(median([-3, -1, -2, -4]), -2.5)


if __name__ == "__main__":
    unittest.main()
