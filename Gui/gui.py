import tkinter as tk
from PIL import Image, ImageTk
from game_logic import GameLogic
from Player.PlayerHumain import TPlayer

class GUI :
    # Constructeur qui initialise la fenetre du jeu : 
    """
    Pour un rendu plus acceptable nous avons verouillé la fonctionnalité d'accroitre la fenetre
    """
    def __init__(self):
        self.fenetre = tk.Tk()
        self.fenetre.title("TIC-TAC-TOE")
        self.fenetre.geometry(f"{800}x{600}")
        self.fenetre.resizable(width=False, height=False)
        self.actuel_frame =None
        self.montrer_acceuil()
    
    # Methode qui initialise le frame de la page d'acceuil
    """
    cette methode initialise le frame ou se trouve les boutons 
    pour acceder à une partie du jeu ou la fentre des parametres
    """
    def montrer_acceuil(self):
        #ici on nettoie la fentre s'il y avait un frame avant
        if self.actuel_frame is not None :
            self.actuel_frame.destroy()
        image_arriere = Image.open("Gui/picture.jpg")  
        image_arriere = image_arriere.resize((800, 600), Image.Resampling.LANCZOS)   
        self.convertir_image = ImageTk.PhotoImage(image_arriere)
        # inserer dans la fenetre l'image 
        self.bg_label = tk.Label(self.fenetre, image=self.convertir_image)
        self.bg_label.place(relwidth=1, relheight=1)
        
        # le frame acceuil :
        self.actuel_frame=tk.Frame(self.fenetre, bg="#29417d", width=400, height=300)
        self.actuel_frame.pack(pady=100)
        self.actuel_frame.pack_propagate(False)
         
        self.titre = tk.Label(self.actuel_frame, text="TIC-TAC-TOE", fg="white" ,font=("Arial", 24), bg="#29417d")
        self.titre.pack(padx=20, pady=20) 

        # les boutons de l'acceuil
        self.commencer= tk.Button(self.actuel_frame,text="Lancer une partie", command=self.montrer_jeu_defaut,bg="#7683e7", fg="white", font=("Arial", 14), relief="solid", borderwidth=2, width=20, height=2)
        self.commencer.pack(pady=20)

        self.parametre=tk.Button(self.actuel_frame,text="Paramétres", command=self.montrer_parametre ,bg="#7683e7", fg="white", font=("Arial", 14),relief="solid", borderwidth=2, width=20, height=2)
        self.parametre.pack(pady=20)
    
    # La methode pour la fenetre paramtres : 
    """" 
    cette methode initialise la fentre parametre qui va permettre 
    au joueur de choisir ses preferences tel la taille de la grille 
    griser des cases ou pas 
    """
    def montrer_parametre(self): 
        if self.actuel_frame is not None : 
            self.actuel_frame.destroy()
        self.actuel_frame=tk.Frame(self.fenetre, bg="#384b7a", width=600, height=300)
        self.actuel_frame.grid(pady=100, padx=80)
        self.actuel_frame.grid_propagate(False)
        # titre des parametres 
        self.titre=tk.Label(self.actuel_frame, text="Paramètres du jeu",font=("Arial", 24), bg="#384b7a",pady=20)
        self.titre.grid ( row=0, column=1, columnspan=2)

         # les boutons : 
         # Première ligne pour la taille de la grille
        self.taille_var = tk.StringVar()
        self.taille_label = tk.Label(self.actuel_frame, text="Taille de la grille:" , bg="#384b7a")
        self.taille_label.grid(row=1, column=0, padx=10, sticky="w")
        self.radio_3x3 = tk.Radiobutton(self.actuel_frame, text="3x3", value="3x3",bg="#384b7a", variable=self.taille_var)
        self.radio_4x4 = tk.Radiobutton(self.actuel_frame, text="4x4", value="4x4", bg="#384b7a",variable=self.taille_var)
        self.radio_5x5 = tk.Radiobutton(self.actuel_frame, text="5x5", value="5x5",bg="#384b7a",variable=self.taille_var)
        self.radio_3x3.grid(row=1, column=1, sticky="w")
        self.radio_4x4.grid(row=1, column=2, sticky="w")
        self.radio_5x5.grid(row=1, column=3, sticky="w")

        # Deuxième ligne pour "cocher des cases"
        self.cocher_var = tk.BooleanVar()
        self.cocher_label = tk.Label(self.actuel_frame, text="Cocher des cases",bg="#384b7a")
        self.cocher_label.grid(row=2, column=0, padx=10, sticky="w")
        self.radio_oui = tk.Radiobutton(self.actuel_frame, text="Oui",value=True, variable=self.cocher_var,bg="#384b7a")
        self.radio_non = tk.Radiobutton(self.actuel_frame, text="Non",value=False, variable=self.cocher_var,bg="#384b7a")
        self.radio_oui.grid(row=2, column=1, sticky="w")
        self.radio_non.grid(row=2, column=2, sticky="w")

        # Troisième ligne pour le nombre de cases à cocher
        self.nb_cases_label = tk.Label(self.actuel_frame, text="Nombre de cases à cocher:", bg="#384b7a" )
        self.nb_cases_label.grid(row=3, column=0, padx=10, sticky="w")
        self.nb_case_frame = tk.Entry(self.actuel_frame)
        self.nb_case_frame.grid(row=3, column=1, pady=5)

        # Quatrième ligne pour la couleur choisi
        self.couleur_var = tk.BooleanVar()
        self.couleur_label = tk.Label(self.actuel_frame, text="Symbole choisi", bg="#384b7a")
        self.couleur_label.grid(row=4, column=0, padx=10, sticky="w")
        self.couleur_red = tk.Radiobutton(self.actuel_frame, text="Rouge", value=True, variable=self.couleur_var,bg="#384b7a")
        self.couleur_blue = tk.Radiobutton(self.actuel_frame, text="Bleu", value=False,variable=self.couleur_var,bg="#384b7a")
        self.couleur_red.grid(row=4, column=1, sticky="w")
        self.couleur_blue.grid(row=4, column=2, sticky="w")

        # Bouton de soumission
        self.soumettre_bouton = tk.Button(self.actuel_frame, text="Valider", command=self.montrer_jeu,bg="#7683e7", fg="white", font=("Arial", 10), relief="solid", borderwidth=2, width=15, height=2)
        self.soumettre_bouton.grid(row=5, column=0, columnspan=3, pady=20)
    
    def montrer_jeu(self):
        # Détruire le précédent frame s'il existe
        if self.actuel_frame is not None: 
            self.actuel_frame.destroy()

        # Créer un nouveau frame pour le jeu
        self.actuel_frame = tk.Frame(self.fenetre, bg="#a1b8dc")
        self.actuel_frame.grid(row=0, column=0, sticky="nsew")
    
        # Configurer la taille de la fenêtre pour qu'elle prenne toute la place
        self.fenetre.grid_rowconfigure(0, weight=1)
        self.fenetre.grid_columnconfigure(0, weight=1)

        # frame qui va servir de menu 
        self.menu_frame = tk.Frame(self.actuel_frame,bg="#a1b8cc")
        self.menu_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
    
        self.bouton1 = tk.Button(self.menu_frame,fg="white",text="Arreter la partie", command=self.montrer_acceuil, relief="solid",bg="#384b7a", font=("Arial", 12, "bold"),width=15, height=2)
        self.bouton1.grid(row=1, column=0, padx=10, pady=10)

        self.bouton2 = tk.Button(self.menu_frame, text="Undo", fg="white", relief="solid", font=("Arial", 12, "bold"),width=15, bg="#384b7a",height=2)
        self.bouton2.grid(row=1, column=1, padx=10, pady=10)

        self.bouton3 = tk.Button(self.menu_frame, text="Vider la grille",bg="#384b7a", command=self.montrer_jeu, fg="white", relief="solid",font=("Arial", 12, "bold"), width=15, height=2)
        self.bouton3.grid(row=1, column=2, padx=10, pady=10)

        # Frame contenant les joueurs à droite
        self.joueurs_frame = tk.Frame(self.actuel_frame, bg="#f0f0f0", width=200, height=300)
        self.joueurs_frame.grid(row=1, column=5, padx= 10,pady=40)
        self.joueurs_frame.grid_propagate(False)
    
        # Titre de la frame des joueurs
        self.titre_joueurs_frame = tk.Label(self.joueurs_frame, text="A qui le tour",font=("Arial", 12, "bold"),padx=30)
        self.titre_joueurs_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky="e")

        # Boutons pour joueur et IA
        self.joueur1 = tk.Button(self.joueurs_frame, text="Joueur", bg="#a1b8cc",fg="white", relief="solid",font=("Arial", 12, "bold"), width=15, height=2, padx=13)
        self.joueur1.grid(row=1, column=1, columnspan=2, pady=10)

        self.joueurIA = tk.Button(self.joueurs_frame, text="Ordinateur", bg="#a1b8cc",fg="white", relief="solid",font=("Arial", 12, "bold"), width=15, height=2, padx=13)
        self.joueurIA.grid(row=2, column=1, columnspan=2, pady=10)

        # frame qui va contenir la grille du jeu : 
        self.grille_frame=tk.Frame(self.actuel_frame,width=600, height=500)
        self.grille_frame.grid(row=1, column=0, columnspan= 4)
        self.grille_frame.grid_propagate(False)
        taille = self.taille_var.get() 
        if taille == "3x3":
            taille_grille = 3
        elif taille == "4x4":
            taille_grille = 4
        else : 
            taille_grille = 5
        # ajustement des repartition des cases selon la dimension
        for i in range(taille_grille):
            self.grille_frame.grid_columnconfigure(i, weight=1) 
            self.grille_frame.grid_rowconfigure(i, weight=1)
        # creation de la grille
        for i in range(taille_grille):
            for j in range(taille_grille):
                bouton = tk.Button(self.grille_frame, text=f"({i},{j})", command=lambda x=i, y=j: print(f"Button {x},{y} clicked"))
                bouton.grid(row=i, column=j, sticky="nsew", padx=0, pady=0)

    def montrer_jeu_defaut(self):
        # Détruire le précédent frame s'il existe
        if self.actuel_frame is not None: 
            self.actuel_frame.destroy()

        # Créer un nouveau frame pour le jeu
        self.actuel_frame = tk.Frame(self.fenetre, bg="#a1b8dc")
        self.actuel_frame.grid(row=0, column=0, sticky="nsew")
    
        # Configurer la taille de la fenêtre pour qu'elle prenne toute la place
        self.fenetre.grid_rowconfigure(0, weight=1)
        self.fenetre.grid_columnconfigure(0, weight=1)

        # frame qui va servir de menu 
        self.menu_frame = tk.Frame(self.actuel_frame,bg="#a1b8cc")
        self.menu_frame.grid(row=0, column=0, columnspan=3, sticky="ew")
    
        self.bouton1 = tk.Button(self.menu_frame,fg="white",text="Arreter la partie", command=self.montrer_acceuil, relief="solid",bg="#384b7a", font=("Arial", 12, "bold"),width=15, height=2)
        self.bouton1.grid(row=1, column=0, padx=10, pady=10)

        self.bouton2 = tk.Button(self.menu_frame, text="Undo", fg="white", relief="solid", font=("Arial", 12, "bold"),width=15, bg="#384b7a",height=2)
        self.bouton2.grid(row=1, column=1, padx=10, pady=10)

        self.bouton3 = tk.Button(self.menu_frame, text="Vider la grille",bg="#384b7a", command=self.montrer_jeu, fg="white", relief="solid",font=("Arial", 12, "bold"), width=15, height=2)
        self.bouton3.grid(row=1, column=2, padx=10, pady=10)

        # Frame contenant les joueurs à droite
        self.joueurs_frame = tk.Frame(self.actuel_frame, bg="#f0f0f0", width=200, height=300)
        self.joueurs_frame.grid(row=1, column=5, padx= 10,pady=40)
        self.joueurs_frame.grid_propagate(False)
    
        # Titre de la frame des joueurs
        self.titre_joueurs_frame = tk.Label(self.joueurs_frame, text="A qui le tour",font=("Arial", 12, "bold"),padx=30)
        self.titre_joueurs_frame.grid(row=0, column=0, columnspan=2, pady=10, sticky="e")

        # Boutons pour joueur et IA
        self.joueur1 = tk.Button(self.joueurs_frame, text="Joueur", bg="#a1b8cc",fg="white", relief="solid",font=("Arial", 12, "bold"), width=15, height=2, padx=13)
        self.joueur1.grid(row=1, column=1, columnspan=2, pady=10)

        self.joueurIA = tk.Button(self.joueurs_frame, text="Ordinateur", bg="#a1b8cc",fg="white", relief="solid",font=("Arial", 12, "bold"), width=15, height=2, padx=13)
        self.joueurIA.grid(row=2, column=1, columnspan=2, pady=10)

        # frame qui va contenir la grille du jeu : 
        self.grille_frame=tk.Frame(self.actuel_frame,width=600, height=500)
        self.grille_frame.grid(row=1, column=0, columnspan= 4)
        self.grille_frame.grid_propagate(False)
        # ajustement des repartitions
        for i in range(3):
            self.grille_frame.grid_columnconfigure(i, weight=1) 
            self.grille_frame.grid_rowconfigure(i, weight=1)
        # creation de la grille 3*3
        for i in range(3):
            for j in range(3):
                bouton = tk.Button(self.grille_frame, text=f"({i},{j})", command=lambda x=i, y=j: print(f"Button {x},{y} clicked"))
                bouton.grid(row=i, column=j, sticky="nsew",padx=0, pady=0)



         


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
        self.fenetre.mainloop()

