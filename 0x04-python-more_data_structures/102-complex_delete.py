#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    item_keys = list(a_dictionary.keys())

    for value_dict in item_keys:
        if value == a_dictionary.get(value_dict):
            del a_dictionary[value_dict]

    return (a_dictionary)
