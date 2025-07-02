# Ce script demande 5 prénoms à l'utilisateur, les stocke dans une liste,
# et affiche un message de bienvenue personnalisé pour chaque prénom.
# Des commentaires amusants sont ajoutés en fonction de la première lettre et de la longueur des prénoms.

noms = []  # Initialise une liste vide pour stocker les prénoms

# Collecte 5 prénoms
for i in range(5):
    while True:  # Boucle pour gérer les entrées vides
        nom = input(f"Entrez le prénom n°{i+1} : ").lower()
        if nom:  # Vérifie si l'entrée n'est pas vide
            noms.append(nom)
            break  # Sort de la boucle si un prénom valide est entré
        else:
            print("Erreur : veuillez entrer un prénom valide.")

# Affiche les prénoms et ajoute des commentaires
print("\nLes prénoms collectés sont :")  # Affiche un titre pour la liste
for nom in noms:
    print(f"Bonjour {nom.capitalize()}, content de te voir aujourd'hui ! 🔅")

    # Commentaires basés sur la première lettre
    if nom[0].lower() == "d":
        print("Ton prénom commence par 'D', comme David ! 🤣")
    elif nom[0].lower() == "a":  # Utilise elif pour éviter de multiples messages si le prénom commence par 'd' et 'a'
        print("Ton prénom est adorable ! 🥰")

    # Commentaire basé sur la longueur du prénom
    if len(nom) > 6:
        print("Quel prénom long et stylé ! ✨")