"""
CP1404 - Trimester 3 2022 - Jacob O'Toole
silver service taxi test
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    my_taxi = SilverServiceTaxi("Taxi1", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(f'Fare = ${SilverServiceTaxi.get_fare(my_taxi):.2f}')


main()
