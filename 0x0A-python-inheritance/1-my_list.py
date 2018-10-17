#!/usr/bin/python3
""" MyList module
"""


class MyList(list):
    """class MyList that inherits from list
    """
    def print_sorted(self):
        """prints the list in sorted ascending order
        """
        print(sorted(self))
