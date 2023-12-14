class Personne:
    def __init__(self, nom, age):
        """
        Initialise une instance de la classe Personne.

        :param nom: Le nom de la personne.
        :param age: L'âge de la personne.
        """
        self.nom = nom
        self.age = age

    def __str__(self):
        """
        Renvoie une représentation conviviale de la personne pour l'affichage avec la fonction print.

        :return: Chaîne de caractères représentant la personne.
        """
        return f"{self.nom}, {self.age} ans"

    def __repr__(self):
        """
        Renvoie une représentation de la personne destinée à la reproduction de l'objet.

        :return: Chaîne de caractères représentant la personne de manière détaillée.
        """
        return f"Personne('{self.nom}', {self.age})"


# Création d'une instance de Personne
personne1 = Personne("Christ", 32)

# Affichage avec print en utilisant __str__
print(personne1)

# Affichage avec print en utilisant __repr__
print(repr(personne1))

# Création d'une liste de personnes
liste_personnes = [
    Personne("Kimi", 22),
    Personne("Jess", 33),
    Personne("Glad", 24)
]

# Affichage de la liste de personnes en utilisant __repr__
print(liste_personnes)
