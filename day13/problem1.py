from helpers.intcode import Intcode


def main():

    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        program = Intcode(intcode)

        # Create the map for the game
        # 0 is empty                `
        # 1 is wall                 X
        # 2 is block                #
        # 3 is horizontal paddle    _
        # 4 is ball                 o
        game_map = [[0] * 200 for _ in range(200)]

        program.execute()
        instructions = program.output_arr

        pointer = 2
        block_count = 0

        while pointer < instructions.__len__():
            if instructions[pointer] == 2:
                block_count += 1
            pointer += 3

        print(block_count)


if __name__ == "__main__":
    main()
