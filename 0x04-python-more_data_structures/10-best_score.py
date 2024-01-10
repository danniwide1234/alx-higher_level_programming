#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        privilege_list = list(a_dictionary.keys())
        score = 0
        highest = ""
        for z in privilege_list:
            if a_dictionary[z] > score:
                score = a_dictionary[z]
                highest = z
        return highest
