#!/usr/bin/env python3
import threading
import time
from task_04_net import start_server, send_data

def main():
    # Démarrer le serveur dans un thread séparé
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Attendre un moment pour que le serveur soit prêt
    time.sleep(1)

    # Exécuter le client pour envoyer des données
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'Paris'
    }
    send_data(sample_dict)

    # S'assurer que le thread du serveur se termine correctement
    server_thread.join()

if __name__ == "__main__":
    main()
