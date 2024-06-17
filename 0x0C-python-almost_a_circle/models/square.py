#!/usr/bin/python3

"""Defines Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String Description of the instance

        Returns:
            str: Description of instance
        """
        form = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return form.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates the instance attributes

        Args:
            args (:obj:tuble): optional values tuble
            kwargs (:obj:dict): optional key/value attributes
        """
        if args:
            attr = (self.id, self.size, self.x, self.y)
            self.id, self.size, self.x, self.y = \
                args + attr[len(args):len(attr)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Dictionary representation of instance

        Returns:
            dict: Attributes of instance
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
