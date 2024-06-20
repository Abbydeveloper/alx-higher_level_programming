#!/usr/bin/python3

"""Rectangle Module"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the Rectangle class, inheriting from BaseGeometry"""

    def __init__(self, width, height):
        """Initialize Rectangle class

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """

        self.integer_validator('height', height)
        self.__width = width
        self.integer_validator('width', width)
        self.__height = height
