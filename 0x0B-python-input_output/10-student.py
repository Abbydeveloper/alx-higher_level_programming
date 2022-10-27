#!/usr/bin/python3
"""Module 10 - Student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """initialize instance of Student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get dict representation of student instance"""

        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()
