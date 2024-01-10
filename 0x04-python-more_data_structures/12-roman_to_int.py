#!/usr/bin/python3
def to_subtract(list_num):
    to_subs = 0
    highest_list = max(list_num)

    for k in list_num:
        if highest_list > k:
            to_subs += k

    return (highest_list - to_subs)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    item_keys = list(rom_n.keys())

    number = 0
    last_rom = 0
    list_num = [0]

    for character in roman_string:
        for r_num in item_keys:
            if r_num == character:
                if rom_n.get(character) <= last_rom:
                    number += to_subtract(list_num)
                    list_num = [rom_n.get(character)]
                else:
                    list_num.append(rom_n.get(character))

                last_rom = rom_n.get(character)

    number += to_subtract(list_num)

    return (number)
