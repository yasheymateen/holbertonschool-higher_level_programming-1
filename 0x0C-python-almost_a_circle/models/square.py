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

    def update(self, *args, **kwargs):
        """Public method that updates the class Square with *args or **kwargs

        For *args:
        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute

        IFF *args does not exist or is empty, then kwargs (a double
        pointer to a dictionary of key-value pairs) is used to update
        the Square instance
        """
        i = 0
        if args and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
                i += 1
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'size':
                    self.size = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Public method that returns the dictionary representation
        of a Square
        """
        ret = {}
        ret['id'] = self.id
        ret['size'] = self.height
        ret['x'] = self.x
        ret['y'] = self.y
        return ret
