#!/usr/bin/python3
"""Module 6 - Load From Json File"""


import json
def load_from_json_file(filename):
    """Create object using content of filename"""

    with open(filename, 'r') as f:
        return json.load(f)
