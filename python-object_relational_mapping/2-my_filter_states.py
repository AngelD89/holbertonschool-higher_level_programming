#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL username, password, database, and state name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create cursor
    cur = db.cursor()

    # Build query using format() exactly as the project requires
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)

    # Execute query
    cur.execute(query)

    # Fetch and print each row exactly as tuples
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close connections
    cur.close()
    db.close()
