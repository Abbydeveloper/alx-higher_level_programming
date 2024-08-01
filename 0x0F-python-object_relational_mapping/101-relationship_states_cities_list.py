#!/usr/bin/python3
""" Create state California and city San Francisco
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id).all()
    for state in result:
        print("{:d}: {:s}".format(state.id, state.name))
        for cities in state.cities:
            print("\t{:d}: {:s{".format(cities.id, cities.name))
    session.commit()
