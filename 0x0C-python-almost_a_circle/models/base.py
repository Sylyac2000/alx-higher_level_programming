#!/usr/bin/python3
"""
This module is about base.py
"""


import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns list of instances"""
        filename = cls.__name__ + ".json"
        alist = []
        try:
            with open(filename, "r") as f:
                instances = cls.from_json_string(f.read())
            for index, dic in enumerate(instances):
                alist.append(cls.create(**instances[index]))
        except Exception as exc:
            pass
        return alist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as f:
            csvwriter = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csvwriter.writerow([obj.id, obj.width,
                                        obj.height, obj.x, obj.y])
                if cls.__name__ == "Square":
                    csvwriter.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        listobjs = []
        filename = cls.__name__ + ".csv"
        with open(filename, 'r', newline='') as f:
            csvreader = csv.reader(f)
            for row in csvreader:
                if cls.__name__ == "Rectangle":
                    dic = {"id": int(row[0]),
                           "width": int(row[1]),
                           "height": int(row[2]),
                           "x": int(row[3]),
                           "y": int(row[4])}
                if cls.__name__ == "Square":
                    dic = {"id": int(row[0]),
                           "size": int(row[1]),
                           "x": int(row[2]),
                           "y": int(row[3])}
                obj = cls.create(**dic)
                listobjs.append(obj)
        return listobjs
