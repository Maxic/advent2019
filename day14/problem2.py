from helpers.intcode import Intcode
import time
score = 0


def main():

    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        # Set 'free play' mode
        intcode[0] = 2

        # Create the map for the game
        game_map = [[' '] * 42 for _ in range(27)]

        program = Intcode(intcode)

        while program.state != 'HALTED':
            program.execute()
            instructions = program.output_arr

            update_game(game_map, instructions)

            joystick_input = get_joystick_input(program.p)
            program.input_array.append(joystick_input)

        print(score)


def get_joystick_input(program):
    return 0
    # while True:
    #     print("Press 'a', 's', or 'd' to move the paddle:")
    #     key = keyboard.read_key(suppress=True)
    #     if key == 'a':
    #         return -1
    #     elif key == 's':
    #         return 0
    #     elif key == 'd':
    #         return 1
    #     # Save and wait for new input
    #     elif key == 'p':
    #         print_program(program)


def update_game(game_map, instructions):
    x_pos_p = 0
    y_pos_p = 1
    tile_p = 2

    while tile_p < instructions.__len__():
        x_pos = instructions[x_pos_p]
        y_pos = instructions[y_pos_p]
        tile = instructions[tile_p]
        global score

        if x_pos == -1 and y_pos == 0:
            score = tile

        # write to map
        write_to_map(x_pos, y_pos, tile, game_map)

        # update position
        x_pos_p, y_pos_p, tile_p = x_pos_p + 3, y_pos_p + 3, tile_p + 3
    time.sleep(.3)
    print_map(game_map)


def write_to_map(x_pos, y_pos, tile, game_map):
    # 0 is empty
    # 1 is wall                 X
    # 2 is block                #
    # 3 is horizontal paddle    _
    # 4 is ball                 o

    if tile == 0:
        game_map[y_pos][x_pos] = ' '
    elif tile == 1:
        game_map[y_pos][x_pos] = 'X'
    elif tile == 2:
        game_map[y_pos][x_pos] = '#'
    elif tile == 3:
        game_map[y_pos][x_pos] = '-'
    elif tile == 4:
        game_map[y_pos][x_pos] = 'o'


def print_map(game_map):
    # print map
    for row in game_map:
        print()
        for char in row:
            print(char, end='')


def print_program(program):
    for i in program:
        print(str(i) + ',', end='')


if __name__ == "__main__":
    main()
