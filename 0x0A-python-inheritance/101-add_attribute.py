#!/usr/bin/python3
"""Module 101 - Add Attribute"""


def add_attribute(obj, attr, val):
    """Check if attribute attr of value val can be added to an object obj"""

    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, val)
