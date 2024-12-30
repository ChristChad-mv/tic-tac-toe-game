from gui import Gui
from GuiParam import GuiParam
import tkinter as tk 

class GuiAcceuil(Gui):
    # le constructuer appelle le constructeur de la mere 
    def __init__(self) :
        super().__init__()
    
    
    def create_widgets(self):
        # creer un frame ou je place les bouton
        self.grid_frame = tk.Frame(self.window, bg="#a1b8cc")
        self.grid_frame.pack(padx=20, pady=20)
        # le titre du jeu 
        self.titre = tk.Label(self.grid_frame, text="TIC-TAC-TOE",  font=("Arial", 24))
        self.titre.pack(padx=20, pady=20)
        # les boutons 
        self.GAStartButton = tk.Button(self.grid_frame, text="Lancer une partie", command=self.GAStart_game)
        self.GAStartButton.pack(pady=20)
        self.GAParamButton = tk.Button(self.grid_frame, text="Parametres", command=self.GAOpen_param)
        self.GAParamButton.pack(pady=20)  
        
    #avec cette methode on va creer une fenetre de jeu quand on clique sur le bouton start
    def GAStart_game(self):
        
       return 0
        
    
    """
    ici on va naviguer vers la fentre des parametres
    on crée donc une instance du module GuiParam
    """
    def GAOpen_param(self):
        param_window = GuiParam()
        param_window.run()
        # on ferme la fenetre acceuil 
        self.fermer_fenetre()
        

if __name__ == "__main__":
    app = GuiAcceuil()
    app.run()
