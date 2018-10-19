#!/usr/bin/python3
"""Base module"""
import json

class Base:
    """class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance of class Base

        Parameters:
        id (int): id to be assigned to instance. If id is None,
        then private class attribute __nb_objects is incremented and
        assigned to the instance.id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON string representation of
        list_dictionaries

        Parameters:
        list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)
