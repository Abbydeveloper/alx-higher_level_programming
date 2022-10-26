#!/usr/bin/python3
"""Module 2 - Append Write"""


def append_write(filename='', text=''):
    """Append text to content of filename"""

    with open(filename, 'a+') as f:
        return f.write(text)
