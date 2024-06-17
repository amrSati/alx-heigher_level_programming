#!/usr/bin/python3

"""Defines ``read_file()`` function
"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename (str): The filename to read
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
