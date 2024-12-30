from Player.color import TColor

class TPlayer:
    """
    Classe de base représentant un joueur de Tic Tac Toe.

    Attributs :
    - cPLRName (str) : Nom du joueur.
    - oPLRColor (TColor) : Couleur du joueur
    - bPLRIsAI (bool) : Indique si le joueur est une IA (True) ou un humain (False).
    """

    def __init__(self, cName: str, bIsAI=False):
        """
        Initialise un joueur avec un nom et définit s'il s'agit d'une IA ou d'un humain.

        @param cName : Nom du joueur
        @param bIsAI : Booléen indiquant si le joueur est une IA (par défaut False)
        """
        self.cPLRName = cName
        self.oPLRColor = None
        self.bPLRIsAI = bIsAI

    def PLRset_color(self, oPlayerColor: TColor):
        """
        Définit la couleur du joueur.

        @param oPlayerColor : Couleur du joueur (TColor)
        """
        self.oPLRColor = oPlayerColor

    def PLRget_color(self) -> TColor:
        """
        Retourne la couleur du joueur.

        @return : TColor (ROUGE, BLEU, ou VIDE)
        """
        return self.oPLRColor

    def PLRget_name(self) -> str:
        """
        Retourne le nom du joueur.

        @return : Nom du joueur (str)
        """
        return self.cPLRName

    def PLRset_name(self, cNewName: str):
        """
        Modifie le nom du joueur.

        @param cNewName : Nouveau nom du joueur
        """
        self.cPLRName = cNewName

    def PLRjouer(self, oGameLogic, iRow: int, iCol: int):
        """
        Le joueur demande à jouer via GameLogic.
        """
        oGameLogic.GLImake_move(self, iRow, iCol)
        