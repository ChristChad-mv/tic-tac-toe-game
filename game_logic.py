import grid 
class game_logic : 
    def __init__(self, playerH, playerIA) :
        # cette classe doit contenir une liste contenant les joueurs 
        # une grille 
        self.lGAMPlayers = [ playerH, playerIA]
        self.grid=grid()
        self.pGAMCurrent_Player = playerIA

    # permuter le joueur actuel 
    def GAMSwitchPlayer(self) : 
        if (self.pGAMCurrent_Player == self.lGAMPlayers[0]): 
            self.pGAMCurrent_Player=self.lGAMPlayers[1]
        else :
             self.pGAMCurrent_Player=self. lGAMPlayers[0]
    def GAMPlayerTurn (self):
        self.pGAMCurrent_Player.PLAPlay(grid, lign , column)



