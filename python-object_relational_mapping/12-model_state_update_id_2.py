#!/usr/bin/python3

'''
changes the name of a State object from the database hbtn_0e_6_usa

usage: [mysql_username] [mysql_password] [database_name]
'''

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]

    # Create an engine and connect to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/'
        f'{database_name}'
        )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with id = 2
    state_to_update = session.query(State).filter_by(id=2).first()

    # Update the name of the State object
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
