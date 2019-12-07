def main():
    valid_passwords = 0
    for password in range(130254, 678275):
        if password_valid(str(password)):
            valid_passwords += 1
    print(valid_passwords)


def password_valid(password):
    # Two adjacent digits are the same (like 22 in 122345)
    if password[0] == password[1] or password[1] == password[2] or password[2] == password[3] or password[3] == password[4] or password[4] == password[5]:
        # Going from left to right, the digits never decrease; they only ever increase or stay the same
        if password[0] <= password[1] <= password[2] <= password[3] <= password[4] <= password[5]:
            return True
    return False


if __name__ == "__main__":
    main()

