# Exercice 1

dicoVilles = {13: "Marseille", 34: "Montpellier", 44: "Nantes", 75: "Paris", 31: "Toulouse"}

# Afficher les clés
print("Clés du dictionnaire:")
for key in dicoVilles.keys():
    print(key)

# Afficher les valeurs
print("\nValeurs du dictionnaire:")
for value in dicoVilles.values():
    print(value)

# Afficher la taille du dictionnaire
print("\nTaille du dictionnaire:", len(dicoVilles))

# Exercice 2

def creer_dictionnaire_longueur(liste_cles):
    return {cle: len(cle) for cle in liste_cles}

# Exemple d'utilisation
liste_cles = ["Coucou", "Hi"]
resultat = creer_dictionnaire_longueur(liste_cles)
print(resultat)

# Exercice 3

# tp09_dictionnaire_exercice3.py

def creer_dictionnaire_occurrences(liste_cles):
    return {cle: liste_cles.count(cle) for cle in set(liste_cles)}

# Exemple d'utilisation
liste_cles = ["Ananas", "Banane", "Orange", "Ananas", "Banane"]
resultat = creer_dictionnaire_occurrences(liste_cles)
print(resultat)

# Exercice 4

# Création de la liste de Salariés
liste_salaries = [
    ("Antoine Dupont", 127, "DSI/JAVA"),
    ("Berthe Casa", 238, "DSI/PHP"),
    ("Fatima Ouassa", 478, "DSI/JAVA"),
    ("Cassian Andor", 156, "DSI/PYTHON"),
    ("Lee Wu", 559, "DSI/PHP"),
    ("Hassan Missen", 96, "DSI/PYTHON"),  # Supprimez le zéro en tête
    ("Aurélien PIC", 889, "DSI/JAVA"),
]

# Création du dictionnaire comptant le nombre de salariés par service
comptage_par_service = {}
for salarie in liste_salaries:
    service = salarie[2]  # L'indice 2 correspond au service dans la liste
    if service in comptage_par_service:
        comptage_par_service[service] += 1
    else:
        comptage_par_service[service] = 1

print("Comptage du nombre de salariés par service:")
print(comptage_par_service)

