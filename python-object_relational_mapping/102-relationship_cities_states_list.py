#!/usr/bin/python3
"""Lists all City objects with their State using one query."""
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import joinedload, sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    query = (session.query(City)
             .options(joinedload(City.state))
             .order_by(City.id))
    for city in query.all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
