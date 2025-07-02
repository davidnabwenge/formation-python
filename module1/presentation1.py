#  un script qui te demande ton prenom,ton age,et ta ville,et calcule l'année où tu auras 100 ans affiche tout dans une phrase tu t'appelle david,tu as 25 ans, tu vis à paris et tu auras 100 ans en 2100 et à la fin mettre la date actuel 

while True:
    try:
       nom=str(input("quel est ton prenom:")).capitalize()
       age=int(input("quel est ton age:"))
       ville=str(input("quel est ta ville:")).capitalize()
       a=int(input("entrez votre année de naissance:"))
       break
    except ValueError:
       print("😱entrez un nombre là où il le faut👇")

if a<1900 or a>2025:
   print("⚠️l'année de naissance est incorrecte.😭")
   exit()

if age<0 or age>120:
   print("⚠️l'age est incorrecte.😭")
   exit()

import datetime
aujourdhui=datetime.date.today()

print(f"tu t'appelle {nom}🤣, tu as {age}ans, et tu vis à {ville}😜, et tu auras 100 ans en {a+100}🤗  et aujourd'hui,nous sommes le {aujourdhui.strftime("%d/%m/%y")}")