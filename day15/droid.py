class Droid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.history = []

    def move(self, direction):
        if direction == 1:
            self.y -= 1
        elif direction == 2:
            self.y += 1
        elif direction == 3:
            self.x -= 1
        elif direction == 4:
            self.x += 1
