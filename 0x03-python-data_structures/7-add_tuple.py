#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = len(tuple_a)
    y = len(tuple_b)

    if x == 0:
        a1 = 0
        a2 = 0
    elif x == 1:
        a1 = tuple_a[0]
        a2 = 0
    else:
        a1 = tuple_a[0]
        a2 = tuple_a[1]

    if y == 0:
        b1 = 0
        b2 = 0
    elif y == 1:
        b1 = tuple_b[0]
        b2 = 0
    else:
        b1 = tuple_b[0]
        b2 = tuple_b[1]

    fresh_tuple = (a1 + b1, a2 + b2)

    return (fresh_tuple)
