# le script 2 demande une somme en euros à l'utilisateur et convertit en dollard us 1€=1.09$ et affiche le resultat formater 100€ équivalent à 109.0$

while True:
    try:                 
        a=float(input("bonjour monsieur quel est le montant de votre transaction:€"))       
        print("merci 🤗 pour votre transaction💵,voici le resultat👇")        
        print(f"{a:.2f}€ equivalent à {a* 1.09:.2f}$")
        break  # Sort de la boucle si l'entrée est valide
    except ValueError:  # Capture l'erreur si l'entrée n'est pas un nombre
        print("✍️entrez un nombre valide👇")


    continuer = input("voulez vous continuer ? (oui/non): ")
    if continuer.lower() != "oui":        
        print("fermeture du programme✅")  # Affiche un message de fermeture
        break  # Quitte la boucle si l'utilisateur ne veut pas continuer
           
