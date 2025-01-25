# =====================================================
#               MODULE : GAME LOGIC
# =====================================================
#  Ce module contient la logique principale du jeu.
#  Il gère :
#    - La création et la manipulation de la grille
#    - La validation des coups
#    - La vérification des conditions de victoire
#  pour une partie de Tic-tac-toe.
# =====================================================

from typing import List
from Player.player import TPlayer
from Player.color import TColor


class GameLogic:
    """
    @class GameLogic
    @brief Classe principale gérant la logique du jeu Tic-tac-toe.

    Elle implémente toutes les fonctionnalités nécessaires pour
    gérer une partie de Tic-tac-toe :
      - Création de la grille (taille iGLISize x iGLISize)
      - Gestion des coups (GLImake_move, GLIundo_move, etc.)
      - Vérification du vainqueur ou du match nul
      - Gestion de la difficulté et des noms de joueurs (pour la GUI)

    @attention Cette classe ne gère pas l'interface. Elle manipule uniquement la logique.
    """

    # ---------------------------------------------------
    #                CONSTRUCTEUR
    # ---------------------------------------------------

    def __init__(self, oPlayer1: TPlayer = None, oPlayer2: TPlayer = None, iGLISize: int = 3, iGLIWinning_condition: int = 3):
        """
        @brief Initialise une nouvelle instance de la logique du jeu Tic-tac-toe.
        @param oPlayer1 [TPlayer]        : Joueur 1
        @param oPlayer2 [TPlayer]        : Joueur 2
        @param iGLISize [int]            : Taille de la grille (par défaut 3)
        @param iGLIWinning_condition [int]: Nombre de symboles alignés nécessaires pour gagner
        """
        self.iGLISize = iGLISize
        self.iGLIWinning_condition = iGLIWinning_condition
        self.tGLIgrid = self.GLIinitialize_grid()
        self.move_history: List[tuple] = []  # Historique (iRow, iCol, TColor)
        self.difficulty_level: int = 1

        # Joueurs
        self.oGLIPlayer1 = oPlayer1
        self.oGLIPlayer2 = oPlayer2

        # Le joueur 1 commence
        self.bGLIIsPlayerOneTurn: bool = True

    # ---------------------------------------------------
    #         GETTERS / SETTERS / DIFFICULTÉ
    # ---------------------------------------------------

    def GLIget_size(self) -> int:
        """
        @brief Retourne la taille actuelle de la grille.
        @return [int] : iGLISize
        """
        return self.iGLISize

    def GLIset_grid_size(self, iNewSize: int) -> None:
        """
        @brief Définit la taille de la grille (sans redimensionner immédiatement).
        @param iNewSize [int] : Nouvelle taille voulue
        """
        self.iGLISize = iNewSize

    def GLIget_winning_condition(self) -> int:
        """
        @brief Retourne la condition de victoire (nombre de symboles alignés).
        @return [int] : iGLIWinning_condition
        """
        return self.iGLIWinning_condition

    def GLIset_winning_condition(self) -> None:
        """
        @brief Définit la condition de victoire à la taille de la grille (iGLISize).
        """
        self.iGLIWinning_condition = self.iGLISize

    def GLIget_difficulty(self) -> int:
        """
        @brief Retourne le niveau de difficulté actuel.
        @return [int] : difficulty_level
        """
        return self.difficulty_level

    def GLIset_difficulty(self, level: int) -> None:
        """
        @brief Définit un nouveau niveau de difficulté.
        @param level [int] : Nouveau niveau
        """
        self.difficulty_level = level
        print(f"Niveau de difficulté mis à jour : {self.difficulty_level}")

    def GLIincrement_difficulty(self) -> None:
        """
        @brief Augmente le niveau de difficulté d’un cran.
        """
        self.GLIset_difficulty(self.difficulty_level + 1)
        print(f"Nouveau niveau de difficulté : {self.difficulty_level}")

    def GLIreset_difficulty(self) -> None:
        """
        @brief Réinitialise le niveau de difficulté à 1.
        """
        self.GLIset_difficulty(1)
        print("Le niveau de difficulté a été réinitialisé.")

    # ---------------------------------------------------
    #          INITIALISATION / REDIMENSION
    # ---------------------------------------------------

    def GLIinitialize_grid(self) -> List[List[TColor]]:
        """
        Crée une grille vide avec des cellules 'VIDE'.
        On retourne la grille créée.

        @return: Grille de taille iGLISize x iGLISize avec des cases vides.
        """
        tGLIGrid: List[List[TColor]] = []

        for _ in range(self.iGLISize):
            tRow: List[TColor] = []
            for _ in range(self.iGLISize):
                tRow.append(TColor.VIDE)
            tGLIGrid.append(tRow)

        return tGLIGrid

    def GLIresize_grid(self, iNewSize: int) -> None:
        """
        @brief Redimensionne la grille à la nouvelle taille.
        Efface l’historique, remet la main au joueur 1.
        @param iNewSize [int] : Nouvelle taille (entre 3 et 7)
        @throws ValueError si iNewSize n’est pas dans [3, 7].
        """
        if 3 <= iNewSize <= 7:
            self.iGLISize = iNewSize
            self.iGLIWinning_condition = min(iNewSize, self.iGLIWinning_condition)
            self.tGLIgrid = [[TColor.VIDE for _ in range(iNewSize)]
                             for _ in range(iNewSize)]
            self.move_history.clear()
            self.bGLIIsPlayerOneTurn = True
        else:
            raise ValueError("La taille de la grille doit être comprise entre 3 et 7.")

    # ---------------------------------------------------
    #           COUP / TOUR / JOUEUR ACTUEL
    # ---------------------------------------------------

    def GLImake_move(self, oPlayer: TPlayer, iRow: int, iCol: int) -> bool:
        """
        @brief Place la couleur du joueur 'oPlayer' dans la grille.
        @param oPlayer [TPlayer] : Joueur qui effectue le coup
        @param iRow [int]        : Index de la ligne
        @param iCol [int]        : Index de la colonne
        @return True si le mouvement est valide, False sinon.
        @throws ValueError si oPlayer est None
        """
        if oPlayer is None:
            raise ValueError("Le joueur est None. Assurez-vous que les joueurs sont initialisés.")

        oColor = oPlayer.PLRget_color()

        if (0 <= iRow < self.iGLISize and
            0 <= iCol < self.iGLISize and
            self.tGLIgrid[iRow][iCol] == TColor.VIDE):

            self.tGLIgrid[iRow][iCol] = oColor
            self.move_history.append((iRow, iCol, oColor))

            # Vérifier gagnant ou match nul
            oWinner = self.GLIcheck_winner(oColor)
            if oWinner:
                print(f"{oWinner.PLRget_name()} est le gagnant !!")
            elif self.GLIcheck_draw(oColor):
                print("Match nul !")

            self.GLIpass_turn()
            return True

        return False

    def GLIget_current_player(self) -> TPlayer | None:
        """
        @brief Retourne le joueur dont c'est le tour.
        @return [TPlayer | None] : oGLIPlayer1 si c’est son tour, sinon oGLIPlayer2
        """
        return self.oGLIPlayer1 if self.bGLIIsPlayerOneTurn else self.oGLIPlayer2

    def GLIpass_turn(self) -> None:
        """
        @brief Passe au joueur suivant (inversion du booléen bGLIIsPlayerOneTurn).
        """
        self.bGLIIsPlayerOneTurn = not self.bGLIIsPlayerOneTurn

    # ---------------------------------------------------
    #         CHECKS DE LIGNE / COLONNE / DIAGONALE
    # ---------------------------------------------------

    def GLIcheck_line(self, iRow: int, iCol: int, oColor: TColor) -> TPlayer | None:
        """
        @brief Vérifie si une ligne est gagnante à partir de (iRow, iCol).
        @param iRow [int] : Index de la ligne
        @param iCol [int] : Index de la colonne
        @param oColor [TColor] : Couleur du joueur qu’on teste
        @return [TPlayer | None] : Le joueur s’il y a ligne gagnante, sinon None
        """
        if iCol + self.iGLIWinning_condition > self.iGLISize:
            return None

        for i in range(self.iGLIWinning_condition):
            if self.tGLIgrid[iRow][iCol + i] != oColor:
                return None
        return self.GLIget_player_by_color(oColor)

    def GLIcheck_column(self, iRow: int, iCol: int, oColor: TColor) -> TPlayer | None:
        """
        @brief Vérifie si une colonne est gagnante à partir de (iRow, iCol).
        @param iRow [int] : Index de la ligne
        @param iCol [int] : Index de la colonne
        @param oColor [TColor] : Couleur du joueur qu’on teste
        @return [TPlayer | None] : Le joueur s’il y a colonne gagnante, sinon None
        """
        if iRow + self.iGLIWinning_condition > self.iGLISize:
            return None

        for i in range(self.iGLIWinning_condition):
            if self.tGLIgrid[iRow + i][iCol] != oColor:
                return None
        return self.GLIget_player_by_color(oColor)

    def GLIcheck_diagonal(self, iRow: int, iCol: int, oColor: TColor) -> TPlayer | None:
        """
        @brief Vérifie si une diagonale (descendante ou montante) est gagnante
        à partir de (iRow, iCol).
        @param iRow [int] : Ligne de départ
        @param iCol [int] : Colonne de départ
        @param oColor [TColor] : Couleur testée
        @return [TPlayer | None] : Le joueur s’il y a diagonale gagnante, sinon None
        """
        # Diagonale descendante
        if (iRow + self.iGLIWinning_condition <= self.iGLISize and
            iCol + self.iGLIWinning_condition <= self.iGLISize):
            for i in range(self.iGLIWinning_condition):
                if self.tGLIgrid[iRow + i][iCol + i] != oColor:
                    break
            else:
                return self.GLIget_player_by_color(oColor)

        # Diagonale montante
        if (iRow + self.iGLIWinning_condition <= self.iGLISize and
            iCol - self.iGLIWinning_condition + 1 >= 0):
            for i in range(self.iGLIWinning_condition):
                if self.tGLIgrid[iRow + i][iCol - i] != oColor:
                    break
            else:
                return self.GLIget_player_by_color(oColor)

        return None

    # ---------------------------------------------------
    #        CHECK GAGNANT / MATCH NUL
    # ---------------------------------------------------

    def GLIcheck_draw(self, oColor: TColor) -> bool:
        """
        @brief Vérifie si la partie est un match nul.
        @param oColor [TColor] : Couleur du dernier coup
        @return True si le plateau est plein et pas de gagnant, sinon False.
        """
        # Plateau plein ?
        for iRow in range(self.iGLISize):
            for iCol in range(self.iGLISize):
                if self.tGLIgrid[iRow][iCol] == TColor.VIDE:
                    return False

        # Pas de vainqueur ?
        return (self.GLIcheck_winner(oColor) is None)

    def GLIcheck_winner(self, oColor: TColor) -> TPlayer | None:
        """
        @brief Vérifie si un joueur a gagné avec la couleur oColor.
        @param oColor [TColor] : Couleur du joueur
        @return [TPlayer | None] : Le joueur vainqueur ou None.
        """
        for iRow in range(self.iGLISize):
            for iCol in range(self.iGLISize):
                oWinner = self.GLIcheck_line(iRow, iCol, oColor)
                if oWinner:
                    return oWinner

                oWinner = self.GLIcheck_column(iRow, iCol, oColor)
                if oWinner:
                    return oWinner

                oWinner = self.GLIcheck_diagonal(iRow, iCol, oColor)
                if oWinner:
                    return oWinner

        return None

    def GLIget_player_by_color(self, oColor: TColor) -> TPlayer | None:
        """
        @brief Retourne le joueur correspondant à la couleur spécifiée.
        @param oColor [TColor] : Couleur cherchée
        @return [TPlayer | None] : Joueur 1 ou Joueur 2 si match, sinon None
        """
        if self.oGLIPlayer1 and self.oGLIPlayer1.PLRget_color() == oColor:
            return self.oGLIPlayer1
        if self.oGLIPlayer2 and self.oGLIPlayer2.PLRget_color() == oColor:
            return self.oGLIPlayer2
        return None

    # ---------------------------------------------------
    #       RESET / UNDO / NOMS DE JOUEURS
    # ---------------------------------------------------

    def GLIreset_game(self) -> None:
        """
        @brief Réinitialise toute la partie :
          - Regénère la grille (VIDE)
          - Efface l’historique
          - Remet bGLIIsPlayerOneTurn = True
        """
        self.tGLIgrid = self.GLIinitialize_grid()
        self.move_history.clear()
        self.bGLIIsPlayerOneTurn = True

    def GLIundo_move(self) -> bool:
        """
        @brief Annule le dernier coup joué (si possible).
        @return True si un coup a été annulé, False sinon.
        """
        if not self.move_history:
            print("Aucun mouvement à annuler.")
            return False

        iRow, iCol, _ = self.move_history.pop()
        self.tGLIgrid[iRow][iCol] = TColor.VIDE
        self.bGLIIsPlayerOneTurn = not self.bGLIIsPlayerOneTurn
        return True

    def GLIset_players_name(self, sPlayer1_name: str, sPlayer2_name: str) -> None:
        """
        @brief Enregistre (modifie) les noms des deux joueurs.
        @param sPlayer1_name [str] : Nouveau nom pour le joueur 1
        @param sPlayer2_name [str] : Nouveau nom pour le joueur 2
        """
        if self.oGLIPlayer1:
            self.oGLIPlayer1.PLRset_name(sPlayer1_name)
        if self.oGLIPlayer2:
            self.oGLIPlayer2.PLRset_name(sPlayer2_name)
