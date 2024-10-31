#!/usr/bin/python3

'''
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
This script connects to a MySQL database
using credentials provided as command-line arguments
and retrieves all states from the 'states' table
where the name starts with 'N', ordered by their ID.

Usage:
    ./1-filter_states.py <mysql_username> <mysql_password> <database_name>
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
        db=sys.argv[3]
    )

    # Créer un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Exécuter une requête SQL
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupérer les résultats de la requête
    rows = cursor.fetchall()

    # Afficher les résultats
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
