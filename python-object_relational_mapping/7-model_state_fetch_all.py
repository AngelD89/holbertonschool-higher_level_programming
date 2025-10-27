#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create connection to MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects sorted by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
