#!/usr/bin/python3

"""``is_same_class`` function definition
"""


def is_same_class(obj, a_class):
    """Checks if ``obj`` is an instance of ``a_class``

    Args:
        obj (::obj::): Any object
        a_class (::obj::): class

    Returns:
        True: if the object is exactly an instance of the specified class
        False: otherwise
    """
    t = type(obj)
    return t == a_class
