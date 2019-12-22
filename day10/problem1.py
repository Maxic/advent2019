asteroid_dict_full = {}
asteroid_dict = {}
width = 0
height = 0


def main():
    global height
    global width
    global asteroid_dict_full
    global asteroid_dict
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    with open("input.txt", "r+") as file:
        content = file.readlines()

        y = 0

        # array with all asteroid coordinates
        for line in content:
            x = 0
            for char in line:
                if char == '#':
                    asteroid_dict_full[(y, x)] = True
                x += 1
            y += 1
        height = content.__len__()
        width = line.__len__()

    for asteroid in asteroid_dict_full.keys():
        asteroid_dict = asteroid_dict_full.copy()

        # set self to false
        asteroid_dict[asteroid] = False

        # Check all directions
        for direction in directions:
            asteroid
            x = asteroid[1]
            y = asteroid[0]

            if check_direction(x, y, direction, True) is not None:
                x, y = check_direction(x, y, direction, True)
                check_direction(x, y, direction, False)

        count = 0
        for value in asteroid_dict.values():
            if value:
                count += 1
        print("Asteroid: {0}. Count: {1}".format(asteroid, count))

    print(asteroid_dict)


def get_new_coords(x, y, direction):
    if direction == 'N':
        return x, y-1
    elif direction == 'NE':
        return x+1, y-1
    elif direction == 'E':
        return x+1, y
    elif direction == 'SE':
        return x+1, y+1
    elif direction == 'S':
        return x, y+1
    elif direction == 'SW':
        return x-1, y+1
    elif direction == 'W':
        return x-1, y
    elif direction == 'NW':
        return x-1, y-1


def check_direction(x, y, direction, first_check):
    x, y = get_new_coords(x,y, direction)
    while x >= 0 and y >= 0 and y < height and x < width:
        if (y, x) in asteroid_dict:
            if first_check:
                return x, y
            asteroid_dict[(y, x)] = False
        x, y = get_new_coords(x, y, direction)


if __name__ == "__main__":
    main()

