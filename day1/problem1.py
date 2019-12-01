def main():
    fuel_sum = 0

    with open("input.txt", "r+") as file:
        content = file.readlines()
        for line in content:
            mass = int(line)
            fuel = mass // 3 - 2
            fuel_sum += fuel
    print(fuel_sum)


if __name__ == "__main__":
    main()

