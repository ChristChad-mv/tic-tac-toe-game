import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from game_logic import GameLogic
from Player.player import TPlayer
from Player.color import TColor
import random

class TicTacToeGUI:
    def __init__(self, game_logic):
        # Initialisation de la fenêtre principale
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

    """
    -------------------- HOME FRAME --------------------
    """
    def GUI_init_home_frame(self):
        """Initialise la page d'accueil."""

        self.GUI_frame_home.configure(bg="#29417d")
        # Charger et afficher l'image de fond
        self.bg_image = Image.open("picture.jpg")  
        self.bg_image = self.bg_image.resize((800, 800),Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Ajouter l'image en arrière-plan
        self.bg_label = tk.Label(self.GUI_frame_home, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  
        # frame contenant les boutons 
        button_frame = tk.Frame(self.GUI_frame_home, bg="#29417d")
        button_frame.place(relx=0.5, rely=0.3, anchor="center")  
        tk.Label(button_frame, text="Bienvenue à Tic Tac Toe!",
                 font=("Arial", 24), bg="#29417d", fg="white").pack(pady=20)

        tk.Button(button_frame, text="Jouer",
                  command=lambda: self.GUI_display_frame(self.GUI_frame_game),
                  font=("Arial", 14), bg="#7683e7", fg="white", width=20, height=2).pack(pady=10)

        tk.Button(button_frame, text="Paramètres",
                  command=lambda: self.GUI_display_frame(self.GUI_frame_settings),
                  font=("Arial", 14), bg="#7683e7", fg="white", width=20, height=2).pack(pady=10)

        tk.Button(button_frame, text="Quitter",
                  command=self.GUI_fenetre.quit,
                  font=("Arial", 14), bg="red", fg="white", width=20, height=2).pack(pady=10)

    """
    -------------------- SETTINGS FRAME --------------------
    """
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
        size_options = [3, 5, 7]
        size_dropdown = tk.OptionMenu(self.GUI_frame_settings, grid_size_var, *size_options)
        size_dropdown.config(font=("Arial", 12), bg="#384b7a", fg="white", width=15)
        size_dropdown.pack(pady=5)

        # Cocher des cases
        tk.Label(self.GUI_frame_settings, text="Cocher des cases:",
                font=("Arial", 14), bg="#384b7a", fg="white").pack(pady=5)
        checkbox_frame = tk.Frame(self.GUI_frame_settings, bg="#384b7a")
        checkbox_frame.pack(pady=5)
        checkbox_var = tk.BooleanVar(value=False)
        self.GUI_frame_settings.checkbox_var = checkbox_var
        tk.Radiobutton(checkbox_frame, text="Oui", variable=checkbox_var, value=True,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack(side="left", padx=10)
        tk.Radiobutton(checkbox_frame, text="Non", variable=checkbox_var, value=False,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack(side="left", padx=10)
        # type de cochage random ou pyramide
        tk.Label(self.GUI_frame_settings, text="Type de cochage:",
                font=("Arial", 14), bg="#384b7a", fg="white").pack(pady=5)
        choicebox_frame = tk.Frame(self.GUI_frame_settings, bg="#384b7a")
        choicebox_frame.pack(pady=5)
        choicebox_var = tk.BooleanVar(value=False)
        tk.Radiobutton(choicebox_frame, text="Random", variable=choicebox_var, value=True,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack(side="left", padx=10)
        tk.Radiobutton(choicebox_frame, text="Pyramid", variable=choicebox_var, value=False,
                    font=("Arial", 12), bg="#384b7a", fg="white").pack(side="left", padx=10)
        # Couleur choisie (liste déroulante)
        tk.Label(self.GUI_frame_settings, text="Choisir la couleur du joueur :",
                font=("Arial", 14), bg="#384b7a", fg="white").pack(pady=5)
        color_var = tk.StringVar(value="Bleu")
        color_options = ["Vert", "Jaune", "Orange"]
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

        self.GUI_game_logic.GLIset_players_name(player_name, "Ordinateur")
        self.GUI_game_logic.oGLIPlayer1.PLRset_color(color_mapping[color])
        self.GUI_game_logic.GLIset_grid_size(grid_size)
        self.GUI_game_logic.GLIset_winning_condition()
        # Mise à jour de la grille
        self.GUI_set_grid_size(grid_size)
        self.GUI_game_logic.GLIresize_grid(grid_size)
        self.GUI_create_grid(grid_size)
        self.GUI_display_frame(self.GUI_frame_game)

        if checkbox:
        # Appeler la fonction pour griser les cases en pyramide ou aléatoirement
            if self.GUI_frame_settings.checkbox_var.get():   
                self.GUI_check_boxes_pyramid(grid_size)
            else:  
                self.GUI_check_boxes_random(grid_size)
    
        self.GUI_display_frame(self.GUI_frame_game)


    """
    -------------------- GAME FRAME --------------------
    """
    def GUI_init_game_frame(self):
        """Initialise la page de jeu."""
        self.GUI_frame_game.configure(bg="#a1b8dc")

        # Menu supérieur
        menu_frame = tk.Frame(self.GUI_frame_game, bg="#a1b8dc")
        menu_frame.pack(fill="x", pady=10)

        tk.Button(menu_frame, text="Arreter la partie", command=lambda: self.GUI_display_frame(self.GUI_frame_home),
                  font=("Arial", 12), bg="#384b7a", fg="white", width=15, height=2).pack(side="left", padx=10)
        tk.Button(menu_frame, text="Undo", font=("Arial", 12), bg="#384b7a", fg="white", width=15, height=2).pack(side="left", padx=10)
        tk.Button(menu_frame, text="Vider la grille", command=self.GUI_reset_game,
                  font=("Arial", 12), bg="#384b7a", fg="white", width=15, height=2).pack(side="left", padx=10)
        
        # Label pour afficher le niveau
        self.GUI_level_label = tk.Label(menu_frame, text=f"Niveau : {self.GUI_game_logic.difficulty_level}",
                                        font=("Arial", 14), bg="#a1b8cc", fg="white")
        self.GUI_level_label.pack(side="right", padx=10)
        """
        # Cadre pour les joueurs
        joueurs_frame = tk.Frame(self.GUI_frame_game, bg="#f0f0f0", width=200, height=300)
        joueurs_frame.pack(side="right", padx=10, pady=40, fill="y")
        joueurs_frame.pack_propagate(False)

        tk.Label(joueurs_frame, text="A qui le tour", font=("Arial", 12, "bold"), bg="#f0f0f0").pack(pady=10)

        tk.Button(joueurs_frame, text="Joueur", bg="#a1b8cc", fg="white", font=("Arial", 12, "bold"), width=15, height=2).pack(pady=10)
        tk.Button(joueurs_frame, text="Ordinateur", bg="#a1b8cc", fg="white", font=("Arial", 12, "bold"), width=15, height=2).pack(pady=10)
        """
        # Grille de jeu
        self.GUI_grid_frame = tk.Frame(self.GUI_frame_game, bg="#a1b8dc")
        self.GUI_grid_frame.pack(expand=False)

        self.GUI_create_grid(self.GUI_grid_size)

    def GUI_create_grid(self, iNewSize: int):
        """Crée une grille de boutons."""
        for widget in self.GUI_grid_frame.winfo_children():
            widget.destroy()
        self.GUI_grid_buttons = []
        for i in range(self.GUI_grid_size):
            self.GUI_grid_frame.grid_rowconfigure(i, weight=1, minsize=80) 
            self.GUI_grid_frame.grid_columnconfigure(i, weight=1, minsize=80)
        self.GUI_grid_buttons = []
        for i in range(iNewSize):
            row = []
            for j in range(iNewSize):
                btn = tk.Button(self.GUI_grid_frame, text="", font=("Arial", 20),
                                command=lambda iRow=i, iCol=j: self.GUI_make_move(iRow, iCol))
                btn.grid(row=i, column=j,sticky="nsew")
                btn.is_grayed = False
                row.append(btn)
            self.GUI_grid_buttons.append(row)

    def GUI_make_move(self, row, col):
        """Gère un mouvement dans la grille"""
        if self.GUI_grid_buttons[row][col].is_grayed:
            print("Cette case est grisée, vous ne pouvez pas y jouer.")  
            return  
        
        current_player = self.GUI_game_logic.GLIget_current_player()
        
        if not current_player.bPLRIsAI:
            # Si c'est le joueur humain qui joue
            current_player.PLRjouer(self.GUI_game_logic, row, col)
            self.GUI_update_button(row, col)
            
            # Vérification immédiate de l'état après le coup humain
            if self.GUI_check_game_state():
                return  # Arrête si la partie est terminée

            # Tour de l'IA
            ai_player = self.GUI_game_logic.GLIget_current_player()
            if ai_player.bPLRIsAI:
                while True :
                    ai_player.PLRjouer(self.GUI_game_logic)
                    last_move = self.GUI_game_logic.move_history[-1]
                    row,col=last_move[0], last_move[1]
                    if self.GUI_grid_buttons[row][col].is_grayed:
                        continue 

                    self.GUI_update_button(last_move[0], last_move[1])
                    self.GUI_check_game_state()
                    break

                if self.GUI_check_game_state():
                    return  
                   
    def GUI_check_game_state(self):
        """Vérifie l'état du jeu et retourne True si la partie est terminée."""
        human_winner = self.GUI_game_logic.GLIcheck_winner(self.GUI_game_logic.oGLIPlayer1.PLRget_color())
        if human_winner:
            messagebox.showinfo("Fin de la partie", f"{human_winner.PLRget_name()} a gagné!")
            self.GUI_game_logic.GLIincrement_difficulty()  # Augmenter le niveau
            self.GUI_level_label.config(text=f"Niveau : {self.GUI_game_logic.difficulty_level}")
            self.GUI_reset_game()  # Réinitialiser la grille uniquement
            return True

        ai_winner = self.GUI_game_logic.GLIcheck_winner(self.GUI_game_logic.oGLIPlayer2.PLRget_color())
        if ai_winner:
            messagebox.showinfo("Fin de la partie", f"{ai_winner.PLRget_name()} a gagné!")
            self.GUI_game_logic.GLIreset_difficulty()  # Réinitialiser le niveau de difficulté
            self.GUI_level_label.config(text=f"Niveau : {self.GUI_game_logic.difficulty_level}")
            self.GUI_reset_game()  # Réinitialiser la grille uniquement
            return True
        all_grayed_or_occupied = True
        for row in range(self.GUI_grid_size):
            for col in range(self.GUI_grid_size):
                if not self.GUI_grid_buttons[row][col].is_grayed and not self.GUI_grid_buttons[row][col].cget("state") == "disabled":
                    all_grayed_or_occupied = False
                    break
            if not all_grayed_or_occupied:
                break

        if self.GUI_game_logic.GLIcheck_draw(None):
            messagebox.showinfo("Fin de la partie", "Match nul!")
            self.GUI_reset_game()  # Réinitialiser la grille uniquement
            return True

        return False



    def GUI_update_button(self, row, col):
        """Met à jour l'apparence d'un bouton après un coup"""
        button = self.GUI_grid_buttons[row][col]
        color_enum = self.GUI_game_logic.tGLIgrid[row][col]
        
        # Détruire tout contenu précédent du bouton pour éviter les doublons
        for widget in button.winfo_children():
            widget.destroy()

        # Dimensions dynamiques pour adapter la taille de l'élément au bouton
        canvas_width = button.winfo_width()
        canvas_height = button.winfo_height()
        oval_diameter = min(canvas_width, canvas_height) - 20  # Marge de 10px

        # Création du canvas pour dessiner un ovale coloré
        canvas = tk.Canvas(
            button,
            width=canvas_width,
            height=canvas_height,
            bg=button.cget("bg"),  # Utilise la couleur d'arrière-plan du bouton
            highlightthickness=0
        )
        canvas.place(relx=0.5, rely=0.5, anchor="center", relwidth=1, relheight=1)

        # Dessiner l'ovale au centre du canvas
        canvas.create_oval(
            (canvas_width - oval_diameter) / 2,
            (canvas_height - oval_diameter) / 2,
            (canvas_width + oval_diameter) / 2,
            (canvas_height + oval_diameter) / 2,
            fill=color_enum.tkinter_color
        )

        # Désactiver le bouton après la mise à jour
        button.config(state="disabled")


    def GUI_reset_game(self):
        """Réinitialise la grille et le jeu."""
        self.GUI_game_logic.GLIreset_game()
        self.GUI_level_label.config(text=f"Niveau : {self.GUI_game_logic.difficulty_level}")
        self.GUI_create_grid(self.GUI_grid_size)

    def GUI_set_grid_size(self, iNewSize):
        """Définit la taille de la grille."""
        self.GUI_grid_size = iNewSize
        

    def GUI_run(self):
        """Lance l'application"""
        self.GUI_fenetre.mainloop()

    def GUI_update_current_player(self):
        """Met à jour l'affichage du joueur actuel"""
        current_player = self.GUI_game_logic.GLIget_current_player()
        if hasattr(self, 'GUI_current_player_label'):
            self.GUI_current_player_label.config(
                text=f"C'est au tour de {current_player.PLRget_name()}")
    

  

    def GUI_check_boxes_pyramid(self, grid_size):
        """Coche des cases en forme de pyramide."""
        middle = grid_size // 2  # Trouver la case centrale
        for i in range(grid_size):
            for j in range(grid_size):
                # Vérifier si (i,j) est dans un "rayon" de la pyramide
                if abs(i - middle) + abs(j - middle) <= middle:
                    self.GUI_grayscale_button(i, j)

    def GUI_check_boxes_random(self, grid_size):
        """Coche des cases aléatoirement."""
        pass 
        # pas encore fait 

    def GUI_grayscale_button(self, row, col):
        """Grise un bouton spécifique de la grille et le désactive."""
        button = self.GUI_grid_buttons[row][col]
        button.config(state="disabled", bg="grey")   
        self.GUI_grid_buttons[row][col].is_grayed = True
