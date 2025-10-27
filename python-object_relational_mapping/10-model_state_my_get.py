#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
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
    state_name = argv[4]
    
    # Create engine and connect to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    
    # Create a Session instance
    session = Session()
    
    # Query for the state with the given name
    state = session.query(State).filter(State.name == state_name).first()
    
    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")
    
    # Close the session
    session.close()
