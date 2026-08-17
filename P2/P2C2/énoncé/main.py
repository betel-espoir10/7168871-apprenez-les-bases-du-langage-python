# Ecrivez votre code ici !
#recuperation du saisie des nombres
nombres = input("Entrez une liste des nombres separes par des virgules :")

#Separation des nombres et insertion dans la liste
liste = nombres.split(",")
#Affiches des nombres dans liste
print("Les elements de la liste sont :", liste)

#conversion des elements de la liste en entier au cas ou ils des chaines de caracteres

liste_en_entiers = []
for nombre in liste:
  nombre_entiers = int(nombre)
  liste_en_entiers.append(nombre_entiers)  

#Calcul du somme des nombres 
sum = 0
for nombre in liste_en_entiers:
  sum += nombre
  print("La somme des nombres est:", sum)

#Calcul de la moyenne
moy = sum / len(liste_en_entiers)
print("La moyenne est :", moy)

#Calcul du nombre des nombres sup a la moy dans la liste
nombre_sup_moyenne = 0
for nombre in liste_en_entiers:
  if nombre > moy:
    nombre_sup_moyenne +=1
print("Le nombre des nombres superieur a la moyenne est :", nombre_sup_moyenne)
  
