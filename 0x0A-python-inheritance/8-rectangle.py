#!/usr/bin/python3
"""BaseGeometry and Rectangle module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """class Rectangle, inherits from class BaseGeometry
    """
    def __init__(self, width, height):
        """Initialize private instance attributes width and height
        and validates that both attributes are integers
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
