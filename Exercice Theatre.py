class Theatre:
    """
    La classe Theatre représente un théâtre avec des attributs liés à sa capacité et à ses inscriptions.

    Attributes:
        nom (str): Le nom du théâtre.
        capacite_max (int): La capacité maximale du théâtre en nombre de personnes.
        total_clients_inscrits (int): Le nombre total de clients actuellement inscrits.
        recette_totale (float): La recette totale de l'établissement.

    Methods:
        __init__(self, nom, capacite_max):
            Constructeur de la classe. Initialise les attributs nom, capacite_max, total_clients_inscrits, et recette_totale.

        inscrire(self, nombre_clients, prix_place):
            Méthode pour inscrire un certain nombre de clients avec un prix de place donné.
            Effectue le traitement en fonction de la capacité maximale du théâtre.

            Args:
                nombre_clients (int): Le nombre de clients à inscrire.
                prix_place (float): Le prix de la place.

            Prints:
                Message de réussite ou d'erreur en fonction de la capacité maximale.

    """

    def __init__(self, nom, capacite_max):
        """
        Constructeur de la classe Theatre.

        Args:
            nom (str): Le nom du théâtre.
            capacite_max (int): La capacité maximale du théâtre en nombre de personnes.
        """
        self.nom = nom
        self.capacite_max = capacite_max
        self.total_clients_inscrits = 0
        self.recette_totale = 0

    def inscrire(self, nombre_clients, prix_place):
        """
        Méthode pour inscrire un certain nombre de clients avec un prix de place donné.
        Effectue le traitement en fonction de la capacité maximale du théâtre.

        Args:
            nombre_clients (int): Le nombre de clients à inscrire.
            prix_place (float): Le prix de la place.

        Prints:
            Message de réussite ou d'erreur en fonction de la capacité maximale.
        """
        if self.total_clients_inscrits + nombre_clients <= self.capacite_max:
            self.total_clients_inscrits += nombre_clients
            recette_inscription = nombre_clients * prix_place
            self.recette_totale += recette_inscription
            print(f"Inscription réussie pour {nombre_clients} clients. Recette : {recette_inscription} €")
        else:
            print("Capacité maximale atteinte. Impossible d'inscrire plus de clients.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'une instance de Theatre
    theatre_example = Theatre(nom="Theatre Example", capacite_max=100)

    # Appels à la méthode inscrire
    theatre_example.inscrire(50, 15)  # Inscrire 50 clients à 15 € la place
    theatre_example.inscrire(30, 11)  # Inscrire 30 clients à 11 € la place
    theatre_example.inscrire(40, 19)  # Tentative d'inscription de 40 clients (capacité dépassée)

    # Affichage du total de clients inscrits
    print(f"Total de clients inscrits : {theatre_example.total_clients_inscrits}")

    # Affichage de la recette totale de l'établissement
    print(f"Recette totale : {theatre_example.recette_totale} €")
