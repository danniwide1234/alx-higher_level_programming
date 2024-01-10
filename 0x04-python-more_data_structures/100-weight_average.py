#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    weight = 0
    avg = 0

    for stre in my_list:
        weight += stre[0] * stre[1]
        avg += stre[1]

    return (weight / avg)
