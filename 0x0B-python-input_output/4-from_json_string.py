#!/usr/bin/python3

"""Returns an object from JSON Module"""


import json

def from_json_string(my_str):
    """Returns the Object epresentation of my_str"""

    return json.loads(my_str)
