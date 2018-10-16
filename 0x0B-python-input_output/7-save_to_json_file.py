#!/usr/bin/python3
"""save_to_json_file module"""


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file,
    using a JSON representation
    """
    if type(filename) is not str:
        raise TypeError("filename must be a string")
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
