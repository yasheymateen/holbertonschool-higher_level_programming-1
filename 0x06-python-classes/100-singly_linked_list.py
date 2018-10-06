#!/usr/bin/python3
"""class Node and Singly Linked List
"""


class Node:
    """Represents a Node in a Singly Linked List
    """

    def __init__(self, data, next_node=None):
        """Initializes node with data, and next_node attributes
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Returns data of Node
        """
        return self.__data

    @property
    def next_node(self):
        """Returns name of next node in a Singly Linked List
        """
        return self.__next_node

    @data.setter
    def data(self, value):
        """Sets value to data portion of a Node
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """Sets value to next node of a Node
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a Singly Linked List
    """

    def __init__(self):
        """Initializes an Empty Sorted Singly Linked List
        """
        self.__head = None

    def __str__(self):
        """Use print to print entire sorted list
        """
        if self.__head is None:
            return str("")
        tmp = self.__head
        while tmp.next_node:
            print(tmp.data)
            tmp = tmp.next_node
        print(tmp.data, end="")
        return str("")

    def sorted_insert(self, value):
        """Insert a Node into sorted singly linked list
        """
        if type(value) is not int:
            raise TypeError
        if self.__head is None:
            new = Node(value)
            self.__head = new
        else:
            tmp = self.__head
            if value <= tmp.data:
                new = Node(value, tmp)
                self.__head = new
            else:
                while value > tmp.data:
                    if tmp.next_node is None:
                        break
                    if tmp.next_node.data >= value:
                        break
                    tmp = tmp.next_node
                new = Node(value, tmp.next_node)
                tmp.next_node = new
