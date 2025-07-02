# manipuler les chaines et les list comme un pro

# demande une liste de prenoms, puis affiche les tous en maj remplace un prenom par un autre verifie s'il y a un prenom qui commence par "a"

prenom=["james","man","yan","dona","jason"]

# tous en maj

for p in prenom:
    print(p.capitalize())
    
    # verifier si un prenom commence par A
    
    if p.lower().startswith("a") or p.lower().endswith("a"):
            print(f"{p} commence par A")


    # remplacer "man" par "esther"

prenom=[p.replace("man","esther")for p in prenom]

print(f"noms après remplacement:{prenom}")

# demande une phrase et affiche chaque mot separemment

phrase=input("ecris une phrase:")
mots=phrase.split()

for mot in mots:
      print(f"-{mot}")

# demande un mot et compte combien de voyelles il contient. 

mot=input("entrer un mot:").lower()
voyelles="aeiouy"
compteur=0

for lettre in mot:
      if lettre in voyelles:
            compteur+=1

print(f"il y a {compteur} voyelles dans le mot {mot}")
