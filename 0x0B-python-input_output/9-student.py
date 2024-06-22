#!/usr/bin/python3

"""9-student.py Module"""


class Student():
    """Class defines a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize the student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get the dictionary representation of a student instance"""

        return self.__dict__
