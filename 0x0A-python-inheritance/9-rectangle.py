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

        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

        def area(self):
            """Calculate and return the area of the rectangle"""

            return (self.__width * self.__height)

        def __str__(self):
            """Return the print() and str() representation of a Rectangle
            instance"""

            string = f'[{Rectangle.__name__}] {self.__width}/{self.__height}'
            return string
