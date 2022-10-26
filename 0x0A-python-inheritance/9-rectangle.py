#!/usr/bin/python3
"""Module 9 - rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class inherits from Base Geometry"""

    def __init__(self, width, height):
        """Initialize an instance of the rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return formatted string"""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))

    def area(self):
        """Calculate the area of the rectangle"""

        return self.__width * self.__height
