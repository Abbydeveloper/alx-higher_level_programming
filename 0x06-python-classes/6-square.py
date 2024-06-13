#!/usr/bin/python3

""" Class Square """


class Square:
    """ A Square Class """

    def __init__(self, size=0, position=(0, 0)):
        """
            Instantiate a square object

            Args:
            size (int) - size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get or set property position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
           len(value) != 2 or
           not all(isinstance(num, int) for num in value) or
           not all(num >= 0 for num in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
            Calculate the area of the square
        """
        area = self.__size * self.__size
        return (area)

    def my_print(self):
        """Print square"""
        for a in range(self.__position[1]):
            print("")
        for x in range(self.__size):
            for b in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print('#', end="")
            print("")

        if self.__size == 0:
            print("")
