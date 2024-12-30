from game_logic import GameLogic
from Player.color import TColor
from Player.player import TPlayer

def main():
    player1 = TPlayer("Christ", False)
    player2 = TPlayer("Chadrak", False)

    player1.PLRset_color(TColor.ROUGE)
    player2.PLRset_color(TColor.BLEU)

    game = GameLogic(player1, player2, iGLISize=3, iWinning_condition=3)

    print("Début de la partie !")
    display_grid(game.tGLIgrid)

    # Les joueurs jouent via GameLogic
    player1.PLRjouer(game, 0, 0)  # Christ joue
    display_grid(game.tGLIgrid)

    player2.PLRjouer(game, 0, 1)  # Chadrak joue
    display_grid(game.tGLIgrid)

    player1.PLRjouer(game, 1, 1)  # Christ joue
    display_grid(game.tGLIgrid)

    player2.PLRjouer(game, 1, 0)  # Chadrak joue
    display_grid(game.tGLIgrid)

    player1.PLRjouer(game, 2, 2)  # Christ joue
    display_grid(game.tGLIgrid)

    # Vérification du gagnant
    winner = game.GLIcheck_winner()
    if winner:
        print(f"{winner.PLRget_name()} a gagné la partie !")
    else:
        print("Pas encore de gagnant...")

    nul = game.GLIcheck_draw()
    if nul:
        print("Match Nul")

    # Tester la réinitialisation du jeu
    print("\nRéinitialisation de la partie...")
    game.GLIreset_game()
    display_grid(game.tGLIgrid)
    print("La partie a été réinitialisée. 😊")

# Fonction pour afficher la grille
# Devrait être passer à la gui
def display_grid(grid):
    for row in grid:
        print(" | ".join(cell.value if isinstance(cell, TColor) else " " for cell in row))
    print("\n" + "-" * (len(grid) * 4 - 1) + "\n")

if __name__ == "__main__":
    main()