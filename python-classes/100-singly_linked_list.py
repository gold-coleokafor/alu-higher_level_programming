#!/usr/bin/python3
"""Defines a Node class and a SinglyLinkedList class."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a node with data and a next node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data, which must be an integer."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node, which must be None or a Node."""
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize an empty list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node in increasing sorted position."""
        new = Node(value)
        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while (current.next_node is not None and
               current.next_node.data < value):
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new

    def __str__(self):
        """Return the list as one number per line."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
