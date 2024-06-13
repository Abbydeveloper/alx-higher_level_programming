#!/usr/bin/python3
"""Define a node of a singly linked list"""


class Node:
    """Singly linked list"""

    def __init__(self, data, next_node=None):
        """
        Instantiate the Node object

        Args:
        data (int) - the data of the Node
        next_node (Node) - The next Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set data property"""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get or set next_node property"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList(Node):
    """Singly Linked List, Inherites From The Node Class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert new Node in specified position in the
            Signly Linked List

            Args:
            value (Node): Node to insert
            """
        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Print a Singly Linked List"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
