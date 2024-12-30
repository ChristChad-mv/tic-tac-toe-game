"""
Ce module GuiParam herite du module generique Gui
il represente la fentre qui s'affiche si l'utilisateur accede aux parametres du jeu 

"""
import tkinter as tk 
from gui import Gui
from PIL import Image, ImageTk

class GuiParam(Gui):

    # Le constructeur appelle le constructeur de la classe parente
    def __init__(self):
        super().__init__()

    def create_widgets(self): 
        """
        Ici on crée un frame qu'on manipule avec le grid pour 
        une meilleure gestion des composantes du formulaire 
        """
        self.grid_frame = tk.Frame(self.window,width=400, height=350, bg="#a1b8cc")
        self.grid_frame.pack(padx=20, pady=20)

        # Titre dans le grid
        self.title_grid = tk.Label(self.grid_frame, text="Paramètres du jeu", font=("Arial", 24))
        self.title_grid.grid(row=0, column=0, columnspan=4, pady=10)

        # Première ligne pour la taille de la grille
        self.taille_var = tk.StringVar()
        self.taille_label = tk.Label(self.grid_frame, text="Taille de la grille:" , bg="#a1b8cc")
        self.taille_label.grid(row=1, column=0, padx=10, sticky="w")
        self.radio_3x3 = tk.Radiobutton(self.grid_frame, text="3x3", value="3x3",bg="#a1b8cc", variable=self.taille_var)
        self.radio_4x4 = tk.Radiobutton(self.grid_frame, text="4x4", value="4x4", bg="#a1b8cc",variable=self.taille_var)
        self.radio_5x5 = tk.Radiobutton(self.grid_frame, text="5x5", value="5x5",bg="#a1b8cc",variable=self.taille_var)
        self.radio_3x3.grid(row=1, column=1, sticky="w")
        self.radio_4x4.grid(row=1, column=2, sticky="w")
        self.radio_5x5.grid(row=1, column=3, sticky="w")

        # Deuxième ligne pour "cocher des cases"
        self.cocher_var = tk.BooleanVar()
        self.cocher_label = tk.Label(self.grid_frame, text="Cocher des cases",bg="#a1b8cc")
        self.cocher_label.grid(row=2, column=0, padx=10, sticky="w")
        self.radio_oui = tk.Radiobutton(self.grid_frame, text="Oui",value=True, variable=self.cocher_var,bg="#a1b8cc")
        self.radio_non = tk.Radiobutton(self.grid_frame, text="Non",value=False, variable=self.cocher_var,bg="#a1b8cc")
        self.radio_oui.grid(row=2, column=1, sticky="w")
        self.radio_non.grid(row=2, column=2, sticky="w")

        # Troisième ligne pour le nombre de cases à cocher
        self.nb_cases_label = tk.Label(self.grid_frame, text="Nombre de cases à cocher:", bg="#a1b8cc")
        self.nb_cases_label.grid(row=3, column=0, padx=10, sticky="w")
        self.nb_case_frame = tk.Entry(self.grid_frame)
        self.nb_case_frame.grid(row=3, column=1, pady=5)

        # Quatrième ligne pour le symbole choisi
        self.symbol_var = tk.BooleanVar()
        self.symbol_label = tk.Label(self.grid_frame, text="Symbole choisi", bg="#a1b8cc")
        self.symbol_label.grid(row=4, column=0, padx=10, sticky="w")
        self.symbol_red = tk.Radiobutton(self.grid_frame, text="Rouge", value=True, variable=self.symbol_var,bg="#a1b8cc")
        self.symbol_blue = tk.Radiobutton(self.grid_frame, text="Bleu", value=False,variable=self.symbol_var,bg="#a1b8cc")
        self.symbol_red.grid(row=4, column=1, sticky="w")
        self.symbol_blue.grid(row=4, column=2, sticky="w")

        # Bouton de soumission
        self.submit_button = tk.Button(self.grid_frame, text="Valider", command=self.GAStart_game)
        self.submit_button.grid(row=5, column=0, columnspan=3, pady=20)
    
    def GAStart_game(self):
        return 0
    

if __name__ == "__main__":
    app = GuiParam()
    app.run()
