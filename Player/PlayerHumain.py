from Player.player import TPlayer
from typing import List, Tuple

class TPlayerHumain(TPlayer):
    """
    Classe représentant un joueur humain.

    Hérite de :
    - TPlayer : Reprend les attributs communs à tous les joueurs.

    Attributs supplémentaires :
    - tPLRMoveHistory (list) : Liste des coups joués par le joueur pour permettre l'annulation (Undo).
    """

    def __init__(self, cName: str):
        """
        Initialise un joueur humain avec une liste pour l’historique des coups.

        @param cName : Nom du joueur humain
        """
        super().__init__(cName, bIsAI=False)
        self.tPLRMoveHistory: List[Tuple[int, int]] = []

    def PLRrecord_move(self, iRow: int, iCol: int):
        """
        Enregistre un coup joué par le joueur.

        @param iRow : Ligne où le coup est joué
        @param iCol : Colonne où le coup est joué
        """
        pass

    def PLRundo_last_move(self) -> Tuple[int, int] | None:
        """
        Annule le dernier coup joué.

        @return : Tuple contenant (ligne, colonne) du dernier coup annulé, ou None si aucun coup à annuler.
        """
        pass

    def PLRjouer(self, oGameLogic, iRow: int, iCol: int):
        """
        Le joueur demande à jouer via GameLogic.
        """
        oGameLogic.GLImake_move(self, iRow, iCol)
