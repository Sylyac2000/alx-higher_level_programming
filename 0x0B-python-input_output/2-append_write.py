#!/usr/bin/python3
"""
Module 2-append_write.py

append text to  file and return number of
characters written:
"""


def append_write(filename="", text=""):
    """append text to file and return string length"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
