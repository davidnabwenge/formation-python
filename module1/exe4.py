# ecrit un script qui demande ton age et affiche un message selon la tranche d'age 0-11:enfant 12-17:ado 18-64:adulte 65+:senior

while True:
    try:
        age=int(input("veuillez inserer votre age:"))
        break
    except ValueError:
        print("✍️entrez un chiffre ou un nombre👇")

if age<12:
    print("vous etes enfant👶")   
elif age<18:
    print("vous etes ado👨‍🦲")
elif age<64:
    print("vous etes adulte👨‍🦱")   
elif age>=65:
    print("vous etes senior🧑‍🦳")         

# verificateur de mot de passe

motdepasse=input("entrer le mot de passe:")

if motdepasse=="python2025":
    print("✅acces autorisé")
else:
    print("❎mot de passe incorrect")

        #    meteo pro

print("bienvenue dans l'assistant météo python")        
print("tape 'exit' à tout moment pour quitter!🖐️")    
prenom=input("votre prenom s'il vous plait:")    

while True:
     try:
         temps=input("quel temps fait-il aujourd'hui?:").lower()

         if temps=="exit":
            print("merci d'avoir utilisé l'assistant météo à bientot!🖐️")
            break

         if temps=="soleil":
            print(f"🔆 salut {prenom} n'oublie pas tes lunettes de soleil🌤️")
         elif temps=="pluie":
            print(f"🥶🌧️ salut  {prenom} prend un parapluie☔")
         elif temps=="neige":
            print(f"❄️🥶😠 salut  {prenom} mets ta veste bien chaude")    
         else:
            print(f"🤔 salut  {prenom} je ne connais pas ce temps")  

     except:
       print("⚠️une erreur est survenue... Essaie encore.")
     
