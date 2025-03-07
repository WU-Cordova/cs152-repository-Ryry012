from cell import Cell
import random
import time

class GameController:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(x, y, random.choice([True, False])) for y in range(cols)] for x in range(rows)]
        self.grid_history = []

    def display_grid(self):
        for row in self.grid:
            print(" ".join(["🦠" if cell.get_state() else " " for cell in row]))
        print()

    def count_neighbors(self, x, y):
        neighbors = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.rows and 0 <= j < self.cols and (i != x or j != y):
                    if self.grid[i][j].get_state():
                        neighbors += 1
        return neighbors

    def update_grid(self):
        new_grid = [[Cell(x, y) for y in range(self.cols)] for x in range(self.rows)]
        for x in range(self.rows):
            for y in range(self.cols):
                neighbors = self.count_neighbors(x, y)
                new_grid[x][y].update_state(neighbors)
        self.grid = new_grid

    def check_stagnation(self):
        return self.grid in self.grid_history[-3:]

    def run(self):
        while True:
            self.display_grid()
            if self.check_stagnation():
                print("The grid has stabilized or is repeating!")
                break

            mode = input("Enter 'A' for Automatic, 'M' for Manual, 'Q' to quit: ").strip().upper()
            if mode == 'A':
                while not self.check_stagnation():
                    self.update_grid()
                    self.display_grid()
                    time.sleep(1)
            elif mode == 'M':
                while not self.check_stagnation():
                    self.update_grid()
                    self.display_grid()
                    input("Press Enter to go to the next generation...")
            elif mode == 'Q':
                break
            else:
                print("Invalid input.")
