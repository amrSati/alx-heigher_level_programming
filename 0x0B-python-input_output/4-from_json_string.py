#!/usr/bin/python3

"""Defines ``from_json_string()`` function
"""
import json


def from_json_string(my_str):
    """Decodes JSON string to Python object

    Args:
        my_str (str): String to decode

    Returns:
        (:obj:Any): Object representation of ``my_str`` string
    """

    return json.loads(my_str)
