#!/usr/bin/python3

"""Defines ``class_to_json()`` function
"""


def class_to_json(obj):
    """Finds the dictionary description of ``obj`` attributes

    Args:
        obj (:obj:Any): Object to serialize

    Returns:
        dict: JSON serialization of an object
    """
    desc = {}

    if hasattr(obj, "__dict__"):
        desc = obj.__dict__.copy()

    return desc
