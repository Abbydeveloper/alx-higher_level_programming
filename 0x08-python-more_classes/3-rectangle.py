#!/usr/bin/python3

"""Module desfining a Rectangle"""


class Rectangle():
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle

        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if (self.__width <= 0 or self.__height <= 0):
            return 0
        return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """Return the printable representation of the Rectangle"""

        if ((self.__width == 0) or (self.__height == 0)):
            return ("")
        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append('#')
            if i < self.__height:
                rectangle.append('\n')
        return ("".join(rectangle))
