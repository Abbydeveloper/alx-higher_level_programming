#!/usr/bin/python3

"""9-student.py Module"""


class Student():
    """Class defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get the dictionary representation of a student instance"""

        str_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    str_dict.update({x: self.__dict__[x]})
                return str_dict
        return self.__dict__
