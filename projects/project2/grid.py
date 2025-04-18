from cell import Cell

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(x, y, False) for y in range(cols)] for x in range(rows)]

    def display(self):
        for row in self.grid:
            print(" ".join(["🦠" if cell.get_state() else " " for cell in row]))
        print()

    def get_cell(self, x, y):
        return self.grid[x][y]

    def set_cell(self, x, y, state):
        self.grid[x][y].set_state(state)

    def count_neighbors(self, x, y):
        neighbors = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.rows and 0 <= j < self.cols and (i != x or j != y):
                    if self.grid[i][j].get_state():
                        neighbors += 1
        return neighbors

    def update(self):
        new_grid = [[Cell(x, y) for y in range(self.cols)] for x in range(self.rows)]
        for x in range(self.rows):
            for y in range(self.cols):
                neighbors = self.count_neighbors(x, y)
                new_grid[x][y].update_state(neighbors)
        self.grid = new_grid
