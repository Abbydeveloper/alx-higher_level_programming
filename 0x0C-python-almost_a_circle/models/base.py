#!/usr/bin/python3
import json
"""Base Module"""


class Base():
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictioanries"""

        if list_dictionaries is None or list_dictionaries == []:
            return ('[]')
        return json.dumps(list_dictionaries)
