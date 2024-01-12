#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

str = ""
last_digit = 0
if (number < 0):
    last_digit = -(-number % 10)
else:
    last_digit = number % 10

if (last_digit > 5):
    str = "is greater than 5"
elif (last_digit == 0):
    str = "is 0"
elif (last_digit < 0 and last_digit != 0):
    str = "is less than 6 and not 0"

print(f"Last digit of {number:d} is {last_digit:d} and {str:s}")
