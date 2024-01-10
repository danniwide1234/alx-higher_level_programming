#!/usr/bin/python3
def number_keys(a_dictionary):
    element = 0
    item_keys = list(a_dictionary.keys())

    for p in item_keys:
        element += 1

    return (element)
