#!/usr/bin/python3
"""Module 0-lookup
Find the list of attributes and methods availabe in an object
"""

def lookup(obj):
    """Return the list of attributes and methods

    Args:
        - obj: oject to get list of available attributes and methods from 
    """
    return (dir(obj))

