from helpers.Intcode import IntCode
import itertools


def main():
    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        # set phase settings
        phase_settings = list(range(5, 10))

        program = IntCode(intcode)
        program.execute()


if __name__ == "__main__":
    main()

