# ==========================================================
#               MODULE : PLAYER
# ==========================================================
#  Ce module contient la classe Mère Player qui 
#  représente un joueur spécifique et qui sera utilisée
#  pour servir de base pour les modules/classes PlayerAI
#  et PlayerHumain. 
#
#  Implémente les setters/getters nous donnant la 
#  possibilité d'avoir accès à des propriétés de la 
#  classe et le méthode abstraite jouer qui sera
#  implémenté différement selon les Player (AI ou Humain)
# ==========================================================

from enum import Enum
from typing import List, Tuple, Optional
from Player.color import TColor


# =====================================================
#               CLASSE TPlayer
# =====================================================

class TPlayer:
    """
    @class TPlayer
    @brief Classe Mère représentant un joueur de Tic Tac Toe.

    Attributs :
      - cPLRName  (str)   : Nom du joueur
      - oPLRColor (TColor): Couleur du joueur (ou None si non définie)
      - bPLRIsAI  (bool)  : Indique si le joueur est une IA (True) ou un humain (False)
    """

    def __init__(self, cPLRName: str, bIsAI: bool = False):
        """
        @brief Constructeur de TPlayer.
        @param cPLRName [str] : Nom du joueur
        @param bIsAI   [bool] : True si c’est un joueur IA, False sinon (par défaut)
        """
        self.cPLRName: str = cPLRName
        self.oPLRColor = None
        self.bPLRIsAI: bool = bIsAI

    # ---------------------------------------------------
    #                GETTERS / SETTERS
    # ---------------------------------------------------

    def PLRget_name(self) -> str:
        """
        @brief Retourne le nom du joueur.
        @return [str] : Nom du joueur
        """
        return self.cPLRName

    def PLRset_name(self, cPLRNewName: str) -> None:
        """
        @brief Modifie le nom du joueur.
        @param cPLRNewName [str] : Nouveau nom du joueur
        """
        self.cPLRName = cPLRNewName

    def PLRget_color(self):
        """
        @brief Retourne la couleur du joueur (TColor).
        @return [TColor | None] : Couleur actuelle ou None
        """
        return self.oPLRColor

    def PLRset_color(self, oPlayerColor):
        """
        @brief Définit la couleur du joueur.
        @param oPlayerColor [TColor] : Nouvelle couleur
        """
        self.oPLRColor = oPlayerColor

    def PLRis_ai(self) -> bool:
        """
        @brief Indique si le joueur est une IA.
        @return [bool] : True si IA, False sinon
        """
        return self.bPLRIsAI

    def PLRset_ai(self, bIsAI: bool) -> None:
        """
        @brief Modifie le statut IA ou humain du joueur.
        @param bIsAI [bool] : True pour IA, False pour humain
        """
        self.bPLRIsAI = bIsAI

    # ---------------------------------------------------
    #           MÉTHODE DE JEU
    # ---------------------------------------------------

    def PLRjouer(self, oGameLogic, iRow: int, iCol: int) -> None:
        """
        @brief Méthode basique : le joueur demande à jouer via GameLogic.
        @param oGameLogic [GameLogic] : Instance de la logique de jeu
        @param iRow [int] : Ligne cible
        @param iCol [int] : Colonne cible
        """
        oGameLogic.GLImake_move(self, iRow, iCol)
