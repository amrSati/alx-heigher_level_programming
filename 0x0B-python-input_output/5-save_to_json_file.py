#!/usr/bin/python3

"""Defines ``save_to_json_file()`` function
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using JSON representation

    Args:
        my_obj (:obj:Any): Object to write
        filename (str): File to write to
    """
    with open(filename, 'w', encoding="utf-8") as json_file:
        json.dump(my_obj, json_file)
