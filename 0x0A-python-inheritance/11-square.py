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

    def __str__(self):
        """Prints details about Square instance
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
