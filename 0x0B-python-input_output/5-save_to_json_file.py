#!/usr/bin/python3

"""5-save_to_json_file.py Module"""


import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file
    using a JSON representation
    """

    with open(filename, mode="w+") as f:
        json.dump(my_obj, f)
