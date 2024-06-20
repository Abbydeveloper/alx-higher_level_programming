#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""Square Module"""


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
