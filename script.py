# Class representing the Sudoku grid
class SudokuGrid:
    def __init__(self):
        # The Sudoku grid is initialized as a 9x9 matrix
        self.grid = [[0] * 9 for _ in range(9)]
        self.initial_grid = [[0] * 9 for _ in range(9)]

    # Method to import and parse a grid from a file
    def import_grid(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            for i in range(9):
                for j in range(9):
                    num = lines[i][j]
                    if num in ('_', '-'):
                        self.grid[i][j] = 0
                    else:
                        self.grid[i][j] = int(num)
                        self.initial_grid[i][j] = int(num)
  

    # Method to display grid in terminal
    def show_grid(self):
        for row_idx, row in enumerate(self.grid):
            row_str = ""
            for col_idx, cell in enumerate(row):
                if cell == 0:
                    row_str += "_ "  
                else:
                    # If the box has been filled by the algorithm, display in red
                    if self.initial_grid[row_idx][col_idx] == 0:
                        # Display in red if inserted
                        row_str += f"\033[31m{cell}\033[0m "  
                    else:
                        # Normal display if already present
                        row_str += f"{cell} "  
            print(row_str)
    # Method to check if a digit is valid in a given position
    def is_valid(self, row, col, num):
        # Check line
        for i in range(9):
            if self.grid[row][i] == num:
                return False
        
        # Check column
        for i in range(9):
            if self.grid[i][col] == num:
                return False
        
        # Check the 3x3 subgrid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        
        return True



    # Method for solving the grid with the backtracking algorithm
    def resolve_backtracking(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0: 
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.grid[row][col] = num
                            print(f"Attempt from {num} to ({row}, {col})")  
                            self.show_grid()  
                            if self.resolve_backtracking():
                                return True
                            self.grid[row][col] = 0  
                            print(f"Go back to ({row}, {col})")
                    return False
        return True

    def solve_brute_force(self):
        """Résout le Sudoku par force brute en testant toutes les combinaisons possibles."""
        empty_cells = [(r, c) for r in range(9) for c in range(9) if self.grid[r][c] == 0]

        def brute_force(index=0):
            """Récursion pour essayer toutes les valeurs possibles dans les cases vides."""
            if index == len(empty_cells):
                return True  # Toutes les cases sont remplies, solution trouvée

            row, col = empty_cells[index]
            for num in range(1, 10):  # Essayer les chiffres de 1 à 9
                if self.is_valid(row, col, num):
                    self.grid[row][col] = num  # Placer le chiffre
                    if brute_force(index + 1):  # Récursivité pour la case suivante
                        return True
                    self.grid[row][col] = 0  # Backtracking si l'essai ne fonctionne pas

            return False  # Aucun chiffre ne fonctionne pour cette case

        return brute_force()