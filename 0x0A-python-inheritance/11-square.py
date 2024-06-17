#!/usr/bin/python3

"""Defines ``Square`` class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square and inherits from ``Rectangle``
    """

    def __init__(self, size):
        """Instantiation method

        Args:
            size (int): size of the square

        Raises:
            TypeError: if size is not int
            ValueError: if size is 0 or less
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Square Description
        """
        return "[{}] {}/{}".format("Square", self.__size, self.__size)
