#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    fresh_dir = a_dictionary.copy()
    item_keys = list(fresh_dir.keys())

    for n in item_keys:
        fresh_dir[n] *= 2

    return (fresh_dir)
