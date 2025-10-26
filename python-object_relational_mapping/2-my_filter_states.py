#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    
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
    
    # Execute SQL query using parameterized query to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))
    
    # Fetch all results
    states = cursor.fetchall()
    
    # Print results
    for state in states:
        print(state)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
