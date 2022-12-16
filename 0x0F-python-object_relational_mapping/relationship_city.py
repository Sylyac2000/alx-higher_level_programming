#!/usr/bin/python3
"""
This module is about a python file that contains the class definition
of a City and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

Base = declarative_base()


class City(Base):
    """
    Class City; instance of Base
    representing MySQL table "city"
    """
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True)  # autoincrements
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
