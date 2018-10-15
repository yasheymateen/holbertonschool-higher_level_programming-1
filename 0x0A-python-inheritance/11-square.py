#!/usr/bin/python3
"""BaseGeometry, Rectangle, and Square module
"""


class BaseGeometry:
    """class BaseGeometry
    """
    def area(self):
        """Public instance method that raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


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

    def __str__(self):
        """Custom magic function to print Rectangles
        """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """Returns area of Rectangle
        """
        return self.__height * self.__width


class Square(Rectangle):
    """class Square, inherits from class Rectangle
    """
    def __init__(self, size):
        """Initialize square of size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return area of a Square
        """
        return self.__size ** 2

    def __str__(self):
        """Prints details about Square instance
        """
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
