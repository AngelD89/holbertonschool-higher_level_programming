#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the database
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get command line arguments
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    
    # Create engine and connect to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session instance
    session = Session()
    
    # Query all State objects that contain the letter 'a', sorted by id
    states = session.query(State).filter(State.name.like('%a%'))\
                                 .order_by(State.id).all()
    
    # Print results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    
    # Close the session
    session.close()
