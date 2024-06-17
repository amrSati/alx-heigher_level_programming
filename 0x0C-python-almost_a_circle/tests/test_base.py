#!/usr/bin/python3

"""Base class unittest
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Testing Base class"""

    def setUp(self):
        print("Base Set Up")
        self.base = Base()

    def tearDown(self):
        print("Tear Down Base")
        del self.base
        del self.base2
        del self.base3

    def testId(self):
        """Tests instances ids"""
        self.assertEqual(self.base.id, 1)
        self.base2 = Base(3)
        self.assertEqual(self.base2.id, 3)
        self.base3 = Base()
        self.assertEqual(self.base3.id, 2)


if __name__ == "__main__":
    unittest.main()
