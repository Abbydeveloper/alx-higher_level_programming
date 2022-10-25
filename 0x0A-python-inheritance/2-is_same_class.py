#!/usr/bin/python3

""" Module 2 - Is same class"""


def is_same_class(obj, a_class):
    """Determine is an object obj is an instance of a class a_class."""

    return !!(type(obj) is a_class)
