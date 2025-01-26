# ==========================================================
#               CLASSE : TCOLOR
# ==========================================================
#  Ce module a essentiellement but de founir des couleurs
#  aux joueurs pour leurs choix avant un jeu.
# ==========================================================


from enum import Enum

class TColor(Enum):
    VIDE = 0
    ROUGE = 1
    BLEU = 2
    VERT = 3
    JAUNE = 4
    ORANGE = 5
    GREY = 6

    @property
    def tkinter_color(self):
        """Retourne la couleur Tkinter correspondante"""
        color_mapping = {
            TColor.VIDE: "white",
            TColor.ROUGE: "red",
            TColor.BLEU: "blue",
            TColor.VERT: "green",
            TColor.JAUNE: "yellow",
            TColor.ORANGE: "orange",
            TColor.GREY: "grey"
        }
        return color_mapping[self]