#!/usr/bin/python3
"""
Defines a function tha prints a text with 2 new lines
after each of these characters: ``.``, ``?`` and ``:``.
"""


def text_indentation(text):
    """Indents text with new lines

    Prints two new lines after each of the following characters:
    ``.``, ``?`` and ``:``.

    There should be no space at the beginning or at the end
    of each printed line.

    Args:
        text (::obj::str): String to be indented

    Raises:
        TypeError: If ``text`` is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")

        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")

            i += 1

            while i < len(text) and text[i] == ' ':
                i += 1

            continue

        i += 1
