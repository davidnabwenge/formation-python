# Ce script demande à l'utilisateur deux nombres et affiche leur somme, différence, produit, puissance, division et modulo.
# Il gère également l'erreur de division par zéro et les entrées non numériques.

while True:
    try:
        continuer = input("Tapez 'exit' pour quitter ou appuyez sur Entrée pour continuer : ")

        if continuer.lower() == "exit":
            print("fermeture du programme✅")
            break  # Utilisation de break pour sortir de la boucle

        a = int(input("Entrez un nombre entier : "))
        b = int(input("Entrez un autre nombre entier : "))

        print(f"Addition : {a + b}")
        print(f"Soustraction : {a - b}")
        print(f"Multiplication : {a * b}")
        print(f"Puissance : {a ** b}")

        if b != 0:
            print(f"Division : {a / b:.2f}")  # Division avec 2 décimales
            print(f"Modulo : {a % b}")
            break  # Sort de la boucle seulement si les entrées sont valides et la division est possible
        else:
            print("Erreur : division par zéro impossible.")
    except ValueError:
        print("Erreur : entrée invalide. Veuillez entrer deux nombres entiers.")
