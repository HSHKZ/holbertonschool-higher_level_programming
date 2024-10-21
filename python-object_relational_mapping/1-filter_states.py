#!/usr/bin/python3
"""Script that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa, sorted by id.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        try:
            # Connexion à la base de données
            db = MySQLdb.connect(
                host="localhost",
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3],
                port=3306
            )

            # Création d'un curseur pour exécuter les requêtes
            cur = db.cursor()

            # Requête SQL pour lister les états dont le nom commence par 'N'
            cur.execute("SELECT id, name FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
            
            # Récupération des résultats
            rows = cur.fetchall()

            # Affichage des résultats
            for row in rows:
                print(row)

            # Fermeture du curseur et de la connexion à la base de données
            cur.close()
            db.close()

        except MySQLdb.Error as err:
            print(f"Error: {err}")
    else:
        print("Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>")
