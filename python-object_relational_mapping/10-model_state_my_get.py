#!/usr/bin/python3

"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.

usge: ./10-model_state_my_get.py
<mysql_username> <mysql_password> <database_name> <state_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and state name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Create engine and bind it to the metadata of the Base class
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the database for the state with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
