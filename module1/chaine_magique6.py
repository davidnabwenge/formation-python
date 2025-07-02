# Ce script demande une phrase à l'utilisateur, supprime les espaces en début et fin,
# compte le nombre de mots, affiche chaque mot en majuscules, et signale les mots commençant par "d".

# Demande une phrase à l'utilisateur
phrase = input("Écris une phrase : ")

# Supprime les espaces inutiles en début et fin
phrase = phrase.strip()

# Vérifie si la phrase est vide
if not phrase:
    print("Vous n'avez entré aucune phrase.")
else:
    # Découpe la phrase en une liste de mots
    mots = phrase.split()

    # Affiche le nombre de mots
    print(f"La phrase contient {len(mots)} mots.")

    # Affiche chaque mot en majuscules avec son numéro
    for i, mot in enumerate(mots, start=1):
        mot_maj = mot.upper()
        print(f"Mot {i} : {mot_maj}")

        # Vérifie si le mot commence par "d"
        if mot.lower().startswith("d"):
            print(f"  -> Le mot '{mot}' commence par la lettre 'd'.")
