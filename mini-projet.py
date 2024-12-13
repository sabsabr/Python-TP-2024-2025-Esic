import os
import shutil
import logging

# Configuration du logging
logging.basicConfig(
    filename="classification_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def classer_fichiers(repertoire_source):
    try:
        # Vérifier si le répertoire source existe
        if not os.path.exists(repertoire_source):
            logging.error(f"Le répertoire source '{repertoire_source}' n'existe pas.")
            print("Le répertoire source spécifié n'existe pas.")
            return

        # Parcourir les fichiers dans le répertoire source
        for fichier in os.listdir(repertoire_source):
            chemin_fichier = os.path.join(repertoire_source, fichier)

            # Ignorer les répertoires
            if not os.path.isfile(chemin_fichier):
                continue

            # Extraire l'extension du fichier
            extension = os.path.splitext(fichier)[-1].lower()
            
            # Ignorer les fichiers sans extension
            if not extension:
                logging.warning(f"Fichier ignoré (pas d'extension) : {fichier}")
                continue

            # Créer un sous-dossier pour l'extension si nécessaire
            sous_dossier = os.path.join(repertoire_source, extension[1:])  # Retirer le point (.) de l'extension
            if not os.path.exists(sous_dossier):
                os.makedirs(sous_dossier)
                logging.info(f"Création du dossier : {sous_dossier}")

            # Déplacer le fichier dans le sous-dossier
            chemin_destination = os.path.join(sous_dossier, fichier)
            try:
                shutil.move(chemin_fichier, chemin_destination)
                logging.info(f"Fichier déplacé : {chemin_fichier} -> {chemin_destination}")
            except Exception as e:
                logging.error(f"Erreur lors du déplacement de {chemin_fichier} : {e}")

        print("Classification terminée. Consultez le fichier de log pour plus de détails.")

    except Exception as e:
        logging.error(f"Erreur inattendue : {e}")
        print("Une erreur est survenue. Consultez le fichier de log pour plus de détails.")

# Demander à l'utilisateur de spécifier le répertoire source
repertoire = input("Entrez le chemin du répertoire source : ")
classer_fichiers(repertoire)