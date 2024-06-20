#!/usr/bin/python3

"""Write to file module"""


def write_file(filename="", text=""):
    """Function to write a string to a text file"""
    
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
