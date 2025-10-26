#!/usr/bin/python3
"""
Script that lists all states with names starting with N from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    
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
    
    # Execute SQL query to select states starting with uppercase N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    
    # Fetch all results
    states = cursor.fetchall()
    
    # Print results
    for state in states:
        print(state)
    
    # Close cursor and database connection
    cursor.close()
    db.close()
