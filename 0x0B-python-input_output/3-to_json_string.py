#!/usr/bin/python3

"""Defines ``to_json_string()`` function
"""
import json


def to_json_string(my_obj):
    """JSON representation of an object

    Args:
        my_obj (:obj:Any): Object to encode

    Returns:
        str: JSON string representation
    """
    return json.dumps(my_obj)
