#!/usr/bin/python3
"""Lists all State objects and their City objects with one query."""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import contains_eager, sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    query = (session.query(State)
             .outerjoin(State.cities)
             .options(contains_eager(State.cities))
             .order_by(State.id, City.id))
    for state in query.all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
