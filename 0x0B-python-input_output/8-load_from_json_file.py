#!/usr/bin/python3
"""load_from_json_file module"""


def load_from_json_file(filename):
    """function that creates an Object from a JSON file and returns it
    """
    import json
    with open(filename, mode="r", encoding='utf-8') as f:
        return json.load(f)
