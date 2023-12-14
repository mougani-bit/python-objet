
class Zoo:
    """Représente un zoo.

    Attributs:
        liste_animaux (list): Liste des espèces d'animaux représentées dans le zoo.
        nombre_total_animaux (int): Nombre total d'animaux dans le zoo.
    """

    liste_animaux = []
    nombre_total_animaux = 0

    @classmethod
    def ajouter_animaux(cls, espece, nombre):
        """Ajoute des animaux au zoo.

        Args:
            espece (str): L'espèce de l'animal à ajouter.
            nombre (int): Le nombre d'animaux à ajouter.

        Si l'espèce n'existe pas dans la liste, cette méthode ajoute l'animal à la liste
        des animaux du zoo. Elle augmente également le nombre total d'animaux du zoo
        du nombre indiqué.
        """
        if espece not in cls.liste_animaux:
            cls.liste_animaux.append(espece)
        cls.nombre_total_animaux += nombre

    @classmethod
    def afficher_animaux(cls):
        """Affiche toutes les espèces du zoo et le nombre total d'animaux."""
        print("Espèces dans le zoo :")
        for espece in cls.liste_animaux:
            print(f"- {espece}")
        print(f"Nombre total d'animaux dans le zoo : {cls.nombre_total_animaux}")


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de Zoo (non nécessaire ici, car toutes les méthodes sont de classe)
    zoo = Zoo()

    # Ajout d'animaux
    Zoo.ajouter_animaux("Lion", 3)
    Zoo.ajouter_animaux("Tigre", 2)
    Zoo.ajouter_animaux("Lion", 2)  # Ajoute plus de lions

    # Affichage des animaux dans le zoo
    Zoo.afficher_animaux()
