#!/usr/bin/python3

for i in range(0, 9):
    for j in range(1, 10 - i):
        if i == 8:
            print('{}{}'.format(i, j + i))
        else:
            print('{}{}'.format(i, j + i), end=', ')
