# creer un script qui demande ton prenom te souhaite bienvenue avec ton prenom(f-strig+emoji), demande ton age, te dit si tu es enfant, ado adulte ou senior 
# si tu es adulte(18-64ans),te demande ta ville et ecrit:"bonhour {prenom}, tu es adulte vivant à {ville},bonne journée!🔆🔅"

while True:
    try:
        prenom=str(input("votre prenom:"))
        age=int(input("votre age:"))
    except ValueError:
        print("entrer un nombre")
        continue

    if age<12:
        print(f"bonjour {prenom} vous etes enfant👶")   
    elif age<18:
        print(f"bonjour {prenom} vous etes ado 👨‍🦲")
    
										# le mystere
    elif age<=64:
        ville=input("votre ville:").capitalize()
        print(f"bonjour {prenom}, tu es adulte 👨‍🦱 vivant à {ville},bonne journée!🔅")   
    else:
        print(f"bonjour {prenom} vous etes senior 🧑‍🦳")     

    
    encore=input("encore le tableau? (o/n):").lower()
    if encore!="o":
        print("au revoir")  
        exit()




