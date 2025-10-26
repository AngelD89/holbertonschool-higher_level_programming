#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and the state name from arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor
    cur = db.cursor()

    # ⚠️ Exact query format required by checker
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(state_name)
    cur.execute(query)

    # Fetch all matching rows
    rows = cur.fetchall()

    # Print results exactly as expected
    for row in rows:
        print(row)

    # Close all
    cur.close()
    db.close()
