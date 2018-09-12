#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    retval = ""
    for i in range(len(str)):
        if i != n:
            retval += str[i]
    return retval
