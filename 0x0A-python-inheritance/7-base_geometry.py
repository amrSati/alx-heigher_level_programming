#!/usr/bin/python3

"""Defines ``BaseGeometry`` Class
"""


class BaseGeometry:
    """BaseGeometry class
    """

    def area(self):
        """ToDo

        Raises:
            Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates ``value``

        Args:
            name (:obj:`str`): name of the variable
            value (int): integer value

        Raises:
            TypeError: if ``value`` is not an integer
            ValueError: if ``value`` is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
