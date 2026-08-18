from bs4 import Beautifull

#Extractions des informations avec BeautifulSoup
with open("index.html", "r", encoding="utf-8") as file:
  soup = Beautifull(file, "index.parse")

#Extraction du titre de la page
title = soup.title.string
print("Le titre de la page est : ", title)

#Extraction du texte de la balise H1
text_h1 = soup.find("h1").string
print("Le texte de la balise h1 est :", text_h1)

#Definition du dictionnaire pour stocker le produits
tous_les_produits = dict()

#Extraction des noms et des prix des produits dans la liste
produits = soup.find_all("li")
for produit in produits:
  name = produit.find("h2").string
  price_str = produit.find("p", class_="price").string
  #Separation de la chaine en liste des mots
  price_list = price_str.split(" ")
  #Recuperation du prix : deuxieme mot
  tous_les_produits[name] = {"price", price_list[1]}

  #Extraction de la description du produit
  description = produit.find_all("p")[-1].string
  tous_les_produits[name]["description"] = description

#Affcihages des informations extraites
print("Produits : ", tous_les_produits)

#transformation des prix en dollars
for name in tous_les_produits.keys():
  price_str = tous_les_produits[name]["price"]
  # Supprimer le symbole €
  price = price_str.split("€")
  #Conversion en float
  price = float(price)
  dollar_price = price * 1.2
  tous_les_produits[name]["dollar_price"] = f"{dollar_price}$"

#Affichage des prix en dollar
print("Tous les produits : ", tous_les_produits)


