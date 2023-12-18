class Salarie:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

if __name__ == "__main__":
    # Déclaration de la chaine de caractères
    chaine = "Christ;Mougani;2 523.5"

    # Tâche 1
    premier_caractere = chaine[0]
    print("Premier caractère: " + premier_caractere)

    # Tâche 2
    longueur_chaine = len(chaine)
    print("Longueur de la chaine: " + str(longueur_chaine))

    # Tâche 3
    index_point_virgule = chaine.index(";")
    print("Index du premier ';': " + str(index_point_virgule))

    # Tâche 4
    index_espace = chaine.index(" ")
    nom_famille = chaine[index_point_virgule + 1:index_espace]
    print("Nom de famille extrait: " + nom_famille)

    # Tâches 5 et 6
    nom_famille_majuscules = nom_famille.upper()
    nom_famille_minuscules = nom_famille.lower()
    print("Nom de famille en majuscules: " + nom_famille_majuscules)
    print("Nom de famille en minuscules: " + nom_famille_minuscules)

    # Tâche 7
    morceaux = chaine.split(";")
    print("Liste obtenue après découpage: " + str(morceaux))

    # Tâche 8 et 9
    nom = morceaux[0]
    prenom = morceaux[1]
    salaire_str = morceaux[2].replace(" ", "")  # Supprimer l'espace
    salaire = float(salaire_str)

    # Création de l'instance de Salarie
    salarie_instance = Salarie(nom=nom, prenom=prenom, salaire=salaire)

    # Affichage des attributs de l'instance de Salarie
    print("Nom: " + salarie_instance.nom)
    print("Prenom: " + salarie_instance.prenom)
    print("Salaire: " + str(salarie_instance.salaire))
