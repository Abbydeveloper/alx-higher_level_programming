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
        if not (isinstance(value, int) or
           isinstance(value, float)):
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """
            Calculate the area of the square
        """
        area = self.__size * self.__size
        return (area)

    def __eq__(self, square2):
        """Compare if two squares are equal"""
        return (self.area() == square2.area())

    def __ne__(self, square2):
        """Check if two squares are not equal"""
        return (self.area() != square2.area())

    def __gt__(self, square2):
        """check if first square is greater than second
        square in area"""
        return (self.area() > square2.area())

    def __ge__(self, square2):
        """check if first square is greater than or equal to
        second square in area"""
        return (self.area() >= square2.area())

    def __lt__(self, square2):
        """check if first square is less than second square
        in area"""
        return (self.area() < square2.area())

    def __le__(self, square2):
        """check if first square is less than or equal to
        second square in area"""
        return (self.area() <= square2.area())
