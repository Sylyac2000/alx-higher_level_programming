#!/usr/bin/python3
"""
Module 5-text_indentation

"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each ".", "?", and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    listlines = [lines.strip(' ') for lines in text.split('\n')]
    res = "\n".join(listlines)
    print(res, end="")
