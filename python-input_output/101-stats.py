#!/usr/bin/python3
import sys
import signal

# Initialiser les variables
taille_totale_fichier = 0
codes_statut = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
compteur_lignes = 0

# Fonction pour afficher les statistiques
def afficher_stats():
    print(f"Taille de fichier: {taille_totale_fichier}")
    for code in sorted(codes_statut.keys()):
        if codes_statut[code] > 0:
            print(f"{code}: {codes_statut[code]}")

# Gestionnaire de signal pour l'interruption clavier (CTRL + C)
def gestionnaire_signal(sig, frame):
    afficher_stats()
    sys.exit(0)

# Enregistrer le gestionnaire de signal
signal.signal(signal.SIGINT, gestionnaire_signal)

# Lire l'entrée et analyser les lignes
try:
    for ligne in sys.stdin:
        compteur_lignes += 1
        elements = ligne.split()

        # Extraire le code de statut et la taille de fichier
        try:
            code_statut = int(elements[-2])
            taille_fichier = int(elements[-1])

            # Mettre à jour la taille totale des fichiers et le compteur de code de statut
            taille_totale_fichier += taille_fichier
            if code_statut in codes_statut:
                codes_statut[code_statut] += 1
        except (ValueError, IndexError):
            continue

        # Afficher les statistiques toutes les 10 lignes
        if compteur_lignes % 10 == 0:
            afficher_stats()

except KeyboardInterrupt:
    afficher_stats()
    sys.exit(0)
