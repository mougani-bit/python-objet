class AdressePostale:
    def __init__(self, numero_rue:int, libelle_rue:str, code_postal:str, ville:str):
        self.numero_rue = numero_rue
        self.libelle_rue = libelle_rue
        self.code_postal = code_postal
        self.ville = ville
    def __str__(self):
        return f"Numero: {self.numero_rue}, rue: {self.libelle_rue}, cp: {self.code_postal}, ville: {self.ville}"

    def __repr__(self):
        return f"Numero: {self.numero_rue}, rue: {self.libelle_rue}, cp: {self.code_postal}, ville: {self.ville}"

    def __eq__(self, other):
        if not isinstance(other, AdressePostale):
            return False
        return self.numero_rue==other.numero_rue and self.libelle_rue==other.libelle_rue and self.code_postal==other.code_postal and self.ville==other.ville

class Personne:
    def __init__(self, nom, prenom, adresse):
        self.nom = nom
        self.prenom = prenom
        self.adresse = adresse

    def __str__(self):
        return f"{self.nom} {self.prenom}, {self.adresse}"

    def __repr__(self):
        return f"Personne(nom={self.nom}, prenom={self.prenom}, adresse={self.adresse})"

    def __eq__(self, other):
        if not isinstance(other, Personne):
            return False
        return self.nom==other.nom and self.prenom==other.prenom and self.adresse==other.adresse

adr1 = AdressePostale(numero_rue=3, libelle_rue="Place Watteau", code_postal="30900", ville="Nîmes")
adr2 = AdressePostale(numero_rue=3, libelle_rue="Place Watteau", code_postal="30900", ville="Nîmes")
personne1 = Personne("Benmira", "Ishak", adr1)
personne2 = Personne("Benmira", "Ishak", adr2)
print(personne1==personne2)
