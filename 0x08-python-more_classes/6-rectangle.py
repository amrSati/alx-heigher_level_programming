#!/usr/bin/python3
"""Defines a rectangle class
"""


class Rectangle:
    """Defines a rectangle (based on 0-rectangle.py)

    Args:
        number_of_instances (int): public class attribute that keeps track
        of the calss's instances.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiates a new rectangle

        Args:
            width (int): rectangle's width
            height (int): rectangle's height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter

        Args:
            value (int): width value

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter

        Args:
            value (int): height value

        Raises:
            TypeError: if height is not int
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """rectangle area

        Returns:
            width * height
        """
        return self.width * self.height

    def perimeter(self):
        """rectangle perimeter

        Returns:
            0 if width or height is 0
            otherwise 2 * (width + height)
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.height + self.width)

    def __str__(self):
        """returns a rectangle of #s
        """
        if self.width == 0 or self.height == 0:
            return ""

        rec = ''
        for i in range(self.height):
            for j in range(self.width):
                rec += '#'

            if i == self.height - 1:
                break
            rec += '\n'

        return rec

    def __repr__(self):
        """return a representation of the rectangle
        to be able to recreate a new instance
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """object destructer
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
