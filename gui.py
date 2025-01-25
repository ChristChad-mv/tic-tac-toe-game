# =====================================================
#  TIC-TAC-TOE GUI
# =====================================================
#  Ce module gère l’interface graphique (Tkinter) du jeu.
#  Il contient :
#    - Une fenêtre principale
#    - Trois écrans (home, settings, game)
#    - La logique d’affichage / mise à jour de la grille
#    - Les méthodes de gestion des événements (clics, undo, etc.)
# =====================================================

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from game_logic import GameLogic
from Player.color import TColor
import random


class TicTacToeGUI:
    """
    @class TicTacToeGUI
    @brief Classe gérant l’interface graphique du jeu Tic-Tac-Toe.
    
    Cette classe utilise le module Tkinter pour afficher :
    - Un écran d’accueil (Home)
    - Un écran de paramètres (Settings)
    - Un écran de jeu (Game)
    
    Les actions de l’utilisateur (clic sur une case, undo, etc.) sont gérées ici,
    et affectent directement la logique du jeu fournie par GameLogic.
    """

    # ---------------------------------------------------
    #                CONSTRUCTEUR
    # ---------------------------------------------------
    
    def __init__(self, game_logic: GameLogic):
        """
        @brief Constructeur de l’interface graphique.
        @param game_logic [GameLogic] : Instance de la logique du jeu.
        
        Initialise la fenêtre principale et configure les trois frames
        (home, settings, game). Affiche l’écran d’accueil par défaut.
        """
        # Fenêtre principale
        self.GUI_fenetre = tk.Tk()
        self.GUI_fenetre.title("TIC-TAC-TOE")
        self.GUI_fenetre.geometry("800x800")
        self.GUI_fenetre.resizable(width=False, height=False)

        # Logique de jeu
        self.GUI_game_logic = game_logic
        self.GUI_grid_size = self.GUI_game_logic.iGLISize

        # Frames
        self.GUI_current_frame = None
        self.GUI_frame_home = tk.Frame(self.GUI_fenetre)
        self.GUI_frame_settings = tk.Frame(self.GUI_fenetre)
        self.GUI_frame_game = tk.Frame(self.GUI_fenetre)

        # Initialisation des trois écrans
        self.GUI_init_home_frame()
        self.GUI_init_settings_frame()
        self.GUI_init_game_frame()

        # Afficher l'accueil au démarrage
        self.GUI_display_frame(self.GUI_frame_home)

    # ---------------------------------------------------
    #                NAVIGATION (FRAMES)
    # ---------------------------------------------------
    
    def GUI_display_frame(self, frame: tk.Frame) -> None:
        """
        @brief Affiche une frame spécifique (home, settings ou game).
        @param frame [tk.Frame] : La frame à afficher.
        """
        if self.GUI_current_frame is not None:
            self.GUI_current_frame.pack_forget()
        frame.pack(fill="both", expand=True)
        self.GUI_current_frame = frame

    # ---------------------------------------------------
    #              HOME FRAME
    # ---------------------------------------------------
    
    def GUI_init_home_frame(self) -> None:
        """
        @brief Initialise la page d’accueil (HOME).
        Charge une image de fond et propose trois options :
          - Jouer : passe à l’écran de jeu
          - Paramètres : passe à l’écran de configuration
          - Quitter : ferme l’application
        """
        self.GUI_frame_home.configure(bg="#29417d")

        # Charger et afficher l'image de fond
        self.bg_image = Image.open("picture.jpg") 
        self.bg_image = self.bg_image.resize((800, 800), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Label d'arrière-plan
        self.bg_label = tk.Label(self.GUI_frame_home, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Conteneur des boutons
        button_frame = tk.Frame(self.GUI_frame_home, bg="#29417d")
        button_frame.place(relx=0.5, rely=0.3, anchor="center")

        tk.Label(button_frame,
                 text="Bienvenue à Tic Tac Toe!",
                 font=("Arial", 24),
                 bg="#29417d",
                 fg="white").pack(pady=20)

        tk.Button(button_frame,
                  text="Jouer",
                  command=lambda: self.GUI_display_frame(self.GUI_frame_game),
                  font=("Arial", 14),
                  bg="#7683e7",
                  fg="white",
                  width=20,
                  height=2).pack(pady=10)

        tk.Button(button_frame,
                  text="Paramètres",
                  command=lambda: self.GUI_display_frame(self.GUI_frame_settings),
                  font=("Arial", 14),
                  bg="#7683e7",
                  fg="white",
                  width=20,
                  height=2).pack(pady=10)

        tk.Button(button_frame,
                  text="Quitter",
                  command=self.GUI_fenetre.quit,
                  font=("Arial", 14),
                  bg="red",
                  fg="white",
                  width=20,
                  height=2).pack(pady=10)

    # ---------------------------------------------------
    #              SETTINGS FRAME
    # ---------------------------------------------------
    
    def GUI_init_settings_frame(self) -> None:
        """
        @brief Initialise la page des paramètres.
        Permet de configurer :
          - Le nom du joueur
          - La taille de la grille (3, 5 ou 7)
          - L’option de griser certaines cases
          - La couleur du joueur
        """
        self.GUI_frame_settings.configure(bg="#384b7a")

        tk.Label(self.GUI_frame_settings,
                 text="Paramètres du jeu",
                 font=("Arial", 24),
                 bg="#384b7a",
                 fg="white").pack(pady=20)

        # Nom du joueur
        tk.Label(self.GUI_frame_settings,
                 text="Nom du Joueur:",
                 font=("Arial", 14),
                 bg="#384b7a",
                 fg="white").pack(pady=5)

        player_name_var = tk.StringVar(value="Joueur 1")
        tk.Entry(self.GUI_frame_settings,
                 textvariable=player_name_var,
                 font=("Arial", 12),
                 bg="#ffffff",
                 width=20).pack(pady=5)

        # Taille de la grille
        tk.Label(self.GUI_frame_settings,
                 text="Taille de la grille:",
                 font=("Arial", 14),
                 bg="#384b7a",
                 fg="white").pack(pady=5)

        grid_size_var = tk.IntVar(value=self.GUI_grid_size)
        size_options = [3, 5, 7]
        size_dropdown = tk.OptionMenu(self.GUI_frame_settings, grid_size_var, *size_options)
        size_dropdown.config(font=("Arial", 12), bg="#384b7a", fg="white", width=15)
        size_dropdown.pack(pady=5)

        # Option : griser des cases ?
        tk.Label(self.GUI_frame_settings,
                 text="Griser des cases ? :",
                 font=("Arial", 14),
                 bg="#384b7a",
                 fg="white").pack(pady=5)

        checkbox_frame = tk.Frame(self.GUI_frame_settings, bg="#384b7a")
        checkbox_frame.pack(pady=5)
        checkbox_var = tk.BooleanVar(value=False)
        self.GUI_frame_settings.checkbox_var = checkbox_var

        tk.Radiobutton(checkbox_frame,
                       text="Oui",
                       variable=checkbox_var,
                       value=True,
                       font=("Arial", 12),
                       bg="#384b7a",
                       selectcolor="lightgrey").pack(side="left", padx=10)

        tk.Radiobutton(checkbox_frame,
                       text="Non",
                       variable=checkbox_var,
                       value=False,
                       font=("Arial", 12),
                       bg="#384b7a",
                       selectcolor="lightgrey").pack(side="left", padx=10)

        # Type de grisage (Random / Pyramid)
        tk.Label(self.GUI_frame_settings,
                 text="Type de grisage :",
                 font=("Arial", 14),
                 bg="#384b7a",
                 fg="white").pack(pady=5)

        choicebox_frame = tk.Frame(self.GUI_frame_settings, bg="#384b7a")
        choicebox_frame.pack(pady=5)
        choicebox_var = tk.StringVar()

        tk.Radiobutton(choicebox_frame,
                       text="Random",
                       variable=choicebox_var,
                       value="Random",
                       font=("Arial", 12),
                       bg="#384b7a",
                       selectcolor="lightgrey").pack(side="left", padx=10)

        tk.Radiobutton(choicebox_frame,
                       text="Pyramid",
                       variable=choicebox_var,
                       value="Pyramid",
                       font=("Arial", 12),
                       bg="#384b7a",
                       selectcolor="lightgrey").pack(side="left", padx=10)

        # Nombre de cases à griser (pour Random)
        tk.Label(self.GUI_frame_settings,
                 text="nombre de cases à griser (random)",
                 font=("Arial", 14),
                 bg="#384b7a",
                 fg="white").pack(pady=5)

        number_case_var = tk.IntVar()
        tk.Entry(self.GUI_frame_settings,
                 textvariable=number_case_var,
                 font=("Arial", 12),
                 bg="#ffffff",
                 width=10).pack(pady=5)

        # Couleur du joueur
        tk.Label(self.GUI_frame_settings,
                 text="Choisir la couleur du joueur :",
                 font=("Arial", 14),
                 bg="#384b7a",
                 fg="white").pack(pady=5)

        color_var = tk.StringVar(value="Bleu")
        color_options = ["Bleu", "Vert", "Jaune", "Orange"]
        color_dropdown = tk.OptionMenu(self.GUI_frame_settings, color_var, *color_options)
        color_dropdown.config(font=("Arial", 12), bg="#384b7a", fg="white", width=15)
        color_dropdown.pack(pady=5)

        # Bouton "Jouer"
        tk.Button(self.GUI_frame_settings,
                  text="Jouer",
                  command=lambda: self.GUI_apply_settings(player_name_var.get(),
                                                          grid_size_var.get(),
                                                          checkbox_var.get(),
                                                          color_var.get(),
                                                          choicebox_var.get(),
                                                          number_case_var.get()),
                  font=("Arial", 14),
                  bg="#7683e7",
                  fg="white",
                  width=15,
                  height=2).pack(pady=10)

    def GUI_apply_settings(self,
                           player_name: str,
                           grid_size: int,
                           checkbox: bool,
                           color: str,
                           choicebox_value: str,
                           number_case_var: int) -> None:
        """
        @brief Applique les paramètres et démarre le jeu.
        @param player_name [str] : Nom du joueur
        @param grid_size [int] : Taille de la grille (3, 5 ou 7)
        @param checkbox [bool] : Indique si on veut griser des cases
        @param color [str] : Couleur choisie pour le joueur (Vert, Jaune, Orange, etc.)
        @param choicebox_value [str] : Type de grisage (Random, Pyramid), None si aucun
        @param number_case_var [int] : Nombre de cases à griser (pour l’option Random)
        """
        if checkbox is None:
            choicebox_value = None
            number_case_var = None

        color_mapping = {
            "Rouge": TColor.ROUGE,
            "Bleu": TColor.BLEU,
            "Vert": TColor.VERT,
            "Jaune": TColor.JAUNE,
            "Orange": TColor.ORANGE
        }

        # Mise à jour de la logique
        self.GUI_game_logic.GLIset_players_name(player_name, "Ordinateur")
        self.GUI_game_logic.oGLIPlayer1.PLRset_color(color_mapping[color])
        self.GUI_game_logic.GLIset_grid_size(grid_size)
        self.GUI_game_logic.GLIset_winning_condition()

        # Mise à jour de l’interface
        self.GUI_set_grid_size(grid_size)
        self.GUI_game_logic.GLIresize_grid(grid_size)
        self.GUI_create_grid(grid_size)
        self.GUI_display_frame(self.GUI_frame_game)

        # Gestion des cases grisées
        if checkbox:
            if choicebox_value == "Random":
                max_allowed_cases = (grid_size * grid_size) // 2
                if number_case_var > max_allowed_cases:
                    messagebox.showerror("Erreur",
                                         f"Le nombre de cases à cocher ne doit pas dépasser {max_allowed_cases}.")
                    self.GUI_display_frame(self.GUI_frame_settings)
                    return
                self.GUI_check_boxes_random(grid_size, number_case_var)

            elif choicebox_value == "Pyramid":
                self.GUI_check_boxes_pyramid(grid_size)

        self.GUI_display_frame(self.GUI_frame_game)

    # ---------------------------------------------------
    #              GAME FRAME
    # ---------------------------------------------------
    
    def GUI_init_game_frame(self) -> None:
        """
        @brief Initialise la page de jeu (GAME).
        Affiche :
          - Des boutons de commande (arrêter, undo, vider la grille)
          - Un label indiquant le niveau de difficulté
          - La grille de jeu (boutons pour chaque case)
        """
        self.GUI_frame_game.configure(bg="#a1b8dc")

        menu_frame = tk.Frame(self.GUI_frame_game, bg="#a1b8dc")
        menu_frame.pack(fill="x", pady=10)

        tk.Button(menu_frame,
                  text="Arreter la partie",
                  command=lambda: self.GUI_stop_game_and_go_home(),
                  font=("Arial", 12),
                  bg="#384b7a",
                  fg="white",
                  width=15,
                  height=2).pack(side="left", padx=10)

        tk.Button(menu_frame,
                  text="Undo",
                  command=self.GUI_undo_move,
                  font=("Arial", 12),
                  bg="#384b7a",
                  fg="white",
                  width=15,
                  height=2).pack(side="left", padx=10)

        tk.Button(menu_frame,
                  text="Vider la grille",
                  command=self.GUI_reset_game,
                  font=("Arial", 12),
                  bg="#384b7a",
                  fg="white",
                  width=15,
                  height=2).pack(side="left", padx=10)

        self.GUI_level_label = tk.Label(menu_frame,
                                        text=f"Niveau : {self.GUI_game_logic.difficulty_level}",
                                        font=("Arial", 14),
                                        bg="#a1b8cc",
                                        fg="white")
        self.GUI_level_label.pack(side="right", padx=10)

        # Grille de jeu
        self.GUI_grid_frame = tk.Frame(self.GUI_frame_game, bg="#a1b8dc")
        self.GUI_grid_frame.pack(expand=False)

        self.GUI_create_grid(self.GUI_grid_size)

    def GUI_check_game_state(self) -> bool:
        """
        @brief Vérifie l'état du jeu et retourne True si la partie est terminée.
        - Si l’humain gagne : incrémente la difficulté et reset la grille
        - Si l’IA gagne : reset la difficulté et retour menu
        - Si match nul : retour menu
        @return True si le jeu est terminé, False sinon.
        """
        human_winner = self.GUI_game_logic.GLIcheck_winner(self.GUI_game_logic.oGLIPlayer1.PLRget_color())
        if human_winner:
            messagebox.showinfo("Fin de la partie", f"{human_winner.PLRget_name()} a gagné!")
            self.GUI_game_logic.GLIincrement_difficulty()
            self.GUI_level_label.config(text=f"Niveau : {self.GUI_game_logic.difficulty_level}")
            self.GUI_reset_game()  
            return True

        ai_winner = self.GUI_game_logic.GLIcheck_winner(self.GUI_game_logic.oGLIPlayer2.PLRget_color())
        if ai_winner:
            messagebox.showinfo("Fin de la partie", f"{ai_winner.PLRget_name()} a gagné!")
            self.GUI_game_logic.GLIreset_difficulty()
            self.GUI_level_label.config(text=f"Niveau : {self.GUI_game_logic.difficulty_level}")
            self.GUI_stop_game_and_go_home()
            return True

        if self.GUI_game_logic.GLIcheck_draw(None):
            messagebox.showinfo("Fin de la partie", "Match nul!")
            self.GUI_stop_game_and_go_home()
            return True

        return False

    def GUI_create_grid(self, iNewSize: int) -> None:
        """
        @brief Crée une grille de boutons pour représenter le plateau de jeu.
        @param iNewSize [int] : Taille de la grille (généralement self.GUI_grid_size).
        """
        for widget in self.GUI_grid_frame.winfo_children():
            widget.destroy()

        self.GUI_grid_buttons = []
        for i in range(self.GUI_grid_size):
            self.GUI_grid_frame.grid_rowconfigure(i, weight=1, minsize=80)
            self.GUI_grid_frame.grid_columnconfigure(i, weight=1, minsize=80)

        for i in range(iNewSize):
            row = []
            for j in range(iNewSize):
                btn = tk.Button(self.GUI_grid_frame,
                                text="",
                                font=("Arial", 20),
                                command=lambda iRow=i, iCol=j: self.GUI_make_move(iRow, iCol))
                btn.grid(row=i, column=j, sticky="nsew")
                btn.is_grayed = False
                row.append(btn)
            self.GUI_grid_buttons.append(row)

    def GUI_stop_game_and_go_home(self) -> None:
        """
        @brief Arrête la partie en cours et retourne à l’écran d’accueil.
        Réinitialise la difficulté, reset la grille, et affiche l’écran HOME.
        """
        self.GUI_game_logic.GLIreset_difficulty()
        self.GUI_reset_game()
        self.GUI_display_frame(self.GUI_frame_home)

    def GUI_make_move(self, row: int, col: int) -> None:
        """
        @brief Gère le clic sur une case (mouvement).
        @param row [int] : Indice de la ligne
        @param col [int] : Indice de la colonne
        """
        if self.GUI_grid_buttons[row][col].is_grayed:
            print("Cette case est grisée, vous ne pouvez pas y jouer.")
            return

        current_player = self.GUI_game_logic.GLIget_current_player()

        if not current_player.bPLRIsAI:
            # Coup humain
            current_player.PLRjouer(self.GUI_game_logic, row, col)
            self.GUI_update_button(row, col)

            # Vérifier si la partie est finie
            if self.GUI_check_game_state():
                return

            # Tour IA
            ai_player = self.GUI_game_logic.GLIget_current_player()
            if ai_player.bPLRIsAI:
                while True:
                    ai_player.PLRjouer(self.GUI_game_logic)
                    last_move = self.GUI_game_logic.move_history[-1]
                    iRow, iCol = last_move[0], last_move[1]
                    print(f"IA joue en ({iRow} - {iCol})")

                    # Si la case est grisée, on break (on ne replacera pas un coup)
                    if self.GUI_grid_buttons[iRow][iCol].is_grayed:
                        break

                    self.GUI_update_button(iRow, iCol)
                    self.GUI_check_game_state()
                    break

                if self.GUI_check_game_state():
                    return

        print("Case cliquée :", row, col)

    def GUI_update_button(self, row: int, col: int, reset: bool = False) -> None:
        """
        @brief Met à jour l'apparence d'un bouton après un coup.
        @param row [int]   : Indice de la ligne
        @param col [int]   : Indice de la colonne
        @param reset [bool]: Indique s’il faut remettre la case en état initial
        """
        button = self.GUI_grid_buttons[row][col]

        if reset:
            # Réinitialise la case
            button.config(state="normal", text="", bg="#f0f0f0")
            button.is_grayed = False
            for widget in button.winfo_children():
                widget.destroy()
            return

        # Récupérer la couleur depuis la logique
        color_enum = self.GUI_game_logic.tGLIgrid[row][col]

        # Supprimer tout contenu précédent du bouton (si existant)
        for widget in button.winfo_children():
            widget.destroy()

        # Calculer la taille de l'ovale
        canvas_width = button.winfo_width()
        canvas_height = button.winfo_height()
        oval_diameter = min(canvas_width, canvas_height) - 20

        # Canvas pour dessiner un ovale coloré
        canvas = tk.Canvas(
            button,
            width=canvas_width,
            height=canvas_height,
            bg=button.cget("bg"),
            highlightthickness=0
        )
        canvas.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # Dessin de l'ovale
        canvas.create_oval(
            (canvas_width - oval_diameter) / 2,
            (canvas_height - oval_diameter) / 2,
            (canvas_width + oval_diameter) / 2,
            (canvas_height + oval_diameter) / 2,
            fill=color_enum.tkinter_color
        )

        # Désactiver le bouton
        button.config(state="disabled")

    def GUI_reset_game(self) -> None:
        """
        @brief Réinitialise la grille et le jeu (GameLogic).
        Conserve la difficulté, mais efface l’historique des coups
        et recrée la grille visuelle.
        """
        self.GUI_game_logic.GLIreset_game()
        self.GUI_level_label.config(text=f"Niveau : {self.GUI_game_logic.difficulty_level}")
        self.GUI_create_grid(self.GUI_game_logic.iGLISize)

    def GUI_set_grid_size(self, iNewSize: int) -> None:
        """
        @brief Définit la taille de la grille (GUI).
        @param iNewSize [int] : Nouvelle taille souhaitée.
        """
        self.GUI_grid_size = iNewSize

    def GUI_run(self) -> None:
        """
        @brief Lance la boucle principale Tkinter.
        """
        self.GUI_fenetre.mainloop()

    def GUI_update_current_player(self) -> None:
        """
        @brief Met à jour l’affichage du joueur actuel (optionnel).
        Nécessite un label spécifique dans l’interface.
        """
        current_player = self.GUI_game_logic.GLIget_current_player()
        if hasattr(self, 'GUI_current_player_label'):
            self.GUI_current_player_label.config(
                text=f"C'est au tour de {current_player.PLRget_name()}")

    # ---------------------------------------------------
    #    FONCTIONS DE GRISAGE DE CASES (RANDOM/PYRAMID)
    # ---------------------------------------------------

    def GUI_check_boxes_pyramid(self, grid_size: int) -> None:
        """
        @brief Grise des cases en forme de pyramide (matrice triangulaire).
        @param grid_size [int] : Taille de la grille.
        """
        for i in range(grid_size):
            for j in range(i + 1):
                if j < grid_size:
                    self.GUI_grayscale_button(i, j)

    def GUI_check_boxes_random(self, grid_size: int, number_of_cases: int) -> None:
        """
        @brief Grise aléatoirement un certain nombre de cases.
        @param grid_size [int] : Taille de la grille
        @param number_of_cases [int] : Nombre de cases à griser
        """
        available_cells = []
        for i in range(grid_size):
            for j in range(grid_size):
                if not self.GUI_grid_buttons[i][j].is_grayed:
                    available_cells.append((i, j))

        if len(available_cells) < number_of_cases:
            messagebox.showerror("Erreur", "Il n'y a pas assez de cases disponibles pour cocher.")
            return

        random.shuffle(available_cells)

        for i in range(number_of_cases):
            row, col = available_cells[i]
            self.GUI_grayscale_button(row, col)

    def GUI_grayscale_button(self, row: int, col: int) -> None:
        """
        @brief Grise un bouton de la grille et désactive sa logique.
        @param row [int] : Indice de la ligne
        @param col [int] : Indice de la colonne
        """
        button = self.GUI_grid_buttons[row][col]
        button.config(state="disabled", bg="grey")
        button.is_grayed = True

        # Mémoriser le grisage dans la logique
        self.GUI_game_logic.tGLIgrid[row][col] = TColor.GREY

    # ---------------------------------------------------
    #                     UNDO
    # ---------------------------------------------------

    def GUI_undo_move(self) -> None:
        """
        @brief Annule le dernier coup joué (si possible).
        Gère également la mise à jour visuelle de la case annulée.
        """
        if self.GUI_game_logic.GLIundo_move():
            last_move = (self.GUI_game_logic.move_history[-1]
                         if self.GUI_game_logic.move_history else None)
            if last_move:
                iRow, iCol, _ = last_move
                self.GUI_update_button(iRow, iCol, reset=True)
                print("Joueur actuel :", self.GUI_game_logic.GLIget_current_player().PLRget_name())
                print("Tour du joueur :",
                      "Joueur 1" if self.GUI_game_logic.bGLIIsPlayerOneTurn else "IA")
            else:
                # Réinitialise toute la grille si aucun coup restant
                self.GUI_create_grid(self.GUI_game_logic.iGLISize)

            self.GUI_update_current_player()
        else:
            messagebox.showinfo("Info", "Aucun coup à annuler.")
