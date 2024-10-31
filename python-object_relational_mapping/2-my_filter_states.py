#!/usr/bin/python3

'''
Display all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
This script connects to a MySQL database
using credentials provided as command-line arguments

usage: ./2-my_filter_states.py
<mysql_username> <mysql_password> <database_name>
'''

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    # Créer un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Exécuter une requête SQL
    cursor.execute("SELECT * FROM states WHERE name = '{}' \
        ORDER BY id ASC".format(sys.argv[4]))

    # Récupérer les résultats de la requête
    query = cursor.fetchall()

    # Exécuter une requête SQL
    cursor.execute(query)

    # Récupérer les résultats de la requête
    query_rows = cursor.fetchall()

    # Afficher les résultats
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)

    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
