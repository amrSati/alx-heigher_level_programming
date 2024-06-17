#!/usr/bin/python3

"""Defines Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inherits from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Args:
            width (int): width
            height (int): height
            x (int): x point
            y (int): y point
            id (int): instance id
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter
        """
        self.validate_value('width', width)
        self.__width = width

    @property
    def height(self):
        """height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter
        """
        self.validate_value('height', height)
        self.__height = height

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter
        """
        self.validate_value('x', x)
        self.__x = x

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter
        """
        self.validate_value('y', y)
        self.__y = y

    def validate_value(self, name, value):
        """Integers validation

        Args:
            name (str): Name of the variable
            value (:obj:Any): The variable's value

        Raises:
            TypeError: if value is not int
            ValueError: if value is less than 1, except x and y
        """
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')

        if value < 1:
            if name in ['x', 'y']:
                if value < 0:
                    raise ValueError(f'{name} must be >= 0')
            else:
                raise ValueError(f'{name} must be > 0')

    def area(self):
        """Computes the area of a rectangle

        Returns:
            int: width * height
        """
        return self.width * self.height

    def display(self):
        """Prints the rectangle to stdout with the character `#`

        update: Consider the instance x, y coordinates
        """
        for y in range(self.y):
            print()

        for i in range(self.height):
            for x in range(self.x):
                print(' ', end="")

            for j in range(self.width):
                print('#', end="")

            print()

    def __str__(self):
        """String description of rectangle instance

        Returns:
            str: The following format:
                `[Rectangle] (<id>) <x>/<y> - <width>/<height>`
        """
        form = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return form.format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assignes an argument to each attribute

        Args:
            args (:obj:tuble): optional arguments list
            kwargs (:obj:dict): attributes dictionary
        """
        if args != ():
            attr = (self.id, self.width, self.height, self.x, self.y)
            self.id, self.width, self.height, self.x, self.y = \
                args + attr[len(args):len(attr)]
        elif kwargs:
            for (name, value) in kwargs.items():
                setattr(self, name, value)

    def to_dictionary(self):
        """Dictionary representation of the instance

        Returns:
            dict: dictionary of the instance attributes
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
