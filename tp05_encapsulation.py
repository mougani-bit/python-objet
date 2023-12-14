
class Livre:
    """
    La classe Livre représente un livre avec des attributs encapsulés.

    Attributes:
        _titre (str): Le titre du livre.
        _auteur (str): L'auteur du livre.
        _achetable (bool): Indique si le livre est achetable (True/False).

    Methods:
        __init__(self, titre, auteur):
            Constructeur de la classe. Initialise les attributs titre, auteur, et achetable.

        titre(self):
            Getter pour l'attribut titre.

        titre(self, value):
            Setter pour l'attribut titre.

        auteur(self):
            Getter pour l'attribut auteur.

        auteur(self, value):
            Setter pour l'attribut auteur.

        achetable(self):
            Getter pour l'attribut achetable.

        achetable(self, value):
            Setter pour l'attribut achetable.
    """

    def __init__(self, titre, auteur):
        """
        Constructeur de la classe Livre.

        Args:
            titre (str): Le titre du livre.
            auteur (str): L'auteur du livre.
        """
        self._titre = titre
        self._auteur = auteur
        self._achetable = False

    @property
    def titre(self):
        """
        Getter pour l'attribut titre.

        Returns:
            str: Le titre du livre.
        """
        return self._titre

    @titre.setter
    def titre(self, value):
        """
        Setter pour l'attribut titre.

        Args:
            value (str): Nouveau titre du livre.
        """
        self._titre = value

    @property
    def auteur(self):
        """
        Getter pour l'attribut auteur.

        Returns:
            str: L'auteur du livre.
        """
        return self._auteur

    @auteur.setter
    def auteur(self, value):
        """
        Setter pour l'attribut auteur.

        Args:
            value (str): Nouvel auteur du livre.
        """
        self._auteur = value

    @property
    def achetable(self):
        """
        Getter pour l'attribut achetable.

        Returns:
            bool: True si le livre est achetable, False sinon.
        """
        return self._achetable

    @achetable.setter
    def achetable(self, value):
        """
        Setter pour l'attribut achetable.

        Args:
            value (bool): Nouvelle valeur indiquant si le livre est achetable.
        """
        self._achetable = value

# Exemple d'utilisation de la classe Livre
mon_livre = Livre(titre="Titre du livre", auteur="Auteur du livre")
mon_livre.titre = "Nouveau titre"
mon_livre.auteur = "Nouvel auteur"
mon_livre.achetable = True

print("Titre:", mon_livre.titre)
print("Auteur:", mon_livre.auteur)
print("Achetable:", mon_livre.achetable)
