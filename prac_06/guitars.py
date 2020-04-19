from prac_06.guitar import Guitar


def main():

    guitar = Guitar("Gibson L-5 CES", 1922, 16035.45)
    print(guitar)
    print("The guitar is {} years old".format(guitar.get_age()))
    print("Vintage : {}".format(guitar.is_vintage()))


main()



