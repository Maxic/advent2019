from helpers.intcode import Intcode
from day15.droid import Droid
import sys
import random

"""
        1 NORTH
    3 WEST     4 EAST
        2 SOUTH

"""

not_found = True


def main():
    global not_found
    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        program = Intcode(intcode, input_array=[])

        # Let's draw a maze:
        maze = [['#'] * 44 for _ in range(44)]
        droid = Droid(22, 22)
        maze[droid.y][droid.x] = '.'

        # run and wait for input
        program.execute()

        while not_found:
            # scan all around
            directions = scan(maze, program, droid)
            print_maze(maze)

            # decide where to move
            smart_move_droid(droid, program, maze, directions)

        print()
        print(droid.history.__len__() + 2)


def scan(maze, program, droid):
    # check all directions, and fill map, return possible directions to move
    possible_directions = []
    global not_found

    for direction in range(1, 5):
        program.input_array.append(direction)
        output = program.execute()

        if output == 1:
            # update droid coordinates if it actually moved
            droid.move(direction)

            # move back
            opp_direction = get_opposite_direction(direction)
            move_droid(droid, program, opp_direction)
            possible_directions.append(direction)
        elif output == 2:
            maze[droid.y][droid.x] = '@'
            not_found = False
        else:
            draw_wall(direction, droid, maze)

    return possible_directions


def get_opposite_direction(direction):
    return direction - 1 if direction % 2 == 0 else direction + 1


def get_coordinates(droid, direction):
    x = droid.x
    y = droid.y

    if direction == 1:
        return x, y-1
    elif direction == 2:
        return x, y+1
    elif direction == 3:
        return x-1, y
    else:
        return x+1, y


def smart_move_droid(droid, program, maze, directions):
    new_directions = []
    backtracking = False

    # determine direction
    for direction in directions:
        x, y = get_coordinates(droid, direction)
        if maze[y][x] != '.':
            new_directions.append(direction)

    # if there are no options, backtrack, otherwise randomly pick from the options
    if not new_directions:
        direction = get_opposite_direction(droid.history[-1])
        droid.history = droid.history[:-1].copy()
        backtracking = True
    else:
        direction = random.choice(new_directions)

    # Actually move in that direction
    program.input_array.append(direction)
    output = program.execute()
    if output == 0:
        sys.exit("CANT DO THAT MASTER")

    # update map and history
    x, y = get_coordinates(droid, direction)
    maze[y][x] = '.'
    droid.move(direction)
    if not backtracking:
        droid.history.append(direction)


def move_droid(droid, program, direction):
    program.input_array.append(direction)
    output = program.execute()
    if output == 0:
        sys.exit("CANT DO THAT MASTER")
    droid.move(direction)


def draw_wall(direction, droid, maze):
    fill_char = '\u2588'

    # paint map
    if direction == 1:
        maze[droid.y-1][droid.x] = fill_char
    elif direction == 2:
        maze[droid.y+1][droid.x] = fill_char
    elif direction == 3:
        maze[droid.y][droid.x-1] = fill_char
    elif direction == 4:
        maze[droid.y][droid.x+1] = fill_char


def print_maze(maze):
    for row in maze:
        print()
        for char in row:
            print(char, end='')

    print()


if __name__ == "__main__":
    main()
