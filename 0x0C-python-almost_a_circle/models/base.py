#!/usr/bin/python3
"""
This module is about base.py
"""


import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json strings of all instances into file"""
        alistofobjs = []
        if list_objs is not None:
            for obj in list_objs:
                alistofobjs.append(cls.to_dictionary(obj))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(cls.to_json_string(alistofobjs))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns Python obj from JSON string"""
        if json_string is None or len(json_string) == 0:
            json_string = "[]"
        return json.loads(json_string)
