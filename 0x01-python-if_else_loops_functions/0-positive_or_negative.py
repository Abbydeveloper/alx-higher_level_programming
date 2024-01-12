#!/usr/bin/python3
import random
number = random.randint(-10, 10)

str = ""
if (number < 0):
    str = "is negative"
elif (number > 0):
    str = "is positive"
else:
    str = "is zero"
print(f"{number:d} {str:s}")
