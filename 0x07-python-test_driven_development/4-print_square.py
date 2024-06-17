#!/usr/bin/python3
"""
Defines ``print_square()`` function
"""


def print_square(size):
    """Prints a square with a givin size

    Prints ``#`` for each ``size`` rows and columns

    Args:
        size (int): size length of the square

    Returns:
        nothing

    Raises:
        TypeError: If ``size`` is not ``int``
        ValueError: If ``size`` is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        pass
    else:
        for i in range(size):
            [print("#", end="") for j in range(size)]
            print()
