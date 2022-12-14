#!/usr/bin/python3
"""Module 9 - Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Initialize instance of Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get dict representation of Student instance"""

        return self.__dict__
