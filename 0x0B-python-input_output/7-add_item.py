#!/usr/bin/python3
"""
Module 7-add_item.py

script that adds all arguments to a Python list,
and then save them to a file
"""

from sys import argv as args
import json

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    content = load_from_json_file(filename)
except FileNotFoundError:
    content = []

my_list = content + args[1:]
save_to_json_file(my_list, filename)
