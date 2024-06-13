#!/usr/bin/python3

""" Class Square """


class Square:
    """ A Square Class """

    def __init__(self, size=0):
        """
            Instantiate a square object

            Args:
            size (int) - size of the square
        """
        self.size = size

    @property
    def size(self):
        """Get or set property size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """
            Calculate the area of the square
        """
        area = self.__size * self.__size
        return (area)
