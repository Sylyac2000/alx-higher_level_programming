#!/usr/bin/python3
"""
Unittest for Base Class
# run with python3 -m unittest discover tests
# run with python3 -m unittest tests/test_base.py
"""

import unittest
from models import base
Base = base.Base


class TestBase(unittest.TestCase):

    def test_id_exist(self):
        """ test id given """
        self.assertTrue(Base(12), self.id == 12)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-5), self.id == -5)

    def test_id_notexist(self):
        """ test id not given """
        self.assertTrue(Base(), self.id == 1)
        self.assertTrue(Base(), self.id == 2)
        self.assertTrue(Base(), self.id == 3)

    def test_private_attr_access(self):
        """Test private attr are not accessible"""
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)
            print(Base.nb_objects)

    def test_invalid_arguments(self):
        """Test too many args given"""
        with self.assertRaises(TypeError):
            Base(50, 50)

    def test_class(self):
        """Test class created"""
        self.assertTrue(Base(100), self.__class__ == Base)

    def test_to_json_string(self):
        """Test dict given into JSON string"""
        d0 = {"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}
        d1 = {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}
        strd01 = Base.to_json_string([d0, d1])
        self.assertTrue(type(d0) == dict)
        self.assertTrue(type(strd01) == str)
        self.assertTrue(strd01,
                        [{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5},
                         {"id": 6, "width": 7, "height": 8, "x": 9, "y": 10}])
