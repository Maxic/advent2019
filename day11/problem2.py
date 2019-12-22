from helpers.intcode import Intcode
from day11.painting_robot import Robot


def main():

    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        program = Intcode(intcode)

        # Create an array of black panels, start the robot somewhere in the middle
        ship_hull = [[0] * 100 for _ in range(100)]
        epr = Robot(x_pos=50, y_pos=50)

        # start on a white panel
        ship_hull[50][50] = 1

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

        for row in ship_hull:
            print()
            for char in row:
                if char == 0:
                    print('`', end='')
                else:
                    print('X', end='')

        # RJLFBUCU


if __name__ == "__main__":
    main()

