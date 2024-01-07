#!/usr/bin/python3
def max_integer(my_list=[]):
    lent = len(my_list)

    if lent == 0:
        return (None)

    max_int = my_list[0]

    for j in range(1, lent):
        if my_list[j] > max_int:
            max_int = my_list[j]

    return (max_int)
