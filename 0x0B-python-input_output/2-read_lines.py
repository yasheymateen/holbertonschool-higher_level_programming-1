#!/usr/bin/python3
"""read_lines module"""


def number_of_lines(filename=""):
    """function that returns the number of lines of a text file
    """
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines

def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file and prints it to stdout
    """
    if type(filename) is not str:
        raise TypeError("filename must be a string")
    line_num = 0
    lines = number_of_lines(filename)
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0 or nb_lines >= lines:
            print(f.read(), end='')
        else:
            for line in f:
                if line_num == nb_lines:
                    break
                print(line, end='')
                line_num += 1
