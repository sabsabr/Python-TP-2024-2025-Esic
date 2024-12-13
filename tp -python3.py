# surveillance de fichiers
import time
import logging
import matplotlib.pyplot as plt
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
 
# Configuration du fichier de log
logging.basicConfig(filename='file_modifications.log', level=logging.INFO, format='%(asctime)s - %(message)s')
 
# Classe pour gérer les événements de fichier
class FileModificationHandler(FileSystemEventHandler):
    def __init__(self):
        self.events = []
 
    def on_modified(self, event):
        if not event.is_directory:
            # Enregistrement de l'événement dans le fichier de log
            event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info(f"Modification détectée : {event.src_path}")
            self.events.append(event_time)
 
    def on_created(self, event):
        if not event.is_directory:
            # Enregistrement de l'événement dans le fichier de log
            event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info(f"Création détectée : {event.src_path}")
            self.events.append(event_time)
 
    def on_deleted(self, event):
        if not event.is_directory:
            # Enregistrement de l'événement dans le fichier de log
            event_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            logging.info(f"Suppression détectée : {event.src_path}")
            self.events.append(event_time)
 
    def get_events(self):
        return self.events
 
# Fonction pour visualiser les événements de modification sous forme de graphique temporel
def visualize_events(events):
    event_times = [datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in events]
    plt.hist(event_times, bins=len(event_times), color='blue', edgecolor='black')
    plt.xlabel('Temps')
    plt.ylabel('Nombre d\'événements')
    plt.title('Modifications de fichiers au fil du temps')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
 
if __name__ == "__main__":
    # Spécification du répertoire à surveiller
    directory_to_watch = input("Entrez le répertoire à surveiller : ")
 
    # Initialisation du gestionnaire d'événements et de l'observateur
    event_handler = FileModificationHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_watch, recursive=True)
 
    try:
        observer.start()
        print(f"Surveillance du répertoire {directory_to_watch} en cours...")
       
        # Lancer un processus de surveillance en continu
        while True:
            time.sleep(1)
   
    except KeyboardInterrupt:
        observer.stop()
        print("Arrêt de la surveillance.")
 
    observer.join()
 
    # Visualisation des événements après la fin de la surveillance
    print("Affichage du graphique des événements...")
    visualize_events(event_handler.get_events())
 
 