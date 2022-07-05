#!/usr/bin/python3
"""
Module 0-read_file.py

read file
"""


def read_file(filename=""):
    """
    read file
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
        print(read_data)
