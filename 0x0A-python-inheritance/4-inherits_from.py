#!/usr/bin/python3
"""inherits_from module
"""


def inherits_from(obj, a_class):
    """function that returns a Boolean if the object is an instance
    of a class that inherited (directly or indirectly) from
    the specified class. Otherwise returns False
    """
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
