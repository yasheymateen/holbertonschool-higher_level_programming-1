#!/usr/bin/python3
""" MyList module
"""

class MyList(list):
    """class MyList that inherits from list
    """
    def print_sorted(self):
        """prints the list in sorted ascending order
        """
        print('[', end='')
        for i in sorted(self):
            if i != sorted(self)[len(self) - 1]:
                print(i, end=', ')
            else:
                print(i, end='')
        print(']')
