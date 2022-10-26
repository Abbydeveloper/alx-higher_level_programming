#!/usr/bin/python3

"""Module 1 - Write file"""


def write_file(filename='', text=''):
    """Write text into filename"""

    with open(filename, 'w+') as f:
        return f.write(text)
