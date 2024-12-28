class grid : 
    # ici on cree la grille du jeu 
    def __init__(self, size):
        self.size = size
        self.grid = [[None] * size for _ in range(size)]

    
    def check_winner(self, symbol):
        # Vérifie les lignes
        for row in self.grid:
            if all(cell == symbol for cell in row):
                return True

        # Vérifie les colonnes
        for col in range(self.size):
            if all(self.grid[row][col] == symbol for row in range(self.size)):
                return True

        # Vérifie les diagonales
        if all(self.grid[i][i] == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size - i - 1] == symbol for i in range(self.size)):
            return True

        return False
