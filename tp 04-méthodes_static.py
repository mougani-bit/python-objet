class ChaineUtils:
    @staticmethod
    def est_anagramme(chaine1, chaine2):
        """
        Vérifie si la première chaîne est un anagramme de la deuxième.

        Args:
            chaine1 (str): Première chaîne.
            chaine2 (str): Deuxième chaîne.

        Returns:
            bool: True si c'est un anagramme, False sinon.
        """
        return sorted(chaine1) == sorted(chaine2)

    @staticmethod
    def comptage_chaine(chaine_principale, chaine_a_compter):
        """
        Compte le nombre de fois où la deuxième chaîne apparaît dans la première.

        Args:
            chaine_principale (str): Chaîne principale.
            chaine_a_compter (str): Chaîne à compter.

        Returns:
            int: Le nombre de fois où la deuxième chaîne apparaît dans la première.
        """
        count = 0
        start_index = 0

        while start_index != -1:
            start_index = chaine_principale.find(chaine_a_compter, start_index)
            if start_index != -1:
                count += 1
                start_index += 1

        return count


# Exemple d'utilisation
if __name__ == "__main__":
    # Test de la méthode est_anagramme
    print(ChaineUtils.est_anagramme("listen", "silent"))  # True
    print(ChaineUtils.est_anagramme("hello", "world"))     # False

    # Test de la méthode comptage_chaine
    print(ChaineUtils.comptage_chaine("ababab", "ab"))     # 3
    print(ChaineUtils.comptage_chaine("python", "java"))   # 0
