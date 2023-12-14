from abc import ABC, abstractmethod

from tp06_methode_redefinie_et_heritage import LivreNumerique, LivrePapier

class Sortie(ABC):

    def __init__(self, date, livre):
        self._date = date
        self._livre = livre

    @abstractmethod
    def get_montant(self):
        pass

class Emprunt(Sortie):

    def __init__(self, date, livre, duree):
        super().__init__(date, livre)
        self._duree =duree

    def get_montant(self):
        if isinstance(self._livre, LivrePapier):
            return self._duree*0.5
        elif isinstance(self._livre, LivreNumerique):
            return self._duree*0.25
        else:
            return 0

class Achat(Sortie):

    def __init__(self, date, livre, montant):
        super().__init__(date, livre)
        self._montant = montant

    def get_montant(self):
        return self._montant

def montant_global(liste_sorties):
    return sum(sortie.get_montant() for sortie in liste_sorties)

livre1 = LivrePapier(titre="La mafia des généraux", auteur="Hichem ABOUD", achetable=False, etat="neuf"),
livre2 = LivreNumerique(titre="Père riche père pauvre", auteur="Robert T.Kiyosaki", achetable=True, format="Kindle"),

sorties =[
    Achat(date="13/12/2023", livre=livre1, montant=50),
    Emprunt(date="12/12/2023", livre=livre2, duree=14)
]
print("montant global des sorties :", montant_global(sorties))
