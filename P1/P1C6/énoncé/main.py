# Écrivez votre code ici !

#Creation de la liste fruits
fruits = ["pomme", "banane", "orange"]
print(fruits)

#Ajout de kiwi
fruits.append("kiwi")
print(fruits)

#suppression de orange dans la liste
fruits.remove("orange")
print(fruits)

#Modification de banane en ananas
fruits[1] = "ananas"
print(fruits)

#Affichage de la taille de la liste
print(len(fruits))

#Tri de la liste par ordre alphabetique
fruits.sort()
print(fruits)
