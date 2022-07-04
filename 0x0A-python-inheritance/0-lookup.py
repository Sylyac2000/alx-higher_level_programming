#!/usr/bin/python3
"""
Module 0-lookup

"""


def lookup(obj):
    """returns list of object's attribute and methods"""
    if isinstance(obj, object):
        return dir(obj)
    return []
