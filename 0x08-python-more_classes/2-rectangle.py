#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle:
    """class Rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes instance of Rectangle. If either width or height
        are ommitted, they are set to 0 by default
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the instance attribute width
        """
        return self.__width

    @property
    def height(self):
        """Returns the instance attribute height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Sets the width to positive integer value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height to positive integer value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__width + self.__height) * 2
