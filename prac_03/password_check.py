MIN_LENGTH = 6


def main():
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(MIN_LENGTH):
    password = input("Enter a password of at least {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        print("Password too short")
        password = input("Enter a password of at least {} characters: ".format(MIN_LENGTH))
    return password


def print_asterisks(sentence):
    print('*' * len(sentence))


main()
