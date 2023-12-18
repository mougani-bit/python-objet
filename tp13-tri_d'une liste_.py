# Dans le fichier tp13_tri_liste.py

class Personne:
    def __init__(self, nom, prenom, age):
        """
        Initialise une instance de la classe Personne.

        :param nom: Nom de la personne.
        :param prenom: Prénom de la personne.
        :param age: Âge de la personne.
        """
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def __eq__(self, other):
        """
        Redéfinit la méthode d'égalité pour les instances de la classe Personne.

        :param other: Autre instance à comparer.
        :return: True si les instances sont égales, False sinon.
        """
        if isinstance(other, Personne):
            return (self.nom == other.nom) and (self.prenom == other.prenom) and (self.age == other.age)
        return False

    def __hash__(self):
        """
        Redéfinit la fonction de hachage pour les instances de la classe Personne.

        :return: Valeur de hachage basée sur les attributs de l'instance.
        """
        return hash((self.nom, self.prenom, self.age))

    def __lt__(self, other):
        """
        Redéfinit l'opérateur "inférieur strict" pour trier les instances de la classe Personne sur le nom.

        :param other: Autre instance à comparer.
        :return: True si l'instance actuelle est inférieure à l'autre, False sinon.
        """
        return self.nom < other.nom

# Créer une liste de personnes
liste_personnes = [
    Personne("Doe", "John", 30),
    Personne("Smith", "Alice", 25),
    Personne("Brown", "Bob", 35)
]

# Tenter de trier la liste
# Cela ne fonctionnera pas correctement sans redéfinir __lt__

# Redéfinir __lt__ pour trier sur le nom
Personne.__lt__ = lambda self, other: self.nom < other.nom

# Afficher la liste triée sur le nom avec une boucle
print("Liste triée sur le nom:")
for personne in sorted(liste_personnes):
    print(f"Nom: {personne.nom}, Prénom: {personne.prenom}, Âge: {personne.age}")

# Redéfinir __lt__ pour trier sur le prénom
Personne.__lt__ = lambda self, other: self.prenom < other.prenom

# Afficher la liste triée sur le prénom avec une boucle
print("\nListe triée sur le prénom:")
for personne in sorted(liste_personnes):
    print(f"Nom: {personne.nom}, Prénom: {personne.prenom}, Âge: {personne.age}")
