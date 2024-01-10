#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    item_ord = list(a_dictionary.keys())
    item_ord.sort()
    for t in item_ord:
        print("{}: {}".format(t, a_dictionary.get(t)))
