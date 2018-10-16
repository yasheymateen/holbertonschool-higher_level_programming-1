#!/usr/bin/python3
"""Student module"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize Student instance with first_name, last_name, and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        If attrs is not a list of strings, then all attributes are returned.
        Else, only attribute names contained in this list are retrieved.
        """
        is_list_of_strings = True
        if type(attrs) is not list:
            is_list_of_strings = False
        else:
            for i in attrs:
                if type(i) is not str:
                    is_list_of_strings = False
        if not is_list_of_strings:
            return self.__dict__
        else:
            retval = {}
            for attr in attrs:
                if attr in self.__dict__:
                    retval[attr] = self.__dict__.get(attr)
            return retval

    def reload_from_json(self, json):
        """function that replaces all attributes of the Student instance
        with key-value pairs from argument `json`
        """
        for k, v in json.items():
            self.__dict__[k] = v
