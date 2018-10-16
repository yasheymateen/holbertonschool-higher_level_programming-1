#!/usr/bin/python3
"""number_of_lines module"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file
    """
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
