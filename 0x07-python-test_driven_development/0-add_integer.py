#!/usr/bin/python3
"""Addition Function

Performes addition operation
"""


def add_integer(a, b=98):
    """adds two integers

    Args:
        a (int/float): first number
        b (int/float): second number

    Returns:
        int/float: Addition operation result
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(a) is float:
        a = int(a)

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    elif type(b) is float:
        b = int(b)

    return a+b
