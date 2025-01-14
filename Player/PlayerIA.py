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

    def PLRget_possible_moves(self, game: GameLogic) -> List[Tuple[int, int]]:
        """
        Retourne toutes les cases vides de la grille comme coups possibles.

        @param game : Instance actuelle du jeu
        @return : Liste des coordonnées des cases disponibles
        """
        moves = []
        for row in range(game.iGLISize):
            for col in range(game.iGLISize):
                if game.tGLIgrid[row][col] == TColor.VIDE:
                    moves.append((row, col))
        return moves
    
    def PLRsimulate_move(self, game: GameLogic, row: int, col: int) -> GameLogic:
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
    
    def PLRminimax(self, game: GameLogic, iGMdepth: int, bPLRisMaximizing: bool) -> Tuple[int, Tuple[int, int] | None]:
        """
        Implémente l'algorithme Minimax pour évaluer les coups possibles.

        @param game : Instance du jeu 
        @param iGMdepth : Profondeur actuelle de la recherche Minimax
        @param bPLRisMaximizing : Booléen indiquant si l'on maximise (True) ou minimise (False) le score
        @return : Tuple contenant le meilleur score et le meilleur mouvement (ligne, colonne)
        """
        
        if game.GLIcheck_winner(self.PLRget_color()):
            return 10, None
        elif game.GLIcheck_winner(game.oGLIPlayer1.PLRget_color()):
            return -10, None
        elif game.GLIcheck_draw(self.PLRget_color()) or iGMdepth == 0:
            return 0, None

        possible_moves = self.PLRget_possible_moves(game)
        
        if bPLRisMaximizing:
            best_score = float('-inf')
            best_move = None
            for row, col in possible_moves:
                simulated_game = self.PLRsimulate_move(game, row, col)
                score, _ = self.PLRminimax(simulated_game, iGMdepth - 1, False)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for row, col in possible_moves:
                simulated_game = self.PLRsimulate_move(game, row, col)
                score, _ = self.PLRminimax(simulated_game, iGMdepth - 1, True)
                if score < best_score:
                    best_score = score
                    best_move = (row, col)
            return best_score, best_move
        
    def PLRjouer(self, game: GameLogic):
        """
        Joue automatiquement le meilleur coup.

        L'IA utilise Minimax pour choisir la meilleure option disponible.
        @param game : Instance actuelle du jeu (GameLogic)
        """
        """L'IA joue en utilisant Minimax avec la profondeur ajustée au niveau."""
        iGMdepth = game.GLIget_difficulty()
        print(f"L'IA joue avec une profondeur de {iGMdepth }.")
        _, best_move = self.PLRminimax(game, iGMdepth=iGMdepth , bPLRisMaximizing=True)
        
        if best_move:
            game.GLImake_move(self, best_move[0], best_move[1])