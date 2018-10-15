#!/usr/bin/python3
"""MyInt module"""


class MyInt(int):
    """class MyInt
    """
    def __init__(self, value):
        """Initialize MyInt with value
        """
        if type(value) is not int:
            raise TypeError("must be an integer")
        self.__value = value

    def __eq__(self, other):
        """Redefine == to return opposite
        """
        return not (self.__value == other)

    def __ne__(self, other):
        return not (self.__value != other)
