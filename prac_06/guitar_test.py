from prac_06.guitar import Guitar


def test_methods():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.45

    guitar = Guitar(name, year, cost)
    another_guitar = Guitar("Another Guitar", 2013, 1500.50)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 98, guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(another_guitar.name, 7, another_guitar.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name, True, guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(another_guitar.name, False, another_guitar.is_vintage()))


if __name__ == '__main__':
    test_methods()
