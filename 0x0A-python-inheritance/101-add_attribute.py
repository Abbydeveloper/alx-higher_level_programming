#!/usr/bin/python3
"""Module 101 - Add Attribute"""


def add_attribute(obj, attr, val):
    """Check if attribute attr of value val can be added to an object obj"""

    if not hasattr(obj, '__slots__') and not hasattr(obj, '_dict__'):
        raise TypeError("can't add new attributes")
    if hasattr(obj, '__slots__') and not hasattr(obj, attr):
        raise TypeError("can't add new attribute")

    setattr(ob, attr, val)
