from Player.player import TPlayer
from typing import List, Tuple
from game_logic import GameLogic

class TPlayerHumain(TPlayer):
    """
    Classe représentant un joueur humain.

    Hérite de :
    - TPlayer : Reprend les attributs communs à tous les joueurs.

    Attributs supplémentaires :
    - tPLRMoveHistory (list) : Liste des coups joués par le joueur.
    """

    def __init__(self, cPLRName: str):
        """
        Initialise un joueur humain avec une liste pour l’historique des coups.

        @param cPLRName : Nom du joueur humain
        """
        super().__init__(cPLRName, bIsAI=False)
        self.tPLRMoveHistory: List[Tuple[int, int]] = []

    def PLRrecord_move(self, iRow: int, iCol: int):
        """
        Enregistre un coup joué par le joueur.

        @param iRow : Ligne où le coup est joué
        @param iCol : Colonne où le coup est joué
        """
        self.tPLRMoveHistory.append((iRow, iCol))

    def PLRundo_last_move(self) -> Tuple[int, int] | None:
        """
        Annule le dernier coup joué.

        @return : Tuple contenant (ligne, colonne) du dernier coup annulé, ou None si aucun coup à annuler.
        """
        if self.tPLRMoveHistory:
            return self.tPLRMoveHistory.pop()
        return None

    def PLRjouer(self, oGameLogic: GameLogic, iRow: int, iCol: int):
        """
        Le joueur demande à jouer via GameLogic.
        """
        if oGameLogic.GLImake_move(self, iRow, iCol):
            self.PLRrecord_move(iRow, iCol)
