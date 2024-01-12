#!/usr/bin/python3

def uppercase(str):
    str2 = ""
    length = len(str)

    for n in range(0, len(str)):
        rev_ch = ord(str[n])
        if rev_ch in range(97, 123):
            str2 += chr(rev_ch - 32)
        else:
            str2 += str[n]

    print("{}".format(str2))
