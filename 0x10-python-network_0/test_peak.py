#!/usr/bin/python3
"""Tests `find_peak` function
"""

import unittest


class TestFindPeak(unittest.TestCase):
    """Test cases class unittest for find_peak function
    """

    def setUp(self):
        """Imports the function from the module
        """
        self.find_peak = __import__('6-peak').find_peak

    def test_empty(self):
        """Case empty list
        """
        self.assertEqual(self.find_peak([]), None)

    def test_notlist(self):
        """Case different type
        """
        self.assertEqual(self.find_peak(5), None)
        self.assertEqual(self.find_peak("5"), None)
        self.assertEqual(self.find_peak({'s': 5}), None)
        self.assertEqual(self.find_peak((5, 5)), None)

    def test_difftypes(self):
        """Case list of different types
        """
        self.assertEqual(self.find_peak([[1], 3, 's']), None)

    def test_multiple(self):
        """Case multiple lists
        """
        self.assertEqual(self.find_peak([1, 2, 4, 6, 3]), 6)
        self.assertEqual(self.find_peak([1]), 1)
        self.assertEqual(self.find_peak([4, 2, 1, 2, 3, 1]), 3)
        self.assertEqual(self.find_peak([2, 2, 2]), 2)
        self.assertEqual(self.find_peak([-2, -4, 2, 1]), 2)
        self.assertEqual(self.find_peak([4, 2, 1, 2, 2, 2, 3, 1]), 4)


if __name__ == "__main__":
    unittest.main()
