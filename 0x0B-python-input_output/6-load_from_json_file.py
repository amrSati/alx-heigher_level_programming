#!/usr/bin/python3

"""Defines ``load_from_json_file()`` function
"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename (str): The JSON file's name

    Returns:
        (:obj:Any): Python object representation of the JSON string
    """
    with open(filename, 'r', encoding="utf-8") as json_file:
        return json.load(json_file)
