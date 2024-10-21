#!/usr/bin/python3
"""Script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    
    # Création du curseur pour exécuter les requêtes
    cur = db.cursor()

    # Requête SQL avec protection contre les injections SQL
    cur.execute("SELECT id, name FROM states WHERE BINARY name = %s ORDER BY id ASC", (sys.argv[4],))

    # Affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cur.close()
    db.close()
