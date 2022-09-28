#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    tuple_first = tuple_a + (0, 0)
    tuple_second = tuple_b + (0, 0)
    new = tuple_first[0] + tuple_second[0], tuple_first[1] + tuple_second[1]
    return new
