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

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes the JSON string representation of
        list_objs to a file.

        Parameters:
        list_objs: list of instances who inherits from Base
        """
        filename = cls.__name__ + '.json'
        if list_objs is None:
            new_list = []
        else:
            new_list = []
            for obj in list_objs:
                new_list.append(obj.to_dictionary())
        with open(filename, "w", encoding='utf8') as f:
            json_string = Base.to_json_string(new_list)
            f.write(json_string)
