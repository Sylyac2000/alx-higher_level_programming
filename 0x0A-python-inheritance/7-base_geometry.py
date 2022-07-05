#!/usr/bin/python3
"""
Module 7-base_geometry.py  (based on 6-base_geometry.py).

"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check if value is int """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
