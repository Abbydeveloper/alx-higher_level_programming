#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    a = 0
    if length == 0:
        a = None
    else:
        a = sentence[0]
    return (length, a)
