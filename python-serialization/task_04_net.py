#!/usr/bin/env python3
import socket
import json

def start_server():
    """
    Fonction qui démarre le serveur, attend les connexions entrantes,
    reçoit des données sérialisées, les désérialise et les affiche.
    """
    # Création d'un socket serveur
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))  # Lier à l'adresse localhost et au port 12345
    server_socket.listen(1)  # Le serveur écoute jusqu'à 1 connexion simultanée
    print("Le serveur écoute sur le port 12345...")

    # Acceptation d'une connexion entrante
    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    # Réception des données (jusqu'à 1024 octets)
    received_data = client_socket.recv(1024)

    # Désérialisation des données reçues
    try:
        received_dict = json.loads(received_data.decode('utf-8'))
        print("Dictionnaire reçu du client :")
        print(received_dict)
    except json.JSONDecodeError:
        print("Erreur de décodage des données JSON")

    # Fermeture de la connexion
    client_socket.close()
    server_socket.close()

def send_data(data):
    """
    Fonction qui envoie un dictionnaire sérialisé au serveur.
    """
    # Création d'un socket client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Connexion au serveur sur localhost et port 12345

    # Sérialisation des données (dictionnaire en JSON)
    serialized_data = json.dumps(data)

    # Envoi des données sérialisées
    client_socket.send(serialized_data.encode('utf-8'))

    # Fermeture de la connexion
    client_socket.close()
