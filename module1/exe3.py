# demander à un utilisateur deux nombres, puis afficher leur somme, difference, produit ,divisiones

while True:
    try:
        a=int(input("entrer un nombre au hazard:"))
        b=int(input("entrer un autre nombre au hazard:"))
        break
    except ValueError:
        print("entrer un nombre")

print(f"voici l'addition:",a+b)
print("voici la soustraction:",a-b)
print("voici la multiplication:",a*b)
print("voici la division:",a/b)

# demander un prenom à l'utilisateur est afficher en maj/min, les 3 premieres lettres,sa longueur,le prenom à l'envers

prenom=str(input("veuillez saisir votre prenom:"))
surnom=prenom[0:3].lower()+"y"

print(prenom.upper())
print(prenom.lower())
print(prenom[0:3])
print(len(prenom))
print(prenom[::-1])
print(f"votre surnom est {surnom}")


