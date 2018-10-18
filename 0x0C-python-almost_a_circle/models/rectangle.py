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
            self.id, self.x, self.y, self.height, self.width)
