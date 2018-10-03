#!/usr/bin/python3
"""class Square"""


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initializes the data with error handling."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Returns size of Square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value