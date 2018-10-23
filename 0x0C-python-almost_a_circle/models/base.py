#!/usr/bin/python3
"""Base module"""
import json
import os.path


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

    @staticmethod
    def from_json_string(json_string):
        """static method that returns the list of the
        JSON string representation

        Parameters:
        json_string: string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all attributes
        already set.

        Parameters:
        **dictionary: double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
            dummy.update(**dictionary)
        elif cls.__name__ == "Square":
            dummy = cls(1)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances
        """
        filename = cls.__name__ + '.json'
        obj_list = []
        if not os.path.exists(filename):
            return obj_list

        with open(filename, "r", encoding="utf8") as f:
            json_string = f.read()
            obj_list2 = Base.from_json_string(json_string)
            for obj_dict in obj_list2:
                obj_list.append(cls.create(**obj_dict))
        return obj_list
