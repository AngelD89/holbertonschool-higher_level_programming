#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa.
The script is SQL injection safe.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()

    # Execute one secure query (SQL injection free)
    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cur.execute(query, (sys.argv[4],))

    rows = cur.fetchall()

    # Display results as comma-separated list on one line
    print(", ".join([row[0] for row in rows]))

    # Close connection
    cur.close()
    db.close()
