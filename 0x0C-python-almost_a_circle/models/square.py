#!/usr/bin/python3
"""Square module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square which inherits from class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize instance of class Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print representation of a Square instance
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """Getter for size attribute
        """
        return self.height

    @size.setter
    def size(self, value):
        """Setter for size attribute
        """
        self.width = value
        self.height = value
