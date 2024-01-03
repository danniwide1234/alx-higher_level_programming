#!/usr/bin/python3
def fizzbuzz():
    for p in range(1, 101):
        if p % 3 == 0 and p % 5 == 0:
            print("FizzBuzz", end='')
        elif p % 3 == 0:
            print("Fizz", end='')
        elif p % 5 == 0:
            print("Buzz", end='')
        else:
            print(p, end='')

        print(" ", end='')
