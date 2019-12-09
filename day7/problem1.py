from helpers.Intcode import IntCode
import itertools


def main():
    with open("input.txt", "r+") as file:
        content = file.readline().split(',')
        intcode = list(map(lambda i: int(i), content))

        # set phase settings
        phase_settings = list(range(0, 5))
        max_thruster_signal = 0

        for permutation in itertools.permutations(phase_settings):
            output_signal = 0
            for phase_setting in permutation:
                program = IntCode(intcode, [phase_setting, output_signal])
                output_signal = program.execute()
            max_thruster_signal = max(output_signal, max_thruster_signal)

        print(max_thruster_signal)


if __name__ == "__main__":
    main()

