#!/usr/bin/python3

def weight_average(my_list=[]):
    if (len(my_list) == 0):
        return (0)

    scores = 0
    weight = 0
    for score_set in my_list:
        scores += score_set[0] * score_set[1]
        weight += score_set[1]
    return (scores / weight)
