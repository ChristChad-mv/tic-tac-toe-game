from game_logic import GameLogic
from Player.player import TPlayer
from Player.PlayerIA import TPlayerIA
from Player.color import TColor
from Player.PlayerHumain import TPlayerHumain


def afficher_grille(game: GameLogic):
    """
    Affiche la grille actuelle du jeu dans la console.
    """
    print("\nÉtat actuel de la grille :")
    print("  " + " ".join(str(i) for i in range(game.iGLIsize)))  # Affiche les numéros de colonnes
    for i, row in enumerate(game.tGLIgrid):
        print(f"{i} " + " | ".join(cell.name if cell != TColor.VIDE else "_" for cell in row))
        if i < game.iGLIsize - 1:
            print("  " + "-" * (game.iGLIsize * 4 - 1))


def joueur_humain_joue(game: GameLogic, player: TPlayer):
    """
    Gère le tour du joueur humain.
    """
    while True:
        try:
            print(f"\nJoueur {player.PLRget_name()} ({player.PLRget_color().name})")
            iRow = int(input(f"Entrez la ligne (0-{game.iGLIsize-1}) : "))
            iCol = int(input(f"Entrez la colonne (0-{game.iGLIsize-1}) : "))

            if 0 <= iRow < game.iGLIsize and 0 <= iCol < game.iGLIsize:
                if game.tGLIgrid[iRow][iCol] == TColor.VIDE:
                    return game.GLImake_move(player, iRow, iCol)
                else:
                    print("❌ Cette case est déjà occupée !")
            else:
                print(f"❌ Position invalide ! Choisissez entre 0 et {game.iGLIsize-1}")
        except ValueError:
            print("❌ Veuillez entrer des nombres valides !")


def partie_terminee(game: GameLogic) -> bool:
    """
    Vérifie si la partie est terminée.
    """
    if game.bGLIIsPlayerOneTurn:
        last_player = game.oGLIPlayer2
    else :
        last_player = game.oGLIPlayer1
        
    last_color = last_player.PLRget_color()
    
    if game.GLIcheck_winner(last_color):
        print(f"\n🏆 {last_player.PLRget_name()} a gagné !")
        return True
    elif game.GLIcheck_draw(last_color):
        print("\n🤝 Match nul !")
        return True
    return False


def main():
    # Initialisation des joueurs
    player1 = TPlayerHumain("Humain")
    player1.PLRset_color(TColor.ROUGE)
    ia = TPlayerIA("Ordinateur")
    ia.PLRset_color(TColor.BLEU)

    # Initialisation du jeu
    game = GameLogic(player1, ia, iGLISize=3, iWinning_condition=3)

    print("\n=== Bienvenue dans le Tic-Tac-Toe ! ===")
    print(f"Vous jouez avec {player1.PLRget_color().name} contre l'IA ({ia.PLRget_color().name})")
    afficher_grille(game)

    while True:
        # Tour du joueur humain
        joueur_humain_joue(game, player1)
        afficher_grille(game)
        if partie_terminee(game):
            break

        # Tour de l'IA
        print("\n💭 L'ordinateur réfléchit...")
        ia.PLRjouer(game)
        afficher_grille(game)
        if partie_terminee(game):
            break

    print("\n=== Fin de la partie ! ===")
    rejouer = input("\nVoulez-vous rejouer ? (o/n) : ").lower()
    if rejouer == 'o':
        print("\n" + "="*40 + "\n")
        main()


if __name__ == "__main__":
    main()
