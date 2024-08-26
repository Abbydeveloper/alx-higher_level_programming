#!/usr/bin/python3
"""Find a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function to find a peak in a list of unsorted integers"""

    length = len(list_of_integers)

    if length == 0:
        return None

    min = 0
    max = length - 1

    while min < max:
        middle = (min + max) // 2

        if list_of_integers[middle] < list_of_integers[middle + 1]:
            min = middle + 1
        else:
            max = middle
    return list_of_integers[min]
