import copy

def expand_oxygen(new_map_arr, y, x):
    # fill north, west, south and east with O

    try:
        if new_map_arr[y + 1][x] != '█':
            new_map_arr[y + 1][x] = 'o'

        if new_map_arr[y][x - 1] != '█':
            new_map_arr[y][x - 1] = 'o'

        if new_map_arr[y - 1][x] != '█':
            new_map_arr[y - 1][x] = 'o'

        if new_map_arr[y][x + 1] != '█':
            new_map_arr[y][x + 1] = 'o'
    except Exception as e:
        print(e)


def main():
    with open("input2.txt", "r+") as file:
        map_arr = list(map(lambda y: list(y), list(map(lambda x: x.replace('\n', ''), file.readlines()))))

        height = map_arr.__len__()
        width = map_arr[0].__len__()
        counter = 1

        while [y for x in map_arr for y in x].__contains__(' '):
            new_map_arr = copy.deepcopy(map_arr)

            for y in range(height):
                for x in range(width):
                    if map_arr[y][x] is 'o':
                        expand_oxygen(new_map_arr, y, x)

            map_arr = copy.deepcopy(new_map_arr)
            counter += 1

        print(counter)


def print_map(map):
    for row in map:
        print()
        for char in row:
            print(char, end='')

    print()


if __name__ == "__main__":
    main()
