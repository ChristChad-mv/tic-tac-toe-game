import tkinter as tk
from PIL import Image, ImageTk
class GUI :
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("TIC-TAC-TOE")
        self.window.geometry(f"{800}x{600}")
        self.window.resizable(width=False, height=False)
        self.actuel_frame =None
        self.montrer_acceuil()
    
    def montrer_acceuil(self):
        #ici on nettoie la fentre s'il y avait un frame avant
        if self.actuel_frame is not None :
            self.actuel_frame.destroy()
        image_arriere = Image.open("Gui\picture.jpg")  
        image_arriere = image_arriere.resize((800, 600), Image.Resampling.LANCZOS)   
        self.convert_image = ImageTk.PhotoImage(image_arriere)
        # inserer dans la fenetre l'image 
        self.bg_label = tk.Label(self.window, image=self.convert_image)
        self.bg_label.place(relwidth=1, relheight=1)
        
        # le frame acceuil :
        self.actuel_frame=tk.Frame(self.window, bg="#29417d", width=400, height=300)
        self.actuel_frame.pack(pady=100)
        self.actuel_frame.pack_propagate(False)
         
        self.titre = tk.Label(self.actuel_frame, text="TIC-TAC-TOE", font=("Arial", 24), bg="white")
        self.titre.pack(padx=20, pady=20) 

        # les boutons de l'acceuil
        self.commencer= tk.Button(self.actuel_frame,text="Lancer une partie", command=self.montrer_jeu,bg="#7683e7", fg="white", font=("Arial", 14), relief="solid", borderwidth=2, width=20, height=2)
        self.commencer.pack(pady=20)

        self.parametre=tk.Button(self.actuel_frame,text="Paramétres", command=self.montrer_parametre ,bg="#7683e7", fg="white", font=("Arial", 14),relief="solid", borderwidth=2, width=20, height=2)
        self.parametre.pack(pady=20)
    
    # la methode pour la fenetre paramtres : 
    def montrer_parametre(self): 
        if self.actuel_frame is not None : 
            self.actuel_frame.destroy()
        self.actuel_frame=tk.Frame(self.window, bg="#384b7a", width=600, height=300)
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

        # Quatrième ligne pour le symbole choisi
        self.symbol_var = tk.BooleanVar()
        self.symbol_label = tk.Label(self.actuel_frame, text="Symbole choisi", bg="#384b7a")
        self.symbol_label.grid(row=4, column=0, padx=10, sticky="w")
        self.symbol_red = tk.Radiobutton(self.actuel_frame, text="Rouge", value=True, variable=self.symbol_var,bg="#384b7a")
        self.symbol_blue = tk.Radiobutton(self.actuel_frame, text="Bleu", value=False,variable=self.symbol_var,bg="#384b7a")
        self.symbol_red.grid(row=4, column=1, sticky="w")
        self.symbol_blue.grid(row=4, column=2, sticky="w")

        # Bouton de soumission
        self.submit_button = tk.Button(self.actuel_frame, text="Valider", command=self.montrer_jeu,bg="#7683e7", fg="white", font=("Arial", 10), relief="solid", borderwidth=2, width=15, height=2)
        self.submit_button.grid(row=5, column=0, columnspan=3, pady=20)
    
    def montrer_jeu(self):
        # Détruire le précédent frame s'il existe
        if self.actuel_frame is not None: 
            self.actuel_frame.destroy()

        # Créer un nouveau frame pour le jeu
        self.actuel_frame = tk.Frame(self.window, bg="#a1b8dc")
        self.actuel_frame.grid(row=0, column=0, sticky="nsew")
    
        # Configurer la taille de la fenêtre pour qu'elle prenne toute la place
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_columnconfigure(0, weight=1)

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
