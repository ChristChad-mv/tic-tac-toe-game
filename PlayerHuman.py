
class PlayerHuman (player) : 

    # definition de la methode abstraite plaplay
    def PLAPlay(grid, lign , column, lPLAPlayed) :
        # le lPLAPlayed va recuper la liste des coups joués par l'adversaire
        # car avant de cliquer une case il faut verifier que celle ci n'est pas cliqués deja par les deux 
        # joueur l'IA et l'humain 
        if ( (lign <0 or lign > len(grid)) or (column< 0 or column > len(grid[0]))) : 
            print ("erreur la case que vous cliquer n'existe pas")
            return False
        if ( (lign , column) in self.getlPLAPlayed ) or ((lign, column) in lPLAPlayed) : 
            print (" la case est deja joué par l'un des joueurs")
            return False
        else :
            PLArecord_move (self, row, col)
            return True 
    # ici cette methode va permettre de revenir sur une case deja choisi
    def PLAHUMundo (self,game_logic):
        #on va biensur mettre à jour la liste des coups joués
        return 0 

