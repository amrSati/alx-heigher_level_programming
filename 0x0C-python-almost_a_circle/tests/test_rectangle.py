#!/usr/bin/python3

"""Defines Rectangle unittest
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Rectangle class unittest"""

    def setUp(self):
        """Setting up test Scenario"""
        print("Rectangles setup")
        self.rectangle = Rectangle(2, 5, 1, 2)

    def tearDown(self):
        """Tears down Rectangle instances"""
        print("Rectangles tear down")
        del self.rectangle
        del self.recterror

    def test_attributes(self):
        """Tests Attributes values"""
        self.assertTrue(self.rectangle.width == 2)
        self.assertEqual(self.rectangle.x, 1)
        self.assertTrue(self.rectangle.id == 1)

    def test_errors(self):
        """Tests raising exceptions"""
        with self.assertRaises(TypeError):
            self.recterror = Rectangle('ss', 3, 's', 4)

        with self.assertRaises(ValueError):
            self.recterror = Rectangle(-3, 1, 4, -1)
        
        self.recterror = Rectangle(1,1)


if __name__ == "__main__":
    unittest.main()
