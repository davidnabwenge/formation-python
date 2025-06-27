# manipuler les chaines et les list comme un pro

# demande une liste de prenoms, puis affiche les tous en maj remplace un prenom par un autre verifie s'il y a un prenom qui commence par "a"

prenom=["ames","man","yan","dona","yes"]

# tous en maj

for p in prenom:
    print(p.capitalize())
    
    # verifier si un prenom commence par A
    
    if p.lower(.startswith("a") or p.lower(.endswith("a"):
            print(f"{p} commence par A")


    # remplacer "man" par "esther"

prenom=[p.replace("man","esther")for p in prenom]
print(f"noms après remplacement:{prenom}")