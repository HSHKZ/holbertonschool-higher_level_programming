#!/usr/bin/python3

"""lists all states that have a specific name"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s \
                    ORDER BY id ASC", (sys.argv[4],))
    states = cursor.fetchall()
    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    cursor.close()
    db.close()
