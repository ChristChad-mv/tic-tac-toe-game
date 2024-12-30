"""
Module GAME LOGIC

Ce module contient la logique principale du jeu.
Il gère la création et la manipulation de la grille de jeu,
la validation des mouvements, et la vérification des conditions de victoire.

Classes:
    GameLogic: Classe principale gérant la logique du jeu

"""

from enum import Enum
from typing import List

from Player.player import TPlayer
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
        iGLIsize (int): Taille de la grille (par défaut 3x3)
        iGLIwinning_condition (int): Nombre de symboles alignés nécessaires pour gagner
        tGLIgrid (list): Grille de jeu 2D
        move_history (list): Historique des mouvements effectués
    """

    def __init__(self, iGLISize=3, iWinning_condition=3):
        """
        Initialise une nouvelle instance de jeu Tic-tac-toe.

        @param iGLIsize: Taille de la grille (iGLIsize x iGLIsize)
        @type iGLIsize: int
        @param iGLIwinning_condition: Nombre de symboles alignés nécessaires pour gagner
        @type iGLIwinning_condition: int
        """
        self.iGLIsize = iGLISize
        self.iGLIwinning_condition = iWinning_condition
        self.tGLIgrid = self.GLIinitialize_grid()
        self.move_history = []

        # Création des joueurs
        self.oGLIPlayer1 = TPlayerHumain("Jouer 1")
        self.oGLIPlayer2 = TPlayerIA("Ordinateur")
        self.bGLIIsPlayerOneTurn = True  # Commence par le joueur humain

    def GLIinitialize_grid(self) -> List[List[TColor]]:
        """
        Crée une grille vide avec des cellules 'VIDE'.

        @return: Grille de taille iGLIsize x iGLIsize avec des cases vides.
        @rtype: list[list[TColor]]
        """
        tGLIGrid: List[List[TColor]] = []

        for _ in range(self.iGLIsize):
            tRow: List[TColor] = []
            for _ in range(self.iGLIsize):
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
        if 0 <= iRow < self.iGLIsize and 0 <= iCol < self.iGLIsize and self.tGLIgrid[iRow][iCol] == TColor.VIDE:
            self.tGLIgrid[iRow][iCol] = oCurrentPlayer.PLRget_color()
            self.move_history.append((iRow, iCol, oCurrentPlayer.PLRget_color()))

            # On vérifie si on a déjà un gagnant ou pas
            oWinner = self.GLIcheck_winner()
            if oWinner:
                print(f"{oWinner.PLRget_name()} est le gagnant !!")
                return True
            
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

    def GLIresize_grid(self, iNewSize: int):
        """
        Redimensionne la grille à la nouvelle taille spécifiée.
        @param iNewSize: Nouvelle taille de la grille
        """
        if iNewSize >= 3 or iNewSize <= 7:
            self.iGLIsize = iNewSize
            self.tGLIgrid = self.GLIinitialize_grid()
        else:
            print("La taille de la grille doit être comprise entre 3 et 7.")

    def GLIcheck_line(self, iRow: int, iCol: int) -> TPlayer | None:
        """
        Vérifie si une ligne est gagnante en partant de la position (iRow, iCol).
        Elle retourne le joueur qui a gagné si une ligne gagnante est trouvée, sinon elle retourne None.
        La fonction GLIget_player_by_color est utilisée pour obtenir le joueur correspondant à la couleur trouvée.
        
        @param iRow: Index de la ligne
        @param iCol: Index de la colonne
        @return: Le joueur qui a gagné, ou None si aucun joueur n'a gagné
        @rtype: TPlayer | None
        """
        if iCol + self.iGLIwinning_condition > self.iGLIsize:
            return None

        oColor = self.tGLIgrid[iRow][iCol]
        if oColor == TColor.VIDE:
            return None

        for i in range(self.iGLIwinning_condition):
            if self.tGLIgrid[iRow][iCol + i] != oColor:
                return None
            
        return self.GLIget_player_by_color(oColor)

    def GLIcheck_column(self, iRow: int, iCol: int) -> TPlayer | None:
        """
        Vérifie si une colonne est gagnante en partant de la position (iRow, iCol).
        Elle retourne le joueur qui a gagné si une colonne gagnante est trouvée, sinon elle retourne None.
        La fonction GLIget_player_by_color est utilisée pour obtenir le joueur correspondant à la couleur trouvée.
        
        @param iRow: Index de la ligne
        @param iCol: Index de la colonne
        @return: Le joueur qui a gagné, ou None si aucun joueur n'a gagné
        @rtype: TPlayer | None
        """
        if iRow + self.iGLIwinning_condition > self.iGLIsize:
            return None

        oColor = self.tGLIgrid[iRow][iCol]
        if oColor == TColor.VIDE:
            return None

        for i in range(self.iGLIwinning_condition):
            if self.tGLIgrid[iRow + i][iCol] != oColor:
                return None
        return self.GLIget_player_by_color(oColor)

    def GLIcheck_diagonal(self, iRow: int, iCol: int) -> TPlayer | None:
        """
        Vérifie si une diagonale est gagnante en partant de la position (iRow, iCol).
        
        @param iRow: Index de la ligne de départ pour la vérification de la diagonale.
        @param iCol: Index de la colonne de départ pour la vérification de la diagonale.
        @return: Le joueur qui a gagné si une diagonale gagnante est trouvée, sinon None.
        @rtype: TPlayer | None
        """
        # Vérifie la diagonale descendante (de gauche à droite)
        if iRow + self.iGLIwinning_condition <= self.iGLIsize and iCol + self.iGLIwinning_condition <= self.iGLIsize:
            oColor = self.tGLIgrid[iRow][iCol]
            if oColor != TColor.VIDE:
                for i in range(self.iGLIwinning_condition):
                    if self.tGLIgrid[iRow + i][iCol + i] != oColor:
                        return None
                return self.GLIget_player_by_color(oColor)
        
        # Vérifie la diagonale montante (de droite à gauche)
        if iRow + self.iGLIwinning_condition <= self.iGLIsize and iCol - self.iGLIwinning_condition + 1 >= 0:
            oColor = self.tGLIgrid[iRow][iCol]
            if oColor != TColor.VIDE:
                for i in range(self.iGLIwinning_condition):
                    if self.tGLIgrid[iRow + i][iCol - i] != oColor:
                        return None
                return self.GLIget_player_by_color(oColor)
          
        return None
    
    def GLIcheck_draw(self) -> bool:
        """
        La fonction vérifier si on est dans le cas d'un match nul
        Nous parcourons chaque ligne et chaque colonne, si vide... false sinon True
        """
        for iRow in range(self.iGLIsize):
            for iCol in range(self.iGLIsize):
                if self.tGLIgrid[iRow][iCol] == TColor.VIDE:
                    return False

        if self.GLIcheck_winner() is None:
            return True
        
        return False

    def GLIcheck_winner(self) -> TPlayer | None:
        """
        Vérifie si un joueur a gagné.
        """
        for iRow in range(self.iGLIsize):
            for iCol in range(self.iGLIsize):
                oWinner = self.GLIcheck_line(iRow, iCol)
                if oWinner:
                    return oWinner
                
                oWinner = self.GLIcheck_column(iRow, iCol)
                if oWinner:
                    return oWinner
                
                oWinner = self.GLIcheck_diagonal(iRow, iCol)
                if oWinner:
                    return oWinner
                
        return None
  
    def GLIget_player_by_color(self, oColor: TColor) -> TPlayer | None:
        """
        Retourne le joueur correspondant à la couleur spécifiée.
        On prends une couleur en paramètre et on retourne le joueur qui a cette couleur.
        Si c'est pas le joueur 1, c'est le joueur 2 surement.
        @param oColor: Couleur qu'on prends en paramètre

        """
        if self.oGLIPlayer1.PLRget_color() == oColor:
            return self.oGLIPlayer1
        return self.oGLIPlayer2
    
    def GLIreset_game(self):
        """
        Cette fonction rénitialise tout le jeu en trois étapes : 
            - Refait le grille
            - Effaces les historiques des mouvements
            - Remettre le tour à zero - donc l'humain commence
        """
        self.tGLIgrid = self.GLIinitialize_grid()
        self.move_history.clear()
        self.bGLIIsPlayerOneTurn = True


    def GLIundo_move(self):
        """
        UN PEU PLUS COMPLIQUÉ À FAIRE : 
        - considérer l'état
        - 
        """
        pass
    
    def GLIset_players_name(self, sPlayer1_name: str, sPlayer2_name: str): 
        """
        Cette fonction enregistrer les noms des joueurs
        Cela va nous aider pour la GUI. 
        Permettant à la GUI de pouvoir afficher le nom des joueurs
        """
        self.oGLIPlayer1.PLRset_name(sPlayer1_name)
        self.oGLIPlayer2.PLRset_name(sPlayer2_name)