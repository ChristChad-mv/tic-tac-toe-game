import tkinter as tk

class GUI :
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TIC-TAC-TOE")
        self.window.geometry(f"{600}x{400}")
        self.actuel_frame =None
        self.montrer_acceuil()
    
    def montrer_acceuil(self):
        #ici on nettoie la fentre s'il y avait un frame avant
        if self.actuel_frame is not None :
            self.actuel_frame.destroy()
        self.actuel_frame=tk.Frame(self.window, bg="#a1b8cc")
        self.actuel_frame.pack(padx=20, pady=20)
        # le frame acceuil :
        self.titre= tk.Label(self.actuel_frame, text="TIC-TAC-TOE", font=("Arial", 24), bg="#a1b8cc")
        self.titre.pack(padx=20, pady=20) 
        # les boutons de l'acceuil
        self.commencer= tk.Button(self.actuel_frame,text="Lancer une partie", command=self.montrer_jeu)
        self.commencer.pack(pady=20)

        self.parametre=tk.Button(self.actuel_frame,text="Paramétres", command=self.montrer_parametre)
        self.parametre.pack(pady=20)
    
    # la methode pour la fenetre paramtres : 
    def montrer_parametre(self): 
        if self.actuel_frame is not None : 
            self.actuel_frame.destroy()
        self.actuel_frame=tk.Frame(self.window, bg="#a1b8cc")
        self.actuel_frame.grid(row=0,column=0, sticky="nsew", padx=50, pady=20)


        # titre des parametres 
        self.titre=tk.Label(self.actuel_frame, text="Paramètres du jeu",font=("Arial", 24), bg="#a1b8cc")
        self.titre.grid ( row=0, column=1, columnspan=2)

         # les boutons : 
         # Première ligne pour la taille de la grille
        self.taille_var = tk.StringVar()
        self.taille_label = tk.Label(self.actuel_frame, text="Taille de la grille:" , bg="#a1b8cc")
        self.taille_label.grid(row=1, column=0, padx=10, sticky="w")
        self.radio_3x3 = tk.Radiobutton(self.actuel_frame, text="3x3", value="3x3",bg="#a1b8cc", variable=self.taille_var)
        self.radio_4x4 = tk.Radiobutton(self.actuel_frame, text="4x4", value="4x4", bg="#a1b8cc",variable=self.taille_var)
        self.radio_5x5 = tk.Radiobutton(self.actuel_frame, text="5x5", value="5x5",bg="#a1b8cc",variable=self.taille_var)
        self.radio_3x3.grid(row=1, column=1, sticky="w")
        self.radio_4x4.grid(row=1, column=2, sticky="w")
        self.radio_5x5.grid(row=1, column=3, sticky="w")

        # Deuxième ligne pour "cocher des cases"
        self.cocher_var = tk.BooleanVar()
        self.cocher_label = tk.Label(self.actuel_frame, text="Cocher des cases",bg="#a1b8cc")
        self.cocher_label.grid(row=2, column=0, padx=10, sticky="w")
        self.radio_oui = tk.Radiobutton(self.actuel_frame, text="Oui",value=True, variable=self.cocher_var,bg="#a1b8cc")
        self.radio_non = tk.Radiobutton(self.actuel_frame, text="Non",value=False, variable=self.cocher_var,bg="#a1b8cc")
        self.radio_oui.grid(row=2, column=1, sticky="w")
        self.radio_non.grid(row=2, column=2, sticky="w")

        # Troisième ligne pour le nombre de cases à cocher
        self.nb_cases_label = tk.Label(self.actuel_frame, text="Nombre de cases à cocher:", bg="#a1b8cc")
        self.nb_cases_label.grid(row=3, column=0, padx=10, sticky="w")
        self.nb_case_frame = tk.Entry(self.actuel_frame)
        self.nb_case_frame.grid(row=3, column=1, pady=5)

        # Quatrième ligne pour le symbole choisi
        self.symbol_var = tk.BooleanVar()
        self.symbol_label = tk.Label(self.actuel_frame, text="Symbole choisi", bg="#a1b8cc")
        self.symbol_label.grid(row=4, column=0, padx=10, sticky="w")
        self.symbol_red = tk.Radiobutton(self.actuel_frame, text="Rouge", value=True, variable=self.symbol_var,bg="#a1b8cc")
        self.symbol_blue = tk.Radiobutton(self.actuel_frame, text="Bleu", value=False,variable=self.symbol_var,bg="#a1b8cc")
        self.symbol_red.grid(row=4, column=1, sticky="w")
        self.symbol_blue.grid(row=4, column=2, sticky="w")

        # Bouton de soumission
        self.submit_button = tk.Button(self.actuel_frame, text="Valider", command=self.montrer_jeu)
        self.submit_button.grid(row=5, column=0, columnspan=3, pady=20)
    
    def  montrer_jeu (self):
        # Détruire le précédent frame s'il existe
        if self.actuel_frame is not None: 
            self.actuel_frame.destroy()

        # Créer un nouveau frame pour le jeu, prenant toute la place
        self.actuel_frame = tk.Frame(self.window, bg="#a1b8cc")
        self.actuel_frame.grid(row=0, column=0, sticky="nsew")
        # Configurer la taille de la fenêtre pour qu'elle prenne toute la place
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

        # Le titre
        self.titre = tk.Label(self.actuel_frame, text="Le jeu", bg="#a1b8cc", font=("Arial",16))
        self.titre.grid(row=0, column=0, padx=10, sticky="w")
    
        # Frame contenant les joueurs à droite
        self.joueurs_frame =tk.Frame(self.actuel_frame, bg="#f0f0f0", width=200)
        self.joueurs_frame.grid(row=1, column=2, padx=10, pady=10, sticky="ne")

        # Titre de la frame des joueurs
        self.titre_joueurs_frame = tk.Label(self.joueurs_frame, text="A qui le tour")
        self.titre_joueurs_frame.grid(row=0, column=0, columnspan=2, pady= 10)

        # Boutons pour joueur et IA
        self.joueur1 = tk.Button(self.joueurs_frame, text="Joueur", bg="#a1b8cc")
        self.joueur1.grid(row=1, column=0, columnspan=2, pady=10)

        self.joueurIA = tk.Button(self.joueurs_frame, text="Ordinateur", bg="#a1b8cc")
        self.joueurIA.grid(row=2, column=0, columnspan=2, pady=10)

        # Configurer la largeur des colonnes et des lignes du grid
        self.actuel_frame.grid_columnconfigure(0, weight=1)
        self.actuel_frame.grid_columnconfigure(1, weight=3)
        self.actuel_frame.grid_columnconfigure(2, weight=1)

        # S'assurer que le contenu à droite s'étend correctement
        self.actuel_frame.grid_rowconfigure(1, weight=3)


        """self.joueur1=tk.Button(self.joueurs_frame,text=self.PLRget_name())
        self.joueur1.grid(row=1, column=1 , columnspan=2)
        self.joueurIA=tk.Button(self.joueurs_frame,text="Ordinateur")
        self.joueur1.grid(row=2, column=1 , columnspan=2)

        #distinguer le joueur actuel 
        self.highlight_current_player()
"""
    """def highlight_current_player(self):
         current_player = self.GLIGameLogic.GLIget_current_player()
        if  current_player.PLRget_name()=="Ordinateur"
            self.joueur1.config(bg="red", relief="sunken")
            self.joueurIA.config(bg="white", relief="raised")
        else :
            self.joueurIA.config(bg="red", relief="sunken")
            self.joueur1.config(bg="white", relief="raised")
       """ 
    #lancer la fenetre 
    def lancer(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = GUI()
    app.lancer()
