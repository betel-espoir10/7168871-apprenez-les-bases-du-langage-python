import csv
# Ecriture du script pour lire le fichier input.csv au format recommander

#Extraction des donnees
def extract(filename = "input.csv"):
    data = []
    with open(filename, mode = "r") as file:
        csv_reader = csv.DictReader(file)
        for line in csv_reader:
            data.append(line)
    return data

#Transformations des donnees
def transfor(data_to_transform):
    data_to_load = []
    for data in data_to_transform:
        transformed_data = {}
        transformed_data["name"] = data["name"]
        transformed_data["salaire"] = int(data["heures_travaillees"]) * 15
        data_to_load.append(transformed_data)
    return data_to_load

#Chargement des donnees
def load(data_to_load, filename = "output.csv"):
    with open(filename, mode = "w") as file:
        fieldnames = ["name", "salaire"]
        writer = csv_reader = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in data_to_load:
            writer.writerow(data)

#Fonction main(): appel des fonctions extract(), transform() et load()
def main():
    data_to_transform = extract("input.csv")
    data_to_load = transfor(data_to_transform)
    load(data_to_load, "output.csv")


# Ne touchez pas le code ci-dessous
if __name__ == "__main__":
    main()
