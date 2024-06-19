#!/usr/bin/python3
"""Define a lookup module"""


def lookup(obj):
    """Function returns the list of available attributes and methods of an
    object"""
    return (dir(obj))
