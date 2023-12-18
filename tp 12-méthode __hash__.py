# Dans le fichier tp12_redefinition_hash.py

class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __eq__(self, other):
        if isinstance(other, Personne):
            return (self.nom == other.nom) and (self.prenom == other.prenom) and (self.age == other.age)
        return False

    def __hash__(self):
        # Redéfinir la méthode __hash__ pour obtenir une valeur de hachage unique
        return hash((self.nom, self.prenom, self.age))

# Instanciation de deux personnes avec les mêmes valeurs d'attributs
personne1 = Personne("Doe", "John", 30)
personne2 = Personne("Doe", "John", 30)

# Mettre ces classes dans un set
ensemble_personnes = {personne1, personne2}

# Afficher le contenu du set avec une boucle
for personne in ensemble_personnes:
    print(f"Nom: {personne.nom}, Prénom: {personne.prenom}, Âge: {personne.age}")
