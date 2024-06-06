#!/usr/bin/python3

def roman_to_int(roman_string):

    if (not roman_string) or (type(roman_string) is not str):
        return (0)
    roman_dict = {'I':1, 'V':5, 'X':10, 'L': 50, 'C':100, 'D':500, 'M':1000 }

    num = 0
    prev_num = 0
    curr_num = 0

    for char in roman_string: 

        if (prev_num  < roman_dict[char] and prev_num != 0):
            num = (roman_dict[char] - prev_num)
        else:
            num += roman_dict[char]

        prev_num = roman_dict[char]

    return (num)
