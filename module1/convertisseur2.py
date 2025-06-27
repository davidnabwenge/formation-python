# le script 2 demande une somme en euros à l'utilisateur et convertit en dollard us 1€=1.09$ et affiche le resultat formater 100€ équivalent à 109.0$

while True:
    try:                 
        a=float(input("bonjour monsieur quel est le montant de votre transaction:€"))       
        break
    except ValueError:
        print("✍️entrez un nombre👇")

b=str(input("tape exit pour quitter:"))

if b.lower()=="exit":
  print("fermeture du programme✅")
  exit()     

print("merci 🤗 pour votre transaction💵,voici le resultat👇")        
print(f"{a:.2f}€ equivalent à {a* 1.09:.2f}$")