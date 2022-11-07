import csv
from prac_06.guitar import Guitar

IN_FILE = 'guitars.csv'


def main():
    guitars = []
    in_file = open(IN_FILE, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], parts[1], float(parts[2]))
        guitars.append(guitar)
        guitars.sort()

    for guitar in guitars:
        print(guitar)


main()
