#!/usr/bin/python3

"""Defines ``append_write()`` function
"""


def append_write(filename="", text=""):
    """Appends text to file

    Args:
        filename (str): The file's name
        text (str): Text to append

    Returns:
        int: Number of characters appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        n_chars = f.write(text)

    return n_chars
