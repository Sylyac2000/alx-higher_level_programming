#!/usr/bin/python3
"""
This module is about a python file that contains the class definition
of a State and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(mysql.INTEGER(11), primary_key=True)
    name = Column(String(128), nullable=False)
