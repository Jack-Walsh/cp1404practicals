from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Silver Service", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)


main()