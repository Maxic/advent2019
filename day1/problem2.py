def main():
    fuel_sum = 0

    with open("input.txt", "r+") as file:
        content = file.readlines()
        for line in content:
            mass = int(line)
            fuel_sum += calc_fuel(mass)
    print(fuel_sum)


def calc_fuel(mass):
    fuel = 0
    while mass > 0:
        mass = mass // 3 - 2
        if mass > 0:
            fuel += mass
    return fuel


if __name__ == "__main__":
    main()
