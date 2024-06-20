#!/usr/bin/python3

"""Base Geometry Module"""


class BaseGeometry():
    """BaseGeometry class"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def area(self):
        """Calculate area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validate integer"""

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
