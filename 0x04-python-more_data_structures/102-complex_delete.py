#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    found = []
    for k, v in a_dictionary.items():
        if value == v:
            found.append(k)
    for key in found:
        del a_dictionary[key]
    return a_dictionary
