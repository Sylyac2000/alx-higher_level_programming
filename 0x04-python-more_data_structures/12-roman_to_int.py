#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    if roman_string == "":
        return 0
    num = 0
    dict_romain = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dict_romain.keys():
            return 0
        elif dict_romain[i] >= dict_romain[j]:
            num += dict_romain[i]
        else:
            num -= dict_romain[i]
    num += dict_romain[roman_string[-1]]
    return num
