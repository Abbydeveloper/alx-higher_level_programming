#!/usr/bin/python3

"""6-load_from_json_file.py Module"""


import json


def load_from_json_file(filename):
    """Create an Object from a JSON file"""

    with open(filename, mode="r") as f:
        return json.load(f)
