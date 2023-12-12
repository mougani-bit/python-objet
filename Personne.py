import adresse_postale

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

    def afficher_nom_prenom_majuscules(self):
        """Affiche le nom et le prénom en majuscules."""
        print(f"{self.nom.upper()} {self.prenom.upper()}")

    def modifier_nom(self, nouveau_nom):
        """Modifie le nom de la personne."""
        self.nom = nouveau_nom

    def modifier_prenom(self, nouveau_prenom):
        """Modifie le prénom de la personne."""
        self.prenom = nouveau_prenom

    def modifier_adresse(self, nouvelle_adresse):
        """Modifie l'adresse de la personne.

        Args:
            nouvelle_adresse (AdressePostale): La nouvelle adresse de la personne.
        """
        self.adresse_postale = nouvelle_adresse

    def retourner_nom(self):
        """Retourne le nom de la personne."""
        return self.nom

    def retourner_prenom(self):
        """Retourne le prénom de la personne."""
        return self.prenom

    def retourner_adresse(self):
        """Retourne l'adresse de la personne."""
        return self.adresse_postale

    def afficher_attributs(self):
        """Affiche les divers attributs de la personne."""
        print(f"Nom: {self.nom}")
        print(f"Prénom: {self.prenom}")
        print(f"Adresse: {self.adresse_postale.__dict__}")


# Exemple d'utilisation des méthodes
adresse1 = AdressePostale(123, "Rue de la Paix", "75001", "Paris")
personne = Personne("Doe", "John", adresse1)

# Affichage des attributs de la personne
personne.afficher_attributs()

# Modification du nom et du prénom
personne.modifier_nom("NewDoe")
personne.modifier_prenom("NewJohn")

# Affichage du nom et du prénom en majuscules
personne.afficher_nom_prenom_majuscules()

# Création d'une nouvelle adresse
nouvelle_adresse = AdressePostale(456, "Avenue des Champs-Élysées", "75008", "Paris")

# Modification de l'adresse
personne.modifier_adresse(nouvelle_adresse)

# Affichage des attributs mis à jour
personne.afficher_attributs()
