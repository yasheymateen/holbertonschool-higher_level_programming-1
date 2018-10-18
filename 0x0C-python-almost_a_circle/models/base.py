#!/usr/bin/python3
"""Base module"""


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
