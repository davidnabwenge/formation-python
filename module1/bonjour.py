# addition des variable int
c=5
d=5

print("bonjour tout le monde")

while True:
    try:  

      a=int(input("entrez un nombre: "))
      b=int(input("entrez un autre nombre: "))
      break
    except ValueError:
       print("entrez le bon chiffre")
somme= int(a)+int(b)
print("la somme est",somme)

while True:
    try:   

       age=int(input("quel age as-tu "))
       nom=str(input("quel est ton prenom "))
       break
    except ValueError: 
        print("entre bien un chiffre")   

print("tu t'appelle",nom,"et tu as",age,"ans.")