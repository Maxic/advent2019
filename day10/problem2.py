def main():

    with open("input.txt", "r+") as file:
        content = file.readlines()
        for line in content:
            print(line)


if __name__ == "__main__":
    main()

