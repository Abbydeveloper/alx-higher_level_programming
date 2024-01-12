#!/usr/bin/python3

def print_last_digit(number):
    if (number < 0):
        n = -number
    else:
        n = number
    last_digit = n % 10
    print("{}".format(last_digit), end="")
    return (last_digit)
