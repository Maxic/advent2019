from helpers.Intcode import IntCode
import itertools


def main():
    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        # set phase settings
        phase_settings = [5, 6, 7, 8, 9]
        max_thruster_signal = 0

        for permutation in itertools.permutations(phase_settings):
            amp_array = [IntCode(intcode, [permutation[0]]), IntCode(intcode, [permutation[1]]),
                         IntCode(intcode, [permutation[2]]), IntCode(intcode, [permutation[3]]),
                         IntCode(intcode, [permutation[4]])]

            i = 0
            output_signal = 0
            while amp_array[4].state != 'HALTED':
                amp_array[i].input_array.append(output_signal)
                output_signal = amp_array[i].execute()
                i += 1
                if i % 5 == 0:
                    i = 0
            max_thruster_signal = max(output_signal, max_thruster_signal)

        print(max_thruster_signal)


if __name__ == "__main__":
    main()

