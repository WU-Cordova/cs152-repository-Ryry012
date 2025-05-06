class Cell:
    def __init__(self, x, y, alive=False):
        self.x = x
        self.y = y
        self.alive = alive

    def get_state(self):
        return self.alive
    
    def update_state(self, neighbors):
        if self.alive:
            if neighbors < 2 or neighbors > 3:
                self.alive = False
        else:
            if neighbors == 3:
                self.alive = True
