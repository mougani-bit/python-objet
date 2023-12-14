class Livre:
    def __init__(self, titre, auteur, achetable=False):
        self._titre = titre
        self._auteur = auteur
        self._achetable = achetable

    @property
    def titre(self):
        return self._titre

    @titre.setter
    def titre(self, nouv_titre):
        self._titre = nouv_titre

    @property
    def auteur(self):
        return self._auteur
    @auteur.setter
    def auteur(self, nouv_auteur):
        self._auteur = nouv_auteur

    @property
    def achetable(self):
        return self._achetable
    @achetable.setter
    def achetable(self, valeur):
        self._achetable = valeur

    def afficher_info(self):
        print(f"Titre: {self._titre}, Auteur: {self._auteur}, Achetable: {self._achetable} ,")

    def __str__(self):
        return f"Titre: {self._titre}, Auteur: {self._auteur}, Achetable: {self._achetable} ,"

class LivrePapier(Livre):

    def __init__(self, titre, auteur, achetable, etat):
        super().__init__(titre, auteur, achetable)
        self._etat = etat

    def afficher_info(self):
        super().afficher_info()
        print(f"Etat: {self._etat}")

    def __str__(self):
        return super().__str__() + f"Etat : {self._etat}"



class LivreNumerique(Livre):

    def __init__(self, titre, auteur, achetable, format):
        super().__init__(titre, auteur, achetable)
        self._format = format

    def afficher_info(self):
        super().afficher_info()
        print(f"Format: {self._format}")

    def __str__(self):
        return super().__str__() + f"Format : {self._format}"


if __name__ == "__main__":
    livres =[
    LivrePapier(titre="La mafia des généraux", auteur="Hichem ABOUD", achetable=False, etat="neuf"),
    LivrePapier(titre="La sale guerre", auteur="Habib SOUAIDIA", achetable=True, etat="moyen"),
    LivreNumerique(titre="Père riche père pauvre", auteur="Robert T.Kiyosaki", achetable=True, format="Kindle"),
    LivreNumerique(titre="Physique Chimie", auteur="Julien Calafell", achetable=False, format="PDF")
    ]
    for livre in livres:
       livre.afficher_info()
       print("--------------------------------------------------------")
