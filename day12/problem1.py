import re
from day12.moon import Moon


def print_moons(moons):
    for moon in moons:
        print('pos=<x={0}, y ={1}, z ={2}> , vel=<x={3}, y={4}, z={5}>'.format(moon.x, moon.y, moon.z, moon.x_v, moon.y_v, moon.z_v))
    print()


def main():
    steps = 1000

    with open("input.txt", "r+") as file:
        content = file.readlines()

        moons = []

        for line in content:
            group = re.match("<x=(.*), y=(.*), z=(.*)>", line)
            moons.append(Moon(int(group[1]), int(group[2]), int(group[3])))

        for step in range(steps):
            coordinates = [(moon.x, moon.y, moon.z) for moon in moons]

            for moon in moons:
                # calc gravity
                moon.apply_gravity(coordinates)
                # calc v
                moon.apply_velocity()

        total_energy = sum([moon.get_total_energy() for moon in moons])

        print(total_energy)


if __name__ == "__main__":
    main()

