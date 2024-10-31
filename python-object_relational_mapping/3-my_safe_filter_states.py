#!/usr/bin/python3

'''
Script that takes in an argument and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument. But this time, write one that is
safe from MySQL injections!

usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>
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

    # Définir la requête SQL
    query = ("SELECT * FROM states WHERE name"
            "LIKE '{}' ORDER"
            "BY id ASC;".format(sys.argv[4]))

    # Exécuter une requête SQL
    cursor.execute(query)

    # Récupérer les résultats de la requête
    rows = cursor.fetchall()

    # Afficher les résultats
    for row in rows:
        print(row)

    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
