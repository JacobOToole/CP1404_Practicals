"""
CP1404 - Trimester 3 2022 - Jacob O'Toole
Unreliable car class inheritance test
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    car = UnreliableCar("Car", 100, 50)
    car.drive(50)
    print(car)


main()
