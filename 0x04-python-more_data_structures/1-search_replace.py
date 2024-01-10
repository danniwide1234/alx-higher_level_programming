#!/usr/bin/python3


def search_replace(my_list, search, replace):
    fresh_list = []
    for element in my_list:
        if element == search:
            fresh_list.append(replace)
        else:
            fresh_list.append(element)
    return fresh_list
