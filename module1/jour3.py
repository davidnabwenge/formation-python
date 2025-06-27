# les operations et les chaines

a=10
b=3

print("addition:",a+b)
print("soustraction:",a-b)
print("multuplication:",a*b)
print("division:",a/b)
print("division entiere:",a//b)
print("modulo:",a%b)
print("puissance:",a**b)

texte="dada est malade"

print("bonjour "+texte)
print("hey"*5)
print(len(texte))
print(texte.upper())
print(texte.lower())
print(texte[::-1])

# generateur de surom

prenom=input("quel est ton prenom ?")
surnom=prenom[:3].upper()+"y"
print("ton surnom stylé est:",surnom)