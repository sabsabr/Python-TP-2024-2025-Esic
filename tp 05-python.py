import itertools
import time
import matplotlib.pyplot as plt

# Simulation du service avec un mot de passe correct
def service_simule(mot_de_passe):
    mot_de_passe_correct = "password123"
    return mot_de_passe == mot_de_passe_correct

# Liste des mots de passe courants (dictionnaire pour brute-force)
liste_mots_de_passe = [
    "123456",
    "password",
    "123456789",
    "12345678",
    "12345",
    "1234567",
    "password123",
    "1234567890",
    "admin",
    "qwerty"
]

# Variables pour enregistrer les tentatives
tentatives_reussies = 0
tentatives_echouees = 0

def brute_force():
    global tentatives_reussies, tentatives_echouees

    print("Début de l'attaque par brute force...\n")
    for mot_de_passe in liste_mots_de_passe:
        print(f"Tentative avec : {mot_de_passe}")
        
        if service_simule(mot_de_passe):
            print(f"\nSUCCÈS : Mot de passe trouvé -> {mot_de_passe}\n")
            tentatives_reussies += 1
            break
        else:
            print("Échec de la tentative.")
            tentatives_echouees += 1

        # Délai simulé entre les tentatives
        time.sleep(0.5)

    print("\nFin de l'attaque.")

# Fonction pour afficher les résultats sous forme de graphique
def visualiser_resultats():
    labels = ['Réussites', 'Échecs']
     valeurs = [tentatives_reussies, tentatives_echouees]

    plt.bar(labels, valeurs, color=['green', 'red'])
    plt.title("Résultats des tentatives de brute-force")
    plt.xlabel("Type de tentative")
    plt.ylabel("Nombre de tentatives")

    for i, v in enumerate(valeurs):
        plt.text(i, v + 0.1, str(v), ha='center', fontweight='bold')

    plt.show()

# Exécution du script
if __name__ == "__main__":
    brute_force()
    visualiser_resultats()
