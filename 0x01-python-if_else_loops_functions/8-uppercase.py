#!/usr/bin/python3

def uppercase(str):
    for element in str:
        if ord(element) >= ord('a') and ord(element) <= ord('z'):
            char = chr(ord(element) - 32)
        else:
            char = element
        print('{:s}'.format(char), end='')
    print('')
