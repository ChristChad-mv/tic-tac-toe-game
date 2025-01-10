import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from game_logic import GameLogic
from Player.player import TPlayer
from Player.color import TColor

class TicTacToeGUI:
    def __init__(self, game_logic):
        # Initialisation de la fenêtre principale
        self.GUI_fenetre = tk.Tk()
        self.GUI_fenetre.title("TIC-TAC-TOE")
        self.GUI_fenetre.geometry("800x600")
        self.GUI_fenetre.resizable(width=False, height=False)

        # Logique de jeu
        self.GUI_game_logic = game_logic
        self.GUI_grid_size = 3  # Par défaut

        # Frames
        self.GUI_current_frame = None
        self.GUI_frame_home = tk.Frame(self.GUI_fenetre)
        self.GUI_frame_settings = tk.Frame(self.GUI_fenetre)
        self.GUI_frame_game = tk.Frame(self.GUI_fenetre)

        # Initialisation des frames
        self.GUI_init_home_frame()
        self.GUI_init_settings_frame()
        self.GUI_init_game_frame()

        # Afficher l'accueil au démarrage
        self.GUI_display_frame(self.GUI_frame_home)

    def GUI_display_frame(self, frame):
        """Affiche une frame spécifique."""
        if self.GUI_current_frame is not None:
            self.GUI_current_frame.pack_forget()
        frame.pack(fill="both", expand=True)
        self.GUI_current_frame = frame

    def GUI_init_home_frame(self):
        """Initialise la page d'accueil."""
        self.GUI_frame_home.configure(bg="#29417d")
        tk.Label(self.GUI_frame_home, text="Bienvenue à Tic Tac Toe!",
                 font=("Arial", 24), bg="#29417d", fg="white").pack(pady=20)

        tk.Button(self.GUI_frame_home, text="Jouer",
                  command=lambda: self.GUI_display_frame(self.GUI_frame_game),
                  font=("Arial", 14), bg="#7683e7", fg="white", width=20, height=2).pack(pady=10)

        tk.Button(self.GUI_frame_home, text="Paramètres",
                  command=lambda: self.GUI_display_frame(self.GUI_frame_settings),
                  font=("Arial", 14), bg="#7683e7", fg="white", width=20, height=2).pack(pady=10)

        tk.Button(self.GUI_frame_home, text="Quitter",
                  command=self.GUI_fenetre.quit,
                  font=("Arial", 14), bg="red", fg="white", width=20, height=2).pack(pady=10)

    def GUI_init_settings_frame(self):
        """Initialise la page des paramètres."""
        self.GUI_frame_settings.configure(bg="#384b7a")

        # Titre
        tk.Label(self.GUI_frame_settings, text="Paramètres du jeu",
                font=("Arial", 24), bg="#384b7a", fg="white").pack(pady=20)

        # Nom du joueur
        tk.Label(self.GUI_frame_settings, text="Nom du Joueur:",
                font=("Arial", 14), bg="#384b7a", fg="white").pack(pady=5)
        player_name_var = tk.StringVar(value="Joueur 1")
        tk.Entry(self.GUI_frame_settings, textvariable=player_name_var,
                font=("Arial", 12), bg="#ffffff", width=20).pack(pady=5)

        # Taille de la grille
        tk.Label(self.GUI_frame_settings, text="Taille de la grille:",
                font=("Arial", 14), bg="#384b7a", fg="white").pack(pady=5)
        grid_size_var = tk.IntVar(value=self.GUI_grid_size)
        tk.Radiobutton(self.GUI_frame_settings, text="3x3", variable=grid_size_var, value=3,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack()
        tk.Radiobutton(self.GUI_frame_settings, text="4x4", variable=grid_size_var, value=4,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack()
        tk.Radiobutton(self.GUI_frame_settings, text="5x5", variable=grid_size_var, value=5,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack()

        # Cocher des cases
        tk.Label(self.GUI_frame_settings, text="Cocher des cases:",
                font=("Arial", 14), bg="#384b7a", fg="white").pack(pady=5)
        checkbox_frame = tk.Frame(self.GUI_frame_settings, bg="#384b7a")
        checkbox_frame.pack(pady=5)
        checkbox_var = tk.BooleanVar(value=False)
        tk.Radiobutton(checkbox_frame, text="Oui", variable=checkbox_var, value=True,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack(side="left", padx=10)
        tk.Radiobutton(checkbox_frame, text="Non", variable=checkbox_var, value=False,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack(side="left", padx=10)

        # Couleur choisie (liste déroulante)
        tk.Label(self.GUI_frame_settings, text="Choisir la couleur du joueur :",
                font=("Arial", 14), bg="#384b7a", fg="white").pack(pady=5)
        color_var = tk.StringVar(value="Rouge")
        color_options = ["Bleu", "Vert", "Jaune", "Orange"]
        color_dropdown = tk.OptionMenu(self.GUI_frame_settings, color_var, *color_options)
        color_dropdown.config(font=("Arial", 12), bg="#384b7a", fg="white", width=15)
        color_dropdown.pack(pady=5)

        # Boutons de navigation
        tk.Button(self.GUI_frame_settings, text="Jouer",
                command=lambda: self.GUI_apply_settings(player_name_var.get(),
                                                        grid_size_var.get(),
                                                        checkbox_var.get(),
                                                        color_var.get()),
                font=("Arial", 14), bg="#7683e7", fg="white", width=15, height=2).pack(pady=10)


    def GUI_apply_settings(self, player_name, grid_size, checkbox, color):
        """Applique les paramètres et démarre le jeu."""
        # Conversion du nom de couleur en TColor
        color_mapping = {
            "Rouge": TColor.ROUGE,
            "Bleu": TColor.BLEU,
            "Vert": TColor.VERT,
            "Jaune": TColor.JAUNE,
            "Orange": TColor.ORANGE
        }
        
        # Mise à jour du joueur
        self.GUI_game_logic.GLIset_players_name(player_name, "Ordinateur")
        self.GUI_game_logic.oGLIPlayer1.PLRset_color(color_mapping[color])
        
        # Mise à jour de la grille
        self.GUI_set_grid_size(grid_size)
        self.GUI_display_frame(self.GUI_frame_game)

    def GUI_init_game_frame(self):
        """Initialise la page de jeu."""
        self.GUI_frame_game.configure(bg="#a1b8dc")

        # Menu supérieur
        menu_frame = tk.Frame(self.GUI_frame_game, bg="#a1b8cc")
        menu_frame.pack(fill="x", pady=10)

        tk.Button(menu_frame, text="Arreter la partie", command=lambda: self.GUI_display_frame(self.GUI_frame_home),
                  font=("Arial", 12), bg="#384b7a", fg="white", width=15, height=2).pack(side="left", padx=10)
        tk.Button(menu_frame, text="Undo", font=("Arial", 12), bg="#384b7a", fg="white", width=15, height=2).pack(side="left", padx=10)
        tk.Button(menu_frame, text="Vider la grille", command=self.GUI_reset_game,
                  font=("Arial", 12), bg="#384b7a", fg="white", width=15, height=2).pack(side="left", padx=10)

        # Cadre pour les joueurs
        joueurs_frame = tk.Frame(self.GUI_frame_game, bg="#f0f0f0", width=200, height=300)
        joueurs_frame.pack(side="right", padx=10, pady=40, fill="y")
        joueurs_frame.pack_propagate(False)

        tk.Label(joueurs_frame, text="A qui le tour", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Button(joueurs_frame, text="Joueur", bg="#a1b8cc", fg="white", font=("Arial", 12, "bold"), width=15, height=2).pack(pady=10)
        tk.Button(joueurs_frame, text="Ordinateur", bg="#a1b8cc", fg="white", font=("Arial", 12, "bold"), width=15, height=2).pack(pady=10)

        # Grille de jeu
        self.GUI_grid_frame = tk.Frame(self.GUI_frame_game, bg="#a1b8dc")
        self.GUI_grid_frame.pack(expand=True)

        self.GUI_create_grid()

    def GUI_create_grid(self):
        """Crée une grille de boutons."""
        for widget in self.GUI_grid_frame.winfo_children():
            widget.destroy()

        self.GUI_grid_buttons = []
        for i in range(self.GUI_grid_size):
            row = []
            for j in range(self.GUI_grid_size):
                btn = tk.Button(self.GUI_grid_frame, text="", font=("Arial", 20),
                                width=5, height=2,
                                command=lambda iRow=i, iCol=j: self.GUI_make_move(iRow, iCol))
                btn.grid(row=i, column=j, padx=5, pady=5)
                row.append(btn)
            self.GUI_grid_buttons.append(row)

    def GUI_make_move(self, row, col):
        """Gère un mouvement dans la grille"""
        current_player = self.GUI_game_logic.GLIget_current_player()
        
        if not current_player.bPLRIsAI:
            # Si c'est le joueur humain qui joue
            current_player.PLRjouer(self.GUI_game_logic, row, col)
            self.GUI_update_button(row, col)
            
            # Vérification de l'état du jeu
            if self.GUI_check_game_state():
                return

            # Tour de l'IA
            ai_player = self.GUI_game_logic.GLIget_current_player()
            if ai_player.bPLRIsAI:
                ai_player.PLRjouer(self.GUI_game_logic)
                # Trouver le dernier coup joué par l'IA
                last_move = self.GUI_game_logic.move_history[-1]
                self.GUI_update_button(last_move[0], last_move[1])
                self.GUI_check_game_state()

    def GUI_check_game_state(self):
        """Vérifie l'état du jeu et retourne True si la partie est terminée"""
        current_player = self.GUI_game_logic.GLIget_current_player()
        winner = self.GUI_game_logic.GLIcheck_winner(current_player.PLRget_color())
        
        if winner:
            messagebox.showinfo("Fin de la partie", f"{winner.PLRget_name()} a gagné!")
            self.GUI_reset_game()
            return True
        elif self.GUI_game_logic.GLIcheck_draw(current_player.PLRget_color()):
            messagebox.showinfo("Fin de la partie", "Match nul!")
            self.GUI_reset_game()
            return True
        return False

    def GUI_update_button(self, row, col):
        """Met à jour l'apparence d'un bouton après un coup"""
        button = self.GUI_grid_buttons[row][col]
        color_enum = self.GUI_game_logic.tGLIgrid[row][col]
        
        # Utilisation directe de la couleur Tkinter depuis TColor
        canvas = tk.Canvas(button, 
                          width=50, 
                          height=50,
                          bg="white",
                          highlightthickness=0)
        canvas.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)
        canvas.create_oval(5, 5, 45, 45, fill=color_enum.tkinter_color)
        button.config(state="disabled")

    def GUI_reset_game(self):
        """Réinitialise la grille et le jeu."""
        self.GUI_game_logic.GLIreset_game()
        self.GUI_create_grid()

    def GUI_set_grid_size(self, iNewSize):
        """Définit la taille de la grille."""
        self.GUI_grid_size = iNewSize
        self.GUI_game_logic.GLIresize_grid(iNewSize)
        self.GUI_create_grid()
        self.GUI_display_frame(self.GUI_frame_game)

    def GUI_run(self):
        """Lance l'application"""
        self.GUI_fenetre.mainloop()

    def GUI_update_current_player(self):
        """Met à jour l'affichage du joueur actuel"""
        current_player = self.GUI_game_logic.GLIget_current_player()
        if hasattr(self, 'GUI_current_player_label'):
            self.GUI_current_player_label.config(
                text=f"C'est au tour de {current_player.PLRget_name()}")
