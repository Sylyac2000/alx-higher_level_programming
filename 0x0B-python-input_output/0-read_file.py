#!/usr/bin/python3
"""
Module 0-read_file.py

read file
"""


def read_file(filename=""):
    """read file """
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
