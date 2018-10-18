#!/usr/bin/python3
"""append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file, after each line
    containing a specific string

    Arguments:
    @search_string: string to be searched for
    @new_string: string to be inserted after line containing search_string
    """
    retval = ""
    with open(filename, "r", encoding="utf8") as f:
        for line in f:
            retval += line
            if search_string in line:
                retval += new_string
    with open(filename, "w", encoding="utf8") as f:
        f.write(retval)
