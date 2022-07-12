#!/usr/bin/python3
"""
This module is about square.py
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    class Square definition inherits from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size
