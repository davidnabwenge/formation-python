nom=str(input("quel est ton prenom:"))
age=int(input("quel est ton age:"))



while True:
    try:
        montant=float(input("entrer un montant en euros:"))
        break
    except ValueError:
        print("Erreur:tu dois entrer un nombre valide")

dollars=montant*1.09
print(f"{montant}€ équivalent à {dollars}$")