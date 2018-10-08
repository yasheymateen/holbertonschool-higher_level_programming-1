#!/usr/bin/python3
"""Rectangle module
"""


class Rectangle:
    """class Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes instance of Rectangle. If either width or height
        are ommitted, they are set to 0 by default
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """Print message 'Bye rectangle...' when an instance of Rectangle
        is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def __str__(self):
        """Print the rectangle with the character specified by the
        public Class instance 'print_sumbol'
        """
        retval = ""
        height = self.height
        width = self.width
        if height != 0 and width != 0:
            for i in range(height):
                retval += str(self.print_symbol) * width
                if i != height - 1:
                    retval += "\n"
        return retval

    def __repr__(self):
        """Return string representation of the rectangle to be able
        to recreate a new instance by using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger triangle based on their areas.
        If the areas are equal, rect_1 is returned
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
