from game_logic import GameLogic
from Player.PlayerIA import TPlayerIA
from Player.color import TColor
from Player.PlayerHumain import TPlayerHumain
from gui import TicTacToeGUI

def main():
    # Initialisation des joueurs
    player1 = TPlayerHumain("Humain")
    player1.PLRset_color(TColor.VERT)
    player2 = TPlayerIA("Ordinateur")
    player2.PLRset_color(TColor.ROUGE)

    game_logic = GameLogic(oPlayer1=player1, oPlayer2=player2, iGLISize=3)

    # Création et lancement de l'interface graphique
    game_gui = TicTacToeGUI(game_logic)
    game_gui.GUI_run()

if __name__ == "__main__":
    main()
