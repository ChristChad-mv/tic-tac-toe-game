# =====================================================
#               CLASSE TPlayerHumain
# =====================================================
from enum import Enum
from typing import List, Tuple, Optional
from Player.player import TPlayer
from game_logic import GameLogic
from Player.color import TColor

class TPlayerHumain(TPlayer):
    """
    @class TPlayerHumain
    @brief Classe représentant un joueur humain.

    Hérite de TPlayer et ajoute :
      - Un historique des coups (tPLRMoveHistory)
    """

    def __init__(self, cPLRName: str):
        """
        @brief Constructeur de TPlayerHumain.
        @param cPLRName [str] : Nom du joueur humain
        """
        super().__init__(cPLRName, bIsAI=False)
        self.tPLRMoveHistory: List[Tuple[int, int]] = []

    def PLRrecord_move(self, iRow: int, iCol: int) -> None:
        """
        @brief Enregistre un coup joué par le joueur (dans l’historique).
        @param iRow [int] : Ligne du coup
        @param iCol [int] : Colonne du coup
        """
        self.tPLRMoveHistory.append((iRow, iCol))

    def PLRundo_last_move(self) -> Optional[Tuple[int, int]]:
        """
        @brief Annule le dernier coup joué (si existant).
        @return [Tuple[int, int] | None] : (iRow, iCol) du coup annulé, ou None si pas de coup
        """
        if self.tPLRMoveHistory:
            return self.tPLRMoveHistory.pop()
        return None

    def PLRjouer(self, oGameLogic: GameLogic, iRow: int, iCol: int) -> None:
        """
        @brief Le joueur humain demande à jouer via GameLogic,
        et enregistre le coup s’il est validé.
        @param oGameLogic [GameLogic] : Instance de la logique du jeu
        @param iRow [int] : Ligne visée
        @param iCol [int] : Colonne visée
        """
        if oGameLogic.GLImake_move(self, iRow, iCol):
            self.PLRrecord_move(iRow, iCol)