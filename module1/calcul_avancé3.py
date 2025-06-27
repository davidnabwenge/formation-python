# demander à un utilisateur deux nombres, puis afficher leur somme, difference, produit ,divisiones arrondi à2 dec, puissance modulo

while True:
    try:
        c=str(input("tape exit pour quitter ou enter pour contunier:"))

        if c.lower()=="exit":
            print("fermeture du programme✅")
            exit()

        a=int(input("entrez un nombre:"))
        b=int(input("entrez encore un nombre:"))

        if b!=0:
            print(f"voici l'addition:{a+b}")
            print(f"voici la soustraction:{a-b}")
            print(f"voici la multiplication:{a*b}")
            print(f"voici la puissance:{a**b}")
            print(f"voici la division:{a/b}")
            print(f"voici le modulo:{a%b}")
        else:
            print("Erreur:division par zero impossible")
            print(f"voici l'addition:{a+b}")
            print(f"voici la soustraction:{a-b}")
            print(f"voici la multiplication:{a*b}")
            print(f"voici la puissance:{a**b}")

        break
    except ValueError:
        print("✍️entrez un chifffre ou un nombre👇")
        



