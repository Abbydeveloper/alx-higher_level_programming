#!/usr/bin/python3

"""Module 8 - rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectange(BaseGeometry):
    """class Rectangle
    Inherits from BaseGeometry
    """

    def __init(self, width, height):
        """Initialize an instance of rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
