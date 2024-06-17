#!/usr/bin/python3

"""Define a square class"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialize new square

        Args:
            size (int): private attribute that must be an int and positive
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
