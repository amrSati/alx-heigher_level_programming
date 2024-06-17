#!/usr/bin/python3

"""Define ``write_file()`` function
"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    Args:
        filename (str): The file's name
        text (str): String to write into file

    Returns:
        int: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        n_chars = f.write(text)

    return n_chars
