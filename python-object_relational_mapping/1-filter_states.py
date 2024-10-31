#!/usr/bin/python3

"""lists all states that start with an N from the database"""

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
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for row in states:
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    db.close()
