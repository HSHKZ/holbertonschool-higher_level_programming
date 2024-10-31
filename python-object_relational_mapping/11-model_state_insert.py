#!/usr/bin/python3

'''
add the State object “Louisiana” to the database hbtn_0e_6_usa

usage: ./11-model_state_insert.py
<mysql_username> <mysql_password> <database_name>
'''

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a new State object
    new_state = State(name="Louisiana")

    # Add the new State object to the session
    session.add(new_state)

    # Commit the session to the database
    session.commit()

    # Print the new state's id
    print(new_state.id)

    # Close the session
    session.close()
