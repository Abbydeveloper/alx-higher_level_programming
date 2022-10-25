#!/usr/bin/python3

"""Module 4 - Inherits from """


def inherits_from(obj, a_class):
    """Check that an object obj is an instance of a class a_class"""
   
   return isinstance(obj, a_class) and type(obj) != a_class
