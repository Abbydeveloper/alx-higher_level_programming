#!/usr/bin/python3

"""Check object BaseClass"""


def is_same_class(obj, a_class):
    """Check if the oject is exactly an instance of the specified class
    """
    if (type(obj) is a_class):
        return (True)
    return (False)
