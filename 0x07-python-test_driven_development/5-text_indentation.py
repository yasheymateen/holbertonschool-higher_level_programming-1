#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """function that that prints a text with 2 new lines after each of
    these characters: ., ?, :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    skip = False
    for c in text:
        if skip:
            skip = False
            continue
        if c != '.' and c != '?' and c != ':':
            line += c
        else:
            line += c
            print(line)
            print()
            line = ""
            skip = True
    print(line, end="")
