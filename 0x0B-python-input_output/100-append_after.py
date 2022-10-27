#!/usr/bin/python3
"""Module 13 - Append After"""


def append_after(filename="", search_string="", new_string=""):
    """Append specified string new_string after search_string
    within filename
    """

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as g:
        h = ""
        for line in text:
            h += line
            if search_string in line:
                h += new_string
        g.write(h)
