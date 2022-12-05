"""
CP1404/CP5632 Practical
Car class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise an Unreliable Car instance based on Car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        value = random.randint(0, 100)
        if value > self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
