class Robot:
    def __init__(self, x_pos, y_pos):
        self.direction = 'N'
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.painted_coords = set()

    def paint(self, instruction, ship_hull):
        ship_hull[self.y_pos][self.x_pos] = instruction
        self.painted_coords.add((self.x_pos, self.y_pos))

    def move(self, instruction):
        if self.direction == 'N':
            if instruction == 0:
                # turn left 90 degrees and move forward
                self.direction = 'W'
                self.x_pos -= 1
            else:
                # turn right 90 degrees and move forward
                self.direction = 'E'
                self.x_pos += 1

        elif self.direction == 'E':
            if instruction == 0:
                # turn left 90 degrees and move forward
                self.direction = 'N'
                self.y_pos -= 1
            else:
                # turn right 90 degrees and move forward
                self.direction = 'S'
                self.y_pos += 1

        elif self.direction == 'S':
            if instruction == 0:
                # turn left 90 degrees and move forward
                self.direction = 'E'
                self.x_pos += 1
            else:
                # turn right 90 degrees and move forward
                self.direction = 'W'
                self.x_pos -= 1

        elif self.direction == 'W':
            if instruction == 0:
                # turn left 90 degrees and move forward
                self.direction = 'S'
                self.y_pos += 1
            else:
                # turn right 90 degrees and move forward
                self.direction = 'N'
                self.y_pos -= 1


