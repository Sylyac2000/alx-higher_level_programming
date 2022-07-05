#!/usr/bin/python3
"""
Module 3-is_kind_of_class.py

"""


def is_kind_of_class(obj, a_class):
    """returns True if obj is an instance 
    of class that it inherited from"""
    return type(obj) == a_class
