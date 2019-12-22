class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.x_v = 0
        self.y_v = 0
        self.z_v = 0

    def apply_gravity(self, coordinates):
        for (x, y, z) in coordinates:
            self.x_v += 1 if x > self.x else 0 if x == self.x else -1
            self.y_v += 1 if y > self.y else 0 if y == self.y else -1
            self.z_v += 1 if z > self.z else 0 if z == self.z else -1

    def apply_velocity(self):
        self.x += self.x_v
        self.y += self.y_v
        self.z += self.z_v

    def get_potential_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def get_kinectic_energy(self):
        return abs(self.x_v) + abs(self.y_v) + abs(self.z_v)

    def get_total_energy(self):
        return self.get_potential_energy() * self.get_kinectic_energy()
