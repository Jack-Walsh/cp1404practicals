from random import randint
from prac_08.car import Car


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_reliability_number = randint(1, 100)
        if random_reliability_number <= self.reliability:
            distance = 0
        super().drive(distance)
        distance_driven = distance
        return distance_driven

    

