#!/usr/bin/python3
"""Module 10 - Square"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


clase Square(Rectangle):
    """Square class, inherits from Rectangle"""

    def __init__(self, size):
        """Initialize a square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """Calculate the area of a square instance"""

        return self.__size ** 2
