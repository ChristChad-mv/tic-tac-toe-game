import gui 
import tkinter as tk 

class GuiAcceuil(gui.Gui):
    # le constructuer appelle le constructeur de la mere 
    def __init__(self) :
        super().__init__()
    
    # 
    def create_widgets(self):
        self.GAStartButton = tk.Button(self.window, text="Lancer une partie", command=self.GAStart_game)
        self.GAStartButton.pack(pady=20)
        self.GAParamButton = tk.Button(self.window, text="Parametres", command=self.GAOpen_param)
        self.GAParamButton.pack(pady=20)  
    #avec cette methode on va creer une fenetre de jeu quand on clique sur le bouton start
    def GAStart_game(self):
        ## rien encore
        return 0
    #ici on va creer la fentre des parametres
    def GAOpen_param(self):
        return 0
        


