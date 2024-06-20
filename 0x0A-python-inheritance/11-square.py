#!/usr/bin/python3

"""Square Module"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Initialize the square class

        Args:
        size (int): the length of each size of the squaare
        """

        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Calculate and return the area of a square"""

        return (self.__size ** 2)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle
            instance"""

        string = f'[{Square.__name__}] {self.__size}/{self.__size}'
        return string

