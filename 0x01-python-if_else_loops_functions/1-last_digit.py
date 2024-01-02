#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digitalize = abs(number) % 10
if number < 0:
    digitalize = -digitalize
print(f"Last digitalize of {number:d} is {digitalize:d} and is ", end="")
if digitalize > 5:
    print("greater than 5")
elif digitalize == 0:
    print("0")
else:
    print("less than 6 and not 0")
