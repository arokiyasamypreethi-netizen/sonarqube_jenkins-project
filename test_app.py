import unittest
from app import calculate_total, calculate_average


class TestApp(unittest.TestCase):

    def test_calculate_total(self):
        self.assertEqual(calculate_total(2, 3), 5)

    def test_calculate_average(self):
        self.assertEqual(calculate_average([1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
