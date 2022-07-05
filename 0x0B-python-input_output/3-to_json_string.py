#!/usr/bin/python3
"""
Module 3-to_json_string.py

function that returns the JSON representation
of an object (string):
"""


def to_json_string(my_obj):
    """Returns JSON representation of obj (string)"""
    import json
    return(json.dumps(my_obj))
