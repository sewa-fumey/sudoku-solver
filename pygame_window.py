import pygame
from config import *

class SudokuPygame:
    def __init__(self, sudoku_grid):
        self.sudoku_grid = sudoku_grid
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.font = pygame.font.SysFont('Arial', 40)

    def draw_title(self, title):
        title_text = self.font.render(title, True, BLACK)
        self.screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 10))

    def draw_grid(self):
        self.screen.fill((WHITE))  

        # Draw the grid boxes
        for row in range(9):
            for col in range(9):
                x, y = col * cell_size, row * cell_size
                pygame.draw.rect(self.screen, (BLACK), (x, y, cell_size, cell_size), 1)

                if self.sudoku_grid.grid[row][col] != 0:
                    # Determine the color (red for values ​​inserted by the algorithm)
                    if self.sudoku_grid.initial_grid[row][col] == 0:
                        color = RED
                    else:
                        color = BLACK
                    
                    text = self.font.render(str(self.sudoku_grid.grid[row][col]), True, color)
                    self.screen.blit(text, (x + 20, y + 10))  

        # Draw the extra lines for the 3x3 squares
        for i in range(1, 9):
            if i % 3 == 0:
                pygame.draw.line(self.screen, (BLACK), (0, i * cell_size), (540, i * cell_size), 5)
                pygame.draw.line(self.screen, (BLACK), (i * cell_size, 0), (i * cell_size, 540), 5)

        # Update the Pygame
        pygame.display.flip()

    def start_display(self):
        running = True
        while running:
            self.draw_title("Sudoku Solver")
            self.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    return
            
            


