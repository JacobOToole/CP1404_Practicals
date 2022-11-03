"""
CP1404 - Trimester 3 2022 - Jacob O'Toole
Guitars program
Estimate: 45 minutes
Actual: 21 minutes
"""

from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My Guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{str(guitar)} added.")
        name = input("Name: ")

    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars: ")
    longest_name = max(len(guitar.name) for guitar in guitars)
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar.name:>{longest_name}} ({guitar.year}), worth ${guitar.cost:10,.2f} {'(vintage)' if Guitar.is_vintage(guitar) else ''}")


main()
