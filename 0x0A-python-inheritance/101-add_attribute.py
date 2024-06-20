#!/usr/bin/python3

"""Add attribute Module"""


def add_attribute(obj, attr, value):
    """Add a new to attribute to an object only if it's possible
    Raise a TypeError exception if not
    
    Args:
    obj (object): object to add attribute to
    attr (str): name of the attribute to add
    value: value of the attribute
    """

    if (hasattr(obj, '__slots__') and not hasattr(obj, attr)):
        raise TypeError("can't add new attribute")
    if (not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__')):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
