#!/usr/bin/python3
"""Module 8 - Class To JSON"""


import json


def class_to_json(obj):
    """Creates a dictionary description of an object obj"""

    return obj.__dict__
