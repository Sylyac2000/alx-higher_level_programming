#!/usr/bin/python3
"""
This module is about base.py
"""

class Base:
    """
    class Base definition
    Class Attributes:
        __nb_objects
    Methods:
        __init__(self, id=None)
    """
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initializes base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
