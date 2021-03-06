#!/usr/bin/python3
"""Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
Syntax: ./10-model_state_my_get.py mysql-username mysql-passwd db-name
state-name-to-search
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state_found = session.query(State).filter_by(name=sys.argv[4]).first()
        print(state_found.id)
    except:
        print("Not found")
