
class PlayerHuman (player) : 

    # definition de la methode abstraite plaplay
    def PLAPlay(self, grid, lign , column) :
        # le lPLAPlayed va recuper la liste des coups joués par l'adversaire
        # car avant de cliquer une case il faut verifier que celle ci n'est pas cliqués deja par les deux 
        # joueur l'IA et l'humain 
        if ( (lign <0 or lign > len(grid)) or (column< 0 or column > len(grid[0]))) : 
            print ("erreur la case que vous cliquer n'existe pas")
            return False
        if (lign,column) in self.lPLAll_moves : 
            print (" la case est deja joué par l'un des joueurs")
            return False
        else :
            self.PLArecord_move (lign, column)
            return True 
    # ici cette methode va permettre de revenir sur une case deja choisi
    def PLAHUMundo (self,row, col):
        # cette methode va annuler la derniere case jouée 
        self.lPLAPlayed((row,col))
        self.lPLAll_moves((row,col))
