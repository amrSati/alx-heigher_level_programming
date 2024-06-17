#!/usr/bin/python3

"""Singly Linked List

Defines a ''Node'' class and ''SinglyLinkedList'' class
"""


class Node:
    """SinglyLinkedList node"""

    def __init__(self, data, next_node=None):
        """Initializes new Node

        Args:
            data (int): data of new node
                must be an integer
            next_node (:obj:'Node', None): reference to next node in list
                must be a Node object or None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: integer in node"""
        return self.__data

    @property
    def next_node(self):
        """:obj:'Node': next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")

        self.__data = value

    @next_node.setter
    def next_node(self, value):
        if value and type(value) is not Node:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """Defines a Singly Linked List"""

    def __init__(self):
        """Initializes a linked list

        Args:
            head (:obj:'Node'): head of singly linked list
        """
        self.__head = None

    def sorted_insert(self, value):
        """Inserts new node

        Inserts a new Node into the correct sorted pposition in the list
        (increasing order)

        Args:
            value (int): data of new node
        """
        new = Node(value, None)
        tmp = None

        if self.__head is None:
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node and tmp.next_node.data < value:
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList"""
        tmp = self.__head
        values = []

        while tmp:
            values.append(str(tmp.data))
            tmp = tmp.next_node

        return '\n'.join(values)
