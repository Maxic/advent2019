from helpers.Intcode import IntCode


def main():
    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        program = IntCode(intcode, [5])
        program.execute()


if __name__ == "__main__":
    main()

