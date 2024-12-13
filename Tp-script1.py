import pandas as pd
import matplotlib.pyplot as plt

# Fonction pour analyser les logs d'accès web
def analyser_logs(fichier_csv):
    try:
        print("Analyse des logs en cours...")
        # Charger les données
        logs = pd.read_csv(fichier_csv, sep=';')

        print("Chargement des données terminé.")

        # Vérifier si les colonnes nécessaires existent
        if 'IP' not in logs.columns or 'Requete' not in logs.columns:
            print("Le fichier CSV doit contenir les colonnes 'IP' et 'Requete'.")
            return

        # Identifier les adresses IP les plus fréquentes
        ip_counts = logs['IP'].value_counts()
        top_ips = ip_counts.head(10)

        # Identifier les types de requêtes les plus fréquents
        requete_counts = logs['Requete'].value_counts()
        top_requetes = requete_counts.head(10)

        # Détecter les IP suspectes avec plus de 100 requêtes
        ip_suspectes = ip_counts[ip_counts > 100]

        # Générer un rapport des IP suspectes
        rapport = "Rapport des IP suspectes:\n"
        for ip, count in ip_suspectes.items():
            rapport += f"IP: {ip} - Nombre de requêtes: {count}\n"

        # Sauvegarder le rapport dans un fichier
        with open('rapport_ip_suspectes.txt', 'w') as f:
            f.write(rapport)

        print("Rapport généré dans 'rapport_ip_suspectes.txt'.")

        # Visualisation des adresses IP les plus fréquentes
        plt.figure(figsize=(10, 5))
        top_ips.plot(kind='bar', title='Top 10 des IP les plus fréquentes', ylabel='Nombre de requêtes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('top_ips.png')
        plt.show()

        print("Graphique 'top_ips.png' généré.")

        # Visualisation des types de requêtes les plus fréquents
        plt.figure(figsize=(10, 5))
        top_requetes.plot(kind='bar', title='Top 10 des types de requêtes', ylabel='Nombre de requêtes')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('top_requetes.png')
        plt.show()

        print("Graphique 'top_requetes.png' généré.")

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Demander à l'utilisateur de fournir le fichier CSV
fichier = "exemple.csv"  # Remplace input par le nom du fichier directement
analyser_logs(fichier)