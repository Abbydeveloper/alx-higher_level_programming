#!/usr/bin/python3

"""Base Geometry Module"""


class BaseGeometry():
    """BaseGeometry class"""

    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def area(self):
        raise Exception('area() is not implemented')
