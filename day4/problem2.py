def main():
    valid_passwords = 0
    for password in range(130254, 678275):
        if password_valid(str(password)):
            valid_passwords += 1
    print(valid_passwords)


def password_valid(password):
    # Two adjacent digits are the same, but are not part of a larger group of matching digits
    if adjacent_matching(password):
        # Going from left to right, the digits never decrease; they only ever increase or stay the same
        if password[0] <= password[1] <= password[2] <= password[3] <= password[4] <= password[5]:
            return True
    return False


def adjacent_matching(password):
    # check number of duplicates
    if (
        password[0] == password[1] or
        password[1] == password[2] or
        password[2] == password[3] or
        password[3] == password[4] or
        password[4] == password[5]
    ):
        # the whole string is the same, or do no leave enough room to contain another duplicate. group 6 and group 5
        if password[1] == password[2] == password[3] == password[4] == password[5]:
            return False
        if password[0] == password[1] == password[2] == password[3] == password[4]:
            return False
        # Groups of 4 are only false if the others are not duplicates
        if password[2] == password[3] == password[4] == password[5] and password[0] != password[1]:
            return False
        if password[0] == password[1] == password[2] == password[3] and password[4] != password[5]:
            return False
        if password[1] == password[2] == password[3] == password[4]:
            return False
        # there is a group of three that contains a duplicate, and the other group does not.
        if password[0] == password[1] == password[2] and password[3] == password[4] == password[5]:
            return False
        if password[0] == password[1] == password[2] and password[3] != password[4] and password[4] != password[5]:
            return False
        if password[1] == password[2] == password[3] and password[4] != password[5]:
            return False
        if password[2] == password[3] == password[4] and password[0] != password[1] and password[4] != password[5]:
            return False
        if password[3] == password[4] == password[5] and password[0] != password[1] and password[1] != password[2]:
            return False
        return True
    return False


if __name__ == "__main__":
    main()
