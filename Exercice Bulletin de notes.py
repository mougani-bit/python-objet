from datetime import datetime

class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

class Note:
    def __init__(self, valeur, date, categorie):
        self.valeur = valeur
        self.date = date
        self.categorie = categorie

class Discipline:
    def __init__(self, nom):
        self.nom = nom
        self.notes = []

class Bulletin:
    def __init__(self, etudiant):
        self.etudiant = etudiant
        self.disciplines = [
            Discipline("Maths"),
            Discipline("Physique"),
            Discipline("Anglais"),
            Discipline("Français"),
            Discipline("Espagnol"),
            Discipline("Sport")
        ]

    def ajouter_note(self, discipline, valeur, date, categorie):
        note = Note(valeur, date, categorie)
        for d in self.disciplines:
            if d.nom == discipline:
                d.notes.append(note)

    def calculer_moyenne(self):
        moyennes = {}
        for discipline in self.disciplines:
            if discipline.notes:
                moyenne = sum(note.valeur for note in discipline.notes) / len(discipline.notes)
                moyennes[discipline.nom] = moyenne
            else:
                moyennes[discipline.nom] = 0.0
        return moyennes

    def afficher_moyenne(self):
        moyennes = self.calculer_moyenne()
        for discipline, moyenne in moyennes.items():
            print(f"Moyenne en {discipline}: {moyenne:.2f}")

# Exemple d'utilisation
etudiant_example = Etudiant("Dupont", "Jean")
bulletin_example = Bulletin(etudiant_example)

bulletin_example.ajouter_note("Maths", 15, datetime(2023, 1, 1), "DS")
bulletin_example.ajouter_note("Maths", 18, datetime(2023, 2, 1), "Interrogation")
bulletin_example.ajouter_note("Physique", 14, datetime(2023, 1, 15), "DS")
bulletin_example.ajouter_note("Français", 16, datetime(2023, 1, 10), "Devoir écrit")

bulletin_example.afficher_moyenne()
