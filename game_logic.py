"""
Module GAME LOGIC

Ce module contient la logique principale du jeu.
Il gère la création et la manipulation de la grille de jeu,
la validation des mouvements, et la vérification des conditions de victoire.

Classes:
    GameLogic: Classe principale gérant la logique du jeu

"""

from enum import Enum
from typing import List, Tuple

from Player.PlayerHumain import TPlayerHumain
from Player.PlayerIA import TPlayerIA

class TColor(Enum):
    """
    Énumération des couleurs disponibles pour les joueurs.
    """
    ROUGE = "rouge"
    BLEU = "bleu"
    VERT = "vert"
    JAUNE = "jaune"
    VIDE = " "  # Utilisé pour les cases vides


class GameLogic:
    """
    Classe gérant la logique du jeu Tic-tac-toe.
    
    Cette classe implémente toutes les fonctionnalités nécessaires pour
    gérer une partie de Tic-tac-toe, incluant la création de la grille,
    la gestion des mouvements et la vérification des conditions de victoire.

    Attributes:
        size (int): Taille de la grille (par défaut 3x3)
        winning_condition (int): Nombre de symboles alignés nécessaires pour gagner
        grid (list): Grille de jeu 2D
        move_history (list): Historique des mouvements effectués
    """

    def __init__(self, size=3, winning_condition=3):
        """
        Initialise une nouvelle instance de jeu Tic-tac-toe.

        @param size: Taille de la grille (size x size)
        @type size: int
        @param winning_condition: Nombre de symboles alignés nécessaires pour gagner
        @type winning_condition: int
        """
        self.size = size
        self.winning_condition = winning_condition
        self.grid = self.initialize_grid()
        self.move_history = []

        # Création des joueurs
        self.oGLIPlayer1 = TPlayerHumain("Christ")
        self.oGLIPlayer2 = TPlayerIA("Ordinateur")
        self.bGLIIsPlayerOneTurn = True  # Commence par le joueur humain

    def GLIinitialize_grid(self) -> List[List[TColor]]:
        """
        Crée une grille vide avec des cellules 'VIDE'.

        @return: Grille de taille iGLISize x iGLISize avec des cases vides.
        @rtype: list[list[TColor]]
        """
        tGLIGrid: List[List[TColor]] = []

        for _ in range(self.iGLISize):
            tRow: List[TColor] = []
            for _ in range(self.iGLISize):
                tRow.append(TColor.VIDE)
            tGLIGrid.append(tRow)

        return tGLIGrid


    def GLImake_move(self, iRow: int, iCol: int, oColor: TColor) -> bool:
        """
        Place une couleur dans la grille à la position spécifiée.

        @param iRow: Index de la ligne
        @param iCol: Index de la colonne
        @param oColor: Couleur du joueur (TColor.ROUGE, TColor.BLEU, etc.)
        @return: True si le mouvement est valide, False sinon
        @rtype: bool
        """
        oCurrentPlayer = self.GLIget_current_player()
        if 0 <= iRow < self.size and 0 <= iCol < self.size and self.grid[iRow][iCol] == TColor.VIDE:
            self.grid[iRow][iCol] = oCurrentPlayer.PLRget_color()
            self.move_history.append((iRow, iCol, oCurrentPlayer.PLRget_color()))
            self.GLIpass_turn()
            return True
        return False
    
    def GLIget_current_player(self):
        """
        Retourne le joueur dont c'est le tour de jouer.
        Si c'est le tour du joueur 1 (humain), retourne oGLIPlayer1.
        Sinon, c'est au tour de l'IA (oGLIPlayer2).
        """
        if self.bGLIIsPlayerOneTurn:
            return self.oGLIPlayer1
        else:
            return self.oGLIPlayer2

    def GLIpass_turn(self):
        """
        Passe au joueur suivant après chaque coup.
        Si c'était le tour du joueur 1, passe au joueur 2 en mettant bGLIIsPlayerOneTurn à False.
        Si c'était le tour du joueur 2, repasse au joueur 1 en mettant bGLIIsPlayerOneTurn à True.
        """
        if self.bGLIIsPlayerOneTurn:
            self.bGLIIsPlayerOneTurn = False
        else:
            self.bGLIIsPlayerOneTurn = True