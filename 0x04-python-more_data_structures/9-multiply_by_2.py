#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        a_new_dictionary = {}
        for elt, value in a_dictionary.items():
            a_new_dictionary[elt] = value * 2
        return a_new_dictionary
    return None
