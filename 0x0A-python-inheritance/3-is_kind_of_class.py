#!/usr/bin/python3

"""``is_kind_of_class`` function definition
"""


def is_kind_of_class(obj, a_class):
    """Checks if ``obj`` is instance of ``a_class`` or its superclass

    Args:
        obj (::obj::Any): object to check
        a_class (::obj::type): class

    Returns:
        ``True`` if the object is an instance of, or if the object is an
        instance of a class that inherited from, the specified class;
        otherwise ``False``.
    """
    return isinstance(obj, a_class)
