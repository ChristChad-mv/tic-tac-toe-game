"""
Module Gui

Ce module represente l'interface standard 
c'est un module abstrait qui sera par la suite implementer par
deux autres classes : guiAcceuil et guiParam et guiPlay chaqu'une specifiant une 
fenetre du jeu
"""

import tkinter as tk 
from abc import ABC
import game_logic

class Gui(ABC) : 
    """
    constructeur : 
    Ici on veut créer une surchage de constructeur car pour les modules
    GuiAcceuil et GuoParam on a pas besoin de la game_logic
    donc si l'utilisateur fourni une isntante game_logic en parametre 
    alors on consider le constructeur avec ce parametre sinon on fait sans 
    Les parametres :
    game_logic : est une instance du module game_logic
     
    """
    def __init__ (self, game_logic=None):
        # le parametre game_logic optionnel selon le module appelant
        if game_logic is not None :
            self.game_logic=game_logic
        else :
            self.game_logic = None
        
        self.window=tk.Tk()
        width_in_pixels = 550
        height_in_pixels = 500
        self.window.geometry(f"{width_in_pixels}x{height_in_pixels}+0+0") 
        self.window.title("Tic-Tac-Toe")
        self.create_widgets()

    # @abstractmethod  
    """
    Cette methode est abstraite elle sera par la suite
    implementer par les modules plus specifiques representant les fenetres des jeux

    """
    def create_widgets(self) :
        pass
    """
    cette methode va contenir la boucle principale 
    pour traiter les evenements tkinter
    """
    def run(self):
        #la boucle principale de la fenetre
        self.window.mainloop()

    
    """
    methode pour fermer la fenetre 
    """
    #fermer la fenetre 
    def fermer_fenetre(self):
        self.window.quit()

