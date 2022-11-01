#!/usr/bin/python3
"""Base class for all other classes in this project.
It manages ghe id atribute in all future classes and avoids
duplication of the same code (by extension, same bugs)"""


class Base:
    """Base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""

        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = Base.__nb_objects
