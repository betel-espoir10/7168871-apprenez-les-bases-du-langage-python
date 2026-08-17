# Ecrivez votre code ici

#definition de la fonction salaire_mensuel
def salaire_mensuel(salaire_annuel):
  return (salaire_annuel / 12)

#definition du salaire_hebdomadaire
def salaire_hebdomadaire(salaire_mensuel):
  return salaire_mensuel / 4

#definition du salaire_horaire
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
  return salaire_hebdomadaire / heures_travaillees

#Saisie du salaire annuel de l'employe
salaire_annuel = float(input("Entrez votre salaire annuel :"))

#Saisie du nombre d'heures travaillees par semaine
heures_travaillees = float(input("Entrez le nombre d'heures travaillees par semaine :"))

#calcul du salaire horaire
mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire = salaire_hebdomadaire(mensuel)
horaire = salaire_horaire(hebdomadaire, heures_travaillees)

print("Votre salaire horaire est de : ", horaire, "XAF.")
