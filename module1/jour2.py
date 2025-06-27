# afficher les type
nom="david"
age=25
taille=1.75
estmineur=False

print(type(nom))
print(type(age))
print(type(taille))
print(type(estmineur))

# exemple
age_str="25"
age_int=int(age_str)
print(age_int+5)
# convertir une chaine en nombre
a=input("entrez un nombre: ")
b=input("entrez en un autre: ")
somme=int(a)+int(b)
print("le resultat est",somme,"$")

# convertir float en int
f=5.8
u=int(f)
print("float:",f, "|int: ",u)
# convertir int en float
x=10
y=float(x)
print("int:",x,"|float:",y)

# convertir les bool
print(bool(""))
print(bool("python"))
print(bool(0))
print(bool(3.14))