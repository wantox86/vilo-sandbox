import unittest

from app.calc import add, divide, sub


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_sub(self):
        self.assertEqual(sub(5, 3), 2)

    def test_divide(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)


if __name__ == "__main__":
    unittest.main()
