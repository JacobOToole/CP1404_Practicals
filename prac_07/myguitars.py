import csv
from prac_06.guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{str(guitar)} added.")
        name = input("Name: ")

    guitars.sort()
    with open('guitars.csv', 'w') as out_file:
        for guitar in guitars:
            print(guitar)
            print(Guitar.format_guitar(guitar), file=out_file)


main()
