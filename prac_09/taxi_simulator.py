"""
CP1404 Practical - Jacob O'Toole
Taxi simulator using classes
"""

from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    total_bill = 0
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != 'q':
        if choice == 'c':
            print("Taxis Available: ")
            display_taxis(taxis)
            current_taxi = choose_taxi(taxis)
        elif choice == 'd':
            if not current_taxi:
                print("You need to choose a taxi before you can drive")
            else:
                drive_taxi(current_taxi, total_bill)
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(current_taxi, total_bill):
    if current_taxi:
        current_taxi.start_fare()
        distance_to_drive = float(input("Drive how far? "))
        current_taxi.drive(distance_to_drive)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        total_bill += trip_cost
    else:
        print("You need to choose a taxi before you can drive")
    return total_bill


def choose_taxi(taxis):
    taxi_chosen = False
    while not taxi_chosen:
        try:
            taxi_choice = int(input("Choose Taxi: "))
            if taxi_choice <= 0 or taxi_choice < len(taxis):
                taxi_chosen = True
                current_taxi = taxis[taxi_choice]
            else:
                print("Invalid taxi choice")
                taxi_chosen = False
        except ValueError:
            print("Invalid taxi choice")
    return current_taxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f'{i} - {taxi}')


main()
