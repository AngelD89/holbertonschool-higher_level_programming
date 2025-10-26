#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    # 💡 NOTE: Holberton expects `states.id` in ORDER BY clause, not just `id`
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(state_name)
    cur.execute(query)

    # Print results exactly as tuples
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
