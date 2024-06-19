#!/usr/bin/python3

"""Check object BaseClass"""


def is_kind_of_class(obj, a_class):
    """Check if the oject is exactly an instance of the specified class or inherites from the specified class
    """
    if (isinstance(obj, a_class)):
        return (True)
    return (False)
