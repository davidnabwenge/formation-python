# creer un script qui demande ton prenom te souhaite bienvenue avec ton prenom(f-strig+emoji), demande ton age, te dit si tu es enfant, ado adulte ou senior 
# si tu es adulte(18-64ans),te demande ta ville et ecrit:"bonjour {prenom}, tu es adulte vivant à {ville},bonne journée!🔆🔅"

while True:
  try:
    prenom = input("votre prenom: ")  # Simplification : input() renvoie déjà une chaîne
    age = int(input("votre age: "))
  except ValueError:
    print("Erreur : veuillez entrer un âge valide (nombre entier).")  # Message plus précis
    continue  # Passe à l'itération suivante en cas d'erreur

  if age < 12:
    print(f"bonjour {prenom} vous etes enfant👶")
  elif age < 18:
    print(f"bonjour {prenom} vous etes ado 👦")  # Emoji plus approprié
  elif age <= 64:
    ville = input("votre ville: ").capitalize()
    print(f"bonjour {prenom}, tu es adulte 👨‍🦱 vivant à {ville},bonne journée!🔅")
  else:
    print(f"bonjour {prenom} vous etes senior 🧑‍🦳")

  encore = input("encore le tableau? (o/n): ").lower()
  if encore != "o":
    print("au revoir")
    break  # Utilisation de break pour une sortie plus propre
