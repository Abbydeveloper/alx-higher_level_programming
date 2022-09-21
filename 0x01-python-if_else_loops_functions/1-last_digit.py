#!/usr/bin/python3

import random

number = random.randint(-10000, 10000)
result = abs(number) % 10
str = 'Last digit of'
if number < 0:
    result = result * -1
if result > 5:
    print(f'{str:s} {number:d} is {result:d} and is greater than 5')
elif result == 0:
    print(f'{str:s} {number:d} is {result:d} and is 0')
elif result < 6 and result != 0:
    print(f'{str:s} {number:d} is {result:d} and is less than 6 and not 0')
