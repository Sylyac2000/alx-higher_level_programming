#!/usr/bin/python3
"""
This module is about listing all states from
a mysql database table called states
"""

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    if len(argv) != 4:
        print("format is:0-select_states.py username password database")
    else:
        list_dbparam = argv[1:]
        # Open database connection
        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                               format(list_dbparam[0], list_dbparam[1],
                                      list_dbparam[2]), pool_pre_ping=True)
        Base.metadata.create_all(engine)
        # create session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Select all to be deleted
        cities = session.query(State, City).join(State).order_by(City.id).all()
        for state, city in cities:
            print("{:s}: ({:d}) {:s}".format(state.name, city.id, city.name))
        session.close()
