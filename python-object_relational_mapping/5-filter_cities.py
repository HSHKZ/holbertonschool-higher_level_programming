#!/usr/bin/python3

'''
lists all cities from the database hbtn_0e_4_usa

Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name>
'''
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name> <state name>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    query = """
        SELECT cities.name 
        FROM cities 
        JOIN states ON cities.state_id = states.id 
        WHERE states.name = %s 
        ORDER BY cities.id ASC
        """
    cursor.execute(query, (state_name,))

    # Fetch all the results
    cities = cursor.fetchall()

    # Print the results
    print(", ".join([city[0] for city in cities]))

    # Close the cursor and the connection
    cursor.close()
    db.close()
