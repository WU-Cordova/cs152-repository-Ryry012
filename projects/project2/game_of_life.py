import random
import time

class Cell:
    def __init__(self, alive=False):
        self.alive = alive

    def update(self, neighbors):
        if self.alive:
            if neighbors < 2 or neighbors > 3:
                self.alive = False
        else:
            if neighbors == 3:
                self.alive = True

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(random.choice([True, False])) for _ in range(width)] for _ in range(height)]

    def get_neighbors(self, x, y):
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                nx, ny = x + i, y + j
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if self.grid[ny][nx].alive:
                        neighbors += 1
        return neighbors

    def update(self):
        new_grid = [[Cell() for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.get_neighbors(x, y)
                new_grid[y][x].update(neighbors)
        self.grid = new_grid

    def display(self):
        for row in self.grid:
            print(" ".join(['X' if cell.alive else '.' for cell in row]))
        print()

def main():
    width, height = 5, 5
    grid = Grid(width, height)

    while True:
        grid.display()
        grid.update()
        time.sleep(1)

if __name__ == "__main__":
    main()
