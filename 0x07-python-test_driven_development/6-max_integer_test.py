#!/usr/bin/python3
"""Module to find the max integer in a list
"""


def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If list find to be empty, the function returns None
    """
    if len(list) == 0:
        return None
    expression = list[0]
    t = 1
    while t < len(list):
        if list[t] > expression:
            expression = list[t]
        t += 1
    return expression
