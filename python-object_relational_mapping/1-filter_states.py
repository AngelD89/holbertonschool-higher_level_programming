#!/usr/bin/python3
"""Script that lists all states with names starting with N from the database"""

import MySQLdb
import sys

def list_states_starting_with_N(username, password, db_name):
    """Connect to MySQL database and list states starting with N"""
    
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    
    # Create cursor
    cursor = db.cursor()
    
    # Execute SQL query to select states starting with N
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    
    # Fetch all results
    states = cursor.fetchall()
    
    # Print results
    for state in states:
        print(state)
    
    # Close cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Get command line arguments
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        
        list_states_starting_with_N(username, password, db_name)
