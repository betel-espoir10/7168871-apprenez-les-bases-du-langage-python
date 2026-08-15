# Ecrivez votre code ici !

#declaration
nombre1 = input("Entrez le nombre1 : ")
nombre2 = input("Entrez le nombre2 : ")

#verification
if (nombre1.isnumeric == False) and (nombre2.isnumeric == False):
  print("Les deux nombres doivent etre des entiers ")
  raise SystemExit("Fin du programme")

#Conversions des nombres en des entiers.
nombre1 = int(nombre1)
nombre2 = int(nombre2)

#creation du variables operateur

operateur = input("Entrez votre operateur de choix ['+', '-', '*'', '/'] : ")

if operateur not in ["+", "-", "*", "/"]:
  print("Erreur: le symbole de l'operateur doit etre '+', '-', '*'', '/' . ")
  raise SystemExit("Fin du programme")

#effectuons le calcul
if operateur == "+":
  resultat = nombre1 + nombre2
elif operateur == "-":
  resultat = nombre1 - nombre2
elif operateur == "*":
  resultat = nombre1 * nombre2
elif operateur == "/":
  #Verification du nombre2
  if nombre2 == 0:   
    print("Erreur: Impossible de diviser un nombre par zero !")
    raise SystemExit("Fin du programme")
  else:
    resultat = (nombre1/nombre2, 2)
#Affichage du resultat
print(f"Le resultat de l'operation est : {round(resultat, 2)}")


