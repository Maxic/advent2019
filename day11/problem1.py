from helpers.intcode import Intcode
from day11.painting_robot import Robot


def main():

    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        program = Intcode(intcode)

        # Create an array of black panels, start the robot somewhere in the middle
        ship_hull = [[0] * 200 for _ in range(200)]
        epr = Robot(x_pos=100, y_pos=100)

        while program.state != 'HALTED':
            current_panel = ship_hull[epr.y_pos][epr.x_pos]
            program.input_array.append(current_panel)
            program.execute()
            instructions = program.output_arr

            # paint the square
            epr.paint(instructions[0], ship_hull)

            # move position
            epr.move(instructions[1])

            # reset output array
            program.output_arr = []

        print(epr.painted_coords.__len__())

        # for row in ship_hull:
        #     print()
        #     for char in row:
        #         if char == 0:
        #             print('`', end='')
        #         else:
        #             print('X', end='')


if __name__ == "__main__":
    main()

