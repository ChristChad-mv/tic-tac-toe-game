from abc import ABC
import game_logic 
class player (ABC) :
    # attriubt statique : 
    # cette listes va contenir toutes les cases jouées par les joueurs ( IA et humain)
    lPLAll_moves=[]  
    # constructeur  
    def __init__(self,sPLAName,sPLAColor, grid) :
        self.sPLAName=sPLAName
        self.sPLAColor=sPLAColor
        self.lPLAPlayed= [] # ce tableau recupere les coups joués par le joueur 
        self.grid=grid 
        
    # les getters et les setters 
    # les  getters
    
    def getsPLAName(self):
        return self.sPLAName
    def getsPLAColor(self):
        return self.sPLAColor
    def getlPLAPlayed(self):
        return self.lPLAPlayed
    
    # les setters : 
    def setsPLAName(self, sPLAName): 
        self.sPLAName=sPLAName

    def setsPLAColor (self, sPLAColor):
        self.sPLAColor=sPLAColor


    # placer un jeton couleur
    # @abstractmethod  
    def PLAPlay(grid, lign , column): 
        # methode abstraite qui sera implementer par les autres classes
        pass

    # cette methode permet de mettre la case jouée par le joueur dans la liste des coups joués
    def PLArecord_move (self, row, col):
        if (row, col) in self.lPLAll_moves :
            print ("la case est deja cliquée\n")
        else : 
            self.lPLAPlayed.append((row,col))
            self.lPLAll_moves.append((row,col))
    
    # cette methode permet de remettre la liste à zero 
    def PLAreset_hsitory(self):
        self.lPLAPlayed= []
        self.lPLAll_moves=[]

    # tostring methode 
    def PLAget_info (self):
       return f"Nom : {self.get_name()}, Couleur : {self.get_color()}"