#!/usr/bin/python3

"""Defines ``inherits_from()`` function
"""


def inherits_from(obj, a_class):
    """Checks if ``obj`` is an instance of ``a_class`` or its superclass

    Args:
        obj (:obj:Any): object to check
        a_class (:obj:type): class

    Returns:
        bool: True if the object is an instance of a class that inherited
        (directlyor indirectly) from the specified class; otherwise False.
    """
    if issubclass(obj.__class__, a_class):
        return obj.__class__ is not a_class

    return False
