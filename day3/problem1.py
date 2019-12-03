import sys
import functools


def main():
    with open("input.txt", "r+") as file:
        content = file.readlines()
        wire_route_1 = content[0].replace('\n', "").split(',')
        wire_route_2 = content[1].replace('\n', "").split(',')
        origin = (0, 0)

        # Get all coordinates
        coordinates_route_1 = get_route_coordinates(origin, wire_route_1)
        coordinates_route_2 = get_route_coordinates(origin, wire_route_2)

        # Intersect the set coordinates to get all intersections
        intersections = set(coordinates_route_1).intersection(coordinates_route_2)

        # calculate all distances
        min_distance = sys.maxsize
        for intersection in intersections:
            min_distance = min(calc_manhattan_distance(origin, intersection), min_distance)

        print(min_distance)


def calc_manhattan_distance(origin, intersection):
    return abs(origin[0]- intersection[0]) + abs(origin[1]- intersection[1])


def get_route_coordinates(origin, route):
    route_coordinates = []
    for instruction in route:
        direction = instruction[:1]
        length = int(instruction[1:])

        origin, path = run_instruction(origin, direction, length)
        route_coordinates.append(path)
    # flatmap and return the list of coordinates
    return functools.reduce(list.__add__, route_coordinates)


def run_instruction(origin, direction, length):
    path = []

    if direction == 'D':
        for i in range(1, length+1):
            path.append((origin[0], origin[1]-i))
    elif direction == 'U':
        for i in range(1, length+1):
            path.append((origin[0], origin[1]+i))
    elif direction == 'R':
        for i in range(1, length+1):
            path.append((origin[0]+i, origin[1]))
    elif direction == 'L':
        for i in range(1, length+1):
            path.append((origin[0]-i, origin[1]))
    else:
        print("Something went wrong, that direction doesn't exist")
        sys.exit()

    return path[-1], path


if __name__ == "__main__":
    main()
