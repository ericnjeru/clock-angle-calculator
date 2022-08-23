import unittest

from main import get_clock_angle


class Test(unittest.TestCase):
    def test_0(self):
        degrees = get_clock_angle("00 00")
        self.assertEqual(degrees, 0, "test 0 failed. Expected 0")

    def test_1(self):
        degrees = get_clock_angle("06 00")
        self.assertEqual(degrees, 90, "test 0 failed. Expected 90")


if __name__ == '__main__':
    unittest.main()
