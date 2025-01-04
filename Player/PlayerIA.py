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
    
    def generate_grid_based_on_next_move(self, game: GameLogic, row: int, col: int) -> GameLogic:
        """
        Génère une nouvelle instance du jeu en simulant un coup.
        """
        simulated_game = deepcopy(game)
        
        # Modification directe de la grille pour la simulation
        if simulated_game.bGLIIsPlayerOneTurn:
            simulated_game.tGLIgrid[row][col] = simulated_game.oGLIPlayer1.PLRget_color()
        else:
            simulated_game.tGLIgrid[row][col] = simulated_game.oGLIPlayer2.PLRget_color()
        
        simulated_game.bGLIIsPlayerOneTurn = not simulated_game.bGLIIsPlayerOneTurn
        return simulated_game