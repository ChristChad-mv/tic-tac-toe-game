import gui 
import tkinter as tk 

class GuiParam(gui.Gui):
    # le constructuer appelle le constructeur de la mere 
    def __init__(self) :
        super().__init__()

    def create_widgets(self): 
        self.grid_frame = tk.Frame(self.window)
        # titre dans le grid
        self.title_grid=tk.Label(self.grid_frame,text="parametres du jeu")
        self.title_grid.grid(row=0, column=1)
        # premiere ligne 
        self.taille_label = tk.Label(self.grid_frame, text="Taille de la grille:")
        self.taille_label.grid(row=1, column=0, padx=10, sticky="w")
        self.radio_3x3 = tk.Radiobutton(self.grid_frame, text="3x3",value="3x3")
        self.radio_4x4 = tk.Radiobutton(self.grid_frame, text="4x4", value="4x4")
        self.radio_5x5 = tk.Radiobutton(self.grid_frame, text="5x5", value="5x5")
        self.radio_3x3.grid(row=1, column=1, sticky="w")
        self.radio_4x4.grid(row=1, column=2, sticky="w")
        self.radio_5x5.grid(row=1, column=3, sticky="w")

        # deuxieme ligne 
        self.case_label = tk.Label(self.grid_frame, text="cocher des cases")
        self.case_label.grid(row=2, column=0, padx=10, sticky="w")
        self.radio_oui = tk.Radiobutton(self.grid_frame, text="Oui", value=True)
        self.radio_non = tk.Radiobutton(self.grid_frame, text="Non", value=False)

        # troisieme ligne 
        self.nb_cases_label = tk.Label(self.grid_frame, text="Nombre de cases à cocher:")
        self.nb_cases_label.grid(row=3, column=0, padx=10, sticky="w")
        self.nb_case_frame = tk.Entry(self.grid_frame)
        self.nb_case_frame.grid(row=3, column=1, pady=5)

        # quatrieme ligne 
        self.symbol_label = tk.Label(self.grid_frame, text="symbole choisi")
        self.case_label.grid(row=4, column=0, padx=10, sticky="w")
        self.symbol_red = tk.Radiobutton(self.grid_frame, text="rouge",value=True)
        self.symbol_blue = tk.Radiobutton(self.grid_frame, text="bleu",value=False)
        # bouton de soumission 
        self.Submit_button = tk.Button(self.grid_frame, text="Valider")
        self.Submit_button.grid(row=13, column=0, columnspan=2, pady=20)