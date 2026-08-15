# Écrivez votre code ici !

#Creation du dictionnaire
fruits = {
  "pomme" : "rouge",
  "banane": "jaune",
  "orange": "orange",
}
print("**************************************")
print(fruits)

#ajout de la cle kiwi pour valeur vert dans le dict
fruits["kiwi"] = "vert"
print(fruits)

#Access a la valeur correspondante à la clé "banane" et son stokage dans une variable appelée `couleur_banane`.
fruits["banane"]
couleur_banane = fruits["banane"]
print(couleur_banane)

#Modification de la valeur associée à la clé `"pomme"` pour `"vert"`.
fruits["pomme"] = "vert"
print(fruits)

#Suppression de la clé `"banane"` du dictionnaire `fruits`.
del fruits["banane"]
print(fruits)

#Affichages des clés restantes dans le dictionnaire.
print(fruits.keys())

#Affichages des Valeurs restantes dans le dictionnaire.
print(fruits.values())