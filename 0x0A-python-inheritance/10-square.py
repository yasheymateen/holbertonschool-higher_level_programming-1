#!/usr/bin/python3
"""BaseGeometry, Rectangle, and Square module
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square, inherits from class Rectangle
    """
    def __init__(self, size):
        """Initialize square of size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
