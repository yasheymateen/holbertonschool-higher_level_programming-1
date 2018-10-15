#!/usr/bin/python3
"""BaseGeometry module
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
