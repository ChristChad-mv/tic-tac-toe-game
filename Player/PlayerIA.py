from Player.player import TPlayer
from typing import List, Tuple
from Player.color import TColor
from game_logic import GameLogic  
from copy import deepcopy

class TPlayerIA(TPlayer):
    """
    Classe représentant un joueur IA

    Hérite de :
    - TPlayer : Reprend les attributs communs à tous les joueurs.

    Spécificités :
    - L'IA n'a pas d'historique de coups (pas de Undo).
    - Implémente Minimax pour choisir les coups automatiquement.
    """

    def __init__(self, cPLRName: str):
        """
        Initialise un joueur IA.

        @param cPLRName : Nom de l'IA (par ex. "Ordinateur")
        """
        super().__init__(cPLRName, bIsAI=True)

    def get_possible_moves(self, game: GameLogic) -> List[Tuple[int, int]]:
        """
        Retourne toutes les cases vides de la grille comme coups possibles.

        @param game : Instance actuelle du jeu
        @return : Liste des coordonnées des cases disponibles
        """
        moves = []
        for row in range(game.iGLIsize):
            for col in range(game.iGLIsize):
                if game.tGLIgrid[row][col] == TColor.VIDE:
                    moves.append((row, col))
        return moves