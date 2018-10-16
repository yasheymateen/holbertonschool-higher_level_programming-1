#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file.
    Returns the number of characters added
    """
    with open(filename, "a", encoding='utf-8') as f:
        chars = f.write(text)
    return chars
