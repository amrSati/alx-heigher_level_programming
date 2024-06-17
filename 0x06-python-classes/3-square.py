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

    def area(self):
        """Returns the square's area

        Area = a^2

        Returns:
            Area of square
        """
        return self.__size ** 2
