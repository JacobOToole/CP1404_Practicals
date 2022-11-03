"""
CP1404 - Trimester 3 2022 - Jacob O'Toole
Guitar class exercise
estimation: 15 minutes
actual: 10 minutes
"""

from prac_06.guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 25)

    print(f"{gibson.name} get_age() - Expected 100, got {gibson.get_age()}")
    print(f"{another_guitar.name} get_age() - Expected 9, got {another_guitar.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True, got {gibson.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - Expected False, got {another_guitar.is_vintage()}")

    print(gibson)

main()