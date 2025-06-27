# cree un script qui demande 5 prenom les met dans une liste et affiche pour chaque prenom:"bonjour {prenom}, content de te voir ajourd'hui"

noms=[]

for i in range(5):
    nom=input(f"entrer le prenom n°{i+1}:").lower()
    noms.append(nom)

    if nom[0].lower()=="d":
     print("ton prenom commence par D, comme David 🤣")           
        
    print("les noms s'afficheront ici")
    for nom in noms:
        print(f"bonjour {nom}, content de te voir aujourd'hui!🔅")

       

       
          
    