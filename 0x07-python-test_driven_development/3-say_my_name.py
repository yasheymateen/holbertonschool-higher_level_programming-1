#!/usr/bin/python3
"""say_my_name module"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>
    first_name is required positional argument
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    retval = 'My name is ' + first_name + ' ' + last_name
    print(retval)
