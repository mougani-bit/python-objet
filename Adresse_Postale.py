class AdressePostale:
    """Représente une adresse postale.

    Attributes:
        numero_rue (int): Le numéro de rue.
        libelle_rue (str): Le libellé de la rue.
        code_postal (str): Le code postal.
        ville (str): La ville.
    """
    def __init__(self, numero_rue, libelle_rue, code_postal, ville):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville


class Personne:
    """Représente une personne.

    Attributes:
        nom (str): Le nom de la personne.
        prenom (str): Le prénom de la personne.
        adresse_postale (AdressePostale): L'adresse postale de la personne.
    """
    def __init__(self, nom, prenom, adresse_postale):
        self.nom = nom
        self.prenom = prenom
        self.adresse_postale = adresse_postale


# Exemples d'utilisation
adresse1 = AdressePostale(123, "Rue de la Paix", "75001", "Paris")
adresse2 = AdressePostale(456, "Avenue des Champs-Élysées", "75008", "Paris")

personne1 = Personne("Doe", "John", adresse1)
personne2 = Personne("Smith", "Jane", adresse2)

# Affichage des attributs des personnes
print(personne1.__dict__)
print(personne2.__dict__)
