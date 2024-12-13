# Détection de phishing
import re
import email
from email.parser import BytesParser
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
 
# Fonction pour analyser un email et détecter les signes de phishing
def detect_phishing(email_content):
    # Expressions régulières pour détecter les liens suspects
    suspicious_links = re.findall(r'http[s]?://[^\s]+', email_content)
    suspicious_senders = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', email_content)
 
    # Liste d'exemples d'expéditeurs non vérifiés
    suspicious_senders_list = ["support@", "noreply@", "admin@", "help@", "service@", "payment@", "no-reply@", "contact@", "info@"]
 
    # Critères de détection de phishing
    phishing_signs = []
   
    # Vérification des liens suspects
    if suspicious_links:
        phishing_signs.append("Liens suspects détectés")
   
    # Vérification des expéditeurs non vérifiés
    for sender in suspicious_senders_list:
        if any(sender in email_content for sender in suspicious_senders_list):
            phishing_signs.append("Expéditeur non vérifié")
   
    return phishing_signs, suspicious_links
 
# Fonction pour analyser plusieurs emails
def analyze_emails(emails):
    phishing_emails = []
    phishing_stats = Counter()
   
    for email_content in emails:
        phishing_signs, suspicious_links = detect_phishing(email_content)
        if phishing_signs:
            phishing_emails.append({
                "email": email_content,
                "phishing_signs": phishing_signs,
                "suspicious_links": suspicious_links
            })
        phishing_stats['Total'] += 1
        if phishing_signs:
            phishing_stats['Phishing'] += 1
   
    return phishing_emails, phishing_stats
 
# Fonction pour visualiser les statistiques
def visualize_statistics(phishing_stats):
    labels = phishing_stats.keys()
    sizes = phishing_stats.values()
   
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
    plt.title('Analyse des Emails : Phishing vs Non-Phishing')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()
 
# Exemple de contenu d'emails pour l'analyse
emails = [
    "Bonjour, vous avez reçu un paiement. Cliquez sur le lien pour confirmer votre compte: http://example.com",
    "Mise à jour importante de votre compte bancaire. Cliquez ici: http://suspiciouslink.com",
    "Rappel : votre abonnement arrive à expiration. Visitez https://safewebsite.com pour plus d'infos.",
    "Chère cliente, nous vous contactons pour confirmer votre demande. Aucun lien n'est nécessaire.",
    "Félicitations ! Vous avez gagné un prix. Cliquez ici pour le récupérer : http://fraudulent-link.com"
]
 
# Analyser les emails
phishing_emails, phishing_stats = analyze_emails(emails)
 
# Affichage des emails suspects
print("Rapport des emails suspects de phishing :")
for phishing_email in phishing_emails:
    print("\nEmail suspect:")
    print(f"Contenu : {phishing_email['email']}")
    print(f"Signe(s) de phishing : {', '.join(phishing_email['phishing_signs'])}")
    print(f"Liens suspects : {', '.join(phishing_email['suspicious_links'])}")
 
# Visualiser les statistiques
visualize_statistics(phishing_stats)
 
 