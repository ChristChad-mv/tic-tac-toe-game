# =====================================================
#               CLASSE TPlayerIA
# =====================================================
from enum import Enum
from typing import List, Tuple, Optional
from Player.player import TPlayer
from game_logic import GameLogic

from Player.color import TColor

class TPlayerIA(TPlayer):
    """
    @class TPlayerIA
    @brief Classe représentant un joueur IA (Intelligence Artificielle).

    Hérite de TPlayer et :
      - Ne conserve aucun historique (pas d’undo).
      - Implémente la logique du Minimax pour choisir automatiquement ses coups.
    """

    def __init__(self, cPLRName: str):
        """
        @brief Constructeur de TPlayerIA.
        @param cPLRName [str] : Nom de l'IA (ex. \"Ordinateur\")
        """
        super().__init__(cPLRName, bIsAI=True)

    # ---------------------------------------------------
    #           MOUVEMENTS POSSIBLES
    # ---------------------------------------------------

    def PLRget_possible_moves(self, game: GameLogic) -> List[Tuple[int, int]]:
        """
        @brief Retourne toutes les cases vides (TColor.VIDE) de la grille.
        @param game [GameLogic] : Instance courante du jeu
        @return [List[Tuple[int, int]]] : Liste des coordonnées (row, col) disponibles
        """
        moves = []
        for row in range(game.iGLISize):
            for col in range(game.iGLISize):
                if game.tGLIgrid[row][col] == TColor.VIDE:
                    moves.append((row, col))
        return moves

    def PLRsimulate_move(self, game: GameLogic, row: int, col: int) -> GameLogic:
        """
        @brief Simule un mouvement dans une copie de GameLogic,
        pour évaluer les conséquences du coup (Minimax).
        @param game [GameLogic] : Instance courante du jeu
        @param row [int] : Ligne du coup
        @param col [int] : Colonne du coup
        @return [GameLogic] : Nouvelle instance (copie) après simulation
        """
        from copy import deepcopy
        simulated_game = deepcopy(game)

        # On place la couleur correspondante directement
        if simulated_game.bGLIIsPlayerOneTurn:
            simulated_game.tGLIgrid[row][col] = simulated_game.oGLIPlayer1.PLRget_color()
        else:
            simulated_game.tGLIgrid[row][col] = simulated_game.oGLIPlayer2.PLRget_color()

        # On change de joueur
        simulated_game.bGLIIsPlayerOneTurn = not simulated_game.bGLIIsPlayerOneTurn
        return simulated_game

    # ---------------------------------------------------
    #                  MINIMAX
    # ---------------------------------------------------

    def PLRminimax(self,
                   game: GameLogic,
                   iGMdepth: int,
                   bPLRisMaximizing: bool) -> Tuple[int, Tuple[int, int] | None]:
        """
        @brief Algorithme Minimax pour évaluer le meilleur coup.
        @param game [GameLogic]        : Instance du jeu à évaluer
        @param iGMdepth [int]          : Profondeur de recherche
        @param bPLRisMaximizing [bool] : True si on cherche à maximiser le score, False sinon
        @return [Tuple(int, (int,int) | None)] :
                - Le meilleur score possible
                - Les coordonnées (row, col) du coup idéal ou None
        """
        # Vérifier si l’IA a gagné
        if game.GLIcheck_winner(self.PLRget_color()):
            return 10, None
        # Vérifier si l’adversaire (humain) a gagné
        elif game.GLIcheck_winner(game.oGLIPlayer1.PLRget_color()):
            return -10, None
        # Vérifier le match nul ou profondeur 0 (pas d’évaluation plus poussée)
        elif game.GLIcheck_draw(self.PLRget_color()) or iGMdepth == 0:
            return 0, None

        possible_moves = self.PLRget_possible_moves(game)

        if bPLRisMaximizing:
            best_score = float('-inf')
            best_move = None
            for (row, col) in possible_moves:
                simulated_game = self.PLRsimulate_move(game, row, col)
                score, _ = self.PLRminimax(simulated_game, iGMdepth - 1, False)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for (row, col) in possible_moves:
                simulated_game = self.PLRsimulate_move(game, row, col)
                score, _ = self.PLRminimax(simulated_game, iGMdepth - 1, True)
                if score < best_score:
                    best_score = score
                    best_move = (row, col)
            return best_score, best_move

    # ---------------------------------------------------
    #                JOUER (IA)
    # ---------------------------------------------------

    def PLRjouer(self, game: GameLogic) -> None:
        """
        @brief Joue automatiquement le meilleur coup selon Minimax.
        @param game [GameLogic] : Instance courante du jeu
        """
        iGMdepth = game.GLIget_difficulty()
        print(f"L'IA {self.PLRget_name()} joue avec une profondeur de {iGMdepth}.")

        best_score, best_move = self.PLRminimax(
            game,
            iGMdepth=iGMdepth,
            bPLRisMaximizing=True
        )

        if best_move:
            game.GLImake_move(self, best_move[0], best_move[1])
        else:
            print("Aucun coup possible pour l’IA.")