#!/usr/bin/python3
"""
Module 1-write_file.py

write text to  file and return number of
characters written:
"""


def write_file(filename="", text=""):
    """write to file and return string length"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return(f.write(text))
