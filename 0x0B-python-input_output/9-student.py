#!/usr/bin/python3

"""9-student.py Module"""


class Student():
    """Class defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student class"""

        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """Get the dictionary representation of a student instance"""

        return self.__dict__
