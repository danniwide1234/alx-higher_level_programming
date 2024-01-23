#!/usr/bin/python3

"""Defining classes for a singly-linked list."""


class Node:
    """Representing  a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initializing a new Node.

        Args:
            data (int): new Node data
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Representing a singly-linked list."""

    def __init__(self):
        """Initalizing a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserting a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        latest = Node(value)
        if self.__head is None:
            latest.next_node = None
            self.__head = latest
        elif self.__head.data > value:
            latest.next_node = self.__head
            self.__head = latest
        else:
            storage = self.__head
            while (storage.next_node is not None and
                    storage.next_node.data < value):
                storage = storage.next_node
            latest.next_node = storage.next_node
            storage.next_node = latest

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        storage = self.__head
        while storage is not None:
            values.append(str(storage.data))
            storage = storage.next_node
        return ('\n'.join(values))
