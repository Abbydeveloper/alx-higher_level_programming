#!/usr/bin/python3

"""100-append_after.py Module"""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text to a file, after each line containing
    a specific string"""

    with open(filename, mode="r") as f:
        text = f.readlines()

    with open(filename, mode="w") as fa:
        string = ""
        for line in text:
            string += line
            if search_string in line:
                string += new_string
        fa.write(string)
