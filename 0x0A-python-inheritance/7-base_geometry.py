#!/usr/bin/python3

"""Module 7 - Base Geometry"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Raises an exception"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validate value argument"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
