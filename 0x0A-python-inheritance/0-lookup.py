#!/usr/bin/python3

"""A function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """Looks for attributes and methods of an object

    Args:
        obj (::obj::): Any object to inspect

    Returns:
        (::obj:: List) A list of available attributes and methods
    """
    return dir(obj)
