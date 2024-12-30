from Player.player import TPlayer
from typing import List, Tuple
from Player.color import TColor

class TPlayerIA(TPlayer):
    """
    Classe représentant un joueur IA (Intelligence Artificielle).

    Hérite de :
    - TPlayer : Reprend les attributs communs à tous les joueurs.

    Spécificités :
    - L'IA n'a pas d'historique de coups (pas de Undo).
    - Implémente Minimax pour choisir les coups automatiquement.
    """

    def __init__(self, cName: str):
        """
        Initialise un joueur IA.

        @param cName : Nom de l'IA (par ex. "Ordinateur")
        """
        super().__init__(cName, bIsAI=True)

    def PLRjouer(self):
        """
        Joue automatiquement le meilleur coup.

        L'IA utilise Minimax pour choisir la meilleure option disponible.
        """
        pass

    def PLRfind_best_move(self, tGrid: List[List[TColor]]) -> Tuple[int, int]:
        """
        Trouve la meilleure position où jouer en utilisant Minimax.

        @param tGrid : Grille actuelle du jeu
        @return : Tuple contenant (ligne, colonne) du meilleur coup à jouer
        """
        pass

    def PLRminimax(self, tGrid: List[List[TColor]], bIsMaximizing: bool) -> int:
        """
        Implémente l'algorithme Minimax pour évaluer les coups possibles.

        @param tGrid : Grille du jeu
        @param bIsMaximizing : True si l'IA maximise, False si elle minimise
        @return : Valeur numérique représentant l'évaluation du coup
        """
        pass