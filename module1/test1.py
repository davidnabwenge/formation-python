# le script 1 modifier avec la date

while True:
    try:    
        nom=str(input("quel est ton prenom:"))
        age=int(input("quel est ton age:"))
        break
    except ValueError:
        print("c'est n'est pas valable")
        


print(f"tu t'appelle {nom},tu as {age}ans,")