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

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
