
class Personne:
    """
    Classe représentant une personne.

    Attributes:
        nom (str): Le nom de la personne.
        prenom (str): Le prénom de la personne.
        age (int): L'âge de la personne.
        adresse (str): L'adresse de la personne (par défaut, une chaîne vide).
    """

    def __init__(self, nom, prenom, age, adresse=""):
        """
        Initialise une instance de la classe Personne.

        Args:
            nom (str): Le nom de la personne.
            prenom (str): Le prénom de la personne.
            age (int): L'âge de la personne.
            adresse (str, optional): L'adresse de la personne (par défaut, une chaîne vide).
        """
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.adresse = adresse

class PersonneException(Exception):
    """
    Classe d'exception spécifique à la validation des personnes.

    Attributes:
        message (str): Le message d'erreur associé à l'exception.
    """

    def __init__(self, message):
        """
        Initialise une instance de la classe PersonneException.

        Args:
            message (str): Le message d'erreur associé à l'exception.
        """
        super().__init__(message)

class PersonneService:
    """
    Classe représentant un service de validation de personnes.

    Methods:
        valider(personne): Valide une instance de la classe Personne.

    Attributes:
        Aucun attribut défini dans cette classe.
    """

    def valider(self, personne):
        """
        Valide une instance de la classe Personne en vérifiant plusieurs conditions.

        Args:
            personne (Personne): Instance de la classe Personne à valider.

        Raises:
            PersonneException: Lève une exception si la validation échoue.
        """
        try:
            # Vérification du nom
            if not personne.nom:
                raise PersonneException("Le nom n'est pas renseigné.")
            if len(personne.nom.strip()) < 2:
                raise PersonneException("Le nom doit avoir au moins 2 caractères (après trim).")

            # Vérification du prénom
            if not personne.prenom:
                raise PersonneException("Le prénom n'est pas renseigné.")
            if len(personne.prenom.strip()) < 2:
                raise PersonneException("Le prénom doit avoir au moins 2 caractères (après trim).")

            # Vérification de l'adresse
            if not personne.adresse:
                raise PersonneException("L'adresse n'est pas renseignée.")

        except PersonneException as e:
            print(f"Validation échouée pour {personne.nom} {personne.prenom}: {e}")

        else:
            print(f"Validation réussie pour {personne.nom} {personne.prenom}.")


if __name__ == "__main__":
    # Exemple d'utilisation
    personne1 = Personne("Doe", "John", 30)
    personne2 = Personne("", "Alice", 25)
    personne3 = Personne("Smith", "Bob", 35)
    personne4 = Personne("Brown", "Charlie", 28, "")
    personne5 = Personne("Young", "David", 22, "123 Main Street")

    # Créez une instance de PersonneService
    service = PersonneService()

    # Validez les personnes avec la méthode valider
    service.valider(personne1)
    service.valider(personne2)
    service.valider(personne3)
    service.valider(personne4)
    service.valider(personne5)
