#!/usr/bin/python3
"""Rectangle module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of Rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter function to return private instance attribute __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for private instance attribute __width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function to return private instance attribute __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for private instance attribute __height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function to return private instance attribute __x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function for private instance attribute __x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function to return private instance attribute __y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for private instance attribute __y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method to return the area of a Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """Public method that prints in stdout the Rectangle instance
        with the character #
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(' ', end='')
            print('#' * self.__width)

    def __str__(self):
        """Prints a Rectangle instance description
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the class Rectangle with *args or **kwargs

        For *args:
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute

        IFF *args does not exist or is empty, then kwargs (a double
        pointer to a dictionary of key-value pairs) is used to update
        the Rectangle instance
        """
        i = 0
        if args and len(args) > 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.height = arg
                elif i == 2:
                    self.width = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        else:
            for key in kwargs:
                if key == 'id':
                    self.id = kwargs[key]
                elif key == 'width':
                    self.width = kwargs[key]
                elif key == 'height':
                    self.height = kwargs[key]
                elif key == 'x':
                    self.x = kwargs[key]
                elif key == 'y':
                    self.y = kwargs[key]

    def to_dictionary(self):
        """Public method that returns the dictionary representation
        of a Rectangle
        """
        ret = {}
        ret['id'] = self.id
        ret['width'] = self.width
        ret['height'] = self.height
        ret['x'] = self.x
        ret['y'] = self.y
        return ret
