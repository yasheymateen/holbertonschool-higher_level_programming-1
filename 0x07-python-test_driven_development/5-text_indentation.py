#!/usr/bin/python3
"""text_indentation module"""


def text_indentation(text):
    """function that that prints a text with 2 new lines after each of
    these characters: ., ?, :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    line = ""
    i = 0
    while i < len(text):
        if text[i] != '.' and text[i] != '?' and text[i] != ':':
            line += text[i]
        else:
            line += text[i]
            print(line)
            print()
            line = ""
            if i != len(text) - 1:
                if text[i+1] == " ":
                    i += 1
        i += 1
    print(line)
