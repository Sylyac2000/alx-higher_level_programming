#!/usr/bin/python3
"""
This module is about a python file that contains the class definition
of a State and an instance Base = declarative_base()
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

# Base = declarative_base()


class State(Base):
    """
    Class State; instance of Base
    representing MySQL table "states"
    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        id (sqlalchemy.Integer): state's id.
        name (sqlalchemy.String): state's name.
        cities (sqlalchemy.orm.relationship): State-City relationship.
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
