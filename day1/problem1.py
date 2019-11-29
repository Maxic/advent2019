def main():
    freq = 0

    with open("input.txt", "r+") as file:
        content = file.readlines()
        for line in content:
            if line[:1] == '+':
                freq = freq + int(line[1:])
            else:
                freq = freq - int(line[1:])
        print(freq)


if __name__ == "__main__":
    main()

