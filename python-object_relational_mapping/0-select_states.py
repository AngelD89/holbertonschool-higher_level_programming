#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute queries
    cur = db.cursor()

    # Execute SQL query to select all states, sorted by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the query result
    rows = cur.fetchall()

    # Display each row
    for row in rows:
        print(row)

    # Clean up
    cur.close()
    db.close()
