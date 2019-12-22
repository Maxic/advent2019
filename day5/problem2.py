from helpers.intcode import Intcode


def main():
    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        program = Intcode(intcode, [5])
        print(program.execute())


if __name__ == "__main__":
    main()

