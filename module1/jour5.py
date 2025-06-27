# 

#    liste de prenom

prenom=["david","sarah","ali","emma"]

for p in prenom:
    print(f"bonjour {p}")

    # notes et moyennes

notes=[14,15.5,13,17,12]
total=0
for note in notes:
    total=total+note

moyenne=total/len(notes)
print(f"la moyenne est de {moyenne:.2f}")    

# determiner les pair et les impair

nombres=[2,7,10,13,6]
for non in nombres:
    if non%2==0:
        print(f"{non} est pair")
    else:
        print(f"{non} est impair")

            # mini tableau liste personalisé
noms=[]
for nom in range(3):
    nom=input(f"entre le prenom n°1:")
    noms.append(nom)

    print("voici la liste de prenom")
    for nom in noms:
        print(f"{nom}")