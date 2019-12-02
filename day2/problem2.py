import sys


def main():
    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        init_intcode = list(map(lambda i: int(i), content))
        intcode = init_intcode.copy()
        break_flag = False

        for x in range(0, 100):
            if break_flag:
                break
            for y in range(0, 100):
                intcode[1] = x
                intcode[2] = y
                result = exec_intcode(intcode)[0]
                if result == 19690720:
                    break_flag = True
                    print(100 * x + y)
                    break
                intcode = init_intcode.copy()


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

