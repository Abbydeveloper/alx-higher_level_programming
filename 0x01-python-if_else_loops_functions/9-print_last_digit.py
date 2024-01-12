#!/usr/bin/python3

def print_last_digit(number):
    if (number < 0):
        n = -number
    else:
        n = number
    return (n % 10)
