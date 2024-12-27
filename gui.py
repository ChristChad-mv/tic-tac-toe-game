import tkinter as tk 
from abc import ABC

class Gui(ABC) : 
    # constructeur 
    def __init__ (self,grid,game_logic):
        #self.grid=grid
        #self.game_logic=game_logic
        self.root = tk.Tk()
        self.window=tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.create_widgets()

    # @abstractmethod  
    def create_widgets(self) :
        pass
    def run(self):
        #la boucle principale de la fenetre
        self.window.mainloop()
    
    #fermer la fenetre 
    def fermer_fenetre(self):
        self.window.quit()

