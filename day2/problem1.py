import sys


def main():
    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        # restore the gravity assist program to the "1202 program alarm" state
        intcode[1] = 12
        intcode[2] = 2

        result = exec_intcode(intcode)
        print(result[0])


def exec_intcode(intcode):
    current_pos = 0

    while current_pos < intcode.__len__():
        opcode = intcode[current_pos]

        # check for halt:
        if opcode == 99:
            break

        # set parameters
        value1 = intcode[intcode[current_pos + 1]]
        value2 = intcode[intcode[current_pos + 2]]
        output_pos = intcode[current_pos + 3]

        # run instruction
        if opcode == 1:
            intcode[output_pos] = value1 + value2
        elif opcode == 2:
            intcode[output_pos] = value1 * value2
        elif opcode != 99:
            print("Unknown opcode encountered: " + str(opcode) + " at position: " + str(current_pos))
            sys.exit()
        current_pos += 4

    return intcode


if __name__ == "__main__":
    main()

