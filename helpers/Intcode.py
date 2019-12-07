import sys


class IntCode:
    def __init__(self, program):
        self.p = program
        self.pointer = 0
        self.instruction = 0

    def execute(self):
        while self.p[self.pointer] != 99:
            instruction = self.p[self.pointer]
            opcode = self.get_opcode(instruction)

            # Addition
            if opcode == 1:
                value1 = self.get_value(instruction, 1)
                value2 = self.get_value(instruction, 2)
                output_pos = self.p[self.pointer + 3]

                self.p[output_pos] = value1 + value2

                self.pointer += 4

            # Multiplication
            elif opcode == 2:
                value1 = self.get_value(instruction, 1)
                value2 = self.get_value(instruction, 2)
                output_pos = self.p[self.pointer + 3]

                self.p[output_pos] = value1 * value2

                self.pointer += 4

            # Get input value
            elif opcode == 3:
                # set parameters
                print("Input needed, please provide an Integer as input:")
                self.p[self.p[self.pointer + 1]] = int(input())

                self.pointer += 2

            # Output value
            elif opcode == 4:
                print("Output: ")
                value1 = self.get_value(instruction, 1)
                print(value1)

                self.pointer += 2

            # jump-if-true
            elif opcode == 5:
                value1 = self.get_value(instruction, 1)
                value2 = self.get_value(instruction, 2)

                if value1 != 0:
                    self.pointer = value2
                else:
                    self.pointer += 3

            # jump-if-false:
            elif opcode == 6:
                value1 = self.get_value(instruction, 1)
                value2 = self.get_value(instruction, 2)

                if value1 == 0:
                    self.pointer = value2
                else:
                    self.pointer += 3

            # less than
            elif opcode == 7:
                value1 = self.get_value(instruction, 1)
                value2 = self.get_value(instruction, 2)
                output_pos = self.p[self.pointer + 3]

                self.p[output_pos] = 1 if value1 < value2 else 0

                self.pointer += 4

            # equals
            elif opcode == 8:
                value1 = self.get_value(instruction, 1)
                value2 = self.get_value(instruction, 2)
                output_pos = self.p[self.pointer + 3]

                self.p[output_pos] = 1 if value1 == value2 else 0

                self.pointer += 4
            else:
                print("Unknown opcode encountered: " + str(opcode) + " at position: " + str(self.pointer))
                sys.exit()
        return self.p

    @staticmethod
    def get_opcode(instruction):
        return instruction % 100

    def get_value(self, instruction, position):
        instruction = str(instruction)

        # default is position mode
        if instruction.__len__() < position + 2:
            return self.p[self.p[self.pointer + position]]

        # get mode
        mode = int(instruction[-(position + 2)])

        # position mode
        if mode == 0:
            return self.p[self.p[self.pointer + position]]

        # immediate mode
        elif mode == 1:
            return self.p[self.pointer + position]

        return self.p[self.p[self.pointer + position]]





