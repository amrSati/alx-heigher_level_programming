#!/usr/bin/python3

"""Defines ``Rectangle`` Class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle that inherits from ``BaseGeometry``
    """

    def __init__(self, width, height):
        """Instantiation with ``width`` and ``height``

        Args:
            width (int): private attribute
            height (int): private attribute

        Raises:
            TypeError: if one of the attributes isn't integer
            ValueError: if one of the attributes is less than or equal 0
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
